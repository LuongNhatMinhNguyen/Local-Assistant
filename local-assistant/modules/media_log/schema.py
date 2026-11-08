from typing import Literal
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timezone

Status = Literal["ongoing", "planned", "finished", "revisiting", "dropped", "on_hold"]
Category = Literal["film", "manga", "lightnovel", "game", "book", "anime"]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class MediaItem(BaseModel):
    title: str
    category: Category
    status: Status
    note: str | None = None
    url: str | None = None
    id: UUID = Field(default_factory=uuid4)
    added_at: datetime = Field(default_factory=utc_now)

class StatusChange(BaseModel):
    item_id: UUID
    status: Status
    timestamp: datetime = Field(default_factory=utc_now)

    