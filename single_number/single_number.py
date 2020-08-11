'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # create an empty dictionary
    dict = {}
    # loop for number in the array store the number of occured
    for number in arr:
        if number in dict: 
            # count how many times it appears
            dict[number] += 1
        else:
            dict[number] = 1

    # loop through the dictionary key and check which one has only one value
    for number in dict:
        if dict[number] == 1:    
            return number
        

    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")