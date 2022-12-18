import math

def getPairs(rucksack:str):
    """
    Take in a rucksack and find any matching letters in each half (Compartment One and Compartment Two).

    Args:
        rucksack (str): Contents of rucksack
    
    Returns:
        List: A list of letters (items) that are in both strings
    """
    items = []
    
    compartOne = rucksack[:math.floor(len(rucksack)/2)]
    compartTwo = rucksack[math.floor(len(rucksack)/2):]
    
    for item in compartOne:
        
        if item in compartTwo:
            compartTwo = compartTwo.replace(item,'')
            items.append(item)
        
    
    return items

def getSolution():

    """
    Read strategy from an input file and determines if win or loss. 
    """
    
    sum = 0

    with open('Solutions\Day3\input.txt') as f:
        
        #Each line in file is a round formatted as (Opponent You).
        try:
            for line in f.readlines():
                
                formatLine = line.rstrip()
                
                compartOne = formatLine[:math.floor(len(line)/2)]
                compartTwo = formatLine[math.floor(len(line)/2):]
                
                letters = getPairs(formatLine)
                
                for l in letters:
                    
                    #Get ASCII of letter and then subtract so that lowercases start at 1 and uppercases start at 27
                    if l.isupper():
                        priority = ord(l)-38
                    else:
                        priority = ord(l)-96

                    sum += priority
                
            print(sum)
                    
        except Exception as e:
            print('Please make sure file is formatted correctly or refer to this exception. \nException: ', e)
            return
        
getSolution()