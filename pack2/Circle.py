class Circle():

    def details(self):
        print(f"Radius: {self.Radius} The area is : {self.area()}, The circumference is: {self.circumference()}")


    def area(self):
        return 3.14*3.14*self.Radius

    def circumference(self):
        return 2*3.14*self.Radius

