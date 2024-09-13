'''
Adeena Ahmed                    ICS2O1 Computer Science                    February 2nd, 2021

This program is a adventure game in which the user can improve their multiplication skills.
The user has to find 4 hidden numbers in a cave, solve two multiplication questions correctly,
and get a score of 10 or more to get out of the cave safely and win the game.
'''
def setup():
    #the function setup() has no parameters and sets up the screen for the program output
    size(900,800)
    global screen, x, y, xPos, yPos, y1, x1,x2, y2, x3, y3, x4, y4, num1, num2, num3, num4, transparent, wrong, almost, almost2, wrong2, selected, position, newPosition, answerX, pastScreen, newPosition2, score, scoreList, speed
    screen = "welcome"#controls which screen is displayed
    transparent = [100, 100, 100, 100]#controls the transparency of the hidden numbers
    selected = [255, 255, 255] #controls the colour of the multiple choice button, so 
    position = [326, 426, 526]
    newPosition = [326, 426, 526]
    answerX = 0  # correct answer for question 2
    newPosition2 = [326, 426, 526]
    y = 0 #y position of dark brown obstacle
    x = random(35, 850)#x position of dark brown obstacle
    yPos = 0#y position of light brown obstacle
    xPos = random(35, 850)#x position of light brown obstacle
    score = 0
    scoreList = []
    maxList = []
    speed = 30#pixels/screen the object moves
