class Alpha:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(c,a,b):
      c.x=a.x+2*b.x
      c.y=a.y+2*b.y 
      return c
      
    def subract(c,a,b):
      c.x=a.x-0.5*b.x
      c.y=a.y-0.5*b.y
      return c
    def multipl(c,a,b):
      c.x=a.x*b.y+a.y*b.x
      c.y=a.x*b.y-a.y*b.x
      return c
    def div(c,a,b):
      c.x = (a.x + b.x) / (a.y + b.y)
      c.y = (a.x - b.x) / (a.y -b.y)
      return c
    def __str__(self):
       return "("+str(self.x ) +" "+str(self.y )+")"
def main():
   o1=Alpha(5,2)
   o2=Alpha(2,3)
   o=Alpha(0,0)
   o3=o.add(o1,o2)
   o4=o.subract(o1,o2)
   o5=o.multipl(o1,o2)
   o6=o.div(o1,o2)
   print(o3,o4,o5,o6)
if __name__=='__main__':
      main()
   




