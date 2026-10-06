import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'

def test_create_high_risk_event():
    payload = {
        'source_ip': '10.10.10.25',
        'destination_ip': '192.168.1.20',
        'protocol': 'HTTPS',
        'severity': 'HIGH',
        'event_type': 'Unauthorized Access'
    }
    response = client.post('/security-events', json=payload)
    assert response.status_code == 201
    assert response.json()['severity'] == 'HIGH'

def test_invalid_severity_rejected():
    payload = {
        'source_ip': '10.0.0.1', 'destination_ip': '10.0.0.2',
        'protocol': 'TCP', 'severity': 'UNKNOWN', 'event_type': 'Probe'
    }
    response = client.post('/security-events', json=payload)
    assert response.status_code == 400
