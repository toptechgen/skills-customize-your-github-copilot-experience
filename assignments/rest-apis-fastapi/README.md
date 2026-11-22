# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages a collection of programming tasks. You will practice defining routes, handling HTTP methods, and using Python data structures to complete CRUD operations.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description

Set up a FastAPI app and define a root endpoint that confirms the API is running.

#### Requirements

Completed program should:

- Import `FastAPI` and create an app instance
- Include a `GET /` endpoint
- Return a JSON object containing an API name and status

### 🛠️ Implement Task Routes

#### Description

Add endpoints that let a client list all tasks and retrieve one task by its numeric ID.

#### Requirements

Completed program should:

- Use an in-memory list of dictionaries to store tasks
- Include a `GET /tasks` endpoint that returns all tasks
- Include a `GET /tasks/{task_id}` endpoint that returns the matching task
- Return an HTTP 404 response when a task ID does not exist

### 🛠️ Add and Remove Tasks

#### Description

Complete the API by allowing clients to create and delete tasks.

#### Requirements

Completed program should:

- Include a `POST /tasks` endpoint that accepts a task title
- Assign a unique numeric ID to each new task
- Return the newly created task
- Include a `DELETE /tasks/{task_id}` endpoint
- Return an HTTP 404 response when the task cannot be found
