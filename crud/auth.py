from db.base import auth_db
from schema import auth
from db.base import pwd_context

class Auth:
    def getUser(self, username: str):
        return auth_db.fetch({"username": username})

    def createUser(self, user: auth.Createuser):
        return auth_db.put({"username": user.username, "password": pwd_context.hash(user.password)})

    def getAllUsers(self):
        return auth_db.fetch()

AUTHCrud = Auth()