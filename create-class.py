# Defines the class:
class Circle(object):
# Defines the attributes to initialize object
    def __init__(self, radius, color):
        self.radius=radius;
        self.color=color;
# Define a method: add_radius
    def add_radius(self,r):
        self.radius=self.radius+r
        return self.add_radius

# Red circle object with radis=3 is initiated
red_circle=Circle(3,'red')
# add_radius method is used to increase radius by 3
red_circle.add_radius(3)
print(red_circle.radius)
