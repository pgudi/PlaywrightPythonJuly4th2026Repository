class Payment:
    def pay(self):
        print("the Payment process has started")

class PhonePay(Payment):
    def pay(self):
        print("the Payment process has started using Phonepay")

class GooglePay(Payment):
    def pay(self):
        print("the Payment process has started using GooglePay")

class NetBanking(Payment):
    def pay(self):
        print("the Payment process has started using NetBanking")

obj=Payment()
obj.pay()

phonepay=PhonePay()
googlepay=GooglePay()
netbanking=NetBanking()

obj=phonepay
obj.pay()

obj=googlepay
obj.pay()

obj=netbanking
obj.pay()