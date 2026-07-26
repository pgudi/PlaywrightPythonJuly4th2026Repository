class CapitalCity:
    def show_city_name(self,name):
        print("The Capital City name is ",name)

class Metropolitan (CapitalCity):
    def __init__(self, cname):
        super().show_city_name(cname)
        
    def show_city_name(self,name):
        print("The Metropolitan City name is ",name)

obj=Metropolitan("Bangalore")
obj.show_city_name("Mumbai")

