from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.analyze import router as analyze_router

app = FastAPI(
    title="Shopify CRO Auditor",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure screenshots directory exists
screenshots_dir = Path("screenshots")
screenshots_dir.mkdir(exist_ok=True)

app.mount(
    "/screenshots",
    StaticFiles(directory=str(screenshots_dir)),
    name="screenshots",
)

app.include_router(analyze_router)


@app.get("/")
def health():
    return {"status": "ok"}