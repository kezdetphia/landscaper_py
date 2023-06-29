day = 0
money = 0
wanna_work = ''
level = 1

# Creating a class to be able to reuse it. Gives a cleaner code.
class Tool:
    def __init__(self, tool, pay, action, cost):
        self.tool = tool
        self.pay = pay
        self.action = action
        self.cost = cost

# New classes in an array to be able to use its properties by calling its index number in a function.
levels = [
    Tool('teeth', 1, 'you are biting grass', 0),
    Tool('a rusty scissors', 5, 'you are cutting grass one by one', 5),
    Tool('a lawnmower', 25, ' you are mowing the lawn, polluting the air', 25),
    Tool('a goat', 50, ' you are currently getting the grass fed to a', 50),
    Tool('a flamethrower', 100, 'you are burning grass', 100),
    Tool('your cousin', 250, 'your cousin working for you', 250),
    Tool('your cousing and her friend', 350, 'your cousing and her friend working for you', 350),
    Tool('a small team of hungry students', 500, 'a bunch of college students doing the work for you', 500)
]

# Function that offers the user to buy the tool once they have enough money.
# Controls the available cash aftert the purchase.
# Updates the level number so the game can progress dynamically.
def offer_tool():
    global money, level
    if level < len(levels) and money >= levels[level].cost:
        wanna_buy = input(f" Ayyee, money ting! There's {levels[level].tool} for {levels[level].cost}. You can make {levels[level].pay} per day with it. You wanna buy it? y/n ")
        if wanna_buy == 'y':
            money -= levels[level].cost
            level += 1
            print(f'You bought the {levels[level -1].tool}. You now have ${money} left. You can start making {levels[level -1].pay} per day. ')


#Function that updates the day and the earned cash from work and sends a message where we at.
def update(x):
    global day,money
    current_level = levels[x-1]
    day += 1
    money += current_level.pay
    print('---------------')
    print(f' THis is day: {day}')
    print(f' Currenty {current_level.action} using {current_level.tool} and making {current_level.pay} a day.')
    print(f' You have ${money}')
    print('---------------')

    offer_tool()
    
 
# Gives an option to the user whether they wanna carry on with the work.
# If the answer is yes, the function updates the global variable which 
# allows the game to continue in the while loop.
def choice():
    quest = input('Do you wanna work? y/n ').lower()
    global wanna_work
    if quest == 'y':
        wanna_work = 'y'
    elif quest == 'n':
        wanna_work = 'n'
      

while money < 1000:
  choice()
  if wanna_work == 'y':
      update(level)
  elif wanna_work == 'n':
      print('Youre a loser go back and work hard')
      

print("Hard work pays off! Now youre a trillionaire! 💰")