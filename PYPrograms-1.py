# Python organized by Brian Fopiano ⋈
import math
import sys
import time
#BASE IMPORT FOR EVERYTHING
def Everything():
    print("""
    
    
    
    














------------------------------------------------------------------------------------
███████╗██╗   ██╗███████╗██████╗ ██╗   ██╗████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ██╗
██╔════╝██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ ██║
█████╗  ██║   ██║█████╗  ██████╔╝ ╚████╔╝    ██║   ███████║██║██╔██╗ ██║██║  ███╗██║
██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝     ██║   ██╔══██║██║██║╚██╗██║██║   ██║╚═╝
███████╗ ╚████╔╝ ███████╗██║  ██║   ██║      ██║   ██║  ██║██║██║ ╚████║╚██████╔╝██╗
╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝                                                                                  
Made by [Brian Fopiano] at Cogswell Polytech, for
9MSU-CS100CA-Introduction to Scripting: Python - J.J. Sheu 
------------------------------------------------------------------------------------


""")
#MODULE ONE HERE
    def module1():
        def main():
            active = True
            while active:
                print( "PROGRAM 1: Starting!")
                time.sleep(0.1)
                print( "Program: 1). The loop through 'Hello, Python!' times" )
                time.sleep(0.01)
                print( "Program: 2). Prints the integers from 0 to 9" )
                time.sleep(0.01)
                print( "Program: 3). Prints the integers from 0 to 10" )
                time.sleep(0.01)
                print( "Program: 4). Prints the even integers from 2 to 20" )
                time.sleep(0.01)
                print( "Program: 5). Prints the squares of the integers from 1 to 10" )
                time.sleep(1)
                try:
                    PNum = int(input( "Which program would you like to see? 1, 2, 3, 4, or 5? (0 to close): " ))
                    if PNum == 1:
                        one(PNum)
                    elif PNum == 2:
                        two(PNum)
                    elif PNum == 3:
                        three(PNum)
                    elif PNum == 4:
                        four(PNum)
                    elif PNum == 5:
                        five(PNum)
                    elif PNum == 0:
                        print("Thank you! Back to Everything!")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers 1-5! or 0 to close")
                except ValueError:
                    print("This is NOT a value Try again!")
        def one(PNum):
            print( 'Program '+ str(PNum) +' Great!')
            print("Please wait...")
            time.sleep(1)
            print("Setting everything up for 10ct Hello!")
            #Start of loop
            Pynum = 1
            while Pynum <= 10:
                print('Hello, Python! Ct: '+ str(Pynum))
                time.sleep(0.05)
                Pynum += 1
            print("Thank you! goodbye!")
            main()
            # End of loop
            # End of Code 1
            #Start of Code 2
        def two(PNum):
            print( 'Program '+ str(PNum) +' Great!')
            print("Please wait...")
            time.sleep(1)
            print("Setting everything up!")
            #Start of loop
            Pynum = 0
            while Pynum <= 9:
                print(str(Pynum))
                time.sleep(0.05)
                Pynum += 1
            print("(2) Thank you! goodbye!")
            main()
            # End of loop
            # End of Code 2
            #Start of Code 3
        def three(PNum):
            print( 'Program '+ str(PNum) +' Great!')
            print("Please wait...")
            time.sleep(1)
            print("Setting everything up!")
            #Start of loop
            Pynum = 0
            while Pynum <= 10:
                print(str(Pynum))
                time.sleep(0.05)
                Pynum += 1
            print("(3) Thank you! goodbye!")
            main()
            # End of loop
            # End of Code 3
            #Start of Code 4
        def four(PNum):
            print( 'Program '+ str(PNum) +' Great!')
            print("Please wait...")
            time.sleep(1)
            print("Setting everything up!")
            #Start of loop
            Pynum = 2
            while Pynum <= 20:
                print(str(Pynum))
                time.sleep(0.05)
                Pynum += 2
            print("(4) Thank you! goodbye!")
            main()
            # End of loop
            #End of Code 4
            #Start of Code 5
        def five(PNum):
            print( 'Program '+ str(PNum) +' Great!')
            print("Please wait...")
            time.sleep(1)
            print("Setting everything up!")
            #Start of loop
            Pynum = 1
            while Pynum <= 10:
                PynumSQ = Pynum*Pynum
                print(str(Pynum), ' : ',str(PynumSQ))
                time.sleep(0.05)
                Pynum += 1
            print("(5) Thank you! goodbye!")
            main()
            # End of loop
            #
            #Kill / deny area
            #
            # 
        def bonus(PNum):


            main()
        main()
