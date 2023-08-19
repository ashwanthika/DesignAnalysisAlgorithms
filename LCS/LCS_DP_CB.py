import timeit #used for getting the time required to execute our code 
import numpy as np #Used to print a structure like array

#please change the path according to your system where the text file is stored 
input_file = open('LCS2.txt', 'r') #opening the file 
input_lines = input_file.readlines() #reading the file
dynamic_len_var=len(input_lines)#Computing length
for i in range(dynamic_len_var):
    a = input_lines[i].split(',') #splitting the file input values by the commas 
    print(str(i) +":",a)
    
val=int(input("Enter the value from the indexes mentioned in the options shown above: ")) #fetching index val from user
a = input_lines[val].split(',') #splitting the file input values by the commas 
var1 = a[0] #assigning the first str to 0th index 
X = var1.rstrip('\n')
var2 = a[1] #assigning the second str to 1st index 
Y = var2.rstrip('\n')
print("The value at row:", X) #Row String
print("The value at column:", Y) #Column String
print("X=",X)
print("Y=",Y)
#printing the arrowmarks along with the function by backtracking from the last index of matrix by checking where \\ are. 
def lcs_print_get(arrow_array, X, val_1, val_2, final_res_arr):
    if val_1 == 0 or val_2 == 0:
        return ;
    if arrow_array[val_1][val_2] == '\\': #(we have used \\ since \ doesnt work and it terminates as it considers that eof)
        lcs_print_get(arrow_array, X, val_1-1, val_2-1, final_res_arr)
        final_res_arr.append(X[val_1-1])
    elif arrow_array[val_1][val_2] == '^':
        lcs_print_get(arrow_array, X, val_1-1, val_2, final_res_arr)
    else:
        lcs_print_get(arrow_array, X, val_1, val_2-1, final_res_arr)
        
        
 # function to compute lcs     
def LCS_DP_CB(X, Y):
    count_array = [[0]*(len(Y)+1) for val_1 in range(len(X)+1)] #array for count 
    arrow_array =  [['']*(len(Y)+1) for val_1 in range(len(X)+1)] #array that stores the arrow marks
    for index1, str1_name in enumerate(X): #enumerate will store values in the form of index:val in each varibale mentioned. that is, x1:x --> 0: p
        for index2, str2_name in enumerate(Y):
            val_1 = index1+1
            val_2 = index2+1
            if str1_name == str2_name: # if they are equal increment the count and recursively call 
                count_array[val_1][val_2] = count_array[val_1-1][val_2-1]+1
                arrow_array[val_1][val_2] = '\\' #update the arrow array with a \\ for that index 
            elif count_array[val_1-1][val_2] <= count_array[val_1][val_2-1]: # if they are <= 
                count_array[val_1][val_2] = count_array[val_1][val_2-1]  #Assign the greater value to our index
                arrow_array[val_1][val_2] = '<' #update the arrow array with < for that index
            else:
                count_array[val_1][val_2] = count_array[val_1-1][val_2] #Assign the greater value to our index
                arrow_array[val_1][val_2] = "^" #update the arrow array with > for that index
    return count_array, arrow_array #Return the computed results
start = timeit.default_timer() #starting timer
count_array, arrow_array = LCS_DP_CB(X, Y) #calling function
res=[[str(alpha) for alpha in sub] for sub in count_array]
#using numpy to add res that has string converted count_array and  arrow_array
new_array = np.char.add(arrow_array,res)
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print(new_array)
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

final_res_arr=[] 
lcs_print_get(arrow_array, X, len(X), len(Y), final_res_arr) #calling function
stop = timeit.default_timer() #ending timer
print (f"Length of longest common subsequence of " +str(X)+" and "+str(Y)+" is ",len(final_res_arr))
print(f'The longest common subsequence of '+str(X)+" and "+str(Y)+' is:',"".join(final_res_arr))
print("Time taken to find length of Longest Subsequence of strings  "+str(X)+ " and "+str(Y)+ " is:",str(stop-start)+" Seconds")