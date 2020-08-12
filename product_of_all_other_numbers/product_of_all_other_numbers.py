'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # check the length of the array
    n = len(arr)

    # create lists for left and right products and also for the result
    left = [1 for _ in range(n)]
    right = [1 for _ in range(n)]
    result = []

    # calculate the left product first
    for i in range(1, n):
        left[i] = left[i - 1] * arr[i - 1]

    # calculate the right product
    # starts from the right side and because it's python you need to -1 
    # and another -1 because we skip the last number so it becomes -2
    for i in range(n-2, -1, -1):
        right[i] = right[i + 1] * arr[i + 1]

    # combine left and right by multiply and store in a new list
    for i in range(n):
        result.append(left[i] * right[i])

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
