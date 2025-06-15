from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from blog.api.deps import post_repo
from blog.usecases.post.create_post import CreatePostUseCase
from blog.usecases.post.delete_post import DeletePostUseCase
from blog.usecases.post.get_all_posts import GetAllPostsUseCase
from blog.usecases.post.get_post_by_id import GetPostByIdUseCase
from blog.usecases.post.update_post import UpdatePostUseCase
from blog.domain.entities.post import Post
import uuid

router = APIRouter()

class PostCreateRequest(BaseModel):
    title: str
    description: str
    content: str
    autor: str
    data: str

class PostUpdateRequest(BaseModel):
    title: str
    description: str
    content: str
    autor: str
    data: str

class PostResponse(BaseModel):
    id: str
    title: str
    description: str
    content: str
    autor: str
    data: str

@router.get("/", response_model=List[PostResponse])
def get_all_posts():
    usecase = GetAllPostsUseCase(post_repo)
    posts = usecase.execute()
    return posts

@router.get("/{post_id}", response_model=PostResponse)
def get_post_by_id(post_id: str):
    usecase = GetPostByIdUseCase(post_repo)
    post = usecase.execute(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/", response_model=PostResponse)
def create_post(data: PostCreateRequest):
    post = Post(
        id=str(uuid.uuid4()),
        title=data.title,
        description=data.description,
        content=data.content,
        autor=data.autor,
        data=data.data
    )
    usecase = CreatePostUseCase(post_repo)
    created_post = usecase.execute(post)
    return created_post

@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: str, data: PostUpdateRequest):
    usecase_get = GetPostByIdUseCase(post_repo)
    existing_post = usecase_get.execute(post_id)
    if not existing_post:
        raise HTTPException(status_code=404, detail="Post not found")

    updated_post = Post(
        id=post_id,
        title=data.title,
        description=data.description,
        content=data.content,
        autor=data.autor,
        data=data.data
    )
    usecase_update = UpdatePostUseCase(post_repo)
    result = usecase_update.execute(updated_post)
    return result

@router.delete("/{post_id}")
def delete_post(post_id: str):
    usecase = DeletePostUseCase(post_repo)
    success = usecase.execute(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
