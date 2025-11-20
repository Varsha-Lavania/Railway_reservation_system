Problem Statement

The core problem this project addresses is: How can we efficiently, automatically, and persistently track and manage the booking, seat 
assignment, and cancellation of train tickets for a single train line?
Currently, managing reservations for even a single train can be a manual nightmare. Relying on paper or simple spreadsheets leads to numerous 
issues:

Inaccuracy and Errors: Mistakes are easily made when assigning unique PNRs or tracking available seats.

Data Loss Risk: Data is not securely persisted, risking the loss of booking information if the system fails or shuts down unexpectedly.

Inefficiency: The process of calculating fares, finding the next available seat, and cross-referencing cancelled tickets is slow.


This system provides a simple, command-line digital solution that automates these complex tasks, ensuring accuracy and data integrity.




Scope of the Project

This project focuses specifically on simulating the core reservation lifecycle for a single, generic train line in a sequential, single-user environment.

What is In Scope (What the system does):

Booking Records: Capturing essential passenger and journey details.

Data Persistence: Using industry-standard CSV files (tickets.csv, cancelled.csv) to save and load all data upon program startup and exit.

Seat Allocation Logic: Implementing a "smart" system that assigns seats sequentially but prioritizes the reuse of seat numbers freed by 
cancellations, maximizing efficiency.

Unique Identification: Generating unique PNR strings and receipt numbers for every transaction to ensure records are non-conflicting.

Basic Financials: Calculating fares using a separate module (faremodule.py) based on two variables: distance traveled and the coach type (AC or 
Sleeper).

System Reports: Providing options to easily view lists of currently booked tickets and a history of cancelled PNRs.


What is Out of Scope (What the system does not do):

Network Features: The system is a single-user CLI tool; it does not handle concurrent access, networking, or multi-user authentication.

Real-time External Data: It does not connect to external databases, live train schedules, or official railway systems.

Advanced Features: Complex features like waiting list management, payment processing, or dynamic route changes are beyond the scope of this 
prototype.

Graphical Interface: The entire interaction is handled via text input and output in the terminal.




Target Users

This system is designed to provide value to a few key audiences:

Railway Clerks / Counter Staff:

Benefit: Provides a fast, clear, and error-reducing tool for the daily tasks of booking and cancelling tickets. It minimizes the manual effort 
involved in managing seat assignments and PNRs.

Casual Testers and Demonstrators:

Benefit: Offers a contained environment to easily test basic system logic, such as ensuring that the seat recycling feature works flawlessly 
after multiple booking and cancellation cycles.




High-Level Features

Book It Quickly: Simple menu option to create a new ticket record with automatic seat assignment and fare calculation.

Cancel and Recycle: Provides immediate cancellation of a ticket via PNR, intelligently reusing the freed seat for the next booking.

View Official Receipt: Generates a clean, structured receipt showing all ticket details, fare, PNR, and receipt number.

Stay Organized: Maintains separate, persistent records for active bookings and historical cancelled PNRs.

Fair Fare Calculation: Calculates ticket costs based on distance and coach type, ensuring consistent pricing.