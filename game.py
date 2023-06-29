day = 0
money = 0
answer = ''

class Tool:
    def __init__(self, tool, pay, action):
        self.tool = tool
        self.pay = pay
        self.action = action
    
    def tool(self):
        return self.tool
    
    def pay(self):
        return self.pay
    
    def action(self):
        return self.action
    

levels = [
    Tool('teeth', 1, 'you are biting grass'),
    Tool('rusty scissors', 5, 'you are cutting grass one by one'),
    Tool('lawnmower', 25, ' you are mowing the lawn, polluting the air'),
    Tool('goat', 50, ' you are letting the goat eat'),
    Tool('flamethrower', 100, 'you are burning grass'),
    Tool('your cousin', 250, 'your cousin working for you'),
    Tool('your cousing and her friend', 350, 'your cousing and her friend working for you'),
    Tool('small team of hungry students', 500, 'a buncH of college students doing the work for you')
]



def update(x):
    global day,money
    current_level = levels[x-1]
    day += 1
    money += current_level.pay
    print('This is day: 'f'{day}.'
          ' Currently ' f'{current_level.action}'
          ' using ' f'{current_level.tool} '
          'and making ' f'{current_level.pay}' ' a day. '
          'You have ' '$' f'{money}! '
        )
    

def choice():
    quest = input('quest Do you wanna work? y/n ')
    global answer
    if quest == 'y':
        answer = 'y'
    elif quest == 'n':
        answer = 'n'
      



choice()

if answer == 'y':
    update(1)





