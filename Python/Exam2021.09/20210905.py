def list_for_loops():
    # 아래의 코드를 수정하지 마세요.
    my_list = []

    # 아래에 코드를 작성해주세요.
    for i in range(9,0,-2):
      my_list.append(i)
    
    # 아래의 코드를 수정하지 마세요.
    return my_list
#print(list_for_loops())

def list_loop():
    # 아래의 코드를 수정하지 마세요.
    my_list = [2, 3, 4, 5, 6]

    # 아래에 코드를 작성해 주세요.
    total=0;
    for i in my_list:
      total+=sum(my_list);

    # 아래의 코드를 수정하지 마세요.
    return total

#print(list_loop())

def get_all_letters():
    # 아래의 코드를 수정하지 마세요.
    str_list = []
    mission_str = "wecode"

    # 아래의 코드를 작성해주세요.
    for i in mission_str:
      mission_str.append[i]
      print(mission_str)

    # 아래의 코드를 수정하지 마세요.
    return str_list

#print(get_all_letters)

# 49. while loop문
def find_smallest_integer_divisor(num): 
    ## 아래 코드를 입력해주세요.
    start_num=1
    if num == 0:
        return 0;
    while start_num <= num:
      start_num+=1;
      if num % start_num == 0:
        return start_num
        break;


#print(find_smallest_integer_divisor(15))


class Database:
  def __init__(self, name, size):
  # 아래에 코드를 작성해 주세요.
    self.name= name
    self.size= size
    self.db={}
    
  def insert(self, field, value):
   # 아래에 코드를 작성해 주세요.
   #if len(self.db) < self.size:
    #self.db[field]=value;
    self.db("name", "정우성")
    print(self.db)
  #def select(self, field):
   # 아래에 코드를 작성해 주세요.
  
  #def update(self, field, value):

  
  #def delete(self, field):
sohn = Database("송승헌", 29)
print(sohn.name,sohn.size)