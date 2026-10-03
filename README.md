# ATLAS

## AI-Powered Engineering Operations Platform

ATLAS is an engineering operations platform being built incrementally from a FastAPI-based backend into a complete system for managing software projects, tasks, deployments, service health, incidents, notifications, and AI-assisted incident analysis.

The project is being developed step by step so that each technology is introduced when the system actually needs it.

---

## About ATLAS

In a real software engineering environment, teams need to manage projects and tasks, deploy applications, monitor services, respond to incidents, and understand what changed when something goes wrong.

ATLAS is designed to bring these engineering activities together into one platform.

The long-term system will connect:

* Project and task management
* Team collaboration
* Authentication and authorization
* Service monitoring
* Deployment tracking
* Incident management
* Notifications
* GitHub integrations
* AI-assisted incident analysis

The larger ATLAS vision is to help engineers move from **detecting a problem → understanding its context → investigating it → resolving it** within one platform.

---

## Current Implementation

ATLAS is currently being developed as a backend-first application.

The current stage focuses on:

* FastAPI
* Project management
* CRUD operations
* Request validation
* HTTP status codes and error handling
* JSON-based persistence
* Clean Architecture
* Automated API testing

### Current Project Flow

```text
Client
   ↓
FastAPI Router
   ↓
Service Layer
   ↓
Repository Layer
   ↓
JSON Storage
   ↓
Response
```

The current implementation provides project APIs such as:

```text
GET    /projects
GET    /project/{id}
POST   /projects
PATCH  /projects/{id}
DELETE /projects/{id}
```

---

## Architecture

ATLAS is being designed using a layered architecture so that different responsibilities remain separated.

```text
                Client
                  │
                  ▼
            API / Router
                  │
                  ▼
              Service
                  │
                  ▼
            Repository
                  │
                  ▼
              Storage
```

### Router

Responsible for handling HTTP requests and responses.

The router receives the request, validates the input through schemas, calls the appropriate service operation, and returns the response.

### Service

Contains application and business logic.

The service layer prevents business logic from being tightly coupled to the API routes or storage implementation.

### Repository

Responsible for data access.

The repository provides an abstraction between the application logic and the underlying storage system.

### Storage

The current implementation uses a JSON file for persistence.

In later versions, this layer will evolve to work with PostgreSQL.

---

## Project Structure

The backend is organized into separate components based on their responsibilities.

```text
ATLAS/
│
├── backend/
│   └── app/
│       ├── main.py
│       │
│       ├── routers/
│       │   └── projects.py
│       │
│       ├── schemas/
│       │   └── project.py
│       │
│       ├── services/
│       │   └── project_service.py
│       │
│       ├── repositories/
│       │   └── ...
│       │
│       └── data/
│           └── store.json
│
├── tests/
│   └── test_project.py
│
├── requirements.txt
└── README.md
```

The exact structure may evolve as ATLAS grows and additional modules are introduced.

---

## API Endpoints

### Get all projects

```http
GET /projects
```

Returns the available projects.

### Get a project

```http
GET /project/{id}
```

Returns a project using its ID.

### Create a project

```http
POST /projects
```

Creates a new project.

### Update a project

```http
PATCH /projects/{id}
```

Updates the provided fields of an existing project.

### Delete a project

```http
DELETE /projects/{id}
```

Deletes an existing project.

If the requested project does not exist, the API returns an appropriate HTTP error response.

---

## Request Flow

For example, when a client creates a project:

```text
Client
  │
  │ POST /projects
  ▼
Router
  │
  │ validate request
  ▼
Service
  │
  │ business logic
  ▼
Repository
  │
  │ save data
  ▼
JSON Storage
  │
  ▼
Repository
  │
  ▼
Service
  │
  ▼
Router
  │
  │ HTTP response
  ▼
Client
```

This separation makes the system easier to understand, test, maintain, and extend.

---

## Tech Stack

### Current

* Python
* FastAPI
* Pydantic
* JSON
* Pytest
* Git / GitHub

### Planned

