from bdb import set_trace
from fastapi import APIRouter, Body, Request, Form
from fastapi.encoders import jsonable_encoder
from elasticsearch import Elasticsearch, helpers
from server.models.search import Esearch, IDsearch, SearchHigh ,IdSearchHigh
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse 
from elasticsearch_dsl import Search

from server.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()
es = Elasticsearch()
templates = Jinja2Templates(directory="utils/")


# For create
@router.post("/", response_description="user data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "user added successfully.")


# For read
@router.get("/", response_description="users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")


# For update
@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "user with ID: {} name update is successful".format(id),
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


# For delete
@router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )


@router.post("/search", response_description="docs retrive successfully")
async def search_es(item: Esearch):

    search_body = jsonable_encoder(item)
    search_query = search_body.get('user_query')
    data = es.search(index="my-inde", body={"query": {
        "multi_match": {
            "query": f"{search_query}",
            "fields": ["content"]
        }
    }})

    meta_list = []
    id_list = []
    # content_list = []
    for i in data['hits']['hits']:

        id_list.append(i["_id"])
        meta_list.append(i["_source"]["metadata"])
        # content_list.append(i["_source"]["content"])

    obj = []
    for (id, meta) in zip(id_list, meta_list):
        obj.append({
            "id": id,
            "meta": meta,
            # "content":content,
        })

    return JSONResponse(content=obj)




@router.post("/search_id", response_description="docs retrive successfully")
async def search_id(item: IDsearch):
    search_body = jsonable_encoder(item)
    search_id = search_body.get('id')
    es = Elasticsearch()
    data = es.search(index="my-inde", body={"query": {
        "ids": {
            "values": [f"{search_id}"]}
    }})
    meta_list = []
    content_list = []
    for i in data['hits']['hits']:
        meta_list.append(i["_source"]["metadata"])
        content_list.append(i["_source"]["content"])
    con = []
    for (meta, content) in zip(meta_list, content_list):
        con.append({
            "meta": meta,
            "content": content
        })
    return JSONResponse(content=con)


@router.post("/search_high", response_description="docs retrive successfully")
async def search_hi(item: SearchHigh):
    search_body = jsonable_encoder(item)
    user_quer = search_body.get('user_quer')
    data = es.search(index="my-inde", body={
        "query": {
            "multi_match": {
                "query": f"{user_quer}",
                # "fields": ["content"]
        }
                },
        "highlight": {
            "type": "unified",
            "number_of_fragments" : 3,
            "fields": {
                "content": {
                    "type":"unified"
                }
            }
        }
    })
    print(item)

    id_list = []
    meta_list = []
    content_list = []

    for i in data['hits']['hits']:
        id_list.append(i["_id"])
        meta_list.append(i["_source"]["metadata"])
        content_list.append(i["_source"]["content"])
    
        
    highli = []
    
    
    
    for (id, meta, content) in zip(id_list, meta_list, content_list):
        highli.append({
            "id": id,
            "meta": meta,
            "content":content,
        })
    
    return JSONResponse(content=highli)


#9o0S1X4BeM9qhV91PzQT
#heer
@router.post("/search_", response_description="docs retrive successfully")
async def search_hi(item: IdSearchHigh):
    search_body = jsonable_encoder(item)
    user_query= search_body.get('user_query')
    id=search_body.get('id')
    
    data = es.search(index="my-inde", body={
        "query": {
            "multi_match": {
                "query": f"{user_query}",
                # "fields": ["content"]
        }
                },
        "highlight": {
            "type": "unified",
            "number_of_fragments" : 3,
            "fields": {
                "content": {
                    "type":"unified"
                }
            }
        }
    })
    
    
   
    id_list = []
    meta_list = []
    content_list = []
    #new_content=[]
    for i in data['hits']['hits']:
        if i["_id"]==id:
            id_list.append(i["_id"])
            meta_list.append(i["_source"]["metadata"])
            content_list.append(i["_source"]["content"])
            
            # for j in content_list:
            #     for i in j:
            #         k=[]
            #         i=i.replace(f"{user_query}",'<mark>'+f"{user_query}"+'</mark>')
 
            #     k.append(i)
            # new_content.append(k)
    highli = []
    
    for (id, meta, content) in zip(id_list, meta_list, content_list):
        highli.append({
            "id": id,
            "meta": meta,
            "content":content,
        })
    list={"error":"id not found"}
    if len(highli)==0:
        return JSONResponse(content=list)
        
    return JSONResponse(content=highli)

@router.post("/search_hi", response_description="docs retrive successfully")
async def search_es(item: Esearch):

    search_body = jsonable_encoder(item)
    search_query = search_body.get('user_query')
    data = es.search(index="my-inde", body={"query": {
        "multi_match": {
            "query": f"{search_query}",
            "fields": ["content"]
        }
    }})

    meta_list = []
    id_list = []
    content_list = []
    new_content=[]
    for i in data['hits']['hits']:

        id_list.append(i["_id"])
        meta_list.append(i["_source"]["metadata"])
        content_list.append(i["_source"]["content"])
        
        
    

    obj = []
    for (id, meta,content) in zip(id_list, meta_list,content_list):
        obj.append({
            "id": id,
            "meta": meta,
            "content":content,
        })

    return JSONResponse(content=obj)

"""

     "highlight": {
    "type" : "unified",
    "number_of_fragments" : 3,
    "fields": {
      "content": {}
                }
            
        }
    })
    id_list = []
    meta_list = []
    content_list = []
    extra=[]
    for i in data['hits']['hits']:
        id_list.append(i["_id"])
        meta_list.append(i["_source"]["metadata"])
        content_list.append(i["_source"]["content"])
        extra.append(i["highlight"]["content"])
    print(extra)
"""