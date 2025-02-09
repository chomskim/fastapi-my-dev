
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import users, posts, auth, vote

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  
models.Base.metadata.create_all(bind=engine)    

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World!!"}

# my_posts = [
#     {
#         "id": 1,
#         "title": "My first post",
#         "content": "This is the content of my first post",
#         "published": True,
#         "rating": 4,
#     },
#     {
#         "id": 2,
#         "title": "My second post",
#         "content": "This is the content of my second post",
#         "published": True,
#         "rating": 5,
#     },
#     {
#         "id": 3,
#         "title": "My third post",
#         "content": "This is the content of my third post",
#         "published": False,
#         "rating": 3,
#     },
# ]


# def find_index_post(post_id):
#     for i, post in enumerate(my_posts):
#         if post["id"] == post_id:
#             return i
#     return None


# @app.get("/sqlalchemy")
# def get_sqlalchemy(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}

# @app.get("/posts", response_model=list[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     # cursor.execute("SELECT * FROM posts")
#     # posts = cursor.fetchall()
#     # print (posts)
#     posts = db.query(models.Post).all()
#     return posts


# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # print(post)
#     # print(post.model_dump())
#     # post_dict = post.model_dump()
#     # post_dict["id"] = len(my_posts) + 1
#     # my_posts.append(post_dict)
#     # print(my_posts)
#     # cursor.execute(
#     #     "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
#     #     (post.title, post.content, post.published),
#     # )
#     # new_post = cursor.fetchone()
#     # conn.commit()
#     new_post = models.Post(**post.model_dump())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get("/posts/latest")
# def get_latest_post():
#     return {"data": my_posts[-1]}


# @app.get("/posts/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     # cursor.execute("SELECT * FROM posts WHERE id=%s", (id,))
#     # post = cursor.fetchone()
#     # post = next((post for post in my_posts if post["id"] == int(id)), None)
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} was not found",
#         )
#     return post


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     # post = next((post for post in my_posts if post["id"] == int(id)), None)
#     # if not post:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_404_NOT_FOUND,
#     #         detail=f"Post with id: {id} was not found",
#     #     )
#     # my_posts.remove(post)
#     # print(my_posts)

#     delete_post = db.query(models.Post).filter(models.Post.id == id).delete(synchronize_session=False)
#     if not delete_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} was not found",
#         )
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute(
#     #     "UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *",
#     #     (post.title, post.content, post.published, id),
#     # )
#     # updated_post = cursor.fetchone()   
#     # conn.commit()
#     print(post.model_dump())
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     updated_post = post_query.first()
#     print(type(updated_post.id), updated_post.title, updated_post.content, updated_post.published)
#     if not updated_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} was not found",
#         )
#     updated_count = post_query.update(post.model_dump(), synchronize_session=False)
#     print(type(updated_count), updated_count)
#     db.commit()
#     # db.refresh(updated_post)
#     # index = find_index_post(id)
#     # if index is None:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_404_NOT_FOUND,
#     #         detail=f"Post with id: {id} was not found",
#     #     )
#     # post_dict = post.model_dump()
#     # post_dict["id"] = id
#     # my_posts[index] = post_dict
#     return post_query.first()

# @app.get("/users", response_model=list[schemas.UserOut])
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get("/users/{id}", response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with id: {id} was not found",
#         )
#     return user

# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     # hash password
#     hashed_password = hash(user.password)
#     user.password = hashed_password

#     new_user = models.User(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
