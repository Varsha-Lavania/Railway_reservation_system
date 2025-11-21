Railway Reservation System (Command Line Interface)


Project Overview

This is a simple command-line application designed to simulate a basic railway reservation system. It allows users to easily book new tickets, cancel existing ones, and retrieve ticket information.

The system is designed for persistence, meaning all booked and cancelled PNRs are saved to and loaded from CSV files (tickets.csv and cancelled.csv), so your data is safe between sessions.



Key Features

Ticket Booking: Input passenger details (name, age, train, distance) to receive a ticket with a confirmed PNR, assigned seat, and calculated fare.

Unique PNR Generation: Automatically creates a unique Passenger Name Record (PNR) based on the passenger's name and the train number.

Smart Seat Management: Seats are assigned sequentially (like S1, S2). If a ticket is cancelled, that seat number is immediately saved and reused  
for the next new booking, ensuring no seats go wasted.

Ticket Cancellation: Allows cancellation by PNR, moving the ticket to the cancelled list and freeing up the assigned seat.

Detailed Receipt: Generates a formatted, easy-to-read receipt for any booked ticket.

Data Persistence: Saves and loads all active and cancelled ticket information using CSV files.

Fare Calculation: Calculates ticket fares based on travel distance and coach type (AC or Sleeper) using the external faremodule.

Display Options: View a list of all current booked tickets or a list of all cancelled PNRs.



Technologies Used

Language: Python

Core Modules: csv and random

Custom Modules: faremodule.py (for the fare calculation logic)



How to Install & Run

Prerequisites: Make sure you have Python 3 installed on your computer.

Save the Files: Place the main application file Railway_reservation_system.py and the faremodule.py in the same directory.

Start the Program: Open your terminal and run the main file from the directory:

python Railway_reservation_system.py



Testing Instructions

To ensure the system works correctly, follow these simple steps using the main menu options:

Book a Ticket: Select Option 1.
Enter sample data for a passenger.
Goal: Verify that a receipt is displayed, and you receive a unique PNR and a seat number.
<img width="426" height="673" alt="image" src="https://github.com/user-attachments/assets/077595a3-5c98-46fe-9caf-2280df02ffda" />


Verify Booking: Select Option 5 (Show All Tickets).
Goal: Confirm the ticket you just booked appears in the active list.
<img width="838" height="112" alt="image" src="https://github.com/user-attachments/assets/db582df3-50fc-4e7b-956e-f9beab270239" />


View Receipt: Select Option 3 (View Ticket Receipt).
Enter the PNR you received in the first step.
Goal: Verify the full ticket details are displayed correctly.
<img width="362" height="376" alt="image" src="https://github.com/user-attachments/assets/b1e05a1c-670d-4a2c-8a13-3287f7603f60" />


Cancel and Check Seat Recycling: Select Option 2 (Cancel Ticket).
Enter the PNR from the first ticket.
Goal: Verify the cancellation is confirmed, and the seat is reported as freed.
<img width="274" height="115" alt="image" src="https://github.com/user-attachments/assets/7dd5af49-281b-4255-83b0-61f7f5f5966e" />


Now, book a new ticket (Option 1). Verify that the new ticket reuses the previously freed seat number (S1) instead of assigning the next sequential one (S2).
<img width="339" height="510" alt="image" src="https://github.com/user-attachments/assets/59188ab9-0080-416b-bfc4-af170d6126e5" />


Check Persistence (Exit and Reload):
Exit the program using Option 6.

Relaunch the program.

Goal: Check Option 5 (Booked Tickets) and Option 4 (Cancelled Tickets) to confirm all previous data was correctly loaded from the CSV files.
<img width="744" height="315" alt="image" src="https://github.com/user-attachments/assets/11788185-774f-48d1-b257-edfe552ad723" />
