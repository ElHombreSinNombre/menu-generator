import json
import httpx
from typing import Iterator, List
from fastapi import HTTPException, Depends, APIRouter, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import text
from sqlalchemy.engine import Connection
from schemas import FoodItem, MenuRequest
from config import engine, OLLAMA_HOST
from prompts import menu_prompt
from fastapi.templating import Jinja2Templates

router = APIRouter()

security = HTTPBearer()

templates = Jinja2Templates(directory="templates")

def verify_token(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    VALID_TOKEN = "secret" 
    accept_header = request.headers.get("accept", "")
    if token != VALID_TOKEN:
        detail= "Invalid or missing Bearer token"
        print(f"Error: {detail}")
        if "text/html" in accept_header:
            return templates.TemplateResponse(
                "error.html",
                context = {"request": request, "code": status.HTTP_401_UNAUTHORIZED},
            )
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = detail,
            headers = {"WWW-Authenticate": "Bearer"},
        )
    return True

def get_db_connection() -> Iterator[Connection]:
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()

@router.get("/", tags=["status"])
def default_route_status(request: Request):
    return templates.TemplateResponse("status.html", context={"request": request})

@router.get("/foods", response_model=List[FoodItem], tags=["foods"], dependencies=[Depends(verify_token)])
def get_all_foods(connection: Connection = Depends(get_db_connection)):
    try:
        query = text("SELECT * FROM foods")
        return list(connection.execute(query).mappings())
    except Exception as e:
        detail = f"Database error: Failed to fetch foods. {e}"
        print(f"Error: {detail}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

@router.post("/generate", tags=["ollama"], dependencies=[Depends(verify_token)])
async def generate_ai_content(prompt_input: MenuRequest):
    ollama_payload = {
        "model": "llama3",
        "prompt": menu_prompt(prompt_input),
        "stream": False,
        "format": "json"
    }
    ollama_url = f"{OLLAMA_HOST}/api/generate"
    try:
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(ollama_url, json=ollama_payload)
            response.raise_for_status()
            data = response.json()
            generated_text = data.get("response")
            if not generated_text:
                detail = f"Ollama error: Text not generated"
                print(f"Error: {detail}")
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
            return json.loads(generated_text)
    except httpx.HTTPError as e:
        detail = f"Error communicating with Ollama AI service: {e}"
        print(f"Error: {detail}")
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail)
    except Exception as e:
        detail = f"Unexpected error: {e}"
        print(f"Error: {detail}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
