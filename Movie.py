print("Welcome to PVR!")

seats = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"]
    ]
booked = []
while True:
    print("1 Book ticket")
    print("2 Cancel ticket")
    print("3 Show available seats")
    print("4 Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        ticket = input("Enter seat: ")
        if ticket not in booked:
            booked.append(ticket)
            print("Ticket booked")
        else:
            print("Seat already booked")
        
    elif choice == 2:
        ticket= input("Enter the seat to cancel: ")
        if t in booked:
            booked.remove(ticket)
            print("Ticket cancelled")
        else:
            print("Seat is not booked")

    elif choice == 3:
        for row in seats:
            for seat in row:
                if seat in booked:
                    print("X", end = " ")
                else:
                    print(seat, end = " ")
    elif choice == 4:
        print("Thanks for visiting!")
        break
    else:
        print("Invalid choice")
