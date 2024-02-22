import pyjokes
from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()


@router.post("/get_jokes/", tags=["NLP"])
def get_joke():
    joke = pyjokes.get_joke()
    return joke
