firstName=input("Enter your first name --> ")
lastName=input("Enter your last name --> ")
age=int(input("Enter your age --> "))
gender=input("Enter your gender --> ")
fatherName=input("Enter your father name -->")
bankName=input("Enter you bank name -->")
branchCode=input("Enter your branch code -->") 
if age>=18:
    password=input("Enter your password --> ")
    confPass=input("Confirm your password --> ")
    if password==confPass:
        print("Terms and Conditions")
        print("1.You hereby confirm that you are providing all the correct informationa about yourself.")
        print("2.You are responsible for your own actions.")
        print("3.You confirm that you are not motivated by game to perform any action in the real world.")
        print("4.You confirm that you are mentally sound to understand the fictionary entertainment tasks performed in the game")
        print("5.You understand that the violence in the game is imagenery and does not harm any real human or animal")
        print("6.To make any complaint against game, you can appeal in honourable high court or honourable supreme court of India")
        print("7.You understand that the winning in the game are just for entertainment and does not promise any real prize")
        choice="yes", "no"
        confirm=input("Enter 'yes' or 'no' ")
        if confirm =="yes":
            print("You can enter")
            print("Quiz starts -")
            print("Q1. Python is what kind of language?")
            highLevel="a"
            lowLevel="b"
            noneOfThese="c"
            bothaandb="d"
            print("a. High level")
            print("b. Low level")
            print("c. none of these")
            print("d. Both a and b")
            choice1=input("Ans-- ")
            if choice1 == highLevel:
                print("Correct answer! You got 1 mark")
                marks=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice1=input("Ans-- ")
                if choice1 == highLevel:
                    print("Correct answer! You got 1 mark")
                    marks=1
                    
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice1=input("Ans-- ")
                    if choice1 == highLevel:
                        print("Correct answer!! You got 1 mark")
                        marks=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks=0
            print("Q2. Python is read by computer with which software?")
            print("a. Compiler")
            print("b. Interpreter")
            print("c. both a and b")
            print("d. none of these")
            compiler="a"
            interpreter="b"
            both="c"
            none="d"
            choice2=input("Ans-- ")
            if choice2 == interpreter:
                print("Correct answer! You got 1 mark")
                marks+=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice2=input("Ans-- ")
                if choice2 == interpreter:
                    print("Correct answer! You got 1 mark")
                    marks=+1            
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice2=input("Ans-- ")
                    if choice2 == interpreter:
                        print("Correct answer!! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks+=0
            print("Q3. How many opertors are there in python")
            print("a. 6")
            print("b. 7")
            print("c. 8")
            print("d. 9")
            six,seven,eight,nine="a","b","c","d"
            choice3=input("Ans -- ")
            if choice3 == seven:
                print("Correct answer! You got 1 mark")
                marks+=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice3=input("Ans-- ")
                if choice3 == seven:
                    print("Correct answer! You got 1 mark")
                    marks=+1            
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice3=input("Ans-- ")
                    if choice3 == seven:
                        print("Correct answer!! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks+=0
            print("Q4. How many logical operators are there in pyhton?")
            print("a. 2")
            print("b. 3")
            print("c. 4")
            print("d. 5")
            two,three,four,five="a","b","c","d"
            choice4=input("Ans-- ")
            if choice4 == three:
                print("Correct answer! You got 1 mark")
                marks+=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice4=input("Ans-- ")
                if choice4 == three:
                    print("Correct answer! You got 1 mark")
                    marks=+1            
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice4=input("Ans-- ")
                    if choice4 == three:
                        print("Correct answer!! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks+=0      
            print("Q5. what symbol is used to add comments in a code in VS Code?")
            print("a. css")
            print("b. dash")
            print("c. both")
            print("d. none")
            css,dash,both2,noneOfTheAbove="a","b","c","d"
            choice5=input("Ans-- ")
            if choice5 == css:
                print("Correct answer! You got 1 mark")
                marks+=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice5=input("Ans-- ")
                if choice5 == css:
                    print("Correct answer! You got 1 mark")
                    marks=+1            
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice5=input("Ans-- ")
                    if choice5 == css:
                        print("Correct answer!! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks+=0       
            print("Q6. Which language is used for web dseigning?")
            print("a. CSS")
            print("b. C++")
            print("c. JAVA")
            print("d. C#")
            css,cPlusPlus,java,cSharp="a","b","c","d"
            choice6=input("Ans-- ")
            if choice6 == css:
                print("Correct answer! You got 1 mark")
                marks+=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice6=input("Ans-- ")
                if choice6 == css:
                    print("Correct answer! You got 1 mark")
                    marks=+1            
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice6=input("Ans-- ")
                    if choice6 == css:
                        print("Correct answer!! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks+=0
            print("Q7. What is the capital of Germany?")
            print("a. Munich")
            print("b. Berlin")
            print("c. Hamburg")
            print("d. Lyon")
            munich,berlin,hamburg,lyon="a","b","c","d"
            choice7=input("Ans-- ")
            if choice7 == berlin:
                print("Correct answer! You got 1 mark")
                marks+=1
            else:
                print("Incorrect answer!!. You can try again two more times.")
                choice7=input("Ans-- ")
                if choice7 == berlin:
                    print("Correct answer! You got 1 mark")
                    marks=+1            
                else:
                    print("Incorrect answer!!. You can try one more time.")
                    choice7=input("Ans-- ")
                    if choice7 == berlin:
                        print("Correct answer!! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. Move to next question")
                        marks+=0
            
            print("Total Marks --> ",marks)                                              
        elif confirm=="no":
            print("You can exit. Thank you!")
        else:
            print("This option is not valid.")
            
    elif password!=confPass:
        print("Password doesn't match! You can try again 3 more times.")
        confPass=input("Confirm your password --> ")
        if password==confPass:
            print("Terms and Conditions")
            print("1.You hereby confirm that you are providing all the correct informationa about yourself.")
            print("2.You are responsible for your own actions.")
            print("3.You confirm that you are not motivated by game to perform any action in the real world.")
            print("4.You confirm that you are mentally sound to understand the fictionary entertainment tasks performed in the game")
            print("5.You understand that the violence in the game is imagenery and does not harm any real human or animal")
            print("6.To make any complaint against game, you can appeal in honourable high court or honourable supreme court of India")
            print("7.You understand that the winning in the game are just for entertainment and does not promise any real prize")
            choice="yes", "no"
            confirm=input("Enter 'yes' or 'no' ")
            if confirm =="yes":
                print("You can enter")
                print("Quiz starts -")
                print("Q1. Python is what kind of language?")
                highLevel="a"
                lowLevel="b"
                noneOfThese="c"
                bothaandb="d"
                print("a. High level")
                print("b. Low level")
                print("c. none of these")
                print("d. Both a and b")
                choice1=input("Ans-- ")
                if choice1 == highLevel:
                    print("Correct answer! You got 1 mark")
                    marks=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice1=input("Ans-- ")
                    if choice1 == highLevel:
                        print("Correct answer! You got 1 mark")
                        marks=1
            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice1=input("Ans-- ")
                        if choice1 == highLevel:
                            print("Correct answer!! You got 1 mark")
                            marks=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks=0
                print("Q2. Python is read by computer with which software?")
                print("a. Compiler")
                print("b. Interpreter")
                print("c. both a and b")
                print("d. none of these")
                compiler="a"
                interpreter="b"
                both="c"
                none="d"
                choice2=input("Ans-- ")
                if choice2 == interpreter:
                    print("Correct answer! You got 1 mark")
                    marks+=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice2=input("Ans-- ")
                    if choice2 == interpreter:
                        print("Correct answer! You got 1 mark")
                        marks=+1            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice2=input("Ans-- ")
                        if choice2 == interpreter:
                            print("Correct answer!! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks+=0
                print("Q3. How many opertors are there in python")
                print("a. 6")
                print("b. 7")
                print("c. 8")
                print("d. 9")
                six,seven,eight,nine="a","b","c","d"
                choice3=input("Ans -- ")
                if choice3 == seven:
                    print("Correct answer! You got 1 mark")
                    marks+=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice3=input("Ans-- ")
                    if choice3 == seven:
                        print("Correct answer! You got 1 mark")
                        marks=+1            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice3=input("Ans-- ")
                        if choice3 == seven:
                            print("Correct answer!! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks+=0
                print("Q4. How many logical operators are there in pyhton?")
                print("a. 2")
                print("b. 3")
                print("c. 4")
                print("d. 5")
                two,three,four,five="a","b","c","d"
                choice4=input("Ans-- ")
                if choice4 == three:
                    print("Correct answer! You got 1 mark")
                    marks+=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice4=input("Ans-- ")
                    if choice4 == three:
                        print("Correct answer! You got 1 mark")
                        marks=+1            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice4=input("Ans-- ")
                        if choice4 == three:
                            print("Correct answer!! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks+=0      
                print("Q5. what symbol is used to add comments in a code in VS Code?")
                print("a. css")
                print("b. dash")
                print("c. both")
                print("d. none")
                css,dash,both2,noneOfTheAbove="a","b","c","d"
                choice5=input("Ans-- ")
                if choice5 == css:
                    print("Correct answer! You got 1 mark")
                    marks+=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice5=input("Ans-- ")
                    if choice5 == css:
                        print("Correct answer! You got 1 mark")
                        marks=+1            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice5=input("Ans-- ")
                        if choice5 == css:
                            print("Correct answer!! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks+=0       
                print("Q6. Which language is used for web dseigning?")
                print("a. CSS")
                print("b. C++")
                print("c. JAVA")
                print("d. C#")
                css,cPlusPlus,java,cSharp="a","b","c","d"
                choice6=input("Ans-- ")
                if choice6 == css:
                    print("Correct answer! You got 1 mark")
                    marks+=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice6=input("Ans-- ")
                    if choice6 == css:
                        print("Correct answer! You got 1 mark")
                        marks=+1            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice6=input("Ans-- ")
                        if choice6 == css:
                            print("Correct answer!! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks+=0
                print("Q7. What is the capital of Germany?")
                print("a. Munich")
                print("b. Berlin")
                print("c. Hamburg")
                print("d. Lyon")
                munich,berlin,hamburg,lyon="a","b","c","d"
                choice7=input("Ans-- ")
                if choice7 == berlin:
                    print("Correct answer! You got 1 mark")
                    marks+=1
                else:
                    print("Incorrect answer!!. You can try again two more times.")
                    choice7=input("Ans-- ")
                    if choice7 == berlin:
                        print("Correct answer! You got 1 mark")
                        marks=+1            
                    else:
                        print("Incorrect answer!!. You can try one more time.")
                        choice7=input("Ans-- ")
                        if choice7 == berlin:
                            print("Correct answer!! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. Move to next question")
                            marks+=0
            
                print("Total Marks --> ",marks)                                              
            elif confirm=="no":
                print("You can exit. Thank you!")
            else:
                print("This option is not valid.")
            
            
        elif password!=confPass:
            print("Password doesn't match! You can try again 2 more times.")
            confPass=input("Confirm your password --> ")
            if password==confPass:
                print("Terms and Conditions")
                print("1.You hereby confirm that you are providing all the correct informationa about yourself.")
                print("2.You are responsible for your own actions.")
                print("3.You confirm that you are not motivated by game to perform any action in the real world.")
                print("4.You confirm that you are mentally sound to understand the fictionary entertainment tasks performed in the game")
                print("5.You understand that the violence in the game is imagenery and does not harm any real human or animal")
                print("6.To make any complaint against game, you can appeal in honourable high court or honourable supreme court of India")
                print("7.You understand that the winning in the game are just for entertainment and does not promise any real prize")
                choice="yes", "no"
                confirm=input("Enter 'yes' or 'no' ")
                if confirm =="yes":
                    print("You can enter")
                    print("Quiz starts -")
                    print("Q1. Python is what kind of language?")
                    highLevel="a"
                    lowLevel="b"
                    noneOfThese="c"
                    bothaandb="d"
                    print("a. High level")
                    print("b. Low level")
                    print("c. none of these")
                    print("d. Both a and b")
                    choice1=input("Ans-- ")
                    if choice1 == highLevel:
                        print("Correct answer! You got 1 mark")
                        marks=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice1=input("Ans-- ")
                        if choice1 == highLevel:
                            print("Correct answer! You got 1 mark")
                            marks=1
                
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice1=input("Ans-- ")
                            if choice1 == highLevel:
                                print("Correct answer!! You got 1 mark")
                                marks=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks=0
                    print("Q2. Python is read by computer with which software?")
                    print("a. Compiler")
                    print("b. Interpreter")
                    print("c. both a and b")
                    print("d. none of these")
                    compiler="a"
                    interpreter="b"
                    both="c"
                    none="d"
                    choice2=input("Ans-- ")
                    if choice2 == interpreter:
                        print("Correct answer! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice2=input("Ans-- ")
                        if choice2 == interpreter:
                            print("Correct answer! You got 1 mark")
                            marks=+1            
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice2=input("Ans-- ")
                            if choice2 == interpreter:
                                print("Correct answer!! You got 1 mark")
                                marks+=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks+=0
                    print("Q3. How many opertors are there in python")
                    print("a. 6")
                    print("b. 7")
                    print("c. 8")
                    print("d. 9")
                    six,seven,eight,nine="a","b","c","d"
                    choice3=input("Ans -- ")
                    if choice3 == seven:
                        print("Correct answer! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice3=input("Ans-- ")
                        if choice3 == seven:
                            print("Correct answer! You got 1 mark")
                            marks=+1            
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice3=input("Ans-- ")
                            if choice3 == seven:
                                print("Correct answer!! You got 1 mark")
                                marks+=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks+=0
                    print("Q4. How many logical operators are there in pyhton?")
                    print("a. 2")
                    print("b. 3")
                    print("c. 4")
                    print("d. 5")
                    two,three,four,five="a","b","c","d"
                    choice4=input("Ans-- ")
                    if choice4 == three:
                        print("Correct answer! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice4=input("Ans-- ")
                        if choice4 == three:
                            print("Correct answer! You got 1 mark")
                            marks=+1            
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice4=input("Ans-- ")
                            if choice4 == three:
                                print("Correct answer!! You got 1 mark")
                                marks+=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks+=0      
                    print("Q5. what symbol is used to add comments in a code in VS Code?")
                    print("a. css")
                    print("b. dash")
                    print("c. both")
                    print("d. none")
                    css,dash,both2,noneOfTheAbove="a","b","c","d"
                    choice5=input("Ans-- ")
                    if choice5 == css:
                        print("Correct answer! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice5=input("Ans-- ")
                        if choice5 == css:
                            print("Correct answer! You got 1 mark")
                            marks=+1            
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice5=input("Ans-- ")
                            if choice5 == css:
                                print("Correct answer!! You got 1 mark")
                                marks+=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks+=0       
                    print("Q6. Which language is used for web dseigning?")
                    print("a. CSS")
                    print("b. C++")
                    print("c. JAVA")
                    print("d. C#")
                    css,cPlusPlus,java,cSharp="a","b","c","d"
                    choice6=input("Ans-- ")
                    if choice6 == css:
                        print("Correct answer! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice6=input("Ans-- ")
                        if choice6 == css:
                            print("Correct answer! You got 1 mark")
                            marks=+1            
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice6=input("Ans-- ")
                            if choice6 == css:
                                print("Correct answer!! You got 1 mark")
                                marks+=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks+=0
                    print("Q7. What is the capital of Germany?")
                    print("a. Munich")
                    print("b. Berlin")
                    print("c. Hamburg")
                    print("d. Lyon")
                    munich,berlin,hamburg,lyon="a","b","c","d"
                    choice7=input("Ans-- ")
                    if choice7 == berlin:
                        print("Correct answer! You got 1 mark")
                        marks+=1
                    else:
                        print("Incorrect answer!!. You can try again two more times.")
                        choice7=input("Ans-- ")
                        if choice7 == berlin:
                            print("Correct answer! You got 1 mark")
                            marks=+1            
                        else:
                            print("Incorrect answer!!. You can try one more time.")
                            choice7=input("Ans-- ")
                            if choice7 == berlin:
                                print("Correct answer!! You got 1 mark")
                                marks+=1
                            else:
                                print("Incorrect answer!!. Move to next question")
                                marks+=0
                
                    print("Total Marks --> ",marks)                                              
                elif confirm=="no":
                    print("You can exit. Thank you!")
                else:
                    print("This option is not valid.")
                
            elif password!=confPass:
                print("Password doesn't match! You can try again 1 more time.")
                confPass=input()
                if password==confPass:
                    print("Terms and Conditions")
                    print("1.You hereby confirm that you are providing all the correct informationa about yourself.")
                    print("2.You are responsible for your own actions.")
                    print("3.You confirm that you are not motivated by game to perform any action in the real world.")
                    print("4.You confirm that you are mentally sound to understand the fictionary entertainment tasks performed in the game")
                    print("5.You understand that the violence in the game is imagenery and does not harm any real human or animal")
                    print("6.To make any complaint against game, you can appeal in honourable high court or honourable supreme court of India")
                    print("7.You understand that the winning in the game are just for entertainment and does not promise any real prize")
                    choice="yes", "no"
                    confirm=input("Enter 'yes' or 'no' ")
                    if confirm =="yes":
                        print("You can enter")
                        print("Quiz starts -")
                        print("Q1. Python is what kind of language?")
                        highLevel="a"
                        lowLevel="b"
                        noneOfThese="c"
                        bothaandb="d"
                        print("a. High level")
                        print("b. Low level")
                        print("c. none of these")
                        print("d. Both a and b")
                        choice1=input("Ans-- ")
                        if choice1 == highLevel:
                            print("Correct answer! You got 1 mark")
                            marks=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice1=input("Ans-- ")
                            if choice1 == highLevel:
                                print("Correct answer! You got 1 mark")
                                marks=1
                    
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice1=input("Ans-- ")
                                if choice1 == highLevel:
                                    print("Correct answer!! You got 1 mark")
                                    marks=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks=0
                        print("Q2. Python is read by computer with which software?")
                        print("a. Compiler")
                        print("b. Interpreter")
                        print("c. both a and b")
                        print("d. none of these")
                        compiler="a"
                        interpreter="b"
                        both="c"
                        none="d"
                        choice2=input("Ans-- ")
                        if choice2 == interpreter:
                            print("Correct answer! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice2=input("Ans-- ")
                            if choice2 == interpreter:
                                print("Correct answer! You got 1 mark")
                                marks=+1            
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice2=input("Ans-- ")
                                if choice2 == interpreter:
                                    print("Correct answer!! You got 1 mark")
                                    marks+=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks+=0
                        print("Q3. How many opertors are there in python")
                        print("a. 6")
                        print("b. 7")
                        print("c. 8")
                        print("d. 9")
                        six,seven,eight,nine="a","b","c","d"
                        choice3=input("Ans -- ")
                        if choice3 == seven:
                            print("Correct answer! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice3=input("Ans-- ")
                            if choice3 == seven:
                                print("Correct answer! You got 1 mark")
                                marks=+1            
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice3=input("Ans-- ")
                                if choice3 == seven:
                                    print("Correct answer!! You got 1 mark")
                                    marks+=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks+=0
                        print("Q4. How many logical operators are there in pyhton?")
                        print("a. 2")
                        print("b. 3")
                        print("c. 4")
                        print("d. 5")
                        two,three,four,five="a","b","c","d"
                        choice4=input("Ans-- ")
                        if choice4 == three:
                            print("Correct answer! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice4=input("Ans-- ")
                            if choice4 == three:
                                print("Correct answer! You got 1 mark")
                                marks=+1            
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice4=input("Ans-- ")
                                if choice4 == three:
                                    print("Correct answer!! You got 1 mark")
                                    marks+=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks+=0      
                        print("Q5. what symbol is used to add comments in a code in VS Code?")
                        print("a. css")
                        print("b. dash")
                        print("c. both")
                        print("d. none")
                        css,dash,both2,noneOfTheAbove="a","b","c","d"
                        choice5=input("Ans-- ")
                        if choice5 == css:
                            print("Correct answer! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice5=input("Ans-- ")
                            if choice5 == css:
                                print("Correct answer! You got 1 mark")
                                marks=+1            
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice5=input("Ans-- ")
                                if choice5 == css:
                                    print("Correct answer!! You got 1 mark")
                                    marks+=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks+=0       
                        print("Q6. Which language is used for web dseigning?")
                        print("a. CSS")
                        print("b. C++")
                        print("c. JAVA")
                        print("d. C#")
                        css,cPlusPlus,java,cSharp="a","b","c","d"
                        choice6=input("Ans-- ")
                        if choice6 == css:
                            print("Correct answer! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice6=input("Ans-- ")
                            if choice6 == css:
                                print("Correct answer! You got 1 mark")
                                marks=+1            
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice6=input("Ans-- ")
                                if choice6 == css:
                                    print("Correct answer!! You got 1 mark")
                                    marks+=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks+=0
                        print("Q7. What is the capital of Germany?")
                        print("a. Munich")
                        print("b. Berlin")
                        print("c. Hamburg")
                        print("d. Lyon")
                        munich,berlin,hamburg,lyon="a","b","c","d"
                        choice7=input("Ans-- ")
                        if choice7 == berlin:
                            print("Correct answer! You got 1 mark")
                            marks+=1
                        else:
                            print("Incorrect answer!!. You can try again two more times.")
                            choice7=input("Ans-- ")
                            if choice7 == berlin:
                                print("Correct answer! You got 1 mark")
                                marks=+1            
                            else:
                                print("Incorrect answer!!. You can try one more time.")
                                choice7=input("Ans-- ")
                                if choice7 == berlin:
                                    print("Correct answer!! You got 1 mark")
                                    marks+=1
                                else:
                                    print("Incorrect answer!!. Move to next question")
                                    marks+=0
                    
                        print("Total Marks --> ",marks)                                              
                    elif confirm=="no":
                        print("You can exit. Thank you!")
                    else:
                        print("This option is not valid.")
                    
                else:
                    print("You have entered wrong password many times. You cannot proceed further.")
            
else:
    print("Not eligible")