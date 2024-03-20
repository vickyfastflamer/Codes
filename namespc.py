str="SASTRA"

def Outerfn():
    global str
    print(str)
    str= str+" university"
    print(str)

    def Innerfn():
      global str
      print(str)
      str= str+" thanjavur"
      print(str)
    Innerfn() 
Outerfn()


