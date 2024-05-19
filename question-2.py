"""Write a program to calculate the sum of series up to n term.
   For example, 
   if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690 """

n=int(input("Enter the size of series:"))
curr_sum=0
sum_of_series=0
for i in range(1,n+1):
    curr_sum=curr_sum *10 + 2
    sum_of_series +=curr_sum
print("The sum of series=",sum_of_series)