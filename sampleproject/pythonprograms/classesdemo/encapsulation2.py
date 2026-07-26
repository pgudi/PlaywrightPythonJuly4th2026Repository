class Bank:
    def __init__(self, bankname,accountnumbner):
        self._bankname=bankname
        self._accountnumber=accountnumbner

    def get_bank_name(self):
        return self._bankname

    def get_account_number(self):
        return self._accountnumber

obj=Bank("ICICI Bank", 1000011)

print(obj.get_bank_name())
print(obj.get_account_number())