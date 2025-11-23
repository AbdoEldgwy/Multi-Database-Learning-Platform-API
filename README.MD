# Multi-Database Learning Platform API

 Just a training lab project for learning how to build APIs with multiple databases.

 How to integrate `PostgreSQL`, `MongoDB`, and `Redis` with FastAPI.

 understanding how to use multiple database systems inside one real-world application.

 ## 0. Table of Contents

 1) [Overview](#overview)
 2) [Project Features](#project-features)
 3) [Architecture](#architecture)
 4) [Technologies Used](#technologies-used)
 5) [Setup Instructions](#setup-instructions)
 6) [Future Improvements](#future-improvements)
 
## 1. Overview
by `FastAPI` , This lab project implements a simple Learning Platform Backend API

## 2. Project Features

- User Authentication and Authorization
- CRUD Operations on Courses, Topics, and Resources
- Activity logging using MongoDB
- Cache using Redis
- Contaiterization using Docker

## 3. Architecture
```bash
FastAPI Application
│
├── PostgreSQL → Users, Courses, Enrollments (structured data)
├── MongoDB   → User Activities, Logs (document store)
└── Redis     → Caching and Sessions (in-memory)
```

## 4. Technologies Used

- Python 
- FastAPI
- PostgreSQL
- MongoDB
- Redis
- Docker

## 5. Setup Instructions

### 5.1 Prerequisites

- Docker
- Docker Compose
- Python 3.9+

### 5.2 Running the Application

1. Clone the repository

```bash
git clone https://github.com/AbdoEldgwy/Multi-Database-Learning-Platform-API.git
```

2. Create a `.env` file in the root directory and add the following environment variables:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=learning_platform

MONGO_INITDB_ROOT_USERNAME=mongoadmin
MONGO_INITDB_ROOT_PASSWORD=mongoadmin

REDIS_PASSWORD=redis
```

3. Build the Docker images

```bash
docker-compose build
```

4. Start the Docker containers

```bash
docker-compose up -d
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

## 6. Future Improvements
 - JWT authentication
 - Frontend UI