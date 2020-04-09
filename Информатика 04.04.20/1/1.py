a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())


class KUB_01:
  def __init__(self, a=a1, h=a4, b=a5):
    self.v = a*b*h
ob1 = KUB_01()
print("Об'єм = ", ob1.v)