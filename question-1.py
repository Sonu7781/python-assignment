"""Write a program to display only those numbers 
   from a list that satisfy the following conditions """
numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0:
        print(number)
