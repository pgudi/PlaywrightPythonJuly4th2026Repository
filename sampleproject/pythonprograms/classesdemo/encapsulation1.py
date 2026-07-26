class Bank:
    def __init__(self):
        self._bankname=""
        self._accountnumber=0

    def set_bank_name(self, bankname):
        self._bankname=bankname

    def set_account_number(self,accountnumber):
        self._accountnumber=accountnumber

    def get_bank_name(self):
        return self._bankname

    def get_account_number(self):
        return self._accountnumber

obj=Bank()
obj.set_bank_name("IDFC Bank")
obj.set_account_number(1000001)
print(obj.get_bank_name())
print(obj.get_account_number())