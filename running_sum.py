"""
Given a one-dimensional array of integers, create a new array that represents the running sum of the original array.

The running sum at position i in the new array is calculated as the sum of all the numbers in the original array from the 0th index up to the i-th index (inclusive). Formally, the resulting array should be computed as follows: result[i] = sum(nums[0] + nums[1] + ... + nums[i]) for each i from 0 to the length of the array minus one.

Examples
Example 1

Input: [2, 3, 5, 1, 6]
Expected Output: [2, 5, 10, 11, 17]
Justification:
For i=0: 2
For i=1: 2 + 3 = 5
For i=2: 2 + 3 + 5 = 10
For i=3: 2 + 3 + 5 + 1 = 11
For i=4: 2 + 3 + 5 + 1 + 6 = 17
"""

def running_sum(arr):
    run_sum_arr = [0] * len(arr)
    run_sum_arr[0] = arr[0]
    for i in range(len(arr)):
        run_sum_arr[i] = run_sum_arr[i-1] + arr[i]
    return run_sum_arr

def main():
    arr = input("Enter the imput array: ")
    if arr is None or len(arr)==0:
        print(f"Input is None or empty")
        exit()
    arr = arr.split(",")
    arr = [int(x) for x in arr ]
    print(f"Input is {arr}")
    run_sum_arr = running_sum(arr)
    print(f"Output is {run_sum_arr}")
    pass

if __name__ == "__main__":
    main()






