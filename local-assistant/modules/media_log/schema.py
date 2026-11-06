from typing import Literal
from pydantic import BaseModel

class MediaItem(BaseModel):
    title: str
    category: Literal["film", "manga", "lightnovel", "game"]
    status: Literal["ongoing", "planned", "finished", "revisiting", "dropped", "on-hold"]
    note: str | None = None
    