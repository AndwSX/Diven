from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates/admin")  # Ruta donde están las vistas

@router.get("/admin", tags=["admin"])
def home(request: Request):
    usuario_id = request.cookies.get("usuario_id")
    if usuario_id:
        return templates.TemplateResponse("layout_admin.html", {"request": request})
    return RedirectResponse(url="/login?error=2", status_code=303)

#Xd