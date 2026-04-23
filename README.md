# GroceryPro-API
GroceryPro-API is a backend service that provide  real-time grocery prices, create lists, and track cost trends across stores.

## Local Development Setup Overview
1. Clone the repository
2. Need .env
3. Build and start the Docker containers
4. Verify the application and Django Admin are accessible locally
5. *** starting app in uvicorn: `uvicorn grocerypro-api.asgi:application --reload`

## Installation
### Prerequisites
Before setting up GroceryPro-API, make sure you have the following installed:
- Docker (v20+)
- Docker Compose (v2+)
- Git
- No local Python or PostgreSQL installation is required — everything runs inside Docker



### Clone the Repository
```bash
   git clone https://github.com/Sabbir999/GroceryPro-API.git
````
cd GroceryPro-API

### Docker Setup
The project is fully containerized using Docker and Docker Compose.
- Key files:
  - Dockerfile – Defines the Django application container
  - docker-compose.yml – Defines the services and how they interact
  - requirements.txt – Python dependencies for the Django application
- Services:
    - web – Django application
    - db – PostgreSQL database

Docker networking allows Django to connect to Postgres via the service name.


### Build and start the containers
```bash
  docker compose up --build
```
This command will: 
- Build the Docker images for the Django application and PostgreSQL database
- Start the PostgreSQL database
- Start the Django application
- Apply database migrations automatically
- Collect static files
- Create a superuser for the Django admin interface (if enabled via environment variables)

Once running, the application will be available at:
```bash
  http://localhost:8000
```
### Database & Migrations
The application uses PostgreSQL as the database. The Docker Compose setup automatically handles database migrations.

### Initial Database Setup
The first time you run the application, it will:
- Create the PostgreSQL database
- Apply all migrations to set up the database schema


## Useful Docker Commands
### View running containers
```bash
  docker compose ps
```
### Stop the application
```bash
    docker compose down
```
### Rebuild the application
```bash
    docker compose up --build
```
### View logs
```bash
    docker compose logs -f
```
### Access the Django shell
```bash
    docker compose exec web python manage.py shell
```
### Run management commands
You can run any Django management command using:
```bash
    docker compose exec web python manage.py <command>
```
