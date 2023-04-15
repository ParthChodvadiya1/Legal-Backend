import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Users
user_collection = database.get_collection("users_collection")


def user_helper(user) -> dict:

    return {
        "id": str(user["_id"]),
        "userID": user["userID"],
        "email": user["email"],
        "userName": user["userName"],
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "middleName": user["middleName"],
        "loginProvider": user["loginProvider"],
        "bio": user["bio"],
        "gender": user["gender"],
        "birthDate": user["birthDate"],
        "birthYear": user["birthYear"],
        "userStatus": user["userStatus"],
        "userRole": user["userRole"],
        "lastSessionStartTime": user["lastSessionStartTime"],
        "lastLoginAt": user["lastLoginAt"],
        "lastSessionEndTime": user["lastSessionEndTime"],
        "failedAttempts": user["failedAttempts"],
        "signinCount": user["signinCount"],
        "token": user["token"],
        "unlockToken": user["unlockToken"],
        "resetPasswordSentAt": user["resetPasswordSentAt"],
        "resetPasswordToken": user["resetPasswordToken"],
        "deviceId": user["deviceId"],
        "deviceToken": user["deviceToken"],
        "ipv6": user["ipv6"],
        "ipv4": user["ipv4"],
        "deviceType": user["deviceType"],
        "deviceOs": user["deviceOs"],
        "location": user["location"],
        "meta": user["meta"],
        "createdAt": user["createdAt"],
        "updatedAt": user["updatedAt"],
        "isDeleted": user["isDeleted"],
        "createdBy": user["createdBy"],
        "updatedBy": user["updatedBy"],
    }

# Retrieve all users present in the database


async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
