def even_value():
    result = [x*y for x in range(2,10)
        for y in range(1,7)]
    print(result)

print(even_value())