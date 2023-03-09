"""
Root fastapi app file
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import router as root_router


def get_app() -> FastAPI:
    """
    Create FastAPI app, add needed config
    """

    application = FastAPI()

    # middleware
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # router
    application.include_router(root_router)

    return application


app = get_app()
