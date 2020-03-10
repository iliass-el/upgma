class Node:
  def __init__(self, id):
    self.id = id
    self.leftDist = 0
    self.rightDist = 0
    self.leftNode = None
    self.rightNode = None
    self.parent = None