#MODULE TWO HERE
    def module2():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 2 EDITION! [SPHERES] Press 1 to start, or back to Everything [0]: ")
                time.sleep(0.1)

                try:
                    PNum = int(input( "Which program: " ))
                    if PNum == 1:
                        isNeg = false

         
                        # CIRCLE CALC
                        pi= float(math.pi)
                        print(pi,'<-- pi')
                        Rad = int(input('Radius: '))
                        if Rad >=0:
                            isNeg = False
                            Sa = 4 * pi * Rad **2
                            Vol = (4/3) * (pi * Rad ** 3)
                            print("Surface Area SU(Square units): ", Sa)
                            print("Volume in CU(Cubic units): ", Vol)
                        elif Rad < 0:
                            print("Please enter a positive value! try again!")
                        #END OF CIRCLE
               

                        input("Press any key to go back to the main menu!")
                        Everything()
                    elif PNum == 0:
                        print(" ")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE THREE HERE
    def module3():
        def main():
            months = str("JanFebMarAprMayJunJulAugSepOctNovDec")
            active = True
            while active:
                print( "This program is to showcase the assignments done! MODULE 3 EDITION [MONTHS]" )
                print("With key: ", months)
                time.sleep(0.1)

                try:
                    
                    MS = -3 
                    ME = 0
                    PAX = 0
                    PNum = int(input( "Start program? [1] or back to Everything [0]: " ))
                    if PNum == 1:
                        #
                        def Monthy():
                        #
                        #
                            PAX = int(input('Give me a number 1-12 or back to Everything [0]: '))
                            if PAX > 0 and PAX < 13:
                                #VArs
                                MDD = int(PAX*3)
                                MSD = int(MDD + MS)
                                MED = int(MDD + ME)
                                #VArs
                                print ('You said: ', months[MSD:MED])
                                print("TRY AGAIN!")
                                time.sleep(0.5)
                                Monthy()
                            elif modi == 0:
                                Everything()
                            else:
                                print("Please use a module! [NOT A NUMBER / IN RANGE]")
                                Monthy() 
                                #
                                #
                        Monthy()                 
                    elif PNum == 0:
                        print(" ")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE FOUR HERE
    def module4():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 4 EDITION! [STRING SLICING] Press 1 to start, or back to Everything [0]: ")
                time.sleep(0.1)

                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))
                    if PNum == 1:

                        # BEGIN SLICER
                        def slicer():
                            print("STARTING THE SLICER... Setting defailts...")
                            
                            #defaults
                            PString = "Example String!"
                            StartInt = 0
                            EndInt = 13
                            #defaults

                            #try the string
                            try:
                                PString = str(input("PLEASE ENTER A STRING: "))
                            except ValueError:
                                print("AhHHHA WhaT diD you dOOoO")
                                slicer()
                            #try the int
                            try:
                                StartInt = float(input("Please enter a starting integer: "))
                            except ValueError:
                                print("That's not a Integer! Whole numbers please!")
                                slicer()                            
                            #try the int
                            try:
                                EndInt = float(input("Please enter a ending integer: "))
                            except ValueError:
                                print("That's not an integer!")
                                slicer()

                            PStringNum = len(PString)
                            
                            print("The lengts of that string is [",PStringNum ,"]")
                            main()
                        #END OF SLICER
                        slicer()
                        input("Press any key to go back to the main menu!")
                        Everything()
                    elif PNum == 0:
                        print(" ")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE FIVE HERE
    def module5():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 5 EDITION! [Character Assignment] Press 1 to start, or back to Everything [Any Negative Number]: ")
                time.sleep(0.1)

                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))
                    if PNum == 1:
                        # BEGIN MODULE
                        try:
                            def NumT():
                                grade = float(input("Please input a number!: ")) 
                                if grade >= float(90):
                                    print("""Character A""")
                                    NumT()
                                elif (grade <90.0 and grade>=80.0):
                                    print("""Character B""")
                                    NumT()
                                elif (grade <80.0 and grade>=70.0):
                                    print("""Character C""")
                                    NumT()
                                elif (grade <70 and grade>=60):
                                    print("Character D")
                                    NumT()
                                elif (grade <60 and grade>=0):
                                    print("Character F")
                                    NumT()
                                elif (grade < 0):
                                    main()
                            NumT()    
                        
                        except ValueError:
                            print("Please use a number!")
                        #END OF MODULE
                    elif PNum == 0:
                        print("You hsve entered a negative value! Goodbye!")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE SIX HERE
    def module6():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 6 EDITION! [PASSWORDS] Press 1 to start, or back to Everything [0]: ")
                time.sleep(0.1)
                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))
                    if PNum == 1:
                        # BEGIN MODULE
                        print("PLACEHOLDER")
                        uC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ♥"
                        lC = "abcdefghijklmnopqrstuvwxyz♥"
                        Num = "0123456789"
                        special = "!@#$%^&*()_-+=\/|/?.>,<`~♥"
                        def PASSWORDINIT():
                            while True:
                                Pas = input("Password please: ")
                                Len = len(Pas)
                                if Len == 0:
                                    break
                                elif Len > 12:
                                    print("YOU MAY NOT HAVE A PASSWORD THAT LONG")
                                    continue
                                elif Len < 6:
                                    print("YOU MAY NOT HAVE A PASSWORD THAT SHORT")
                                    continue
                                elif ' ' in Pas:
                                    print("""The " " Character is not allowed!""")
                                    continue
                                error = True
                                for i in uC:
                                    if i in Pas:
                                        error = False
                                        break
                                if error:
                                    print("You need an upper case character!" )
                                    continue
                                error = True
                                for i in lC:
                                    if i in Pas:
                                        error = False
                                        break
                                if error:
                                    print("You need a lowercase character!" )
                                    continue
                                error = True
                                for i in Num:
                                    if i in Pas:
                                        error = False
                                        break
                                if error:
                                    print("YOU NEED A NUMBER!!!")
                                    continue
                                error = True
                                for i in special:
                                    if i in Pas:
                                        error = False
                                        break
                                if error:
                                    print("Be sure to have a Special character!")
                                    continue
                                print("Password set!")
                        PASSWORDINIT()
                        #END OF MODULE
                    elif PNum == 0:
                        print("Goodbye!")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE SEVEN HERE
    def module7():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 7 EDITION! [interleave Lists] Press 1 to start, or back to Everything [0]: ")
                time.sleep(0.1)
                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))      
                    if PNum == 1:
                        def stuff():
                            # BEGIN MODULE
                            #DEFAULT VALUES
                            PrimNum = [1,2,3,4,5,6,7 ]
                            SecoNum = ['A','B','C','D','E']
                            Mediator = []
                            #DEFAULT VALUES
                            Count = len(PrimNum)
                            #Get the length of PrimNum
                            Spell = len(SecoNum)
                            #Get the length of SecNum
                            FxRange = min(Count,Spell)
                            #Make a range minimum (array) with the numbers of Count and Spell
                            #\/ While "Var" is in the range of  "FxRange" do...
                            for var in range( FxRange ):
                                Mediator.append(PrimNum[var])
                                Mediator.append(SecoNum[var])
                                #... append in an alternating mediator the first/second 
                            #if the count(number of places in PrimNim) is larger than the roral range...
                            if(Count>FxRange):
                                for var in range(FxRange,Count):
                                    Mediator.append(PrimNum[var])
                                    #... keep doing this ^
                            elif(Spell >FxRange):
                                for var in range(FxRange,Spell):
                                    Mediator.append(SecoNum[var])
                            print("""  
                            """)
                            print("VARIABLES INCLUDE: ", PrimNum, " AND ", SecoNum)
                            time.sleep(1)
                            print("RESULT: ", Mediator )
                            time.sleep(3)
                        stuff() 
                            #END OF MODULE
                    elif PNum == 0:
                        print("Goodbye!")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