* PostgreSQL
* SQLAlchemy
* Redis
* RabbitMQ
* WebSockets
* GitHub Webhooks
* AI / LLM integration
* Docker
* Nginx
* GitHub Actions

---

## Running Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd ATLAS
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI application

From the backend directory:

```bash
fastapi dev app/main.py
```

The API can then be accessed through the local development server.

FastAPI's interactive API documentation can be used to explore and test the endpoints.

---

## Testing

ATLAS uses **Pytest** for automated testing.

Tests cover the project API behavior, including operations such as:

* Retrieving projects
* Creating projects
* Updating projects
* Deleting projects
* Handling non-existent project IDs

Run the tests with:

```bash
pytest
```

The goal is to verify application behavior rather than relying only on manual API testing.

---

## Future Roadmap

ATLAS will evolve through multiple stages.

```text
ATLAS v0
   ↓
Project Backend
   ↓
ATLAS v1
Clean Architecture
   ↓
ATLAS v2
Authentication + Organizations
   ↓
ATLAS v3
Tasks + Collaboration
   ↓
ATLAS v4
PostgreSQL + SQLAlchemy
   ↓
ATLAS v5
Activity + Notifications
   ↓
ATLAS v6
Monitoring
   ↓
ATLAS v7
Incident Management
   ↓
ATLAS v8
GitHub Integration + Deployments
   ↓
ATLAS v9
AI Incident Analysis
   ↓
ATLAS v10
Docker + CI/CD + Production Deployment
```

---

## Planned Technologies

### PostgreSQL

Will become the primary persistent database for ATLAS.

It will eventually store entities such as:

* Users
* Organizations
* Projects
* Tasks
* Comments
* Services
* Metrics
* Incidents
* Deployments
* Notifications
* Activity

### Redis

Will be used for fast temporary data operations such as:

* Caching
* Rate limiting
* Temporary state

PostgreSQL will remain the primary source of truth.

### RabbitMQ

Will support asynchronous background processing.

For example:

```text
Incident Created
      ↓
   RabbitMQ
      ↓
 ┌────┴─────────────┐
 ↓                  ↓
Notification      AI Worker
Worker
```

This allows long-running operations to be processed without unnecessarily blocking the main API request.

### Monitoring

ATLAS will eventually monitor services for:

* Health
* Response time
* Errors
* Uptime

A service failure can trigger an incident.

### Incident Management

Incidents will represent significant engineering problems and can be associated with:

* Projects
* Services
* Deployments
* Metrics
* Activity

### GitHub Integration

GitHub webhooks will allow ATLAS to receive external events such as deployment-related information.

### AI Incident Analysis

The AI component will analyze incident context such as:

* Recent deployments
* Metrics
* Errors
* Logs
* Activity

The goal is to provide engineers with useful context, possible causes, and suggested investigation steps.

The AI is intended to assist engineers rather than blindly make production changes.

### Docker

Docker will eventually package ATLAS and its supporting services for consistent development and deployment.

### GitHub Actions

GitHub Actions will eventually automate processes such as:

```text
git push
   ↓
GitHub Actions
   ↓
Run Tests
   ↓
Build
   ↓
Build Docker Image
   ↓
Deploy
```

### Nginx

Nginx will eventually sit in front of the production application and handle incoming traffic.

---

## Engineering Approach

ATLAS is being developed incrementally.

Each feature follows a development cycle:

```text
Requirement
    ↓
Understand the problem
    ↓
Design the solution
    ↓
Implement
    ↓
Run
    ↓
Test
    ↓
Debug
    ↓
Improve
    ↓
Commit
```

The objective is not to memorize code or introduce technologies before they are needed.

Instead, each technology is learned and implemented when it solves a real problem in the ATLAS system.

---

## Project Goal

The final goal of ATLAS is not simply to create a collection of APIs.

The goal is to build a complete engineering system that demonstrates an understanding of:

* Backend development
* API design
* Clean Architecture
* Database design
* Authentication and authorization
* Testing
* Asynchronous processing
* Monitoring
* Incident management
* Integrations
* AI-assisted engineering workflows
* Containerization
* CI/CD
* Production deployment

