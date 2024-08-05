from config import db

class Contact(db.Model):
  id = db.column(db.Integer,primary_key=True)
  first_name = db.column(db.String(50),unique=False,nullable=False)
  last_name = db.column(db.String(50),unique=False,nullable=False)
  email = db.column(db.String(100),unique=True,nullable=False)

  def to_json(self):
    return {
      "id": self.id,
      "firstName": self.first,
      "lastName": self.last_name,
      "email": self.email,
    }

  