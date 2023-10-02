
rivers = {"Nile River":"Africa",
          "Amazon River":"South America",
          "Mississippi River":"United States"}

for x in rivers:
    print(x+" runs through "+rivers.get(x))
print("")
for x in rivers:
    print(x)
print("")
for x in rivers:
    print(rivers.get(x))