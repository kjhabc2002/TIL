def remove_odd_numbers(numbers):
    # 여기에 코드를 작성해주세요.
  if(numbers[4] % 2 == 1):
    del numbers[4]
  if(numbers[3] % 2 == 1):
    del numbers[3]
  if(numbers[2] % 2 == 1):
    del numbers[2]
  if(numbers[1] % 2 == 1):
    del numbers[1]
  if(numbers[0] % 2 == 1):
    del numbers[0]
  
  return numbers

input=[1, 2, 3, 4, 5];

print(remove_odd_numbers(input));