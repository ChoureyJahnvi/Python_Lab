def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
num = int(input("Enter any number: "))
answer = fact(num)
print("Factorial of number is", answer)
