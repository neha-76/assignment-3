from fastapi import FastAPI
from routes.report import router as report_router
from routes.ingest import router as ingest_router
from routes.fetch import router as fetch_router

app = FastAPI()

app.include_router(ingest_router)
app.include_router(fetch_router)
app.include_router(report_router)