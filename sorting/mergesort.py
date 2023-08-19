#timeit is a python library that helps us to compute the time analysis for our program
import timeit

# starting time

def merge_sort(array):
# this function divides all the elements by 2 recursively into left anf right until the array length becomes 2.   
    if len(array)>1:
        
        middle_ele=len(array)//2
#left split contains start to middle element
        left_split=array[:middle_ele]
# right split contains middle element + 1 until last element 
        right_split=array[middle_ele:]
        merge_sort(left_split)
        merge_sort(right_split)
# calling merge function to conquer now that we have completed dividing
        merge(array,left_split,right_split)

def merge(array, left_split, right_split):
#creating temp arrays to store the divided elements while swapping it if needed as a way of sorting
    x=y=z=0
    
    while x< len(left_split) and y<len(right_split):

        if left_split[x]< right_split[y]:
            array[z]=left_split[x]
            x+=1
        else:
            array[z]=right_split[y]
            y+=1
        z+=1
        
    while x<len(left_split):
            array[z]=left_split[x]
            x=x+1
            z=z+1
            
    while y<len(right_split):
            array[z]=right_split[y]
            y=y+1
            z=z+1
        
def print_element(array):
    print("The sorted array is:")
# sorted_array contains elements that are sorted. We pass the elements into a loop to print all the elements.    
    for var in range(len(array)):
        print (str(var+1)+') '+str(array[var]))
    print()
      
    
if __name__ == '__main__':
   
    print("\n")
    print("                   ---------------------            ")
    print("                   MERGE SORT ALGORITHM             ")
    print("                   ---------------------            ")
    print("\n")
    
    print("Choose from one of the below 4 options to perform Merge sort using divide and conquer:")
# In random_number.py we have generated 4 methods to create 4 text files having array of 20,100,1000,4000 elements that ranges from 0 to 6000.
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
# Calling the function to perform merge sort
        merge_sort(array)
# Stopping the timer for runtime calculation.
        stop = timeit.default_timer()
# Calling the function to print the sorted elements
        print_element(array)
        print('Time: ', stop - start)
        

    elif(input_user=='2'):
        input_file = open('C:/Users/ADMIN/Desktop/CSE5311-02-P1-1001854976-1001960012/arr100.txt', 'r')
        input_lines = input_file.readlines()
        str1 = ""
        str1 = str1.join(input_lines)
        arr = str1[1:len(str1)-1].split(", ")
        array = [int(numeric_string) for numeric_string in arr]
        start = timeit.default_timer()
        merge_sort(array)
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
        merge_sort(array)
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
        merge_sort(array)
        stop = timeit.default_timer()
        print_element(array)
        print('Time: ', stop - start)
    else:
        print("Enter a valid choice!")    

