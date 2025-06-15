from fastapi import FastAPI
from blog.api.routes import user, post, comment

app = FastAPI(title="Blog API", version="1.0.0")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])
app.include_router(comment.router, prefix="/comments", tags=["Comments"])
