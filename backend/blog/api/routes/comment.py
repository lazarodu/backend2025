from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from blog.api.deps import comment_repo
from blog.usecases.comment.add_comment import AddCommentUseCase
from blog.usecases.comment.delete_comment import DeleteCommentUseCase
from blog.usecases.comment.get_comments_by_post import GetCommentsByPostUseCase
from blog.usecases.comment.get_comments_by_user import GetCommentsByUserUseCase
from blog.domain.entities.comment import Comment
import uuid

router = APIRouter()

class AddCommentRequest(BaseModel):
    postId: str
    userId: str
    comment: str
    data: str

class CommentResponse(BaseModel):
    id: str
    postId: str
    userId: str
    comment: str
    data: str

@router.get("/post/{post_id}", response_model=List[CommentResponse])
def get_comments_by_post(post_id: str):
    usecase = GetCommentsByPostUseCase(comment_repo)
    comments = usecase.execute(post_id)
    return comments

@router.get("/user/{user_id}", response_model=List[CommentResponse])
def get_comments_by_user(user_id: str):
    usecase = GetCommentsByUserUseCase(comment_repo)
    comments = usecase.execute(user_id)
    return comments

@router.post("/", response_model=CommentResponse)
def add_comment(data: AddCommentRequest):
    comment = Comment(
        id=str(uuid.uuid4()),
        postId=data.postId,
        userId=data.userId,
        comment=data.comment,
        data=data.data
    )
    usecase = AddCommentUseCase(comment_repo)
    added_comment = usecase.execute(comment)
    return added_comment

@router.delete("/{comment_id}")
def delete_comment(comment_id: str):
    usecase = DeleteCommentUseCase(comment_repo)
    success = usecase.execute(comment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}