<<<<<<< Updated upstream
#MODULE EIGHT HERE
    def module8():
=======
#MODULE 305 HERE
    def module7():
>>>>>>> Stashed changes
        def main():
            active = True

            while active:
<<<<<<< Updated upstream
                print( "This program is to showcase the assignments done!" )
                print("MODULE 6 EDITION! [PASSWORDS] Press 1 to start, or back to Everything [0]: ")
                time.sleep(0.1)
                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))
                    if PNum == 1:
                        # BEGIN MODULE
                        print("PLACEHOLDER")
                        def _5000():
                            SVar = 0
                            TVar = 0
                            Cont = 0.1
                            print("TVar =+ 1")
                            while SVar<5000:
                                if SVar < 90:
                                    Cont = 0.3
                                else:
                                    Cont = 0.01
                                TVar += 1
                                SVar = SVar + TVar
                                print("Svar: ",SVar,"|  TVar: ",TVar)
                                time.sleep(Cont)
                            else:
                                print(SVar)
                                exit()
                                pass
                        _5000()
                        #END OF MODULE
=======
                print( "." )
                print("MODULE: ")
                time.sleep(0.1)
                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))      
                    if PNum == 1:
                        def stuff():
                            win = GraphWin('Smiley Faces', 400, 400) # give title and dimensions
                            win.setBackground('cyan')
                            win.setCoords(0, 0, 400, 400)
                            
                            def drawFace(center, size,window):
                            
                                head = Circle(center,size*20)
                                head.setFill("green")
                                head.draw(win)
                            
                                mouth = Circle(center, size*13)
                                mouth.setFill("red")
                                mouth.setOutline("red")
                                mouth.draw(win)
                                smile = Circle(center, size*14)
                                smile.move(0,size*4)
                                smile.setFill("green")
                                smile.setOutline("green")
                                smile.draw(win)
                            
                                eyebrow = Circle(center,size*4)
                                eyebrow.move(-size*8,size*10)
                                eyebrow.setFill('black')
                                eyebrow.draw(win)
                                eyebrow2 = eyebrow.clone()
                                eyebrow2.draw(win)
                                eyebrow2.move(size*16, 0)
                                eyecircle = Circle(center,size*4)
                                eyecircle.move(-size*8,size*9)
                                eyecircle.setFill('green')
                                eyecircle.setOutline('green')
                                eyecircle.draw(win)
                                eyecircle2 = eyecircle.clone()
                                eyecircle2.draw(win)
                                eyecircle2.move(size*16, 0)
                            
                                eyelid = Circle(center,size*3)
                                eyelid.move(-size*8,size*8)
                                eyelid.setFill('brown')
                                eyelid.draw(win)
                                eyelid2 = eyelid.clone()
                                eyelid2.draw(win)
                                eyelid2.move(size*16, 0)
                            
                                eye = Circle(center, size*3)
                                eye.move(-size*8,size*6)
                                eye.setFill('orange')
                                eye.draw(win)
                                eye2 = eye.clone()
                                eye2.draw(win)
                                eye2.move(size*16, 0)
                            
                                pupil = Circle(center,size)
                                pupil.move(-size*9,size*7)
                                pupil.setFill('blue')
                                pupil.draw(win)
                                pupil2 = pupil.clone()
                                pupil2.draw(win)
                                pupil2.move(size*16,0)
                            
                                nose = Circle(center,size*3)
                                nose.move(0,-size*2)
                                nose.setOutline('yellow')
                                nose.setFill('yellow')
                                nose.draw(win)
                            
                            def main():
                            
                                i = 0
                                for i in range (1,5):
                                    center = Point(350,490-i*110)#top to bottom, increasing radius
                                    Face = drawFace(center,i*.8,win)
                                    center = Point(-50+i*85,-50+i*90)#bottom left to top right, decreasing radius
                                    Face = drawFace(center,3-(i*.5),win)
                                    center = Point(340-i*75,-65+i*100)#bottom right to top left, increasing radius
                                    Face = drawFace(center,i,win)
                            
                                message = Text(Point(200, 380), 'Click anywhere to quit.')
                                message.setFill('blue')
                                message.draw(win)
                                win.getMouse()
                                win.close()
                            
                            main()
