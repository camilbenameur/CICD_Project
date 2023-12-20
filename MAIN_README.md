## Auteurs
- [Camil BENAMEUR](https://github.com/camilbenameur)
- [Lionel NGUYEN](https://github.com/LionelKhoi)

## Spécialité
- Spécialité : ILC (Ingénierie Logicielle et des Connaissances)

# Summary: ESIREM - 4A - ILC CI/CD Project

## Project Deadline
December 20, 2023, 23:59

## 1. General Project Requirements

### GitHub
- Dedicated GitHub repository with the instructor added as a collaborator.
- Collaborative commit history.
- Automated Docker image build using GitHub Actions.
- Repository documentation via README and Swagger.

### Docker
- Push at least three different images to the Google Container Registry (GCR).
- Generated Docker image executable with `docker run`.

### Documentation
- Main README with project overview, group members, technologies used, CI badges, and API execution procedure.
- Additional READMEs for each folder.
- Valid Swagger file for API endpoints.

## 2. Project Objectives

### Objective
Create a Flask API for CRUD operations on a calendar.

### Language
Python

## 2.1 Initial REST API Version

- Routes: E1 to E6 for event creation, list display, participant addition, next event details, and data import from CSV.

## 2.2 API Documentation

- README and Swagger file detailing API usage and loading data procedure.

## 2.3 Continuous Integration (CI)

- Three GitHub Actions for continuous integration:
  1. Triggered on each change to build the application.
  2. Manually triggered to create a Docker image using Dockerfile.
  3. Triggered on each semver tag to build and push the API image with specified version.

## 2.4 Continuous Deployment (CD)

- Automatic publication of new versions to Google Container Registry (GCR).

## 2.5 Initial Release

- Deploy a public release of the API on GitHub with a tag matching the semantic version.

## 2.6 API Improvement

For each feature:
1. Add event descriptions.
2. Release with an appropriate version tag.
3. Calculate total time spent on events for a person (daily, weekly, monthly).
4. Release with version tag.
5. Correct time calculation to consider events with more than one person.
6. Release with version tag.
7. Add a route to calculate time remaining before a date or event.
8. Release with version tag.
