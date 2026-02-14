import uvicorn
from fastapi import FastAPI
from routers.facts_en import router as fact_en
from routers.facts_ua import router as fact_ua

app = FastAPI()
app.include_router(fact_en)
app.include_router(fact_ua)
if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)