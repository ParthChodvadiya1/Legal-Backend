from typing import Optional, List, Dict, Set
from pydantic import BaseModel, Field
from datetime import datetime

class DocsModel(BaseModel):
    category1: Optional[str]
    category2: Optional[str]
    category3: Optional[str]
    title: Optional[str]
    author: Optional[str]
    edition: Optional[str]
    tribunal: Optional[str]
    act:  Optional[str]
    href: Optional[str] = ""
    ref: Optional[List[str]] = []
    rel_ref: Optional[List[List[str]]] = [[]] 
    original_source: Optional[str] = ""
    html: Optional[str]
    view_count: int
    to_display: Optional[bool] = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)





