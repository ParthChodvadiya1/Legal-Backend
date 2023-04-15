from typing import List, Optional
from pydantic import BaseModel


class Esearch(BaseModel):
    user_query: Optional[str]
    
class IDsearch(BaseModel):
    id: Optional[str]
    
class SearchHigh(BaseModel):
    user_quer: Optional[str]

class IdSearchHigh(BaseModel):
    user_query: Optional[str]
    id: Optional[str]
