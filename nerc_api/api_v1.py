from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel

from .services import nerc_service


class NERCEntitySpan(BaseModel):
    word: str
    start: int
    end: int
    entity_group: str
    score: float


# Create router
router = APIRouter(prefix="/v1/nerc")


@router.post("/extract", response_model=list[NERCEntitySpan])
async def extract_entities(text: str = Body(..., media_type="text/plain")) -> list[NERCEntitySpan]:
    """
    Extract named entities from the input text.

    :param text: Input text for NER processing
    :return: Extracted entities
    """
    try:
        return nerc_service.predict(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))