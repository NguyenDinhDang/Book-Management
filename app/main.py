from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import author, category, book

app = FastAPI(
    title="Book management API",
    description="Simple API to manage books, author, category add book cover",
    version="1.0.0"
)

#include router

app.include_router(author.router, prefix="/authors", tags=["Author"])
app.include_router(category.router, prefix="/category", tags=["Category"])
app.include_router(book.router, prefix="/books", tags=["Books"])

#static file for cover image

@app.get("/")
def read_root():
    return{"message":"Book management is running"}
