class Cylinder:
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height

  def getradius(self):
    return self.radius
  
  def getheight(self):
    return self.height
  
  def setradius(self, radius):
    if radius > 0: self.radius = radius
    else: print("It cannot be negative number")

  def setheight(self,height):
    self.height = height

  def base_area(self):
    base_area = 3.14*2*self.radius
    return base_area
  
  def surface_area(self):
    surface_area = 3.14*2*self.radius*self.height
    return surface_area

  def area(self):
    area = 2*self.base_area() + self.surface_area()
    return area

  def volume(self):
    volume = self.base_area() * self.height
    return volume

c1 = Cylinder(radius=3, height=5)
print("Area:", c1.area())
print("Volume:", c1.volume())

