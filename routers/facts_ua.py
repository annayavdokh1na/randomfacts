from fastapi import APIRouter
from services.get_facts import get_facts_ua
router = APIRouter(prefix="/fact/ua", tags=["Українська версія"])


@router.get("/",summary='Отримати рандомний факт',
            description="Отримай рандомний факт! Просто кликни 'try it out' -> 'execute' та отримай факти")
def get_fact():
    return get_facts_ua()