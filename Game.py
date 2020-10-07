from graphics import *

class Game:

    def __init__(self,win):
        self.Rectangle = Rectangle(Point(0,0),Point(1,1))
        self.ball = Circle(Point(0,0),5)
        self.message = Text(Point(100,190),"Click on two sides to create the rectangle where the ball will bounce, use the lower half of the"
                       " window").draw(win)

    def updatePointsCourt(self,win):
        p1Rec = win.getMouse()
        p1Rec.draw(win)
        p2Rec = win.getMouse()
        p2Rec.draw(win)
        p1Rec.undraw()
        p2Rec.undraw()

        error = True
        while error:  # I do this so that the court does not get in the way of the text that will be displayed on the top
            if (p1Rec.getY() > 130 or p2Rec.getY() > 130):
                self.message.setText("Court is to big!")
                p1Rec = win.getMouse()
                p1Rec.draw(win)
                p2Rec = win.getMouse()
                p2Rec.draw(win)
                p1Rec.undraw()
                p2Rec.undraw()
            else:
                error = False
        self.Rectangle = Rectangle(p1Rec,p2Rec)
        self.Rectangle.setFill('black')
        self.Rectangle.draw(win)

    def updateBallCenter(self,win):
        self.message.setText("Now click where you want the starting point of the ball")
        centerBall = win.getMouse()

        error = True
        while error:  # This checks that the ball is only spawned on the court not outside of it
            if (centerBall.getX() >= self.Rectangle.getP2().getX() or centerBall.getX() <= self.Rectangle.getP1().getX() or
                    centerBall.getY() >= self.Rectangle.getP2().getY() or centerBall.getY() <= self.Rectangle.getP1().getY()):
                self.message.setText("Out of court")
                centerBall = win.getMouse()
            else:
                error = False
        self.ball = Circle(centerBall, 5)
        self.ball.setFill('cyan')
        self.ball.draw(win)

    def gameLoop(self, numRebounds, changex, changey, n):
        for x in range(1000):
            center = self.ball.getCenter()
            update(n)

            if center.getX() + 5 >= self.Rectangle.getP2().getX():
                changex = -changex
                numRebounds = numRebounds + 1
            if center.getX() - 5 <= self.Rectangle.getP1().getX():
                changex = -changex
                numRebounds = numRebounds + 1
            if center.getY() + 5 >= self.Rectangle.getP2().getY():
                changey = -changey
                numRebounds = numRebounds + 1
            if center.getY() - 5 <= self.Rectangle.getP1().getY():
                changey = -changey
                numRebounds = numRebounds + 1
            self.ball.move(changex, changey)

        return numRebounds

    def getUserGuess(self, guess, win):
        self.message.setText("Enter the guess for rebounds: ")
        guess.setText("0")
        guess.draw(win)
        win.getMouse()
        return int(guess.getText())

    def insertionSort(self, scoreList, nameList):
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

    def printReboundsScore(self,numRebounds, userGuess, totalPoints, win):
        if numRebounds == userGuess:
            totalPoints = totalPoints + 1

        output = "Total Rebounds: " + str(numRebounds)
        textOutput = Text(Point(100, 180), output).draw(win)
        textOutput2 = Text(Point(100, 170), "Score: " + str(totalPoints)).draw(win)
        win.getMouse()

        textOutput.undraw()
        textOutput2.undraw()

        return totalPoints

    def checkIfNewHighScore(self,scoreList, nameList, totalPoints, win):
        # If a new HighScore has occured then the name, score, and email are written into a file
        # if there was an existing file the old score is erased and user data since the new score is higher
        textOutput3 = Text(Point(100, 160), "Enter your user data!").draw(win)
        textOutput4 = Text(Point(100, 150), "Enter your ID: ").draw(win)
        answer = Entry(Point(130, 150), 10)
        answer.setText("")
        answer.draw(win)
        win.getMouse()
        id = answer.getText()
        win.getMouse()

        scoreList.append(totalPoints)
        nameList.append(id)
        self.insertionSort(scoreList, nameList)
        dataList = []
        # Used to save the top 3 scores (Hall of Fame)
        if (len(scoreList) >= 3):
            for x in range(0, len(scoreList) - 1):
                dataList.append(nameList[x])
                dataList.append(str(scoreList[x]))
                print(dataList)  #For testing
        else:
            for x in range(0, len(scoreList)):
                dataList.append(nameList[x])
                dataList.append(str(scoreList[x]))
                print(dataList)  #For testing

        win.getMouse()
        outFile = open("highScore.txt", "w")

        count = 0
        for x in dataList:
            if (count == len(dataList) - 1):  # 5
                outFile.write(x)
            else:
                outFile.write(x)
                outFile.write(" ")
            count = count + 1
        outFile.close()

        textOutput3.undraw()
        textOutput4.undraw()
        answer.undraw()
        self.printHallofFame(dataList, win)

    def printHallofFame(self,dataList, win):

        for x in range(0, len(dataList) - 1, 2):
            textOutput = Text(Point(100, 180), "Hall of Fame:").draw(win)
            textOutput2 = Text(Point(100, 170), dataList[x] + " " + dataList[x + 1]).draw(win)
            win.getMouse()
            textOutput.undraw()
            textOutput2.undraw()

    def undraw(self):
        self.ball.undraw()
        self.Rectangle.undraw()
        self.message.undraw()


    def messages(self,win):

        message2 = Text(Point(100, 180),
                        "Start by pointing the lower left of the rectangle and then the upper right").draw(win)
        message3 = Text(Point(100, 170),
                        "Also, draw your court below the dashed line, if not the program will warn you").draw(win)

        message4 = Text(Point(100, 130),
                        "-----------------------------------------------------------------------------------------------"
                        "-----------------------------------------------------------------------------------------------").draw(
            win)
        win.getMouse()
        message2.undraw()
        message3.undraw()









