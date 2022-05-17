def roman_to_num(s):
    num={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #int로 초기값0 선언
    int=0
    #로마의 길이만큼 한글자씩 대입해가며
    for i in range(len(s)):
        if i > 0 and num[s[i]] > num[s[i - 1]]:
            #1번째 인덱스부터 해당 인덱스의 정수가 그 전 인덱스의 정수보다 큰지를 비교
            #
            int += num[s[i]] - 2 * num[s[i - 1]]
        else:
            int += num[s[i]]
    return int

print(roman_to_num('IX'))
