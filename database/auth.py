import re
import bcrypt
import sqlite3
from database.database import Database

class Auth:

  def __init__(self):
    self.db=Database()

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
    )

    try:

      self.db.cursor.execute(
        """
        INSERT INTO users(username,email,password)
        VALUES(?,?,?)
        """,
        (username,email,hashed)
      )

      self.db.connection.commit()

      return "Success"

    except sqlite3.IntegrityError:
      return "Email Exists"

  def login(self,email,password):
    self.db.cursor.execute(
      """
      SELECT id,username,email,password
      FROM users
      WHERE email=?
      """,
      (email,)
    )

    user=self.db.cursor.fetchone()
    if user is None:
      return None
    if bcrypt.checkpw(
        password.encode(),
        user[3]
    ):
        return{
          "id":user[0],
          "username":user[1],
          "email":user[2]
        }

    return None