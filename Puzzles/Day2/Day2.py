import time  

#Option Pairs PlayType:Score
playerPoints = {
    "Rock":1,
    "Paper":2,
    "Scissors":3
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

losingPair = {
    "Paper":"Rock",
    "Scissors":"Paper",
    "Rock":"Scissors"
}

def getSolution():

    """
    Read strategy from an input file and determines if win or loss. 
    """
    
    score = 0

    with open('Puzzles\Day2\input.txt') as f:
        
        #Each line in file is a round formatted as (Opponent You).
        try:
            for line in f.readlines():
                
                formatLine = line.rstrip()
                
                opponent = opponentPairs[formatLine.split(" ")[0]]
                roundEnd = formatLine.split(" ")[1]
                
                #Loss Handling
                if roundEnd == "X":
                    points = playerPoints[losingPair[opponent]]
                    score = score + points
                
                #Draw Handling
                elif roundEnd == "Y":
                    score = score + playerPoints[opponent] + 3    
                
                #Win Handling    
                elif roundEnd == "Z":
                    points = playerPoints[winningPair[opponent]]
                    score = score + points + 6      
                    
        except Exception as e:
            print('Please make sure file is formatted correctly. \nException: ', e)
            return

        print("Score:",score)










#Timer setup and start solution
start = time.time()
getSolution()
print("%.3gms" % ((time.time()-start)*1000))