>>>>>>> Stashed changes
                    elif PNum == 0:
                        print("Goodbye!")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or back to Everything [0]: ")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
<<<<<<< Updated upstream
=======
#MODULE IDENTIFICATION HERE
>>>>>>> Stashed changes
#MODULE IDENTIFICATION HERE
    try:
        
        print("Module 1: Week-01 Wed-Thu (07/10 - 07/11) Assignment [] (5 Programs)")
        print("Module 2: Week-02 Mon-Tue (07/15 - 07/16) Assignment [] (Sphere Calculaion)")
        print("Module 3: Week-02 Wed-Thu (07/17 - 07/18) Assignment [] (Month by number)")
        print("Module 4: Week-03 Mon-Tue (07/22 - 07/23) Assignment [] (Slicing Index) ")
        print("Module 5: Week-03 Wed-Thu (07/24 - 07/25) Assignment [] (Grades by Number)")
        print("Module 6: Week-04 Mon-Tue (07/29 - 07/30) Assignment [] (PassWord) ")
        print("Module 7: Week-03 Mon-Tue (07/22 - 07/23) Assignment [] (interleave Lists)")
        print("Module 8: Week-04 Wed-Thu (07/31 - 08/01) Assignment [] (Add Up To 5000)")
        print("Module 9: Week-05 Mon-Tue (08/05 - 08/06) Assignment [] (Python Java Scores)")
        print("Module 10: Week-05 Wed-Thu (08/07 - 08/08) Assignment [] (Slicing Boundary Checking)")
        print("Module 11: Week-06 Mon-Tue-Wed-Thu (08/12 - 08/13) Assignment [] (Face)")
        
        modi = int(input( "Which Module? module: [1], [2], [3], [4], OR CLOSE WITH --> [0]: " ))

        if modi == 1:
            module1()
        elif modi == 2:
            module2()
        elif modi == 3:
            module3()
        elif modi == 4:
            module4()
        elif modi == 5:
            module5()
        elif modi == 6:
            module6()
        elif modi ==7:
            module7()
        elif modi ==8:
            module8()
        elif modi == 0:
            exit()
        else:
            print("Please use a module!")
            Everything()
    except ValueError:
        print("This is NOT a module!!!")
