from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlmodel import select, Session

from app.database import create_db_and_tables, get_session
from app.models import KanbanBoard
from app.routers.board import router as board_routers
from app.routers.card import router as card_routers
from app.routers.column import router as column_routers

def create_app(create_tables_on_startup: bool = True) -> FastAPI:  
    #False w celu szybszego uruchamiania aplikacji, 
    #jeżeli aplikacja jest uruchamiana pierwszy raz to należy zostawić True w celu utworzenmia bazy danych z tabelami
    application = FastAPI()

    application.include_router(board_routers)
    application.include_router(card_routers)
    application.include_router(column_routers)

    application.mount("/static", StaticFiles(directory="app/static"), name="static")
    templates = Jinja2Templates(directory="app/templates")
    
    if create_tables_on_startup:
        create_db_and_tables()

    @application.get("/")
    def home(request: Request, session: Session = Depends(get_session)):
        boards = session.exec(select(KanbanBoard)).all()

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "boards": boards
            }
        )

    @application.get("/health", tags=["system"])
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return application

app = create_app()