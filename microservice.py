from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Contract Device Service")

# In-memory store of contracts and their devices
contracts = {}

class DeviceRequest(BaseModel):
    device_name: str

@app.post('/contracts/{contract_id}/devices')
def add_device(contract_id: str, request: DeviceRequest):
    """Add a device to an existing contract."""
    devices = contracts.setdefault(contract_id, [])
    if len(devices) >= 3:
        raise HTTPException(status_code=400, detail="Maximum 3 devices per contract")
    devices.append(request.device_name)
    return {"contract_id": contract_id, "devices": devices}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
