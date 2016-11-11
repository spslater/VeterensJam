class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y

class Robbers():
   def __init__(self, name, resource_limit, resource_count, position):
      self.name = name
      self.resource_limit = resource_limit
      self.resource_count = resource_count
      self.position = position
      self.moving = False
      self.far = False
      self.wheretogo = Point(0,0)

class Cops():
   def __init__(self, name, resource_limit, resource_count, position):
      self.name = name
      self.resource_limit = resource_limit
      self.resource_count = resource_count
      self.position = position

class Bank():
   def __init__(self, name, rate, position):
      self.name = name
      self.rate = rate
      self.position = position

class Money():
   def __init__(self, name, position):
      self.name = name
      self.position = position
