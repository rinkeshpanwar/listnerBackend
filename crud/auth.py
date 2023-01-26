from db.base import listner_db
from utils import utlis
from schema import auth
from db.base import pwd_context

class Auth:
    def getUser(self, username: str):
        return listner_db.fetch({"username": username, utlis.COLLECTION: utlis.USER_COLLECTION})

    def createUser(self, user: auth.Createuser):
        return listner_db.put({"username": user.username, "password": pwd_context.hash(user.password), utlis.COLLECTION: utlis.USER_COLLECTION})

    def getAllUsers(self):
        return listner_db.fetch({utlis.COLLECTION: utlis.USER_COLLECTION})

AUTHCrud = Auth()