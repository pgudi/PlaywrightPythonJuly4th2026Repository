class Bank:
    def __init__(self):
        self.__bankname=""
        self.__accountnumber=0

    def set_bank_name(self, bankname):
        self.__bankname=bankname

    def set_account_number(self,accountnumber):
        self.__accountnumber=accountnumber

    def get_bank_name(self):
        return self.__bankname

    def get_account_number(self):
        return self.__accountnumber

obj=Bank()
# print(obj.__bankname)
# print(obj.__accountnumber)

obj.set_bank_name("IDFC Bank")
obj.set_account_number(1000001)
print(obj.get_bank_name())
print(obj.get_account_number())