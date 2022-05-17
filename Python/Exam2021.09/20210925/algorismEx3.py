def is_valid(string):
    # 리스트 이용
    left = ['(', '{', '[']
    right = [')', '}', ']']
    stack = []
    
    # letter변수는 string 문자열의 요소하나하나를 반복하겠다는 for반복문 선언
    for letter in string:
	    if letter in left:
		    stack.append(letter)
        #right 리스트의 요소들과 string요소가 서로 일치하는지 확인
	    elif letter in right:
        #  stack의 길이가 0보다 작거나 같다면 false
		    if len(stack) <= 0:
			    return False
		    if left.index(stack.pop()) != right.index(letter):
			    return False
   #stack배열의 길이가 0이면 True
   #stack은 letter에 담긴 문자가 right리스트안에 들어있는 요소와 일치하거나   
    return len(stack) == 0
     
print(is_valid('([)]'))
     
     