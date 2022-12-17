import time

#Set how many elves we want the maxes of.
numMaxes = 3

maxSums = [0]*numMaxes

def checkMaxElfs(sum: int):
    
    """
    Check input sum vs maxSum and replace if it is more.

    Args:
        int (sum): Sum to compare.
    """
    
    for i,maxSum in enumerate(maxSums):
        if sum >= maxSum:
            maxSums.insert(i,sum)
            maxSums.pop()
            break
    

def getSolution():

    """
    Read ints from an input file to get a sum and compares it to the maxSums. 
    """

    with open('Puzzles\Day1\input.txt') as f:
        
        sum = 0
        max = 0

        #Each blank line in file is next elf.
        try:
            for line in f.readlines():
                if line.isspace():
                    checkMaxElfs(sum)
                    sum = 0
                else:
                    sum += int(line)
        except ValueError:
            print('Please make sure file only contains integers.')
            return

        #TotaL our maxSums
        for maxSum in maxSums:
            max += maxSum
        
        print(max)










#Timer setup and start solution
start = time.time()
getSolution()
print("%.3gms" % ((time.time()-start)*1000))