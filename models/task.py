class Task:

  def __init__(self,name, completed=False):
    self.name=name 
    self.completed=completed

  def toggle(self):
    self.completed=not self.completed

  def edit(self,newname):
    self.name=newname

  def to_dict(self):
    return{
      "name":self.name,
      "completed":self.completed
    }

  @classmethod
  def from_dict(cls,data):
    return cls(
      data["name"],
      data["completed"]
    )