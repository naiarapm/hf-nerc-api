from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from nerc_api import api_v1


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(
        title="NERC Web Service",
        description="Named Entity Recognition and Classification API",
        version="0.1.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_v1.router)

    return app


app = create_app()
