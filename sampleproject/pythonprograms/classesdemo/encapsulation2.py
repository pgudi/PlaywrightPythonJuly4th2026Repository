class Bank:
    def __init__(self, bankname,accountnumbner):
        self.__bankname=bankname
        self.__accountnumber=accountnumbner

    def get_bank_name(self):
        return self.__bankname

    def get_account_number(self):
        return self.__accountnumber

obj=Bank("ICICI Bank", 1000011)
print(obj.__bankname)
print(obj.__accountnumber)

print(obj.get_bank_name())
print(obj.get_account_number())