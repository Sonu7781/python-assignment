# Write a program to find out the prime factors of a number.
def prime_factors(n):
    factors=[]
    
    while n%2 == 0:
        factors.append(2)
        n = n//2

    for i in range(3,n+1,2):
        while n%i == 0:
            factors.append(i)
            n =n//i
    
    if n>2:
        factors.append(n)
    
    return factors

number=int(input("Enter a number:"))
print("The prime factors of", number, "are:", prime_factors(number))
