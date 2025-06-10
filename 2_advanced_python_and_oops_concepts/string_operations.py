
s1 = "Joby is a google employee"
s2 = "google"

#to check whether a string is substring of other string
print(s2 in s1)

# concatenation
print(s1 + " at hyderabad" + s2)

#index operations

print(s1.index(s2)) # gives index of first occurance
print((s1+s2).rindex(s2)) # gives first occurance from right side
print(s1.index(s2, 5, 20)) # looks for substring in a cetain range 

print(len(s1))
print(s1.lower())
print(s2.upper())

print(s1.islower())
print(s1.isupper())

print(s1.startswith("Joby"))
print(s1.startswith("i", 5))
print(s1.startswith("i", 5, len(s1)))
print(s1.endswith("Joby"))

print(s1.split())
s3 = "Alpha, Beta, Gamma"
print(s3.split(","))
print(s1.join(" "))


s4 = "___Joby___"
print(s4.strip("_"))
print(s4.lstrip("_"))
print(s4.rstrip("_"))

print(s4.find("ob"))
print(s4.find("oy"))
