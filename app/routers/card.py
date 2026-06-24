from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session
from fastapi.responses import RedirectResponse
from datetime import datetime

from app.database import get_session
from app.models import KanbanBoard, KanbanColumn, Card

router = APIRouter()

@router.post("/board/{board_id}/column/{column_id}/card", tags=["card"])
def add_card(
    board_id: int,
    column_id: int,
    title: str = Form(...),
    description: str = Form(...),
    deadline: datetime = Form(...),
    session: Session = Depends(get_session)) -> RedirectResponse:
        
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
        
        kanban_card = Card(
            title=title,
            description=description,
            deadline=deadline,
            column_id=column_id
        )
        session.add(kanban_card)
        session.commit()

        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@router.post("/board/{board_id}/column/{column_id}/card/{card_id}", tags=["card"])
def modify_card(
    board_id: int,
    column_id: int,
    card_id: int,
    title: str = Form(...),
    description: str = Form(...),
    deadline: datetime = Form(...),
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

        card = session.get(Card, card_id)    

        if card is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Card not found",
            )

        if card.column_id != column_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Card not found in this column",
            )

        card.title=title
        card.description=description
        card.deadline=deadline


        session.add(card)
        session.commit()

        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@router.delete("/board/{board_id}/column/{column_id}/card/{card_id}",status_code=status.HTTP_204_NO_CONTENT, tags=["card"])
def delete_card(
    board_id: int,
    column_id: int,
    card_id: int,
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

        card = session.get(Card, card_id)    

        if card is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Card not found",
            )

        if card.column_id != column_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Card not found in this column",
            )

        session.delete(card)
        session.commit()