class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            print("Points are same")
        else:
            print("Points are different")

P1=point(5,7)
P2=point(7,5)

if P1==P2:
    print("Same points")
else:
    print("Different points")