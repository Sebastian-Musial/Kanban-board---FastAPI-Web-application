from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session
from fastapi.responses import RedirectResponse

from app.database import get_session
from app.models import KanbanBoard

router = APIRouter()



@router.post("/board", tags=["board"])
def add_board(name: str = Form(...), session: Session = Depends(get_session)) -> RedirectResponse:
    kanban_board = KanbanBoard(
        name=name
    )
    session.add(kanban_board)
    session.commit()

    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@router.post("/board/{board_id}", tags=["board"])
def modify_board(board_id: int, name: str = Form(...), session: Session = Depends(get_session))  -> RedirectResponse:
    board = session.get(KanbanBoard, board_id)

    if board is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Board not found",
        )

    board.name = name

    session.add(board)
    session.commit()

    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@router.delete("/board/{board_id}",status_code=status.HTTP_204_NO_CONTENT, tags=["board"])
def delete_board(board_id: int,session: Session = Depends(get_session))  -> None:
    board = session.get(KanbanBoard, board_id)

    if board is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Board not found",
        )

    session.delete(board)
    session.commit()