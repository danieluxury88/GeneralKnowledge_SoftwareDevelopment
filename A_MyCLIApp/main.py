# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import apps.ninety_nine_hours as ninety_nine_hours
import apps.chat_gpt_handler_api as chat_gpt_handler_api
import apps.tasks_handler as tasks_handler
import devtests.dev_test as dev_test
import apps.list_handler as list_handler



class CLIMenuHandler:

    # Define a function to display a menu and get user input</h1>
    def __init__(self):
        print("Init Main")
        self.chatgpt_app = chat_gpt_handler_api.ChatGPTHandler()
        self.nnnh_app = ninety_nine_hours.NinetyNineHours()
        self.tasks_app = tasks_handler.TasksHandler()
        self.list_app = list_handler.ListHandler('data/list.json')

    
        self.MAIN_MENU = {
            ' ': 'Question',
            'c': 'Configure Chat',
            'n': '99Hours',
            't': 'Enter new task',
            'l': 'List',
            'd': 'DevTest',
            'q': 'Quit',
        }

        self.NESTED_MENU_1 = {
            '1': 'Nested Option 1',
            '2': 'Nested Option 2',
            '0': 'Back'
        }

        self.NESTED_MENU_2 = {
            '1': 'Nested Option 3',
            '2': 'Nested Option 4',
            '0': 'Back'
        }

        self.NESTED_MENUS = {
            '1': self.NESTED_MENU_1,
            '2': self.NESTED_MENU_2,
            '0': 'Back'
        }

        self.FAST_OPTIONS_MENUS = {
            'e': 'endulzar',
            'd': 'default mode',
            '0': 'Back',
        }
        os.system('cls' if os.name == 'nt' else clear)

        

    def get_user_choice(self, menu):
        for key, value in menu.items():
            print(f'{key}: {value}')
        choice = input('Please enter your choice: ')
        return choice


    def execute_choice(self, choice):
        if choice == '0' or choice == 'q':
            print('Exiting')
            exit()
        elif choice == 'd':
            self.dev_app.run()
        elif choice == 'l':
            self.list_app.run()
        elif choice == 'n':
            self.nnnh_app.run()
        elif choice == 't':
            self.tasks_app.run()
        elif choice == 'c':
            self.chatgpt_app.configure()
        else:
            question = choice
            self.chatgpt_app.execute(question)


    def run(self):
        print("Start Main")
        while(True):
            choice = self.get_user_choice(self.MAIN_MENU)
            self.execute_choice(choice)
            os.system('cls' if os.name == 'nt' else clear)


if __name__ == "__main__":
    menu_handler = CLIMenuHandler()
    menu_handler.run()
    