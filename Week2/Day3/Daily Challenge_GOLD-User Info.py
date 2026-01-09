# Step 1: Collect user data
users = []

for _ in range(5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    users.append((name, age, score))

# Step 2: Sort using lambda (Name > Age > Score)
users.sort(key=lambda x: (x[0], x[1], x[2]))

# Step 3: Display result
print(users)
