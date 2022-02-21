from fastapi import FastAPI

from domain.controllers import evaluation

app = FastAPI()


app.include_router(evaluation.router)
