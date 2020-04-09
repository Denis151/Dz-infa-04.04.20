class KOLO_01:
  def __init__(self, r=7):
    self.s = 4*3.14*r

ob1 = KOLO_01()


class KOLO_02:
  def __init__(self, r=5):
    self.v = (4/3)*3.14*(r**3)

ob2 = KOLO_02()
print("Площа = ", ob1.s, ";", "Об'єм = ", ob2.v)
