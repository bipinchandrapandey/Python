def fibonacci_Series(a):
    if a <= 0:
        return

    m = 0
    n = 1

    if a >= 1:
        print(m)

    if a >= 2:
        print(n)

    for i in range(2, a + 1):
        fibo = m + n
        print(fibo)
        m = n
        n = fibo

fibonacci_Series(int(input("Enter a number: ")))