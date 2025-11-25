# Railway Reservation System (Command Line Interface)


## Project Overview

A comprehensive Python-based railway reservation system that simulates real-world ticket booking operations. This command-line application provides a complete solution for managing train ticket reservations, cancellations, and passenger information with persistent data storage.

The system mimics actual railway booking processes with unique PNR generation, seat allocation, fare calculation, and receipt generation, making it an ideal educational project that demonstrates real-world application development concepts.


## Key Features

### Core Functionality
Ticket Booking: Complete reservation system with passenger details

Ticket Cancellation: Secure cancellation with seat recycling

Receipt Generation: Professional-looking ticket receipts

Real-time Availability: Dynamic seat management

### Smart Systems
Automatic PNR Generation: Unique booking references

Seat Allocation: Intelligent seat assignment and reuse

Fare Calculation: Distance-based pricing with coach differentiation

Data Persistence: Automatic saving to CSV files

### Management Tools
View All Bookings: Complete booking overview

Cancellation History: Track cancelled tickets

Receipt Retrieval: Access tickets anytime using PNR

Input Validation: Error handling and data integrity


## Technologies Used

Language: Python

Core Modules: csv and random

Custom Modules: faremodule.py (for the fare calculation logic)



## How to Install & Run

Prerequisites: Make sure you have Python 3 installed on your computer.

Save the Files: Place the main application file Railway_reservation_system.py and the faremodule.py in the same directory.

Start the Program: Open your terminal and run the main file from the directory:

python Railway_reservation_system.py



## Testing Instructions

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


Goal: Check Option 5 (Booked Tickets) and Option 4 (Cancelled Tickets) to confirm all previous data was correctly loaded from the CSV files.
<img width="744" height="315" alt="image" src="https://github.com/user-attachments/assets/11788185-774f-48d1-b257-edfe552ad723" />

Relaunch the program.

# Expected Outcomes

## After Successful Testing
Tickets booked with unique PNRs

Seats properly allocated and recycled

Receipts generated with correct fare calculation

Data persisted between sessions

Cancellations properly handled

Error messages for invalid inputs

## Files Created

tickets.csv - Active bookings database

cancelled.csv - Cancellation records


# Getting Started Ready?
## Quick Start:

Download both Python files

Open terminal in the folder

Run python main.py

Start booking tickets!

## Perfect for:

Learning Python file handling

Understanding reservation systems

Practicing CLI application development

Demonstrating real-world programming concepts




