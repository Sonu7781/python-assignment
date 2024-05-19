"""A number is called perfect if the sum of proper divisors of 
   that number is equal to the number. For example 28 is perfect number, 
   since 1+2+4+7+14=28. Write a program to print all the perfect
   numbers in a given range
"""
def sum_of_proper_divisors(n):
    sum_div = 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                sum_div += i
            else:
                sum_div += i + n // i
    return sum_div

def is_perfect(n):
    return n > 1 and sum_of_proper_divisors(n) == n

def find_perfect_numbers(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Example usage:
start_range = 1
end_range = 28
perfect_numbers = find_perfect_numbers(start_range, end_range)
print("Perfect numbers in the range", start_range, "to", end_range, "are:", perfect_numbers)
