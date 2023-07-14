import random
while True:
  roll =[]
    
  dice =int(input("Dice : "))
  if dice <= 0:
        print ('not possible')
        print("quit")
        print('play on.')
  sides =int(input('sides: '))
    
  if sides <=0 :
      print('Impossible')
      quit()
      
  for i  in range (0, dice):

        face = random.randint(1,sides)
        roll.append(face)
  
  break
print(roll)