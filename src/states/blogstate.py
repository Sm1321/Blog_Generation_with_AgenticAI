from typing import TypedDict
from pydantic import BaseModel,Field





class Blog(BaseModel):
    title:str = Field(description = "The Title of the BLog Post")
    content:str = Field(description = "The main contnet of the blog post")


class BlogState(TypedDict):
    topic:str 
    blog:Blog
    current_language:str
        