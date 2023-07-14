


if__name__ = "__main__"                                                             
 
name_of_bags = [ "gucci, lacoste, dior , burberry, D&G, " ]
  
while True :
    print("1 to check price of bags ")
    print("2 to check name of bags  ")
    print("3 to check name to bag   ")
    option = input("to acess enter [1-3]")  

    if option == "1":
        if name_of_bags:
            print("names of bags avalaible")
            for bag in name_of_bags :
                print("Brand: ", bag["brand"] )
                print("amount: ",bag ["amount"])
                print("quality: ", bag["quality"])
                print("---------------------")

