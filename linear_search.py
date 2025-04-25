
def linear_search(array, var):
    for i in range (len(array)):
        if array[i] == var:
            return i
        return -1

def main ():
    array = [1, 3, 5, 7, 9]
    var = 3
    result = linear_search(array, var)
    if result != -1:
        print(f"Found at {result}")
    else:
        print(f"Not found")

if __name__ == "__main__":
    main()