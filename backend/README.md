# FastAPI Todo Backend

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at http://localhost:8000

## Endpoints
- `GET /todos` - List all todos
- `POST /todos` - Create a new todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo
