# Our story begins with Alice
name = "Alice"  # A string representing the person's name
print(name + " starts her day with a smile.")

# Alice's bank balance
balance = 50  # A number representing her money in dollars
print(name + " has $" + str(balance) + " in her wallet.")

# Is Alice happy?
is_happy = True  # A boolean (True means yes, she is happy)
print("Is " + name + " happy? " + str(is_happy))

# Alice buys a coffee
coffee_price = 5
balance = balance - coffee_price  # Subtract coffee cost
print(name + " buys a coffee for $" + str(coffee_price))
print("Her balance is now $" + str(balance))

# She finds a $20 bill on the street
balance = balance + 20  # Add money
print(name + " finds $20 on the street!")
print("Her balance is now $" + str(balance))

# Alice remembers her best friend's name
best_friend = "Bob"
print(name + " calls her best friend " + best_friend + ".")

# Alice gives Bob $10 as a gift
gift = 10
balance = balance - gift
print(name + " gives $" + str(gift) + " to " + best_friend + ".")
print("Her balance is now $" + str(balance))

# At the end of the day, Alice is still happy
is_happy = True
print("At the end of the day, is " + name + " happy? " + str(is_happy))