def draw():
    #The draw() function has no parameters and continuously displays the content in the function body.
    global screen, x, y, xPos, yPos, y1, x1, x2, y2, x3, y3, x4, y4, num1, num2, num3, num4, transparent, wrong, almost, almost2, wrong2, answer, selected, position, newPosition, answerX, newPosition2, score, scoreList, maxList, speed
    background(0)
    if screen == "collapsingCave":#add image backrounds if screen is the "collapsing cave", main menu, cave or end screen
        collapsing = loadImage("cave.jpg")
        image(collapsing, 0, 0, 900, 800)
    elif screen == "welcome":
        entrance = loadImage("cave_entrance.jpg")
        image(entrance, 25, 25, 850, 750)
    elif screen == "cave":
        search = loadImage("cave_search.jpg")
        image(search, 0, 0, 900, 800)
    elif screen == "end" and score >= 10:
        caveExit = loadImage("cave_exit.jpg")
        image(caveExit, 0, 0, 900, 800)
    #displays score at top left of screen
    stroke(255)
    strokeWeight(3)
    fill(255, 125, 3)
    rect(40, 35, 200, 40, 7)
    #displays the start, exit and menu buttons
    fill(107, 0,175)
    rect(30, height/3, 80, 50)# Start Page button
    rect(30, height/3+120, 80, 50)# Exit button
    rect(30, height/3+240, 80, 50)#Menu button
    if screen == "welcome":#if screen is on main menu page
        stroke(255)
        strokeWeight(3)
        fill(0, 255, 0, 127)
        rect(40, 105, 820, 80)
        textSize(50)
        fill(107, 0,175)#purple
        text("\nThe Multiplication Cave of Doom", 50, 80)
        textSize(27)
        fill(255)
        text("Start",35, height/3+30)
        scoreFile = loadStrings("scoreFile.txt")
        maxList = []
        for lines in scoreFile:#goes through each line in scoreFile and appends it to maxList
            maxList.append(int(lines.strip()))
        if len(maxList) != 0:#if there are scores in maxList display high score
            stroke(255)
            strokeWeight(3)
            fill(0, 255, 0, 127)
            rect(320, 210, 300, 160)
            textSize(50)
            fill(107, 0,175)
            text("High Score:", 340, height/3)
            text(max(maxList), 445, height/3+60)
    elif screen == "story":#if screen is on the instructions page
        rect(200, 650, 80, 50)
        rect(690, 650, 95, 50)
        textSize(27)
        fill(255)
        text("Back", 210, 685)
        text("Play", 710, 685)
        text("You are on an expedition to explore a cave.", 220, 175)
        text("You will have to find 4 numbers and solve 2\n  multiplication questions along the way.", 220, 230)
        text("You must get out before the cave collapses.\n       Dodge at least 10 falling objects\n                    to get out safely.", 220, 340)
        text("Press play to continue.", 320, 500)
    elif screen == "Menu":
        textSize(40)
        fill(255)
        text("                How To Play:", width/5, 80)
        text("                     Hint:", width/5, 400)
        textSize(25)
        text("Find 4 numbers in the cave by hovering your mouse\nover the numbers.", 220, 140)
        text("Once you have found all the numbers press\nthe space bar to answer two multiplication questions.", 220, 220)
        text("Dodge at least 10 falling obstacles by moving your\nmouse left and right to get out of the cave safely.", 220, 300)
        text("    - Anything multiplied by 1 is itself", width/5, 460)
        text("    - Anything multiplied by 0 is 0",width/5, 520)
        text("    - To multiply a number by 10, add a 0 to the end\n      of the number",width/5, 580)
        text("    - Some numbers could be hidden under the buttons\n      or where the score display is",width/5, 680)
    elif screen == "collapsingCave":#if screen is on the collapsing cave page
        stroke(255)
        strokeWeight(3)
        noFill()
        rect(570, 20, 320, 100)
        fill(255, 0, 0)
        text("Oh No! The cave is collapsing!\nMove your mouse left and right\nto dodge the falling objects.", 580, 50)
        fill(107, 0,175)
        rect(30, 650, 80, 50)#back
        fill(255)
        textSize(30)
        text("Back", 40, 685)
        #character:
        strokeWeight(40)#flashlight
        stroke(229, 237, 117)
        triangle(mouseX+10, 690, mouseX-10, 690, mouseX, 710)
        noStroke()
        #neck
        fill(0, 255, 44)
        rect(mouseX-10, 750, 20, 40)
        #body
        fill(29, 203, 62)
        ellipse(mouseX, 800,90, 80)
        #helmet
        fill(0)
        ellipse(mouseX,730, 50,50) 
        strokeWeight(2)
        stroke(207,255,0)
        ellipse(mouseX,725, 49, 49)
        #obstacles
        noStroke()
        createObstacle(70, 70)
        createObstacle2(70, 70)
        if x - 70 <= mouseX <= x + 70 and 660 <= y <= 800:#if player collides with the dark brown obstacle go to the end screen
            screen = "end"
            scoreList.append(str(score))
            saveStrings("scoreFile.txt", scoreList)
        elif y >= 800:#if dark brown obstacle doesn't hit the player,it will come down again at an increased speed
            y = 0
            x = random(35, 850)
            createObstacle(70, 70)
            score += 1
            if speed <= 100:#if the dark brown obstacle is less than 100 pixels/screen increase the speed otherwise stay at same speed
                speed += 5
        if xPos - 70 <= mouseX <= xPos + 70 and 660 <= yPos <= 800:#if player collides with the light brown obstacle go to the end screen
            screen = "end"
            scoreList.append(str(score))
            saveStrings("scoreFile.txt", scoreList)
        elif yPos >= 800:#if light brown obstacle doesn't hit the player,it will come down again at an increased speed
            yPos = 0
            xPos = random(35, 850)
            createObstacle2(70, 70)
            score += 1
            if speed <= 100:#if the light brown obstacle is less than 100 pixels/screen increase the speed otherwise stay at same speed
                speed += 5
        if screen == "collapsingCave":#object doesn't move when not on collapsing cave screen
            y += speed
            yPos += speed
        else:
            y = 0
            yPos = 0
    elif screen == "cave":#if screen is on the cave screen
        stroke(255)
        strokeWeight(3)
        fill(0)
        rect(570, 20, 320, 100)
        fill(255, 0, 0)
        textSize(15)
        text("Once you have found all the numbers\npress the space bar to answer two\nmultiplication questions", 600, 50)
        #hidden numbers
        textSize(40)
        fill(0, 255, 249, transparent[0])#first number
        text(str(num1), x1, y1)
        fill(0, 255, 249, transparent[1])#second number
        text(str(num2), x2, y2)
        fill(0, 255, 249,transparent[2])#third number
        text(str(num3), x3, y3)
        fill(0, 255, 249,transparent[3])#fourth number
        text(str(num4), x4, y4)
        #flashlight
        strokeWeight(40)
        stroke(255, 255, 98)
        triangle(mouseX-70, mouseY+10, mouseX-70, mouseY-10, mouseX-30, mouseY)
        stroke(37,216,185)
        line(mouseX, mouseY, mouseX+80, mouseY)
        #if mouse is hovering over a hidden number make it opaque
        if x1 - 20 <= mouseX <= x1 + 60 and y1 - 60 <= mouseY <= y1 + 40 and screen == "cave":
            transparent[0] = 255
        elif x2 - 20 <= mouseX <= x2 + 60 and y2 - 60 <= mouseY <= y2 + 40 and screen == "cave":
            transparent[1] = 255
        elif x3 - 20 <= mouseX <= x3 + 60 and y3 - 60 <= mouseY <= y3 + 40 and screen == "cave":
            transparent[2] = 255
        elif x4 - 20 <= mouseX <= x4 + 60 and y4 - 60 <= mouseY <= y4 + 40 and screen == "cave":
            transparent[3] = 255
    elif screen == "Question1":#if screen is on the page with the first question
       textSize(30)
       fill(107, 0,175)
       stroke(255)
       rect(200, 650, 80, 50)#back
       rect(690, 650, 90, 50)#next
       fill(255)
       text("Back", 210, 685)
       text("Check", 692, 685)
       textSize(60)
       text(str("What is "+str(num1)+" x "+str(num2)+" ? "), 300, 200)
       #stores right answer of question
       answer = num1*num2
       #multiple choice answer options
       strokeWeight(3)
       fill(selected[0])
       ellipse(300, 300, 20, 20)        
       fill(selected[1])
       ellipse(300, 400, 20, 20)
       fill(selected[2])
       ellipse(300, 500, 20, 20)
       fill(255)
       #if all options are different show the options
       if almost != wrong and almost != answer and wrong != answer:
           text(almost, 375, newPosition[0])
           text(wrong, 375, newPosition[1])
           text(answer, 375, newPosition[2])
       else:#if 2 options are the same, change the values of almost and wrong and then show the options
           almost = answer + 5 
           wrong = answer - 19
           text(almost, 375, newPosition[0])
           text(wrong, 375, newPosition[1])
           text(answer, 375, newPosition[2]) 
    elif screen == "Question2":#if screen is on the page with the second question
        textSize(30)
        fill(107, 0,175)
        stroke(255)
        rect(200, 650, 80, 50)
        rect(690, 650, 95, 50)
        fill(255)
        textSize(30)
        text("Back", 210, 685)
        text("Next", 695, 685)
        textSize(60)
        text(str("What is "+str(num3)+" x "+str(num4)+" ? "), 300, 200)
        #stores right answer of question
        answer = num3*num4
        #multiple choice answer options
        stroke(255)
        strokeWeight(3)
        fill(selected[0])
        ellipse(300, 300, 20, 20)        
        fill(selected[1])
        ellipse(300, 400, 20, 20)
        fill(selected[2])
        ellipse(300, 500, 20, 20)
        fill(255)
        #if all options are different
        if almost2 != wrong2 and almost2 != answer and wrong2 != answer:
            text(almost2, 375, newPosition2[0])#show options
            text(wrong2, 375, newPosition2[1])
            text(answer, 375, newPosition2[2])
        else:#if 2 options are the same, change the values of almost and wrong
            almost2 = answer + 5 
            wrong2 = answer - 19
            text(almost2, 375, newPosition2[0])#show options
            text(wrong2, 375, newPosition2[1])
            text(answer, 375, newPosition2[2])
    elif screen == "score1":#if on score screen of question 1
        if newPosition[2] == answerX + 26:#if answer is correct
            fill(107, 0,175)
            rect(200, 650, 80, 50)
            rect(690, 650, 95, 50)
            fill(255)
            textSize(30)
            text("Back", 210, 685)
            text("Next", 695, 685)
            textSize(70)
            text("       Correct!\n       You got\n       it right!", width/5, height/3)
        elif answerX == 0:#if no answer is selected
            fill(107, 0,175)
            rect(200, 650, 80, 50)
            rect(690, 650, 95, 50)
            fill(255)
            textSize(30)
            text("Redo", 205, 685)
            text("Next", 700, 685)
            fill(255)
            textSize(70)            
            text("       Uh oh.\n  Looks like you\nforgot to answer.\n  Would you like\n   to try again?", width/4, height/5)
        else:#if answer is incorrect
            fill(107, 0,175)
            rect(200, 650, 80, 50)
            rect(690, 650, 95, 50)
            textSize(30)
            fill(255)
            text("Redo", 205, 685)
            text("Next", 695, 685)
            textSize(70)            
            text("Sorry that's\nincorrect.\nWould you like\nto try again?", width/3, height/4)
    elif screen == "score2":#if on score screen of question 2
        if newPosition2[2] == answerX + 26:#if answer is correct
            fill(107, 0,175)
            rect(200, 650, 80, 50)
            rect(690, 650, 95, 50)
            fill(255)
            textSize(30)
            text("Back", 210, 685)
            text("Next", 695, 685)
            textSize(70)
            text("       Correct!\n       You got\n       it right!", width/5, height/3)
        elif answerX == 0:#if no answer is selected
            fill(107, 0,175)
            rect(200, 650, 80, 50)
            rect(690, 650, 95, 50)
            textSize(30)
            fill(255)
            text("Redo", 205, 685)
            text("Next", 695, 685)
            textSize(70)            
            text("       Uh oh.\n  Looks like you\nforgot to answer.\n  Would you like\n   to try again?", width/4, height/5)
        else:#if answer is incorrect
            fill(107, 0,175)
            rect(200, 650, 80, 50)
            rect(690, 650, 95, 50)
            textSize(30)
            fill(255)
            text("Redo", 205, 685)
            text("Next", 695, 685)
            textSize(70)            
            text("Sorry that's\nincorrect.\nWould you like\nto try again?", width/3, height/4)
    elif screen == "end":#if on the last screen
        textSize(30)
        fill(255)
        textSize(20)
        text("Restart",35, height/3+34)
        fill(255, 0, 0)
        textSize(60)
        if score >= 10:#if the score is greater than or equal to 10, display congratulations message
            fill(3, 202, 255, 127)
            rect(165, 80, 700, 475)
            fill(255, 0, 0)
            text("    Congratulations!\n You have successfully\nmade it out of the cave!\n Try beating your score\n          next time!", 160, 160)
        else:#if score is less than 10, display game over message
            text("Game Over\nBetter Luck\nNext Time", 320, height/3)
        fill(107, 0,175)
        rect(525, 590, 300, 80)
        fill(255)
        text("Score: " + str(score), 550, 650)
    noStroke()
    fill(255)
    textSize(27)
    text("Exit", 35, height/3+150)# exit game button
    text("Score: "+str(score), 45, 65)
    if screen != "Menu":#if on help menu page button displays "Help"
        text("Help", 35, height/3+270)# help menu button
    else:
        textSize(20)#if not on help menu page button displays "resume"
        text("Resume", 35, height/3+270)#goes back to previous page
    #if not on welcome or end screen, button displays "Start Page"
    if screen != "welcome" and screen != "end":
        textSize(20)
        text("Start", 45, height/3+24)
        text("Page", 45, height/3+44)  
    #if on a question or score page make a white rectangular border
    if screen == "Question1" or screen == "Question2" or screen == "score1" or screen == "score2" or screen == "story":
        noFill()
        strokeWeight(10)
        stroke(255)
        rect(200, 100, 600, 500)
