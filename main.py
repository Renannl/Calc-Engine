from fastapi import FastAPI

from interfaces.http.routes.pricing import (
    router as pricing_router,
)


app = FastAPI(
    title="Cost Calculator API",
    version="1.0.0",
)

app.include_router(pricing_router)