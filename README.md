# Contract Device Microservice

This repository contains a small FastAPI-based microservice that allows adding
up to three devices to a single contract. It can be used to support scenarios
where a customer wants multiple contract phones associated with the same phone
number.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running

Launch the service using:

```bash
python microservice.py
```

The service exposes `POST /contracts/{contract_id}/devices` where `{contract_id}`
is an arbitrary contract identifier. The request body should be JSON with a
`device_name` field. Example:

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"device_name": "iPhone 15"}' \
    http://localhost:8000/contracts/123/devices
```

This will register the device under contract `123`. Attempting to add more than
three devices results in an error.
