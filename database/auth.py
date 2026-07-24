import re
import bcrypt
from database.database import Database

class Auth:

  def __init__(self):
    self.db=Database().get_client()

  def valid_email(self,email):
    pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern,email)

  def valid_password(self,password):
    if len(password)<8:
      return False
    if not re.search(r"[A-Z]",password):
      return False
    if not re.search(r"[a-z]",password):
      return False
    if not re.search(r"\d",password):
      return False
    return True

  def register(self,username,email,password):
    if not self.valid_email(email):
      return "Invalid Email"
    if not self.valid_password(password):
      return "Weak Password"
    hashed=bcrypt.hashpw(
      password.encode(),
      bcrypt.gensalt()
    ).decode()

    existing=(
      self.db.table("users")
      .select("*")
      .eq("email",email)
      .execute()
    )

    if existing.data:
      return"Email Exists"
    self.db.table("users").insert({
      "username":username,
      "email":email,
      "password":hashed
    }).execute()
    return"Success"


  def login(self,email,password):
    result=(
      self.db.table("users")
      .select("*")
      .eq("email",email)
      .execute()
    )
    if not result.data:
      return None
    user=result.data[0]

    if bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    ):
        return{
          "id":user["id"],
          "username":user["username"],
          "email":user["email"]
        }

    return None