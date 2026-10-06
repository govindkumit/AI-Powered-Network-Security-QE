from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Network Security QE Demo", version="1.0")
EVENTS = []

class SecurityEvent(BaseModel):
    source_ip: str
    destination_ip: str
    protocol: str
    severity: str
    event_type: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/security-events", status_code=201)
def create_event(event: SecurityEvent):
    if event.severity.upper() not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        raise HTTPException(400, "Invalid severity")
    record = event.model_dump()
    record["id"] = len(EVENTS) + 1
    EVENTS.append(record)
    return record

@app.get("/security-events")
def list_events():
    return EVENTS
