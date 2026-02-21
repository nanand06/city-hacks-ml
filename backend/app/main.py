from __future__ import annotations

import os

from fastapi import FastAPI, Query

from app.services.network_vulnerability import NetworkVulnerabilityService

app = FastAPI(title="Civic Dashboard API")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/cityhacks")
network_service = NetworkVulnerabilityService(database_url=DATABASE_URL, cache_ttl_seconds=600)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/network-vulnerability")
def network_vulnerability(refresh: bool = Query(default=False)) -> list[dict]:
    return network_service.get_scores(force_refresh=refresh)
