# EpiRecipes Search Platform Backend

This is the backend part of the **EpiRecipes Search Platform**, built using **Django** and **Django REST Framework**. The backend provides an API for searching recipes stored in an **OpenSearch** index.

## Features

- Search recipes by title or tags
- Dynamic filtering of recipe fields
- Integration with OpenSearch for fast and scalable search functionality

## Tech Stack

- **Django**: Web framework for the backend.
- **Django REST Framework (DRF)**: To build the API endpoints.
- **OpenSearch**: Search engine to index and search recipe data.

## Prerequisites

- **Python** (Version >= 3.8)
- **Pipenv** or **pip** for package management
- **OpenSearch**: Make sure you have an OpenSearch instance running on your machine or server.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/swayyyam/EpiRecipes-Search-Platform-backend.git
   cd EpiRecipes-Search-Platform-backend

## Create a virtual environment and install dependencies

- pipenv install
- python3 -m venv env
- source env/bin/activate
- pip install -r requirements.txt


## Run migrations

- python manage.py migrate

## Start the development server

- python manage.py runserver
