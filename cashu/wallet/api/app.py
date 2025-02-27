from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from ...core.settings import settings
from .router import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Cashu Wallet REST API",
        description="REST API for Cashu Nutshell",
        version=settings.version,
        license_info={
            "name": "MIT License",
            "url": "https://raw.githubusercontent.com/cashubtc/cashu/main/LICENSE",
        },
    )
    return app


app = create_app()


@app.middleware("http")
async def catch_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


app.include_router(router=router)
