# FastAPI Docker Book API 📚

A containerized REST API built using **FastAPI**, **PostgreSQL**,
**SQLAlchemy**, and **Docker**.\
This project demonstrates backend API development, database integration,
and containerized deployment.

------------------------------------------------------------------------

## 🚀 Features

-   FastAPI backend with REST endpoints
-   PostgreSQL database integration
-   SQLAlchemy ORM
-   Pydantic request validation
-   Docker containerization
-   Docker Compose multi-container setup
-   Interactive Swagger documentation

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3.11
-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   Docker & Docker Compose
-   Uvicorn

------------------------------------------------------------------------

## 📂 Project Structure

    fastapi-docker-book-api
    │
    ├── app
    │   ├── main.py
    │   ├── database.py
    │   ├── models.py
    │   ├── schemas.py
    │   └── crud.py
    │
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ How to Run the Project

### Prerequisites

-   Docker Desktop installed
-   Git installed

### Clone Repository

``` bash
git clone https://github.com/YOUR-USERNAME/fastapi-docker-book-api.git
cd fastapi-docker-book-api
```

### Start the Application

``` bash
docker compose up --build
```

------------------------------------------------------------------------

## 🌐 Access the API

Open in browser: http://localhost:8000/docs

------------------------------------------------------------------------

## 📮 API Endpoints

### Create Book

POST `/books`

``` json
{
  "title": "Python",
  "author": "Guido"
}
```

### Get All Books

GET `/books`

------------------------------------------------------------------------

## 🧠 How It Works

-   FastAPI handles HTTP requests
-   SQLAlchemy communicates with PostgreSQL
-   Docker Compose runs both API and DB containers
-   Containers communicate through internal Docker network

------------------------------------------------------------------------

## 🔧 Environment Configuration

  Environment   Database Host
  ------------- ---------------
  Local Run     localhost
  Docker        db

------------------------------------------------------------------------

## 📌 Future Improvements

-   JWT Authentication
-   Update & Delete endpoints
-   Cloud deployment
-   Kubernetes deployment

------------------------------------------------------------------------

## 👨‍💻 Author

Keerthi --- Backend Developer (Python, FastAPI, SQL)

⭐ If you found this useful, please star the repo!
