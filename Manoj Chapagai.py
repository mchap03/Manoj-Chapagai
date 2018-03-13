Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("choose one:")

new_list=[]

category= "Games","Sports"


print(new_list)


category_choice =input ("Games,Sports?: ")
if category_choice == "Games":
    print ("which game?")
    Games = input("Fortnite, Fifa 18, or Overwatch?: ")
    if Games == "Fifa 18":
        print ("Not a bad choice")
        new_list.append(Games)
    if Games == "Fortnite":
        print ("That's the top 5 best game ever made.")
        new_list.append(Games)
    if Games == "Overwatch":
        print ("Hope you enjoy playing this game.")
        new_list.append(Games)


elif category_choice == "Sports":
    print("which sports?")
    Sports = input ("Soccer, Baseball, Basketball?: ")
    if Sports == "Soccer":
        print ("That's the best choice you made.")
        new_list.append(Sports)
    if Sports == "Baseball":
        print ("Hope you have good time playing baseball.")
        new_list.append(Sports)
    if Sports == "Basketball":
        print ("That's the best sport.")
        new_list.append(Sports)

print(new_list)
