from graphics import *
from Buttons import Button
from Game import Game
import os.path # Will be used to test if a file exists
#Cedric R. Perez Narvaez

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

def main():
    win = GraphWin("Count the Rebounds Game", 720, 480)
    win.setCoords(0, 0, 200, 200)

    totalPoints = 0
    n = 0
    continueButton = Button(win,Point(160,160),12,10,"Yes")
    quitButton = Button(win,Point(180,160),12,10,"Quit")
    continueButton.activate()
    quitButton.activate()
    textOutput = Text(Point(100, 160), "Want to play?").draw(win)

    pt = win.getMouse()
    while not quitButton.clicked(pt) and continueButton.clicked(pt):
        scoreList = []
        nameList = []
        nameList, scoreList = checkForFile()

        game1 = Game(win)
        game1.messages(win)
        game1.updatePointsCourt(win)
        game1.updateBallCenter(win)

        numRebounds = 0
        changex = 1
        changey= 1
        n = n + 50
        textOutput.undraw()
        numRebounds = game1.gameLoop(numRebounds,changex,changey,n)

        guess = Entry(Point(135,190),3)
        userGuess = game1.getUserGuess(guess,win)
        totalPoints = game1.printReboundsScore(numRebounds,userGuess,totalPoints,win)
        game1.checkIfNewHighScore(scoreList,nameList,totalPoints,win)

        textOutput.undraw()

        textOutput3 = Text(Point(80, 160),"Want to play again? It gets harder every time!").draw(win)
        pt = win.getMouse()
        guess.undraw()
        textOutput3.undraw()
        game1.undraw()

    continueButton.deactivate()
    quitButton.deactivate()
    win.getMouse()
    win.close()

main()