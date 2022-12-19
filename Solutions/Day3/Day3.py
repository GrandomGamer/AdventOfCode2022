import math

def getPairs(rucksacks:list):
    """
    Take in a group of rucksacks and find any matching letters that are in all of the rucksacks.

    Args:
        rucksacks (list): List of rucksacks.
    
    Returns:
        List: A list of letters (items) that are in both strings
    """
    items = []
    
    for item in rucksacks[0]:
        
        if all(item in ruck for ruck in rucksacks[1:]):
            rucksacks[1:] = [ruck.replace(item, '') for ruck in rucksacks[1:]]
            items.append(item)
        
    return items

def getSolution():

    """
    Read strategy from an input file and determines if win or loss. 
    """
    
    sum = 0
    nextGroup = 0
    rucksToCount = 3
    
    rucks = [""]*rucksToCount

    with open('Solutions\Day3\input.txt') as f:
        
        #Each line in file is a rucksack.
        lines = f.readlines()
        
        try:
            #Get each group of 3 lines.
            while nextGroup != len(lines):
                    
                    #Set rucks list to the next group of 3 lines from input.
                    for i in range(0,rucksToCount):
                        rucks[i] = lines[nextGroup+i].rstrip()
                    
                    letters = getPairs(rucks)
                    
                    for l in letters:
                        
                        #Get ASCII of letter and then subtract so that lowercases start at 1 and uppercases start at 27
                        if l.isupper():
                            priority = ord(l)-38
                        else:
                            priority = ord(l)-96

                        sum += priority

                    nextGroup += rucksToCount
                    print(nextGroup)
                    
            print(sum)
                    
        except Exception as e:
            print('Please make sure file is formatted correctly or refer to this exception. \nException: ', e)
            return
        
getSolution()