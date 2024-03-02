
# Declare name list.
names = [] 
 # Declare birth_date list.
birth_date = []
# Opening file
f = open(r"C:\Users\shahz\Desktop\Task 14\DOB.txt", encoding="utf-8")
# Reading file and saving it into data.
data = f.readlines() 
# Running for loop on readed data.
for line in data: 
    # Spliting the line and saving into parts.
    parts = line.split()
    # Appending names into name list.
    names.append(parts[:2])
    # Appending birthdate into birth_date list.
    birth_date.append(parts[2:])
# Closing the file.
f.close()

print("Name")
# Running for loop on name list and starting it from index 1
for i, name in enumerate(names, start=1):
    # Printing name and i is the number which is started from 1.
    print("{}. {}".format(i, " ".join(name)))

print("Birthdate")
# Running for loop on birth_date list and starting it from index 1
for i, birthday in enumerate(birth_date, start=1):
    # Printing name and i is the number which is started from 1.
    print("{}. {}".format(i, " ".join(birthday)))