import time

maxSum = 0


def checkMaxElf(sum: int):
    """
    Check input sum vs maxSum and replace if it is more.

    Args:
        int (sum): Sum to compare.
    """

    
    global maxSum

    if sum > maxSum:
        maxSum = sum

def getSolution():
    
    """
    Read ints from an input file. 
    """

    with open('Puzzles\Day1\input.txt') as f:
        sum = 0

        for line in f.readlines():
            try:
                if line.isspace():
                    checkMaxElf(sum)
                    sum = 0
                else:
                    sum += int(line)
            except ValueError:
                print("Please make sure all inputs are integers.")
                return

        print(maxSum)










#Timer setup and start solution.
start_time = time.time()
getSolution()
print(time.time() - start_time)

    

