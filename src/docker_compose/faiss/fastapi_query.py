from fastapi import FastAPI
from faiss_index import FAISSindex

import uvicorn


app = FastAPI()
faiss_search = FAISSindex()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/predict')
def read_item(prompt):
    return faiss_search.search_similar_docs(prompt, 1)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
