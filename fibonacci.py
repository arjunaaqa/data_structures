def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter which term of fibonacci sequence you want to know - "))
    result = fibonacci(n-1)
    print(f"{n}th term of fibonacci sequnce is {result}")

if __name__ == "__main__":
    main()