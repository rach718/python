menu_selection = None
menu_text = 'Welcome to the menu\nPlease select what youd like to do:\na. print hello\nb. say your name\nx.exit:'
while menu_selection != 'x':
    menu_selection = input(menu_text)
    if menu_selection == 'a':
        print('hello')
    elif menu_selection == 'b':
        user_name = input('Tell me your name')
        print(f'Hello {user_name}')

