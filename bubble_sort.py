numbers_list = [64, 34, 25, 12, 7, 9, 11, 89, 23, 54]
def numbers_list_bubblesort(numbers_list):
    #get length of the list
    numbers_list_length = len(numbers_list)
    #loop through the list to find the numbers position
    for records in range(numbers_list_length - 1):
        # loop through the list to find the numbers position but in a reducing mannner
        for rec in range(0, numbers_list_length - records - 1):
            #compare the numbers if one is greater than the other and swap positions
            if numbers_list[rec] > numbers_list[rec + 1]:
                numbers_list[rec], numbers_list[rec + 1] = numbers_list[rec + 1], numbers_list[rec]
#call our numbers_list_bubblesort function with the numbers_list parameters
numbers_list_bubblesort(numbers_list)
for number in range(len(numbers_list)):
    print("%s" % numbers_list[number]) # makes sure that our code is working by printing the expected results
