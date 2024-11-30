'''

*****
 ****
  ***
   **
    *

'''

num = 5
star = num
space = 0
for row in range(1,num+1):
    for sp in range(space):
        print(' ', end = ' ')
    for st in range(star):
        print('*', end = ' ')
    space += 1
    star -= 1
    print()

