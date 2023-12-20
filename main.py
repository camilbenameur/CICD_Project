from flask import Flask, request, jsonify
import csv
from datetime import datetime, timedelta
app = Flask(__name__)


events_db = []

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# E1 - Créer un évènement
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = {
    'timestamp': data['timestamp'],
    'duration': data['duration'],
    'participants': data['participants'],
    'name': data['name'],
    'description': data['description']
    
}
    events_db.append(event)
    return jsonify({'message': 'Évènement créé avec succès'}), 201


# E2 - Afficher une liste de tous les événements dans l’ordre chronologique
@app.route('/events', methods=['GET'])
def get_all_events():
    sorted_events = sorted(events_db, key=lambda x: x['timestamp'])
    return jsonify(sorted_events)




# E3 - Afficher une liste de tous les événements dans l’ordre chronologique liées à une personne
@app.route('/events/<participant>', methods=['GET'])
def get_events_by_participant(participant):
    participant_events = [event for event in events_db if participant in event['participants']]
    sorted_events = sorted(participant_events, key=lambda x: x['timestamp'])
    return jsonify(sorted_events)


# E4 - Ajouter un participant à un évènement
@app.route('/events/<event_name>/add-participant', methods=['PUT'])
def add_participant(event_name):
    data = request.get_json()
    for event in events_db:
        if event['name'] == event_name:
            event['participants'].append(data['participant'])
            return jsonify({'message': f"Participant ajouté à l'évènement {event_name}"}), 200
    return jsonify({'message': f"Évènement {event_name} non trouvé"}), 404


# E5 - Afficher le détails du prochain évènement
@app.route('/next-event', methods=['GET'])
def get_next_event():
    if not events_db:
        return jsonify({'message': 'Aucun évènement trouvé'}), 404
    next_event = min(events_db, key=lambda x: x['timestamp'])
    return jsonify(next_event)


# E6 - Importer des données depuis un fichier csv
# @app.route('/import-csv', methods=['POST'])
# def import_csv():
    
#     if 'file' not in request.files:
#         return jsonify({'message': 'Aucun fichier trouvé'}), 400

#     file = request.files['file']

    
#     if file.filename == '':
#         return jsonify({'message': 'Aucun fichier sélectionné'}), 400

    
#     if not file.filename.endswith('.csv'):
#         return jsonify({'message': 'Le fichier doit être au format CSV'}), 400

#     try:
#         # Lisez le fichier CSV
#         csv_data = file.read()

#         # Utilisez le module CSV pour traiter les données
#         csv_reader = csv.reader(csv_data.splitlines())
        
#         for row in csv_reader:
            
#             event = {
#                 'timestamp': row[0],
#                 'name': row[1],
#                 'participants': row[2].split(',')
#             }
#             events_db.append(event)

#         return jsonify({'message': 'Données importées avec succès'}), 200

#     except Exception as e:
#         return jsonify({'message': f'Erreur lors de l\'importation du fichier CSV : {str(e)}'})


# Connaître le temps total passé pour une période donnée
@app.route('/total-time/<participant>', methods=['GET'])
def get_total_time(participant):
    try:
        current_timestamp = int(datetime.timestamp(datetime.now()))

        total_time_day = 0
        total_time_seven_days = 0
        total_time_month = 0

        for event in events_db:
            if participant in event['participants'] and len(event['participants']) > 1:
                event_timestamp = event['timestamp']
                event_duration = event['duration']

                time_difference =   current_timestamp - event_timestamp
                print(f"Event Timestamp: {event_timestamp}, Time Difference: {time_difference} seconds")

                if time_difference <= 86400: 
                    total_time_day += event_duration
                if 0 <= time_difference < 604800:  
                    total_time_seven_days += event_duration
                if 0 <= time_difference <= 2592000:  
                    total_time_month += event_duration

        result = {
            'participant': participant,
            'total_time_day': total_time_day,
            'total_time_seven_days': total_time_seven_days,
            'total_time_month': total_time_month
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération du temps total : {str(e)}'})
    

#Connaître le temps restant avant la date choisie (en secondes)
@app.route('/time-remaining', methods=['GET'])
def get_time_remaining():
        
    target_timestamp_str = request.args.get('target_timestamp')

    target_timestamp = int(target_timestamp_str)
    current_timestamp = int(datetime.timestamp(datetime.now()))

    time_remaining_seconds = current_timestamp - target_timestamp 

    result = {
        'target_timestamp': target_timestamp,
        'time_remaining_seconds': time_remaining_seconds
    }

    return jsonify(result)

    
# Nouvelle route pour la racine ("/")
@app.route('/')
def home():
    return "Bienvenue !"



if __name__ == '__main__':
    app.run(debug=True)
