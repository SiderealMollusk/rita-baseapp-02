import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_hello_default():
    # Ensure APP_VERSION is not set for this test
    if "APP_VERSION" in os.environ:
        del os.environ["APP_VERSION"]
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, user! from version unknown"}

def test_read_hello_with_version():
    os.environ["APP_VERSION"] = "1.2.3"
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, user! from version 1.2.3"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
