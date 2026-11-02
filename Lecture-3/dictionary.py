student = {"name":"karthik","age":14,"gender":"male","height":5.6}
# print(student["name"])
# print(student["school"])
# adding and modifying existing elements 
# student["age"] = 15 
# student["school"] = "NY Public School"
# print(student)

# copy - which will create copy of a dictionary 
student_copy = student.copy()
# student_copy["name"] = "Aryaan"
# print(student_copy)
# print(student)

# clear - which will clear the elements inside a dictionary 
# student_copy.clear()
# print(student_copy)

#keys - we can get all the keys from the dictionary 
# print(student.keys())
# for key in student.keys(): 
#     print(f"{key.title()}: {student[key]}")

#values - we can get all the values from the dictionary 
# print(student.values())
# for value in student.values(): 
#     print(value)

# items - you will get the list of (key,value) 
# print(student.items())

# get - it will safely retreive the value from dictionary 
# print(student.get("school"))
# print(student.get("name"))
# print(student.get("roll number",0))

#pop - it will remove the key value pair 
# gender = student.pop("gender")
# print(gender)
# print(student)

#popitem - it will remove last key value pair 
# student.popitem()
# print(student)

#fromkeys - it will create a diction from the provide keys and set a default value to them
product = dict.fromkeys(["name","description","rating","price"])
# product["name"] = "Table"
# product["description"] = "High productive table."
# product["rating"] = 4.6 
# product["price"] = 100 
# print(product)

#update - takes key word arguments (kwargs) and update them in the dictionary 
product.update(name="Chair",description="Comfortable chair",rating=4.3,price=50,available=True)
# print(product)

#setdefault - it works same as get  
# print(product.setdefault("available",True))

if "available" in product: 
    print(product["available"])