from scene import *
from SnowFlake import *
import random

class World(Scene):
  def setup(self):
    self.snow = []
    for i in range(1,2000):
      self.snow = self.snow + [self.create_random_snowflake()]
  
  def create_snowflake(self, position):
    return SnowFlake(position, 4)
      
  def create_random_snowflake(self):
      x = random.uniform(0, self.size[0]) 
      y = random.uniform(0, self.size[1])
      return self.create_snowflake((x, y))
      
  def create_top_random_snowflake(self):
      x = random.uniform(0, self.size[0]) 
      y = self.size[1]
      return self.create_snowflake((x,y))    
      
  def draw(self):
    background(0,0,0)
    fill(1,1,1)
    stroke(1,1,1)
    stroke_weight(4)
    for snowflake in self.snow:
      snowflake.draw()
           
  def update(self):
    for i, snowflake in enumerate(self.snow):
      snowflake.update()
      if not snowflake.is_inside(self.size):
        self.snow[i] = self.create_top_random_snowflake()
      
              
run(World(), show_fps=True)
