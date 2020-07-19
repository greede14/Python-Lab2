fibo = [0,1]
i = 1
x = "null"
while x != "exit" :
    n = int(input("Enter n: "))
    

    while i <= n :
        fibo.append(fibo[i] + fibo[i-1])
        i+=1
    print("fib(%i) =" %(n), fibo[n])
    x = input("To exit program type 'exit' : ")