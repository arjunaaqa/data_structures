import time

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[len(array) // 2]
    left = [ x for x in array if x < pivot]
    middle = [ x for x in array if x == pivot]
    right = [ x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)




def main():
    array = [1, 11, 7, 3, 9, 2, 5]
    start_time = time.perf_counter()
    result = bubble_sort(array)
    end_time = time.perf_counter()
    print(f"Sorted array is {array}")
    time_taken = float(end_time - start_time)
    print(f"Bubble sort time taken is {time_taken: .10f} seconds")

    array = [1, 11, 7, 3, 9, 2, 5]
    start_time = time.perf_counter()
    sorted_array = quick_sort(array)
    end_time = time.perf_counter()
    time_taken = float(end_time - start_time)
    print(f"Sorted array is {sorted_array}")
    print(f"Quick sort time taken is {time_taken:.10f} seconds")

if __name__ == "__main__":
    main()