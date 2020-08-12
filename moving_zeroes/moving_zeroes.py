'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # set a new index to zero as a start
    new_index = 0

    # start inserting the number that isn't zero to the new list by looping 
    # the original list

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[new_index] = arr[i]
            new_index += 1

    # add the number that is zero to the new list at the end
    for i in range(new_index, len(arr)):
        arr[i] = 0

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")