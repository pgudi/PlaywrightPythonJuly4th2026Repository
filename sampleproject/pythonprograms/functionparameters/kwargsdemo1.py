# def readContent(**kwargs):
#     for k, v in kwargs.items():
#         print(k," -> ",v)


# readContent(firstname="Santosh", coursename="Research")

def readContentNew(**kwargs):
    print(kwargs.get("ename"))

readContentNew()
readContentNew(ename="Santosh")