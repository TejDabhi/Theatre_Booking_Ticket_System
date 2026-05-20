# 🎬 Theatre Ticket Booking System

## 📌 Project Description
The Theatre Ticket Booking System is a Python console-based application that allows users to book movie tickets online.  
The system provides separate functionalities for **Admin** and **Users**.

- Admin can add/remove movies and view all bookings.
- Users can view movies, book tickets, and view their bookings.
- The system includes exception handling and seat capacity management.

---

# ✨ Features

## 👨‍💼 Admin Features
- Add new movies
- Remove movies
- View all bookings
- Add movie timings
- Set movie seat capacity

## 👤 User Features
- View available movies
- Book movie tickets
- Select movie timing
- Choose payment method
- View personal bookings

---

# 🛠 Technologies Used
- Python
- Object-Oriented Programming (OOP)
- Exception Handling
- Lists & Dictionaries

---

# ⚠️ Custom Exceptions Used

| Exception Name | Purpose |
|---|---|
| InvalidPhoneNumberError | Raised when phone number is invalid |
| InvalidMovieIdError | Raised when movie ID is invalid |
| InvalidMovieDurationError | Raised for invalid duration |
| InvalidLanguageTypeError | Raised for invalid language input |

---

# 🎟 Payment Methods
- Cash
- Credit Card (5% Discount)
- Online Payment (5% GST)

---

# 🪑 Seat Capacity Feature
Each movie has:
- Total seat capacity
- Booked seats tracking
- Remaining seats calculation

Users cannot book tickets if seats are unavailable.

---

# 📂 Project Structure

```bash
Theatre Ticket Booking System
│
├── main.py
└── README.md
```

---

# ▶️ How To Run

## Step 1: Install Python
Download Python from:
https://www.python.org/

## Step 2: Run the Program

```bash
python main.py
```

---

# 🖥 Example Inputs

## Add Movie

```txt
Enter Movie ID: 101
Enter Movie Name: Pushpa 2
Enter movie timing: 10:00 AM
Enter movie timing: 2:00 PM
Enter movie timing: done
Enter movie language: Hindi
Enter movie duration: 02:45
Enter ticket price: 250
Enter total seat capacity: 120
```

---

# 📌 Example Booking

```txt
Enter Movie ID to book: 101
Enter your name: Tej
Enter phone number: 9876543210
Select timing: 1
Enter number of persons: 2
Choose payment method: 1
```

---

# 📸 Sample Output

```txt
Booking Successful!
Movie          : Pushpa 2
Timing         : 10:00 AM
Persons        : 2
Payment Method : Cash
Total Price    : 500
```

---

# 🔥 Future Improvements
- Database Integration
- GUI Interface
- Online Payment Gateway
- Login Authentication
- Seat Selection System

---

# 👨‍💻 Author
Tej Dabhi
```
