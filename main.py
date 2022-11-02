from typing import Union
from fastapi import FastAPI
from mongo import add_suggestion, vote
from models import suggestion


app = FastAPI()

# land on main page
@app.get("/")
def read_root():
    return {"Hello": "World"}

# create new suggestion
@app.post("/new-suggestion")
def suggestion_post(sugestion: suggestion):
    add_suggestion(sugestion.__dict__)
    return {"Status": "200", "Mensagem": "Sugestao adicionada com sucesso!"}

# update vote for suggestion
@app.put("/{suggestion_id}")
def vote(suggestion_id: mongoose.Types.ObjectId, sugestion: suggestion):
    vote(suggestion_id, sugestion.__dict__)
    return {"Status": "200", "Mensagem": "Voto Registrado!"}


# upvote/downvote
#@app.put



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}