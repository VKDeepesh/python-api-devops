import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app


def test_hello():
    client = app.test_client()

    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json == {"message": "Hello from my Python API"}


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}