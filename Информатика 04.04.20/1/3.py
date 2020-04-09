vall = 1590357
vt = 810124
vc = 780233
zall = 1258777 
zt = 465538
zc = 793239
xall = 2701188
xt = 2178792
xc = 522396
tall = 1059192
tt = 473632
tc = 595460
pall = 1426828 
pt = 885606
pc = 541222



class KOLO_01:
  def __init__(self, v1=vt, v2 =vall,z1=zt, z2 =zall,x1=xt, x2 =xall,t1=tt, t2 =tall,p1=pt, p2 =pall):
    self.vpt = v1/(v2 /100)
    self.zpt = z1/(z2 /100)
    self.xpt = x1/(x2 /100)
    self.tpt = t1/(t2 /100)
    self.ppt = p1/(p2 /100)

ob1 = KOLO_01()


class KOLO_02:
  def __init__(self, v1=vc, v2 =vc,z1=zc, z2 =zall,x1=xc, x2 =xall,t1=tc, t2 =tall,p1=pc, p2 =pall):
    self.vpc = v1/(v2 /100)
    self.zpc = z1/(z2 /100)
    self.xpc = x1/(x2 /100)
    self.tpc = t1/(t2 /100)
    self.ppc = p1/(p2 /100)

ob2 = KOLO_02()


r1 = vt/(vall /100)
r2 = zt/(zall /100)
r3 = xt/(xall /100)
r4 = tt/(tall /100)
r5 = pt/(pall /100)

class KOLO_03:
  def __init__(self, a1=r1, a2=r2, a3=r3, a4=r4, a5=r5):
    self.m = max(a1,a2,a3,a4,a5)

ob3 = KOLO_03()

print(ob1.vpt,";", ob1.zpt,";", ob1.xpt,";", ob1.ppt,";", ob1.tpt)
print(ob2.vpc,";", ob2.zpc,";", ob2.xpc,";", ob2.ppc,";", ob2.tpc)
print(ob3.m)
