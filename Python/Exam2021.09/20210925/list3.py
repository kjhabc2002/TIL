
date = [] #빈리스트생성

x=int(input("1일차 턱걸이 횟수 >>>"))
date.append(x)

x=int(input("2일차 턱걸이 횟수 >>>"))
date.append(x)

x=int(input("3일차 턱걸이 횟수 >>>"))
date.append(x)

x=int(input("4일차 턱걸이 횟수 >>>"))
date.append(x)

x=int(input("5일차 턱걸이 횟수 >>>"))
date.append(x)

x=int(input("6일차 턱걸이 횟수 >>>"))
date.append(x)

x=int(input("7일차 턱걸이 횟수 >>>"))
date.append(x)

total=date[0]+date[1]+date[2]+date[3]+date[4]+date[5]+date[6]
avg = total/7

print(int(avg))