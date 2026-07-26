class Human:
    firstname=None
    age=None
    location=None

obj=Human()
obj.firstname="Adams"
obj.age=44
obj.location="Bangalore"
print(obj.firstname, obj.age, obj.location)
print("------------------")
Human.firstname="Santosh"
Human.age=22
Human.location="California"
print(Human.firstname, Human.age, Human.location)