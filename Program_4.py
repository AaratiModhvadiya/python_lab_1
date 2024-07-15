# Initialize an empty list to store employee names
EMPNAME = []

# Add some initial names to the list
EMPNAME.extend(["Alice", "Bob", "Charlie"])

# Print current list of employees
print("Initial list of employees:", EMPNAME)

# Add a new employee
EMPNAME.append("David")
print("After adding 'David':", EMPNAME)

# Remove an employee
EMPNAME.remove("Bob")
print("After removing 'Bob':", EMPNAME)

# Append another employee
EMPNAME.append("Eve")
print("After appending 'Eve':", EMPNAME)
