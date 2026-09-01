#String Methods

# 1 - len()
city = "Tampa"
print("The length of the city name is:", len(city))


# 2 - [] Notation used to access individual characters in a string
print("The first character of the city name is:", city[0])
print("The last character of the city name is:", city[-1])
print(city[0:3])  # Slicing the string to get the first three characters


# 3 - Concatenation
country = "USA"
city = "Tampa"
full_address = city + ", " + country
print("The full address is:", full_address)


#4 - upper() and lower()
print("City name in uppercase:", city.upper())
print("City name in lowercase:", city.lower())


#5 - strip()
#removes leading and trailing whitespace
greeting = "   Hello, World!   "
print("Greeting before strip:", greeting)
print("Greeting after strip:", greeting.strip())

#6 - find()
team = "Bucs"
print("The index of 'u' in team name is:", team.find('u'))

#7 - replace()
print("Team name after replacing 's' with 'x':", team.replace("s", "x"))

#8 - in operator
print ("Is 'Bucs' in the team name?", "Bucs" in team)
print ("Is 'D' in the team name?", "D" in team)

#9 - not operator
print ("Is 'D' not in the team name?", "D" not in team)