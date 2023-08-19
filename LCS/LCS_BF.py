import timeit #used for getting the time required to execute our code 

#function used to compute the common substring using bruteforce method 
def lcs_bf(str1,str2,len_strX,len_strY):      
    if len_strX == 0 or len_strY == 0: # checking if the strings are empty
        return 0
    elif str1[len_strX-1] == str2[len_strY-1]: # checking if the strings at their index are same 
        return 1 + lcs_bf(str1, str2, len_strX-1, len_strY-1);
    else: #if the charcter dont match we try taking the max of characters returned by either by moving str1 or str2 
        return max(lcs_bf(str1, str2, len_strX, len_strY-1), lcs_bf(str1, str2, len_strX-1, len_strY));

#please change the path according to your system where the text file is stored 
input_file = open('LCS1.txt', 'r') #opening file
input_lines = input_file.readlines() #reading the file 
dynamic_len_var=len(input_lines)
for i in range(dynamic_len_var):
    a = input_lines[i].split(',') #splitting the file input values by the commas 
    print(str(i) +":",a)
val=int(input("Enter the value from the indexes mentioned in the options shown above: ")) #fetching index val from user
a = input_lines[val].split(',') #splitting the file input values by the commas 
X = a[0] #assigning the first str to 0th index 
Y = a[1] #assigning the second str to 1st index 
m = len(X) #finding the len of 1st str
n = len(Y) #finding len of second str
start = timeit.default_timer() #starting timer
lcs_bf(X,Y,m,n) #calling function 
stop = timeit.default_timer() #ending timer
print("\n")
print("                   -------------------------------------            ")
print("                   LONGEST COMMON SEQUENCE - BRUTE FORCE             ")
print("                   -------------------------------------            ")
print("\n")
print ("Length of LCS in " +str(X)+" and "+str(Y)+" is ", lcs_bf(X,Y,m,n))
print("Time taken to find length of Longest Subsequence of strings "+str(X)+" and "+str(Y)+ " is:",str(stop-start)+" Seconds")

            


    
