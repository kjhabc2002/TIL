# class만들기
class Database:
  def __init__(self, name, size):
  # 아래에 코드를 작성해 주세요.
    self.name= name
    self.size= size
    self.db={}
  
    
  def insert(self, field, value):
   # 아래에 코드를 작성해 주세요.
    if len(self.db) < self.size:
      self.db[field] = value
  
  def select(self, field):
   # 아래에 코드를 작성해 주세요.
    if field in self.db:
      return self.db[field]
    else:
      return None
  
  def update(self, field, value):
    if field in self.db:
      self.db[field] = value
      
  def delete(self, field):
    if field not in self.db:
      return
    else:
      del self.db[field]

test=Database("정우성",10)
print(test)
