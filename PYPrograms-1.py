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
                print("MODULE 6 EDITION! [FACTORIALIZED ADDITION TO 5000] Press 1 to start, or back to Everything [0]: ")
                time.sleep(0.1)
                try:
                    PNum = int(input( "Start program? [1] Go back [0] " ))
                    if PNum == 1:
                        # BEGIN MODULE
                        print("PLACEHOLDER")







                        
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
#MODULE IDENTIFICATION HERE
    try:
        
        print("Module 1: Week-01 Wed-Thu (07/10 - 07/11) Assignment [] (5 Programs)")
        print("Module 2: Week-02 Mon-Tue (07/15 - 07/16) Assignment [] (Sphere Calculaion)")
        print("Module 3: Week-02 Wed-Thu (07/17 - 07/18) Assignment [] (Month by number)")
        print("Module 4: Week-03 Mon-Tue (07/22 - 07/23) Assignment [] (Slicing Index) ")
        print("Module 5: Week-03 Wed-Thu (07/24 - 07/25) Assignment [] (Grades by Number)")
        print("Module PREP: Week-04 Mon-Tue (07/29 - 07/30) Preparation[---] ")
        print("Module 6: Week-04 Wed-Thu (07/31 - 08/01) Assignment [] (Count to 5000 Factorial)")
        print("Module 7: Week-05 Mon-Tue (08/05 - 08/06) Assignment [] (Java/Python Justification)")
        
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
        elif modi == 0:
            exit()
        else:
            print("Please use a module!")
            Everything()
    except ValueError:
        print("This is NOT a module!!!")
#Run it! 
Everything()

