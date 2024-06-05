import pytest
from httpx import AsyncClient
from app.main import app
from app.models import Todo, TodoPost

@pytest.mark.asyncio
async def test_read_todos():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_todo():
    todo = {"name": "Test Todo", "content": "This is a test todo"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/todos/", json=todo)
    assert response.status_code == 200
    assert response.json()["name"] == todo["name"]
    assert response.json()["content"] == todo["content"]

@pytest.mark.asyncio
async def test_create_duplicate_todo():
    todo = {"name": "Test Todo", "content": "This is a duplicate test todo"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/todos/", json=todo)
        assert response.status_code == 200  # First creation should succeed

        response = await ac.post("/todos/", json=todo)
        assert response.status_code == 404  # Second creation should fail with HTTP 404

@pytest.mark.asyncio
async def test_update_todo():
    todo_post = {"name": "Updated Test Todo", "content": "This is an updated test todo"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/todos/", json={"name": "Original Test Todo", "content": "Original content"})
        todo_id = response.json()["id"]

        response = await ac.put(f"/todos/{todo_id}", json=todo_post)
    assert response.status_code == 200
    assert response.json()["name"] == todo_post["name"]
    assert response.json()["content"] == todo_post["content"]

@pytest.mark.asyncio
async def test_delete_todo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/todos/", json={"name": "To Be Deleted", "content": "This will be deleted"})
        todo_id = response.json()["id"]

        response = await ac.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}
