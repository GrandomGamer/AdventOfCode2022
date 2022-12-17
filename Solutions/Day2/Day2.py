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


def handleEnd(end:str,opponent:str):
    
    """
    Handle the different types of endings for the game.

    Args:
        end (str): How the game should end.
        opponent (str): What your opponent is playing.
    """
    
    score = 0
    
    #Loss Handling
    if end == "X":
        points = playerPoints[losingPair[opponent]]
        return points
    
    #Draw Handling
    elif end == "Y":
        return playerPoints[opponent] + 3    
    
    #Win Handling    
    elif end == "Z":
        points = playerPoints[winningPair[opponent]]
        return points + 6      


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
                
                
                score += handleEnd(roundEnd,opponent)
                    
        except Exception as e:
            print('Please make sure file is formatted correctly. \nException: ', e)
            return

        print("Score:",score)



getSolution()