def mouseClicked():
    '''This function runs when the mouse is clicked and has no arguments.
    It allows the buttons to work so that the screens can change.'''
    global screen, x1, y1, x2, y2, x3, y3, x4, y4, num1, num2, num3, num4, transparent, wrong, almost, wrong2, almost2, selected, answerX, pastScreen, position, newPosition, newPosition2, score, maxList, scoreFile
    scoreFile = loadStrings("scoreFile.txt")
    if 30 <= mouseX <= 110 and height/3 + 120 <= mouseY <= height/3 + 170:#exit button
        del maxList
        del scoreFile
        exit()
    elif 30 <= mouseX <= 110 and height/3 + 240 <= mouseY <= height/3 + 290 and screen != "Menu":#Help button
        pastScreen = screen
        screen = "Menu"
    elif 30 <= mouseX <= 110 and height/3 + 240 <= mouseY <= height/3 + 290 and screen == "Menu":#resume button on help menu page
        screen = pastScreen
    elif 30<=mouseX<=110 and height/3<=mouseY<=height/3+50 and screen == "welcome":#start button on start page 
        screen = "story"      
    elif 200 <= mouseX <= 280 and 650 <= mouseY <= 700 and screen == "story":#back button
        screen = "welcome"
    elif screen == "story" and 690 <= mouseX <= 780 and 650 <= mouseY <= 700:#next button to story screen
        screen = "cave"
        transparent = [100, 100, 100, 100]
        y1 = random(30,770)#turn these into lists
        x1 = random(30,870)
        y2 = random(30,770)
        x2 = random(30,870)
        y3 = random(30,770)
        x3 = random(30,870)
        y4 = random(30,770)
        x4 = random(30,870)
        num1 = int(random(1,11))
        num2 = int(random(1,11))
        num3 = int(random(1,11))
        num4 = int(random(1,11))
        wrong = int(random(0, 20))
        almost = int(random(0,20))
    elif 30 <= mouseX <= 110 and height/3 <= mouseY <= height/3 + 50: #start page button to go back to start page
        screen = "welcome"
        transparent = [15, 15, 15, 15]
        selected = [255, 255, 255]
        answerX = 0 
        y = 0
        yPos = 0
        score = 0
    elif screen == "Question1":#if on question 1 screen
        #changes the multiple choice buttons from white(255) to black(0) or black to white
        if 280 <= mouseX <= 320 and 280 <= mouseY <= 320:
            if selected[0] == 255:
                selected[0] = 0
                answerX = 300
                selected[1:3] = [255,255]
            elif selected[0] == 0:
                selected[0] = 255
                answerX = 0
        elif 280 <= mouseX <= 320 and 380 <= mouseY <= 420:
            if selected[1] == 255:
                selected[1] = 0
                selected[0] = 255
                selected[2] = 255
                answerX = 400
            elif selected[1] == 0:
                selected[1] = 255
                answerX = 0
        elif 280 <= mouseX <= 320 and 480 <= mouseY <= 520:
            if selected[2] == 255:
                selected[2] = 0
                selected[0:2] = [255,255]
                answerX = 500
            elif selected[2] == 0:
                selected[2] = 255
                answerX = 0  
        if 200 <= mouseX <= 280 and 650 <= mouseY <= 700:#back button
            screen = "cave"
        elif 690 <= mouseX <= 780 and 650 <= mouseY <= 740:#next button
            screen = "score1"
    elif screen == "Question2":#if on question 2 screen
        #changes the multiple choice buttons from white(255) to black(0) or black to white
        if 280 <= mouseX <= 320 and 280 <= mouseY <= 320:
            if selected[0] == 255:
                selected[0] = 0
                answerX = 300
                selected[1:3] = [255,255]
            elif selected[0] == 0:
                selected[0] = 255
                answerX = 0
        elif 280 <= mouseX <= 320 and 380 <= mouseY <= 420:
            if selected[1] == 255:
                selected[1] = 0
                selected[0] = 255
                selected[2] = 255
                answerX = 400
            elif selected[1] == 0:
                selected[1] = 255
                answerX = 0
        elif 280 <= mouseX <= 320 and 480 <= mouseY <= 520:
            if selected[2] == 255:
                selected[2] = 0
                selected[0:2] = [255,255]
                answerX = 500
            elif selected[2] == 0:
                selected[2] = 255
                answerX = 0
        #back button
        if 200 <= mouseX <= 280 and 650 <= mouseY <= 700:
            screen = "score1"
        #next button
        elif 690 <= mouseX <= 780 and 650 <= mouseY <= 700:
            screen = "score2"
    elif screen == "score1":#if on score page of question 1
        if 200 <= mouseX <= 280 and 650 <= mouseY <= 700:#back button
            screen = "Question1"
        elif 690 <= mouseX <= 780 and 650 <= mouseY <= 700:#next button
            screen = "Question2"
            selected = [255, 255, 255]
            wrong2 = int(random(0, 20))
            almost2 = int(random(0,20))
            answerX = 0            
            newPosition2 = [326, 426, 526]
            newPosition2[0] = position[int(random(0,3))]
            newPosition2[1] = position[int(random(0,3))]
            newPosition2[2] = position[int(random(0,3))]
            #if any 2 positions are the same change their values
            if newPosition2[0] == newPosition2[1] or newPosition2[0] == newPosition2[2] or newPosition2[1] == newPosition2[2]:
                newPosition2 = [426, 326, 526]
    elif screen == "score2":#if on score page of question 2
        if 200 <= mouseX <= 280 and 650 <= mouseY <= 700:#back button
            screen = "Question2"
        elif 690 <= mouseX <= 780 and 650 <= mouseY <= 700:#next button
            screen = "collapsingCave"
    if 30 <= mouseX <= 110 and 650 <= mouseY <= 700 and screen == "collapsingCave":#back button on collapsing cave screen
        screen = "score2"
def keyPressed():
    '''This function runs when a key is pressed and has no parameters.
    It allows the program to go from the cave screen to the screen with the first question.''' 
    global screen, transparent, position, newPosition
    #if spacebar pressed on cave screen and all numbers have been found
    if screen == "cave" and transparent[0] == 255 and transparent[1] == 255 and transparent[2] == 255 and transparent[3] == 255 and key == " ":
        screen = "Question1"
        position = [326, 426, 526]
        newPosition = [326, 426, 526]
        newPosition[0] = position[int(random(0,3))]
        newPosition[1] = position[int(random(0,3))]
        newPosition[2] = position[int(random(0,3))]
        if newPosition[0] == newPosition[1] or newPosition[0] == newPosition[2] or newPosition[1] == newPosition[2]:
            newPosition = [326, 426, 526] 
def createObstacle(width, height):
    #This function takes 2 parameters, width and height and draws a dark brown obstacle in the shape of a circle.
    fill(64,58,44)
    ellipse(x, y, width, height)
def createObstacle2(width, height):#light brown obstacle
    #This function takes 2 parameters, width and height and draws a light brown obstacle in the shape of a circle.
    fill(144, 112, 41)
    ellipse(xPos, yPos, width, height)
