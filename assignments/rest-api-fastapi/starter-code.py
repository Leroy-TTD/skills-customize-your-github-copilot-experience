from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Task 1: Create a basic FastAPI application
# Create a root endpoint that returns a welcome message
@app.get("/")
def read_root():
    # Return a welcome message
    pass

# Task 2: Implement CRUD endpoints
# Define a Pydantic model for Item
class Item(BaseModel):
    name: str
    description: str = None
    price: float

# In-memory storage for items
items = {}

@app.get("/items")
def get_items():
    # Return a list of all items
    pass

@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Return a single item by ID
    pass

@app.post("/items")
def create_item(item: Item):
    # Create a new item and return it with an assigned ID
    pass

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # Update an existing item
    pass

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Delete an item and return a confirmation message
    pass

# Task 3: Add request validation and error handling
# Modify the endpoints to return appropriate status codes and error messages
