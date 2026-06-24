from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

#SQL model
class KanbanBoard(SQLModel, table=True):
    __tablename__ = "kanban_boards"

    board_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=30)
    columns: list["KanbanColumn"] = Relationship(back_populates="board")


class KanbanColumn(SQLModel, table=True):
    __tablename__ = "kanban_columns"

    column_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=30)
    order_id: int
    
    board_id: int = Field(foreign_key="kanban_boards.board_id")
    board: KanbanBoard = Relationship(back_populates="columns")
    cards: list["Card"] = Relationship(back_populates="column")


class Card(SQLModel, table=True):
    __tablename__ = "cards"

    card_id: int | None = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=30)
    description: str = Field(min_length=1)
    deadline: datetime

    column_id: int = Field(foreign_key="kanban_columns.column_id")
    column: KanbanColumn = Relationship(back_populates="cards")
