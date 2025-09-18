def fibonacci(n):
    a, b = 0 , 1
    # a= 1, b = 1
    # a = 1, b = 2
    # a = 2 , b =3

    for _ in range(n):
        
        print(a, end= " ")
        a, b = b , a + b 


fibonacci(10)




