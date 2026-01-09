import random

# Given code
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def find_pairs(numbers, target):
    seen = {}
    pairs = []

    for num in numbers:
        complement = target - num

        if complement in seen:
            # Add as many pairs as complement has appeared
            for _ in range(seen[complement]):
                pairs.append((complement, num))

        # Count occurrences of each number
        seen[num] = seen.get(num, 0) + 1

    return pairs

pairs = find_pairs(list_of_numbers, target_number)

# Display results
for a, b in pairs:
    print(f"{a} and {b} sums to the target_number {target_number}")

print(f"\nTotal pairs found: {len(pairs)}")
