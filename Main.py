from graphics import *
import os.path # Will be used to test if a file exists
#Cedric R. Perez Narvaez

def checkForFile():
    if os.path.isfile("highScore.txt"):
        myFile = open("highScore.txt","r")
        data = myFile.read()
        dataList = data.split(" ")
        myFile.close()
        return dataList

def createCourt(win):

    p1Rec = win.getMouse()
    p1Rec.draw(win)
    p2Rec = win.getMouse()
    p2Rec.draw(win)
    p1Rec.undraw()
    p2Rec.undraw()
    return Rectangle(p1Rec,p2Rec)

def createBall(win,message,court):
    message.setText("Know click where you want the starting point of the ball")
    centerBall = win.getMouse()

    error = True
    while error:
        if (centerBall.getX() >=  court.getP2().getX() or centerBall.getX() <= court.getP1().getX() or
                centerBall.getY() >= court.getP2().getY() or centerBall.getY() <= court.getP1().getY()):
            message.setText("Out of court")
            centerBall = win.getMouse()
        else:
            error = False
    return Circle(centerBall,5)

def gameLoop(ball,court,numRebounds,changex,changey,n):
    for x in range(1000):
        center = ball.getCenter()
        update(n)

        if center.getX() + 5 >= court.getP2().getX():
            changex = -changex
            numRebounds = numRebounds + 1
        if center.getX() - 5 <= court.getP1().getX():
            changex = -changex
            numRebounds = numRebounds + 1
        if center.getY() + 5 >= court.getP2().getY():
            changey = -changey
            numRebounds = numRebounds + 1
        if center.getY() - 5 <= court.getP1().getY():
            changey = -changey
            numRebounds = numRebounds + 1
        ball.move(changex, changey)

    return numRebounds

def getUserGuess(message,guess,win):
    message.setText("Enter the guess for rebounds: ")
    guess.setText("0")
    guess.draw(win)
    win.getMouse()
    return int(guess.getText())

def checkIfNewHighScore(totalPoints,win):
    textOutput3 = Text(Point(100, 160), "New High Score! ").draw(win)
    textOutput4 = Text(Point(100, 150),"Enter your ID: ").draw(win)
    answer = Entry(Point(130, 150), 10)
    answer.setText("")
    answer.draw(win)
    win.getMouse()
    id = answer.getText()
    win.getMouse()
    textOutput5 = Text(Point(85,140),"Enter your email address: ").draw(win)
    answer2 = Entry(Point(150,140),30)
    answer2.setText("")
    answer2.draw(win)
    win.getMouse()
    email = answer2.getText()
    win.getMouse()
    outFile = open("highScore.txt","w")
    print(id,totalPoints,email,file=outFile)
    textOutput3.undraw()
    textOutput4.undraw()
    textOutput5.undraw()
    answer.undraw()
    answer2.undraw()

def askRepeat(win,answer):
    answer.setText("")
    answer.draw(win)
    win.getMouse()
    return answer.getText()

def undraw(ball,guess,textOutput,textOutput2,textOutput3,answer,court,message):
    ball.undraw()
    guess.undraw()
    textOutput.undraw()
    textOutput2.undraw()
    textOutput3.undraw()
    answer.undraw()
    court.undraw()
    message.undraw()

def main():
    win = GraphWin("Count the Rebounds Game", 720, 480)
    win.setCoords(0, 0, 200, 200)

    dataList = checkForFile()

    playAgain = 'yes'
    totalPoints = 0
    n = 0

    while playAgain == 'yes':
        message = Text(Point(100, 190), "Click on two sides to create the rectangle where the ball will bounce, use the lower part of the"
                                        " window").draw(win)
        court = createCourt(win)
        court.setFill('black')
        court.draw(win)

        ball = createBall(win,message,court)
        ball.setFill('cyan')
        message.setText("Start counting the rebounds!")
        ball.draw(win)

        numRebounds = 0
        changex = 1
        changey= 1
        n = n + 50
        win.getMouse()

        numRebounds = gameLoop(ball,court,numRebounds,changex,changey,n)

        guess = Entry(Point(135,190),3)
        userGuess = getUserGuess(message,guess,win)

        if numRebounds == userGuess:
            totalPoints = totalPoints + 1

        output = "Total Rebounds: " + str(numRebounds)
        textOutput = Text(Point(100, 180),output).draw(win)
        textOutput2 = Text(Point(100, 170),"Score: " + str(totalPoints)).draw(win)

        if not dataList:
            checkIfNewHighScore(totalPoints,win)
        else:
            if totalPoints > int(dataList[1]):
                checkIfNewHighScore(totalPoints,win)

        textOutput3 = Text(Point(100, 160),"Want to play again? It gets harder every time! ").draw(win)
        answer = Entry(Point(160, 160), 3)
        playAgain = askRepeat(win,answer)

        undraw(ball,guess,textOutput,textOutput2,textOutput3,answer,court,message)

main()