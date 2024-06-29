from deta import Deta

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



deta = Deta("d0dl0fz4_MZw2CVP7BncUMX6mbScFqqTFHwsHD8rW")

listner_db = deta.Base("listner")
auth_db = deta.Base("auth")
question_db = deta.Base("question")
answer_db = deta.Base("answer")
