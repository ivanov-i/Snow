from scene import *

class SnowFlake:
  def __init__(self, position, radius):
    self.position = position
    self.radius = 4
 
  def draw(self):
    ellipse(self.position[0], self.position[1], self.radius, self.radius)
    
  def update(self):
    (x,y) = self.position
    self.position = (x,  y - 1)
    
  def is_inside(self, size):
    (w, h) = size
    (x, y) = self.position
    return x >= 0 and y >= 0 and x <= w and y <= h
