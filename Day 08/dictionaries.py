student = {
    "name" : "Pasindu",
    "age" : 20,
    "Married" : True,
    "Address" : "Pasindu",
    "contact" : ["0987654"]
}

# print(student["name"])
#
# student["name"] = "Rashmika"
#
# print(student["name"])
#
# student["grades"] = "A"
#
# if "grades" in student:
#     print(student["grades"])

student["contact"].append("0987654321234567")

for num in student["contact"]:
    print(num)


for keys in student.keys():
    print(keys)

for val in student.values():
    print(val)

for key,val in student.items():
   print(f"Key - {key} and value - {val}")