from optparse import Option
from typing import Dict, Optional, List
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr, Field

# now = datetime.now()
# class LatLong(BaseModel):
#     lat : Optional[int]
#     long : Optional[int]


class LocationSchema(BaseModel):
    type: Optional[str]
    coardinates: Optional[List[int]] = [1234.2, 234.3]


class UserSchema(BaseModel):
    userID: str
    email: str
    userName: str
    firstName: str
    lastName: str
    middleName: str
    loginProvider: str
    bio: str
    gender: str
    birthDate: str
    birthYear: str
    userStatus: str
    userRole: str
    lastSessionStartTime: Optional[datetime] = Field(
        ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    lastLoginAt: Optional[datetime] = Field(
        ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    lastSessionEndTime: Optional[datetime] = Field(
        ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    failedAttempts: int
    signinCount: int
    token: str
    unlockToken: str
    resetPasswordSentAt: Optional[datetime] = Field(
        ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    resetPasswordToken: str
    deviceId: str
    deviceToken: str
    ipv6: str
    ipv4: str
    deviceType: str
    deviceOs: str
    meta: str
    createdAt: Optional[datetime] = Field(
        ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    updatedAt: Optional[datetime] = Field(
        ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    isDeleted: Optional[bool] = True
    createdBy: Optional[str]
    location: Optional[LocationSchema]
    updatedBy: str

    class Config:
        schema_extra = {
            "example": {
                "userID": "kuytfvghj",
                "email": "akshit@gmail.com",
                "userName": "iuytfghj",
                "firstName": "iuytfdxcvhn",
                "lastName": "uygfvhjn",
                "middleName": "uyghj",
                "loginProvider": "uytrtyh",
                "bio": "iuytgjhc",
                "gender": "jytghg",
                "birthDate": "12/3/21",
                "birthYear": "2022",
                "userStatus": "uytrfygf",
                "userRole": "juytfguhg",
                "lastSessionStartTime": "2019-04-01T00:00:00.000Z",
                "lastLoginAt": "2019-04-01T00:00:00.000Z",
                "lastSessionEndTime": "2019-04-01T00:00:00.000Z",
                "failedAttempts": "1",
                "signinCount": "1",
                "token": "uytrfgyhgtyuytrfty",
                "unlockToken": "gfghjh",
                "resetPasswordSentAt": "2019-04-01T00:00:00.000Z",
                "resetPasswordToken": "juytghj",
                "deviceId": "yghujhgfhh",
                "deviceToken": "htguytgyuytgh",
                "ipv6": "ytfghhtrfghuyg",
                "ipv4": "iuytghjgfg",
                "deviceType": "uytghuytfghyt",
                "deviceOs": "iuytghuytghyg",
                "meta": "null",
                "createdAt": "2019-04-01T00:00:00.000Z",
                "updatedAt": "2019-04-01T00:00:00.000Z",
                "isDeleted": "False",
                "createdBy": "frgthtfd",
                "location": {"type": "Points", "cordinates": [12.12, 34.34]},
                "updatedBy": "eatrytykjt",
            }
        }


class UpdateUserModel(BaseModel):
    userID: Optional[str]
    email: Optional[EmailStr]
    userName: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    middleName: Optional[str]
    loginProvider: Optional[str]
    bio: Optional[str]
    gender: Optional[str]
    birthDate: Optional[str]
    birthYear: Optional[str]
    userStatus: Optional[str]
    userRole: Optional[str]
    failedAttempts: Optional[int]
    signinCount: Optional[int]
    token: Optional[str]
    unlockToken: Optional[str]
    resetPasswordToken: Optional[str]
    deviceId: Optional[str]
    deviceToken: Optional[str]
    ipv6: Optional[str]
    ipv4: Optional[str]
    deviceType: Optional[str]
    deviceOs: Optional[str]
    location: Optional[str]
    meta: Optional[str]
    isDeleted: Optional[bool] = True
    createdBy: Optional[str]
    location: Optional[LocationSchema]
    updatedBy: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "userID": "kuytfvghj",
                "email": "akshit@gmail.com",
                "userName": "iuytfghj",
                "firstName": "iuytfdxcvhn",
                "lastName": "uygfvhjn",
                "middleName": "uyghj",
                "loginProvider": "uytrtyh",
                "bio": "iuytgjhc",
                "gender": "jytghg",
                "birthDate": "12/3/21",
                "birthYear": "2022",
                "userStatus": "uytrfygf",
                "userRole": "juytfguhg",
                "failedAttempts": "1",
                "signinCount": "1",
                "token": "uytrfgyhgtyuytrfty",
                "unlockToken": "gfghjh",
                "resetPasswordToken": "juytghj",
                "deviceId": "yghujhgfhh",
                "deviceToken": "htguytgyuytgh",
                "ipv6": "ytfghhtrfghuyg",
                "ipv4": "iuytghjgfg",
                "deviceType": "uytghuytfghyt",
                "deviceOs": "iuytghuytghyg",
                "meta": "null",
                "isDeleted": "False",
                "createdBy": "frgthtfd",
                "location": {"type": "Points", "cordinates": [12.12, 34.34]},
                "updatedBy": "eatrytykjt",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
