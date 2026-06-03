# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a production-ready REST API using the FastAPI framework. You will create endpoints to manage a collection of items, implement request validation, and understand HTTP methods and status codes.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Create a GET endpoint at `/` that returns a JSON response with a welcome message
- Start the server using `uvicorn` and verify it runs on `http://localhost:8000`
- Example response: `{"message": "Welcome to the Item Management API"}`

### 🛠️ Implement CRUD Endpoints for Items

#### Description
Build endpoints to Create, Read, Update, and Delete items in an in-memory storage system.

#### Requirements
Completed program should:

- Create a GET endpoint at `/items` that returns a list of all items
- Create a GET endpoint at `/items/{item_id}` that returns a single item by ID
- Create a POST endpoint at `/items` that accepts a new item and returns it with an assigned ID
- Create a PUT endpoint at `/items/{item_id}` that updates an existing item
- Create a DELETE endpoint at `/items/{item_id}` that removes an item and returns a confirmation message
- Use Pydantic models for request/response validation with fields like `name`, `description`, and `price`

### 🛠️ Add Request Validation and Error Handling

#### Description
Implement proper validation and HTTP status codes for API responses.

#### Requirements
Completed program should:

- Return status code 201 for successful item creation
- Return status code 404 when trying to access a non-existent item
- Return status code 200 for successful GET/PUT requests
- Return status code 204 for successful DELETE requests
- Validate that required fields are provided (e.g., `name` and `price` for items)
- Return appropriate error messages when validation fails
