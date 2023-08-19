#timeit is a python library that helps us to compute the time analysis for our program
import timeit
# Function to perform insertion sort
def insertionSort(arr):
# Traverse through 1 to len(arr)
    for var_1 in range(1, len(arr)):
        key = arr[var_1]
        var_2 = var_1-1
        while var_2 >=0 and key < arr[var_2] :
                arr[var_2+1] = arr[var_2]
                var_2 = var_2-1
        arr[var_2+1] = key
    
def print_element(sorted_array):
    print("The sorted array is:")
# sorted_array contains elements that are sorted. We pass the elements into a loop to print all the elements.
    for var_3 in range(len(sorted_array)):
        print (str(var_3+1)+') '+str(sorted_array[var_3]))
    print()
           
if __name__ == '__main__':
    print("\n")
    print("                   ---------------------            ")
    print("                   INSERTION SORT ALGORITHM             ")
    print("                   ---------------------            ")
    print("\n")
    
    
    print("Choose from one of the below 4 options to perform Insertion sort:")
# In random_number.py we nhave generated 4 methods to create 4 text files having array of 20,100,1000,4000 elements that ranges from 0 to 6000.
    print("1: Array of 20 elements, 2: Array of 100 elements, 3: Array of 1000 elements, 4: Array of 4000 elements")
    input_user = input("Enter the the choice 1 or 2 or 3 or 4  ")
# User chooses 1 among the 4 files to perfom the sorting.
    if (input_user=='1'):
# Reading the file
        input_file = open('C:/Users/ADMIN/Desktop/CSE5311-02-P1-1001854976-1001960012/arr20.txt', 'r')
        input_lines = input_file.readlines()
        str1 = ""
# Converting the input_lines into a string format and appending it to the variable arr which is of type list with commas
        str1 = str1.join(input_lines)
        arr = str1[1:len(str1)-1].split(", ")
# Converting the arr elements into integer elements by passing it into a loop
        array = [int(numeric_string) for numeric_string in arr]
# Starting the timer for runtime calculation.
        start = timeit.default_timer()
# Calling the function to perform insertion sort
        insertionSort(array)
# Stopping the timer for runtime calculation.
        stop = timeit.default_timer()
# Calling the function to print the sorted elements
        print_element(array)
        print('Time it took to sort the elements: ', stop - start)
    elif(input_user=='2'):
        input_file = open('C:/Users/ADMIN/Desktop/CSE5311-02-P1-1001854976-1001960012/arr100.txt', 'r')
        input_lines = input_file.readlines()
        str1 = ""
        str1 = str1.join(input_lines)
        arr = str1[1:len(str1)-1].split(", ")
        array = [int(numeric_string) for numeric_string in arr]
        start = timeit.default_timer()
        insertionSort(array)
        stop = timeit.default_timer()
        print_element(array)
        print('Time: ', stop - start)
    elif(input_user=='3'):
        input_file = open('C:/Users/ADMIN/Desktop/CSE5311-02-P1-1001854976-1001960012/arr1000.txt', 'r')
        input_lines = input_file.readlines()
        str1 = ""
        str1 = str1.join(input_lines)
        arr = str1[1:len(str1)-1].split(", ")
        array = [int(numeric_string) for numeric_string in arr]
        start = timeit.default_timer()
        insertionSort(array)
        stop = timeit.default_timer()
        print_element(array)
        print('Time: ', stop - start)
    elif(input_user=='4'):
        input_file = open('C:/Users/ADMIN/Desktop/CSE5311-02-P1-1001854976-1001960012/arr4000.txt', 'r')
        input_lines = input_file.readlines()
        str1 = ""
        str1 = str1.join(input_lines)
        arr = str1[1:len(str1)-1].split(", ")
        array = [int(numeric_string) for numeric_string in arr]
        start = timeit.default_timer()
        insertionSort(array)
        stop = timeit.default_timer()
        print_element(array)
        print('Time: ', stop - start)
    else:
        print("Enter a valid choice!")    
    
    
