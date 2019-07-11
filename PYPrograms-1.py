# Python organized by Brian Fopiano ⋈
import math
import sys
import time
#BASE IMPORT FOR EVERYTHING
def Everything():
    print("""------------------------------------------------------------------------------------
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
        main()
#MODULE TWO HERE
    def module2():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 2 EDITION! [SPHERES] Press 1 to start, and 0 to close!")
                time.sleep(0.1)

                try:
                    PNum = int(input( "Which program: " ))
                    if PNum == 1:
                        pi= float(math.pi)
                        print(pi,'<-- pi')
                        Rad = int(input('Radius: '))
                        Sa = 4 * pi * Rad **2
                        Vol = (4/3) * (pi * Rad ** 3)
                        print("Surface Area SU(Square units): ", Sa)
                        print("Volume in CU(Cubic units): ", Vol)
                        input("Press any key to go back to the main menu!")
                        Everything()
                    elif PNum == 0:
                        print(" ")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or 0 to close")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE THREE HERE
    def module3():
        def main():
            active = True

            while active:
                print( "This program is to showcase the assignments done!" )
                print("MODULE 3 EDITION [MONTHS]")
                time.sleep(0.1)

                try:
                    PNum = int(input( "Which program: " ))
                    if PNum == 1:
#
                        print("Thank you! Ill send you back to the menu!")
                        time.sleep(2.5)
                        Everything()
                    elif PNum == 0:
                        print(" ")
                        active = False
                        Everything()
                    elif PNum > 5:
                        print("Please use proper numbers or 0 to close")
                except ValueError:
                    print("This is NOT a value Try again!")
        main()
#MODULE IDENTIFICATION HERE
    try:
        
        print("Module 1: Week-01 Mon-Tue (07/08 - 07/09) Assignment (DONE) [BASICS]")
        print("Module 2: Week-01 Wed-Thu (07/10 - 07/11) Assignment (DONE) [SPHERE VOLUME]")
        print("Module 3: Week-02 Mon-Tue (07/15 - 07/16) Assignment (NOT DONE) []")
        print("Module 4: Week-02 Wed-Thu (07/17 - 07/18) Assignment (NOT DONE) [MONTHS]")
        modi = int(input( "Which Module? module: 1, 2, 3, 4, or close '0':" ))

        if modi == 1:
            module1()
        elif modi == 2:
            module2()
        elif modi == 0:
            SystemExit()
        else:
            print("Please use a module!")
            Everything()
    except ValueError:
        print("This is NOT a module!!!")
#Run it! 
Everything()

