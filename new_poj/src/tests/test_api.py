from src.app.main import app
import pytest
from httpx import AsyncClient, ASGITransport

transport = ASGITransport(app)


@pytest.mark.asyncio
async def test_app():
    async with AsyncClient(transport=transport, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/registrations/registration", params={
            "name": "Iphone",
            "weight": 0.345,
            "typ": 3,
            "cost": 4200,
        })
    assert response.status_code == 200
