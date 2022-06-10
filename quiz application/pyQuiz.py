class QuizApp:
    def __init__(self):
        self.username=""

    def startup(self):
        self.greeting()
        self.username= input('What is your name? ')
        print(f'Welcome, {self.username} !')

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to PyQuiz! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()
    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    
    def menu(self):
        self.menu_header()
    #get the user's selection and act on it. This loop will  
    #run until the user exits the app
        selection=""
        while(True):
            selection=input('Selection? ')
            if len(selection)==0:
                self.menu_error()
                continue

            selection=selection.capitalize()
            if selection[0]=='E':
                self.goodbye()
                break
            elif selection[0]=='M':
                self.menu_header()
                continue
            elif selection[0]=='L':
                print('\n Available Quizzes are: ')
                #todo list the quizzes
                print('--------------------------------\n')
                continue
            elif selection[0]=='T':
                try:
                    quiznum=int(input('Quiz number: '))
                    print(f"You've selected quiz n° {quiznum}")
                except:
                    self.menu_error()
            else:
                self.menu_error()
""" if __name__=="__main__":
    app=QuizApp()
    app.run() """