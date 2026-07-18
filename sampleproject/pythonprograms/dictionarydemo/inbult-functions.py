employee={
    "empid":101,
    "ename":"Santosh",
    "jobname":"Analyst",
    "salary":37000
}
print(employee)

# Read Elements from Dictionary
for k,v in employee.items():
    print(k," --> ",v)

# Read A speciifc value
print(employee.get("ename"))

# pop function
employee.pop("jobname")
print(employee)

# popItem function
employee.popitem()
print(employee)

# display All Keys
employee1={
    "empid":101,
    "ename":"Santosh",
    "jobname":"Analyst",
    "salary":37000
}

print(employee1.keys())

# display All values
print(employee1.values())

# update function
employee1.update({"cityname":"Bangalore"})
print(employee1)