def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    import random
    
    box = ['green','green','green','red','red','red']
    outcomes=[]
    outcome=0
    for x in range(numTrials):
       # print(x)
        box2=box.copy()
        #print(box2)
        outcomes=[]
        for i in range(3):
            #print(i)
            x =random.choice(box2)
            outcomes.append(x)
            box2.remove(x)
        #print(outcomes)
        if (outcomes[0]=='green' and outcomes[1]=='green' and outcomes[2]=='green'
            or outcomes[0]=='red' and outcomes[1]=='red' and outcomes[2]=='red' ):
            outcome+=1

    return outcome/numTrials
#ispravno resenje:
    
##def oneTrial():
##    '''
##    Simulates one trial of drawing 3 balls out of a bucket containing
##    3 red and 3 green balls. Balls are not replaced once
##    drawn. Returns True if all three balls are the same color,
##    False otherwise.
##    '''
##    balls = ['r', 'r', 'r', 'g', 'g', 'g']
##    chosenBalls = []
##    for t in range(3):
##        # For three trials, pick a ball
##        ball = random.choice(balls)
##        # Remove the chosen ball from the set of balls
##        balls.remove(ball)
##        # and add it to a list of balls we picked
##        chosenBalls.append(ball)
##    # If the first ball is the same as the second AND the second is the same as the third,
##    #  we know all three must be the same color.
##    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
##        return True
##    return False
##
##def noReplacementSimulation(numTrials):
##    '''
##    Runs numTrials trials of a Monte Carlo simulation
##    of drawing 3 balls out of a bucket containing
##    3 red and 3 green balls. Balls are not replaced once
##    drawn. Returns the a decimal - the fraction of times 3 
##    balls of the same color were drawn.
##    '''
##    numTrue = 0
##    for trial in range(numTrials):
##        if oneTrial():
##            numTrue += 1
##
##    return float(numTrue)/float(numTrials)
