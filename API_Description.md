# Flask Event Management API

This is a Flask-based API for managing events. It provides endpoints for creating events, getting event details, adding participants to events, and more.
The API is the main.py file.
All request other than GET will be typed on powershell because curl method do not work for me.

## How to Run

  Run the Flask app:

    ```powershell
    $env:FLASK_APP = "main.py"
    ```

    ```powershell
    python -m flask run  
    ```

 The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### 1. Create an Event

- **Endpoint:** `/events`
- **Method:** `POST`
- **Request Body:**
  ```powershell
  {
    $body = @{
    "timestamp" = 1703106336
    "duration" = 6400
    "name" = "Example"
    "participants" = @("John","Jack")
    "description" = "Description"
  } | ConvertTo-Json

  $headers = @{
    "Content-Type" = "application/json"
  }

  Invoke-RestMethod -Uri "http://127.0.0.1:5000/events" -Method Post -Headers $headers -Body $body

  }
  ```
- **Response:**
  ```json
  {
    "message": "Évènement créé avec succès"
  }
  ```

### 2. Get All Events

- **Endpoint:** `/events`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
     "timestamp" = 1703106336
      "duration" = 6400
      "name" = "Example"
      "participants" = @("John","Jack")
      "description" = "Description"
    },
    ...
  ]
  ```

### 3. Get Events by Participant

- **Endpoint:** `/events/<participant>`
- **Method:** `GET`
- **Exemple:** `/events/John`
- **Response:**
  ```json
  [
    {
      "timestamp" = 1703106336
      "duration" = 6400
      "name" = "Example"
      "participants" = @("John")
      "description" = "Description"
    },
    ...
  ]
  ```

  In this code, firstly i filtered events so that only those which have the participant is taken.
  Then i sorted them by date.

### 4. Add Participant to an Event

- **Endpoint:** `/events/<event_name>/add-participant`
- **Method:** `PUT`
- **Request Body:**
  ```powershell
  $body = @{
    "participant" = "Jean"
  } | ConvertTo-Json

  $headers = @{
    "Content-Type" = "application/json"
  }

  Invoke-RestMethod -Uri "http://127.0.0.1:5000/events/Example/add-participant" -Method Put -Headers $headers -Body $body
  ```
- **Response:**
  ```json
  {
    "message": "Participant ajouté à l'évènement Example"
  }
  ```

### 5. Get Details of the Next Event

- **Endpoint:** `/next-event`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "timestamp" = 1703106336
      "duration" = 6400
      "name" = "Example"
      "participants" = @("John")
      "description" = "Description"
  }
  ```

### 6. Get Total Time for a Participant

- **Endpoint:** `/total-time/<participant>`
- **Method:** `GET`
- - **Exemple:** `/total-time/John`
- **Response:**
  ```json
  {
    "participant": "John",
    "total_time_day": 3600,
    "total_time_seven_days": 7200,
    "total_time_month": 14400
  }
  ```
I made 3 separates variables so they do not depend on each other so it minimize the risk of a problem to occur.   
I also choose to let the date in timestamp to keep things simpler to use.
### 7. Get Time Remaining Before a Date

- **Endpoint:** `/time-remaining`
- **Method:** `GET`
- - **Exemple:** `/time-remaining/1703106336`
- **Query Parameter:**
  - `target_timestamp`: Target timestamp to calculate time remaining
- **Response:**
  ```json
  {
    "target_timestamp": 1703106336,
    "time_remaining_seconds": 3600
  }
  ```

  I choose to let the date in timestamp to keep things simpler to use.







