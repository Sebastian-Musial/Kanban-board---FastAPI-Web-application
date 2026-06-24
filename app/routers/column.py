from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session
from fastapi.responses import RedirectResponse

from app.database import get_session
from app.models import KanbanBoard, KanbanColumn

router = APIRouter()

@router.post("/board/{board_id}/column", tags=["column"])
def add_column(
    board_id: int,
    name: str = Form(...),
    order_id: int = Form(...),
    session: Session = Depends(get_session)) -> RedirectResponse:
        
        board = session.get(KanbanBoard, board_id)

        if board is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Board not found",
            )
        
        kanban_column = KanbanColumn(
            name=name,
            board_id=board_id,
            order_id=order_id
        )
        session.add(kanban_column)
        session.commit()

        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@router.post("/board/{board_id}/column/{column_id}", tags=["column"])
def modify_column(
    board_id: int,
    column_id: int,
    name: str = Form(...),
    session: Session = Depends(get_session))  -> RedirectResponse:

        board = session.get(KanbanBoard, board_id)

        if board is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Board not found",
            )

        column = session.get(KanbanColumn, column_id)    

        if column is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Column not found",
            )
        
        if column.board_id != board_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Column not found in this board",
            )

        column.name = name

        session.add(column)
        session.commit()

        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@router.delete("/board/{board_id}/column/{column_id}",status_code=status.HTTP_204_NO_CONTENT, tags=["column"])
def delete_column(
    board_id: int,
    column_id: int,
    session: Session = Depends(get_session))  -> None:

        board = session.get(KanbanBoard, board_id)

        if board is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Board not found",
            )
        
        column = session.get(KanbanColumn, column_id)    

        if column is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Column not found",
            )
        
        if column.board_id != board_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Column not found in this board",
            )

        session.delete(column)
        session.commit()