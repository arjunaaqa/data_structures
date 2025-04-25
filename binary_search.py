
def binary_search(array, var):
    low = 0
    high = len(array)-1
    while(low<=high):
        mid = (low + high) // 2
        if array[mid]<var:
            low = mid+1
        elif array[mid]>var:
            high = mid-1
        else:
            return mid
    return -1

def main():
    array = [1, 3, 5, 7, 9]
    var = 3
    result = binary_search(array, var)
    if result == -1:
        print(f"Not found")
    else:
        print(f"Found at {result}")
    
if __name__ == "__main__":
    main()