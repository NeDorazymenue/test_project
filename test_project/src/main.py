from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
import uvicorn

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.api.auth import router as router_auth
from src.api.users import router as router_users
from src.api.admins import router as router_admins
from src.api.webhook import router as routers_webhook



app = FastAPI(docs_url=None)


app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_admins)
app.include_router(routers_webhook)


@app.get("/")
def func():
    return "hello world!"

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)