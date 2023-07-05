command = ""
started=False
while True:
    command=input('> ').lower()
    if command == 'start':
        if started:
            print('car already started')
        else:
            started=True
            print("car started..")
    elif command == 'stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print("car stopped..")
    elif command == 'help':
        print(    '''
Start- to start the car 
Stop- to stop the car 
Quit - to quit ''')
    elif command== 'quit':
        break
    else:
        print("can't understand what you are telling")


