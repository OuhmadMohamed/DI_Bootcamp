x = int(input('Enter the Number: '))

# Find the sum of proper divisors (excluding the number itself)
sum_divisors = 0

for i in range(1, x):
    if x % i == 0:   # i is a divisor
        sum_divisors += i

# Check if it's a perfect number
if sum_divisors == x:
    print(True)
else:
    print(False)
