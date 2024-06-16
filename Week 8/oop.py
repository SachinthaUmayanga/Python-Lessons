class Person:
    def __init__(self,food_name: str, company: str, comfort:str) -> None:
        self._food_name = food_name
        self._company = company
        self._comfort = comfort
    
    def eat(self):
        return f"eat {self._food_name}"
    
    def sleep(self):
        return f"sleep {self._company}"
    
    def work(self):
        return f"work {self._comfort}"
    
p = Person("Mango","Sysco","Good")
print(p.eat()," ",p.sleep()," ",p.work())