# tests/test_health.py
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import app

client = TestClient(app)

def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    # FastAPI returns JSON by default
    assert resp.headers.get("content-type", "").startswith("application/json")
    assert resp.json() == {"status": "ok"}
