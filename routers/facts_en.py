from fastapi import APIRouter
from services.get_facts import get_facts_en

router = APIRouter(prefix='/fact/en', tags=['English version'])


@router.get("/",summary='Get a random fact', description= "Get a random fact! Just click 'try it out' -> 'execute' and get some facts.")
def get_fact():
    return get_facts_en()