#Run it! 
Everything()

from graphics import *
 
win = GraphWin('Smiley Faces', 400, 400) # give title and dimensions
win.setBackground('cyan')
win.setCoords(0, 0, 400, 400)
 
def drawFace(center, size,window):
 
    head = Circle(center,size*20)
    head.setFill("green")
    head.draw(win)
 
    mouth = Circle(center, size*13)
    mouth.setFill("red")
    mouth.setOutline("red")
    mouth.draw(win)
    smile = Circle(center, size*14)
    smile.move(0,size*4)
    smile.setFill("green")
    smile.setOutline("green")
    smile.draw(win)
 
    eyebrow = Circle(center,size*4)
    eyebrow.move(-size*8,size*10)
    eyebrow.setFill('black')
    eyebrow.draw(win)
    eyebrow2 = eyebrow.clone()
    eyebrow2.draw(win)
    eyebrow2.move(size*16, 0)
    eyecircle = Circle(center,size*4)
    eyecircle.move(-size*8,size*9)
    eyecircle.setFill('green')
    eyecircle.setOutline('green')
    eyecircle.draw(win)
    eyecircle2 = eyecircle.clone()
    eyecircle2.draw(win)
    eyecircle2.move(size*16, 0)
 
    eyelid = Circle(center,size*3)
    eyelid.move(-size*8,size*8)
    eyelid.setFill('brown')
    eyelid.draw(win)
    eyelid2 = eyelid.clone()
    eyelid2.draw(win)
    eyelid2.move(size*16, 0)
 
    eye = Circle(center, size*3)
    eye.move(-size*8,size*6)
    eye.setFill('orange')
    eye.draw(win)
    eye2 = eye.clone()
    eye2.draw(win)
    eye2.move(size*16, 0)
 
    pupil = Circle(center,size)
    pupil.move(-size*9,size*7)
    pupil.setFill('blue')
    pupil.draw(win)
    pupil2 = pupil.clone()
    pupil2.draw(win)
    pupil2.move(size*16,0)
 
    nose = Circle(center,size*3)
    nose.move(0,-size*2)
    nose.setOutline('yellow')
    nose.setFill('yellow')
    nose.draw(win)
 
def main():
 
    i = 0
    for i in range (1,5):
        center = Point(350,490-i*110)#top to bottom, increasing radius
        Face = drawFace(center,i*.8,win)
        center = Point(-50+i*85,-50+i*90)#bottom left to top right, decreasing radius
        Face = drawFace(center,3-(i*.5),win)
        center = Point(340-i*75,-65+i*100)#bottom right to top left, increasing radius
        Face = drawFace(center,i,win)
 
    message = Text(Point(200, 380), 'Click anywhere to quit.')
    message.setFill('blue')
    message.draw(win)
    win.getMouse()
    win.close()
 
main()