# TripMap

## Project Description
TripMap is a Django-based web application designed to visualize and manage travel itineraries or points of interest on a map. It integrates with a PostgreSQL database and uses Pillow for image processing, suggesting features like storing location-based data and potentially displaying associated images. The application is containerized using Docker and Docker Compose for easy setup and deployment.

## Features
- **Map-based Visualization:** Display trips, locations, or points of interest on an interactive map.
- **Trip Management:** Create, read, update, and delete trip data.
- **Image Handling:** Support for uploading and displaying images related to trips or locations (powered by Pillow).
- **PostgreSQL Database:** Robust data storage for all application data.
- **Containerized Development & Deployment:** Easy setup and consistent environment using Docker and Docker Compose.

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/tripmap.git
    cd tripmap
    ```

2.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```
    This command will:
    - Build the Docker image for the Django application.
    - Start the PostgreSQL database container.
    - Start the Django application container.

3.  **Perform database migrations:**
    Once the containers are running, execute migrations to set up the database schema:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4.  **Create a superuser (optional):**
    To access the Django admin panel, create a superuser:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5.  **Access the application:**
    The application should be accessible in your web browser at `http://localhost:8000`. The Django admin panel will be available at `http://localhost:8000/admin`.

## Usage
- Navigate to `http://localhost:8000` to access the main application interface.
- Use the admin panel (`/admin`) to manage trips, locations, and other data if you've created a superuser.

## Project Structure
- `config/`: Django project settings, URLs, WSGI.
- `trips/`: Django application containing models, views, templates, and migrations for trip-related functionalities.
- `media/`: Directory for user-uploaded media files (e.g., trip images).
- `docker-compose.yml`: Defines the services for Docker Compose (web application and database).
- `Dockerfile`: Defines the Docker image for the Django application.
- `requirements.txt`: Python dependencies.
- `manage.py`: Django's command-line utility.
