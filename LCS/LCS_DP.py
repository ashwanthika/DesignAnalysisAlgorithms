import timeit #used for getting the time required to execute our code 

#performing dynamic programing of lcs function
def lcs_dp(str1, str2):   
    len_str1=len(str1) #calculating the length of str1 and 2 
    len_str2=len(str2)
    result=[[0]*(len_str2+1) for var1 in range(len_str1+1)] #having a result matrix with initial 0 vals
    for var1 in range (len_str1 +1): #assigning row and col to 0
        result[var1][0]=0
    for var2 in range(len_str2 +1):
        result[0][var2]=0
    for var1 in range (1, len_str1+1):
        for var2 in range (1,len_str2+1):
            if str1[var1-1] == str2[var2-1]: #checking if they are equal if yes incrementing count 
                result[var1][var2] = result[var1-1][var2-1]+1
            else: #if the charcter dont match we try taking the max of characters returned by either by moving str1 or str2 
                result[var1][var2]=max(result[var1-1][var2], result[var1][var2-1])
    return result[len_str1][len_str2]
#please change the path according to your system where the text file is stored 
input_file = open('LCS1.txt', 'r') #opening the file 
input_lines = input_file.readlines()#reading the file
dynamic_len_var=len(input_lines)#Computing length
for i in range(dynamic_len_var):
    a = input_lines[i].split(',') #splitting the file input values by the commas 
    print(str(i) +":",a)
val=int(input("Enter the value from the indexes mentioned in the options shown above: ")) #fetching index val from user
a = input_lines[val].split(',') #splitting the file input values by the commas 
X = a[0] #assigning the first str to 0th index 
Y = a[1] #assigning the second str to 1st index 
start = timeit.default_timer() #starting timer
lcs_dp(X,Y)  #calling function 
stop = timeit.default_timer() #ending timer
print("\n")
print("                   ---------------------------------------------            ")
print("                   LONGEST COMMON SEQUENCE - DYNAMIC PROGRAMMING             ")
print("                   ---------------------------------------------            ")
print("\n")
print ("Length of LCS in " +str(X)+" and "+str(Y)+" is ", lcs_dp(X,Y))
print("Time taken to find length of Longest Subsequence of strings "+str(X)+ "and "+str(Y)+ " is:",str(stop-start)+" Seconds")