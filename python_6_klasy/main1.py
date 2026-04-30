class Person:
    def __init__(self, name:str):
        self.name = name
        
    def greet(self):
        return "Cześć, jestem " + self.name
        
    def farewell(self):
        return "Do widzenia, jestem " + self.name