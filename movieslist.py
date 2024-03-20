movieslist=["monty python and the holy grail","cat on a hot tin roof","on the waterfront"]

def add_movies():
    newmov=input("enter the name of the movie to be added:")
    movieslist.append(newmov)
    print("the movie", newmov,"is added to the movieslist")
def list():
    print("the movies in your list are:\n")
    for i in range(0, len(movieslist)):
         print(movieslist[i])
def delete():
    delmov=input("enter the name of movie to be deleted:")
    movieslist.remove(delmov)
    print(delmov ,"is deleted")
def loop():
     print("\n welcome to your movies list\n")
     print("you have the following options\n")
     print("list- list all movies \n add - add a new movie \n del- delete a movie\n exit - exit program")
     inpuser=input("your choice:")
     if inpuser=="list":
         list()
         loop()
     elif inpuser=="add":
         add_movies()
         loop()
     elif inpuser=="del":
        delete()
        loop()
     else:
       exit()
       
loop()

