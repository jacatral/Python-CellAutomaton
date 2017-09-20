length = 100
density = 0.75
grid = [0 for x in range(length)]

# random distribution of 1's
import random
for x in range(round(length*density)):
    grid[random.randrange(0,length-1)] = 1

file = open("Rule184.txt","w+")

def RunCycle(line, size):
    for x in range(size-1,-1,-1):
        if(x == size-1):
            line[x] = 0
        else:
            if(line[x] == 1 and line[x+1] == 0):
                line[x] = 2
                line[x+1] = 1
    for x in range(size):
        if(line[x] == 2):
            line[x] = 0

while(sum(grid) > 0):
    #print(''.join(str(item) for item in grid))
    file.write(''.join(str(item) for item in grid) + '\n')
    
    RunCycle(grid, length)

file.write(''.join(str(item) for item in grid) + '\n')
file.write('\n')
#print(''.join(str(item) for item in grid))

file.close()
            
