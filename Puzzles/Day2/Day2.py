import time  

#Option Pairs Key:[PlayType,Score]
playerPairs = {
    "X":["Rock",1],
    "Y":["Paper",2],
    "Z":["Scissors",3]
}

#Opponent pairs as Key:PlayType
opponentPairs = {
    "A":"Rock",
    "B":"Paper",
    "C":"Scissors"
}

#Winning pairs as PlayType:PlayType
winningPair = {
    "Rock":"Paper",
    "Paper":"Scissors",
    "Scissors":"Rock"
}

def getSolution():

    """
    Read strategy from an input file and determines if win or loss. 
    """
    
    score = 0

    with open('Puzzles\Day2\input.txt') as f:
        
        #Each line in file is a round formatted as (Opponent You).
        #try:
        for line in f.readlines():
            
            formatLine = line.rstrip()
            
            opponent = opponentPairs[formatLine.split(" ")[0]]
            you = playerPairs[formatLine.split(" ")[1]]
            needWin = winningPair[opponent]
            
            if needWin == you[0]:
                score = score + you[1] + 6
            elif opponent == you[0]:
                score = score + you[1] + 3
            else:
                score += you[1]      
                    
        #except Exception as e:
            #print('Please make sure file is formatted correctly. \nException: ', e)
            #return

        print("Score:",score)










#Timer setup and start solution
start = time.time()
getSolution()
print("%.3gms" % ((time.time()-start)*1000))