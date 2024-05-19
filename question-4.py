"""Write a function prodDigits() that inputs a number 
   and returns the product of digits of that number. """

def prodDigits(n):
    product=1
    while n>0:
        rem=n%10
        product=product*rem
        n=n//10
    return product

number=int(input("Enter a number: "))
print("The product of digits of given number is:",prodDigits(number))