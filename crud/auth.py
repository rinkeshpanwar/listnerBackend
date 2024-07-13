from db.base import auth_db
from schema import auth
from db.base import pwd_context
from sqlalchemy.orm import Session
from models.user import User as userModal
class Auth:
    def getUser(self, username: str, db: Session):
        # return auth_db.fetch({"username": username})
        return db.query(userModal).filter(userModal.user_name == username).first()

    def createUser(self, user: auth.Createuser, db: Session):
        db_user = userModal()
        db_user.user_name = user.username
        db_user.password = pwd_context.hash(user.password)
        db.add(db_user)
        db.commit()
        db.flush()
        return {"username": db_user.user_name}

    def getAllUsers(self, db:Session):
        return db.query(userModal).all()

AUTHCrud = Auth()