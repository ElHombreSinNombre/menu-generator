from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from config import origins
import routes  
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="Menu Generator API")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    code = exc.status_code
    accept_header = request.headers.get("accept", "")
    if "text/html" in accept_header:
        return templates.TemplateResponse(
            "error.html",
            context = {"request": request, "code": code},
        )
    return JSONResponse(
        content = {"status": "Error", "code": code, "detail": exc.detail},
    )
