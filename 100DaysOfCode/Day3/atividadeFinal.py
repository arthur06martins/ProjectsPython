print("""
  __________________
      /\  ______________ \
     /::\ \ZZZZZZZZZZZZ/\ \
    /:/\.\ \        /:/\:\ \
   /:/Z/\:\ \      /:/Z/\:\ \
  /:/Z/__\:\ \____/:/Z/  \:\ \
 /:/Z/____\:\ \___\/Z/    \:\ \
 \:\ \ZZZZZ\:\ \ZZ/\ \     \:\ \
  \:\ \     \:\ \ \:\ \     \:\ \
   \:\ \     \:\ \_\;\_\_____\;\ \
    \:\ \     \:\_________________\
     \:\ \    /:/ZZZZZZZZZZZZZZZZZ/
      \:\ \  /:/Z/    \:\ \  /:/Z/
       \:\ \/:/Z/      \:\ \/:/Z/
        \:\/:/Z/________\;\/:/Z/
         \::/Z/_______itz__\/Z/
          \/ZZZZZZZZZZZZZZZZZ/
      
""")

print("Welcome to the, mistery box")
choice1 = input('You\'re at a crpssrpad, where do you want to g? Type "left" or "right".').lower


if choice1 == "left":
    choice2 = input('you\'ve come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across')
    if choice2 ==  "wait":
        choice3 = input("You arrive at the island unharmed. There is a housse with 3 doors. One red, one yellow and one blue. Whinch colour do you choose?".lower())
        if choice3 == "red":
            print("it is a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the box! you win")
        elif choice3 == "blue":
            print("tou enter a room of beasts. Game Over")
        else:
            print("you choose a door that doesn't. Game Over")
    else:
        print("You got attacked by an angry trout.Game OVer")
else:
    print("you gell into a hole. Game Over.")