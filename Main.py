from graphics import *
import os.path # Will be used to test if a file exists
#Cedric R. Perez Narvaez

#This will be modified with Classes
def checkForFile():
    nameList = []
    scoreList = []
    if os.path.isfile("highScore.txt"):
        myFile = open("highScore.txt","r")
        data = myFile.read()
        dataList = data.split(" ")
        myFile.close()


        for x in range(0, len(dataList), 2):
            nameList.append(dataList[x])
            scoreList.append(int(dataList[x + 1]))

        return nameList, scoreList
    else:
        return nameList,scoreList

def messages(win):
    message = Text(Point(100, 190),
                   "Click on two sides to create the rectangle where the ball will bounce, use the lower half of the"
                   " window").draw(win)
    message2 = Text(Point(100, 180), "Start by pointing the lower left of the rectangle and then the upper right").draw(
        win)
    message3 = Text(Point(100, 170),
                    "Also, draw your court below the dashed line, if not the program will warn you").draw(win)

    message4 = Text(Point(100, 130),
                    "-----------------------------------------------------------------------------------------------"
                    "-----------------------------------------------------------------------------------------------").draw(win)
    win.getMouse()
    message2.undraw()
    message3.undraw()
    return message

def createCourt(message,win):

    p1Rec = win.getMouse()
    p1Rec.draw(win)
    p2Rec = win.getMouse()
    p2Rec.draw(win)
    p1Rec.undraw()
    p2Rec.undraw()

    error = True
    while error: # I do this so that the court does not get in the way of the text that will be displayed on the top
        if (p1Rec.getY() > 130 or p2Rec.getY() > 130):
            message.setText("Court is to big!")
            p1Rec = win.getMouse()
            p1Rec.draw(win)
            p2Rec = win.getMouse()
            p2Rec.draw(win)
            p1Rec.undraw()
            p2Rec.undraw()
        else:
            error = False

    return Rectangle(p1Rec,p2Rec)

def createBall(win,message,court):
    message.setText("Now click where you want the starting point of the ball")
    centerBall = win.getMouse()

    error = True
    while error: # This checks that the ball is only spawned on the court not outside of it
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

def insertionSort(scoreList, nameList):
    for x in range(1, len(scoreList)):
        score = scoreList[x]
        name = nameList[x]
        left = x - 1
        while left >= 0:
            if score > scoreList[left]:
                scoreList[left + 1] = scoreList[left]
                nameList[left + 1] = nameList[left]

                scoreList[left] = score
                nameList[left] = name
                left = left - 1
            else:
                break

def checkIfNewHighScore(scoreList,nameList,totalPoints,win):
    #If a new HighScore has occured then the name, score, and email are written into a file
    #if there was an existing file the old score is erased and user data since the new score is higher
    textOutput3 = Text(Point(100, 160), "Enter your user data!").draw(win)
    textOutput4 = Text(Point(100, 150),"Enter your ID: ").draw(win)
    answer = Entry(Point(130, 150), 10)
    answer.setText("")
    answer.draw(win)
    win.getMouse()
    id = answer.getText()
    win.getMouse()

    scoreList.append(totalPoints)
    nameList.append(id)
    insertionSort(scoreList,nameList)
    dataList = []
    #Used to save the top 3 scores (Hall of Fame)
    if(len(scoreList) >= 3):
        for x in range(0,len(scoreList) - 1):
            dataList.append(nameList[x])
            dataList.append(str(scoreList[x]))
            print(dataList) #Borrar esto luego
    else:
        for x in range(0,len(scoreList)):
            dataList.append(nameList[x])
            dataList.append(str(scoreList[x]))
            print(dataList) #Borrar esto luego


    win.getMouse()
    outFile = open("highScore.txt","w")

    count = 0
    for x in dataList:
        if(count == len(dataList)-1): #5
            outFile.write(x)
        else:
            outFile.write(x)
            outFile.write(" ")
        count = count + 1
    outFile.close()

    textOutput3.undraw()
    textOutput4.undraw()
    answer.undraw()
    printHallofFame(dataList, win)

def printReboundsScore(numRebounds,userGuess,totalPoints,win):
    if numRebounds == userGuess:
        totalPoints = totalPoints + 1

    output = "Total Rebounds: " + str(numRebounds)
    textOutput = Text(Point(100, 180), output).draw(win)
    textOutput2 = Text(Point(100, 170), "Score: " + str(totalPoints)).draw(win)
    win.getMouse()

    textOutput.undraw()
    textOutput2.undraw()

    return totalPoints

def printHallofFame(dataList,win):

    for x in range(0,len(dataList)-1,2):
        textOutput = Text(Point(100, 180), "Hall of Fame:").draw(win)
        textOutput2 = Text(Point(100, 170), dataList[x]+ " " + dataList[x+1]).draw(win)
        win.getMouse()
        textOutput.undraw()
        textOutput2.undraw()


def askRepeat(win,answer):
    answer.setText("")
    answer.draw(win)
    win.getMouse()
    return answer.getText()

def undraw(ball,guess,textOutput3,answer,court,message):
    ball.undraw()
    guess.undraw()
    textOutput3.undraw()
    answer.undraw()
    court.undraw()
    message.undraw()

def main():
    win = GraphWin("Count the Rebounds Game", 720, 480)
    win.setCoords(0, 0, 200, 200)
    playAgain = 'yes'
    totalPoints = 0
    n = 0

    while playAgain == 'yes':
        scoreList = []
        nameList = []

        nameList, scoreList = checkForFile()

        message = messages(win)

        court = createCourt(message,win)
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

        totalPoints = printReboundsScore(numRebounds,userGuess,totalPoints,win)

        checkIfNewHighScore(scoreList,nameList,totalPoints,win)

        textOutput3 = Text(Point(100, 160),"Want to play again? It gets harder every time!(yes/no)").draw(win)
        answer = Entry(Point(160, 160), 3)
        playAgain = askRepeat(win,answer)

        undraw(ball,guess,textOutput3,answer,court,message)

main()