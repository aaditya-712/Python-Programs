command = ""

while True:
    command = input("> ").lower()
    if command == "start":
        print("Car is started...")
    elif command == "stop":
        print("Car is stopped...")
    elif command == "help":
        print("""
            Commands to play game
            start - to start car
            stop - to stop car
            quit - to quit game        
        """)
    elif command == "quit":
        break
    else:
        print("keyword doesn't match, type 'help' for help.")