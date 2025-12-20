from fastapi import FastAPI
from router.user_route import user_route
from router.cat_route import cat_router
from router.authors import authors_route
from router.book_route import book_route
from router.reviews import review_route
app=FastAPI()

app.include_router(user_route)
app.include_router(cat_router)
app.include_router(authors_route)
app.include_router(book_route)
app.include_router(review_route)