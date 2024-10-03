# EpiRecipes Search Platform Backend

This is the backend part of the **EpiRecipes Search Platform**, built using **Django** and **Django REST Framework**. The backend provides an API for searching recipes stored in an **OpenSearch** index. The dataset used is from the EpiRecipes Kaggle dataset, which is indexed into OpenSearch.

## Prerequisites

- Python 3.10+
- OpenSearch
- Kaggle dataset (EpiRecipes)
- Pipenv or pip for package management

## Features

- Search recipes by title or tags
- Dynamic filtering of recipe fields
- Integration with OpenSearch for fast and scalable search functionality

## Tech Stack

- **Django**: Web framework for the backend.
- **Django REST Framework (DRF)**: To build the API endpoints.
- **OpenSearch**: Search engine to index and search recipe data.


## Environment Setup

- You'll need to configure the paths for OpenSearch and Kaggle dataset based on your system. The paths in the project are based on my system setup:

- OpenSearch Path: localhost:9200
- Kaggle Dataset Path: I've stored the dataset at a specific location on my system. You will need to update the path to where the dataset is stored on your machine.

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
