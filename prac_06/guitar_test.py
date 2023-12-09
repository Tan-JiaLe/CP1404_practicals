from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 500)

print(f"{gibson.name} get_age() - Expected 100.") # got 100
print(f"{another.name} get_age() - Expected 9.") # got 9
print(f"{gibson.name} is_vintage() - Expected True") # got True
print(f"{another.name} is_vintage() - Expected False") # got False