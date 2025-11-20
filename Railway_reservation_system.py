import csv
import random
import faremodule

# Global variables
tickets = []
cancelled_pnrs = []
freed_seats = []
next_seat_number = 1

TICKETS_FILE = "tickets.csv"
CANCELLED_FILE = "cancelled.csv"

# File operations
def load_data():
    global tickets, cancelled_pnrs, next_seat_number
    
    # Load tickets
    try:
        with open(TICKETS_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)      # skip header
            tickets = []
            for row in reader:
                if row:                   
                    if len(row) > 9:
                        receipt_no = row[9]
                    else:                        
                        receipt_no = random.randint(100000, 999999)
                    
                    ticket = {"pnr": row[0],
                        "name": row[1],
                        "age": int(row[2]),
                        "train_name": row[3],
                        "train_no": row[4],
                        "coach": row[5],
                        "seat": row[6],
                        "distance": int(row[7]),
                        "fare": float(row[8]),
                        "receipt_no": receipt_no}
                    tickets.append(ticket)
    except:
        tickets = []
    
    # Load cancelled PNRs
    try:
        with open(CANCELLED_FILE, 'r') as file:
            reader = csv.reader(file)
            cancelled_pnrs = []
            for row in reader:
                if row:
                    cancelled_pnrs.append(row[0])
    except:
        cancelled_pnrs = []

def save_data():
    # Save tickets
    try:
        with open(TICKETS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["pnr", "name", "age", "train_name", "train_no", "coach", "seat", "distance", "fare", "receipt_no"])
            for ticket in tickets:
                writer.writerow([ticket["pnr"],
                    ticket["name"],
                    ticket["age"],
                    ticket["train_name"],
                    ticket["train_no"],
                    ticket["coach"],
                    ticket["seat"],
                    ticket["distance"],
                    ticket["fare"],
                    ticket["receipt_no"]])
    except:
        print("Error saving tickets")
    
    # Save cancelled PNRs
    try:
        with open(CANCELLED_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for pnr in cancelled_pnrs:
                writer.writerow([pnr])
    except:
        print("Error saving cancelled tickets")

# Utility functions
def get_seat():
    global next_seat_number
    if freed_seats:
        num = freed_seats.pop()
    else:
        num = next_seat_number
        next_seat_number = next_seat_number + 1
    return "S" + str(num)

def make_pnr(name, train_no):
    name_part = name[:2].upper()
    train_part = train_no[-3:]
    base = name_part + train_part
    pnr = base
    count = 1
    
    all_pnrs = []
    for t in tickets:
        all_pnrs.append(t["pnr"])
    for c in cancelled_pnrs:
        all_pnrs.append(c)
    
    while pnr in all_pnrs:
        pnr = base + str(count)
        count = count + 1
    return pnr

def generate_receipt(ticket):
    # Create a list of all the receipt lines
    lines = []
    lines.append("\n" + "=" * 40)
    lines.append("    TICKET RECEIPT")
    lines.append("=" * 40)
    lines.append("Receipt: " + str(ticket['receipt_no']))
    lines.append("PNR: " + ticket['pnr'])
    lines.append("Name: " + ticket['name'])
    lines.append("Age: " + str(ticket['age']))
    lines.append("-" * 40)
    lines.append("Train: " + ticket['train_name'])
    lines.append("Train No: " + ticket['train_no'])
    lines.append("Coach: " + ticket['coach'])
    lines.append("Seat: " + ticket['seat'])
    lines.append("Distance: " + str(ticket['distance']) + " km")
    lines.append("-" * 40)
    lines.append("Fare: Rs. " + str(ticket['fare']))
    lines.append("=" * 40)
    lines.append("  Thank you!")
    lines.append("=" * 40)
    
    # Join all lines with newline characters
    return "\n".join(lines)

# Core functionality
def book_ticket():
    print("\n=== BOOK TICKET ===")
    
    name = input("Passenger Name: ")
    if not name:
        print("Please enter name")
        return
    
    try:
        age = int(input("Age: "))
    except:
        print("Please enter valid age")
        return
    
    train_name = input("Train Name: ")
    train_no = input("Train Number: ")
    coach = input("Coach (AC/Sleeper): ").upper()
    if coach == "AC":
        coach_type = "AC"
    else:
        coach_type = "Sleeper"
    
    try:
        distance = int(input("Distance (km): "))
    except:
        print("Please enter valid distance")
        return
    
    seat = get_seat()
    pnr = make_pnr(name, train_no)
    fare = faremodule.cal_fare(distance, coach_type)
    receipt_no = random.randint(100000, 999999)                # Generate receipt number once during booking
    
    ticket = {"pnr": pnr,
        "name": name,
        "age": age,
        "train_name": train_name,
        "train_no": train_no,
        "coach": coach_type,
        "seat": seat,
        "distance": distance,
        "fare": fare,
        "receipt_no": receipt_no}                # using dict.
    
    tickets.append(ticket)
    save_data()
    
    # Generate and display receipt
    receipt = generate_receipt(ticket)
    print(receipt)
    
    print("Ticket Booked Successfully!")
    print("PNR: " + pnr)
    print("Seat: " + seat)
    print("Fare: Rs." + str(fare))
    print("Receipt No: " + str(receipt_no))
    print()

def cancel_ticket():
    print("\n=== CANCEL TICKET ===")
    pnr = input("Enter PNR: ")
    
    for i in range(len(tickets)):
        if tickets[i]["pnr"] == pnr:
            seat_str = tickets[i]["seat"]
            if seat_str.startswith("S"):
                num_str = seat_str[1:]
                if num_str.isdigit():
                    freed_seats.append(int(num_str))
            
            tickets.pop(i)
            cancelled_pnrs.append(pnr)
            save_data()
            
            print("Ticket cancelled: " + pnr)
            print("Seat freed: " + seat_str)
            print()
            return
    
    print("PNR not found")
    print()

# Display functions
def show_receipt():
    print("\n=== VIEW TICKET RECEIPT ===")
    pnr = input("Enter PNR: ")
    
    # Search in current tickets
    for ticket in tickets:
        if ticket["pnr"] == pnr:
            receipt = generate_receipt(ticket)
            print(receipt)
            return
    
    print("PNR not found")
    print()

def show_cancelled():
    print("\n=== CANCELLED TICKETS ===")
    if not cancelled_pnrs:
        print("No cancelled tickets")
    else:
        for pnr in cancelled_pnrs:
            print("PNR: " + pnr)
    print()

def show_tickets():
    print("\n=== BOOKED TICKETS ===")
    if not tickets:
        print("No tickets booked")
    else:
        for ticket in tickets:
            print("PNR: " + ticket["pnr"] + " | Name: " + ticket["name"] + " | Train: " + ticket["train_name"] + " | Seat: " + ticket["seat"] + " | Fare: Rs." + str(ticket["fare"]) + " | Receipt: " + str(ticket["receipt_no"]))
    print()

# Main program
def main():
    load_data()
    
    while True:
        print("=== RAILWAY RESERVATION SYSTEM ===")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Ticket Receipt")
        print("4. Show Cancelled Tickets")
        print("5. Show All Tickets")
        print("6. Exit")
        print()
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            book_ticket()
        elif choice == "2":
            cancel_ticket()
        elif choice == "3":
            show_receipt()
        elif choice == "4":
            show_cancelled()
        elif choice == "5":
            show_tickets()
        elif choice == "6":
            print("Thank you for using Railway Reservation System!")
            break
        else:
            print("Invalid choice")
            print()

main()