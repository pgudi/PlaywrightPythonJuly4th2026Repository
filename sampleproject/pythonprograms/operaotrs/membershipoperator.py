# membership operator at list level
list = [10,30,"Mango","Camel","Sunflower",True]
# in operator
print("Camel" in list)

# in operator
print(30 in list)

# not in Operator
print("Banana" not in list)
print("Sunflower" not in list)
print("--------------------------------")
# membership operator at tuple level
tup=("Lotus","Mumbai","Mysore","Kolar")
print("Mumbai" in tup)
print("Chennai" not in tup)

print("--------------------------------")
# membership operator at set level
cities={"Lotus","Mumbai","Mysore","Kolar"}
print("Mumbai" in cities)
print("Chennai" not in cities)

print("--------------------------------")
# membership operator at dictionary level
employee={
    "empid":101,
    "ename":"Santosh",
    "jobname":"Analyst",
    "salary":37000
}
print("jobname" in employee.keys())
print("bonus" in employee.keys())
print("bonus"  not in employee.keys())