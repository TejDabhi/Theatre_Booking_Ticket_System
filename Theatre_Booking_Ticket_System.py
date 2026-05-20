class InvalidPhoneNumberError(Exception):
    pass


class InvalidMovieIdError(Exception):
    pass


class InvalidMovieDurationError(Exception):
    pass


class InvalidLanguageTypeError(Exception):
    pass


class Theatre_Ticket_Booking_System:

    def __init__(self):
        self.movies = {}
        self.bookings = []

    # ---------------- ADMIN FUNCTIONS ---------------- #

    def add_movie(self):
        try:
            movie_id = input("Enter Movie ID (integer): ")

            if not movie_id.isdigit():
                raise InvalidMovieIdError("Movie ID must be integer.")

            movie_id = int(movie_id)

            movie_name = input("Enter Movie Name: ")

            # Movie Timings
            movie_timings = []

            while True:
                timing = input("Enter movie timing or type 'done': ")

                if timing.lower() == 'done':
                    break

                movie_timings.append(timing)

            # Language
            movie_language = input("Enter movie language (Hindi/English): ")

            if movie_language.isdigit():
                raise InvalidLanguageTypeError("Language must be string.")

            # Duration
            movie_duration = input("Enter movie duration (HH:MM): ")

            try:
                hours, minutes = map(int, movie_duration.split(":"))

                if hours < 0 or minutes < 0 or minutes > 59 or hours > 3:
                    raise InvalidMovieDurationError(
                        "Duration cannot exceed 3 hours."
                    )

            except ValueError:
                raise InvalidMovieDurationError(
                    "Invalid duration format."
                )

            # Price
            price = float(input("Enter ticket price: "))

            # Capacity
            capacity = int(input("Enter total seat capacity: "))

            self.movies[movie_id] = {
                'name': movie_name,
                'price': price,
                'timings': movie_timings,
                'language': movie_language,
                'duration': movie_duration,
                'capacity': capacity,
                'booked_seats': 0
            }

            print(f"\nMovie '{movie_name}' added successfully.")

        except Exception as e:
            print(e)

    def remove_movie(self):

        if not self.movies:
            print("No movies available.")
            return

        self.view_movies()

        try:
            movie_id = int(input("Enter Movie ID to remove: "))

            if movie_id in self.movies:
                del self.movies[movie_id]
                print("Movie removed successfully.")
            else:
                print("Movie not found.")

        except ValueError:
            print("Invalid Movie ID.")

    def view_all_bookings(self):

        if not self.bookings:
            print("No bookings available.")
            return

        print("\nAll Bookings:\n")

        for booking in self.bookings:
            print(booking)

    # ---------------- USER FUNCTIONS ---------------- #

    def view_movies(self):

        if not self.movies:
            print("No movies available.")
            return

        print("\nAvailable Movies:\n")

        for movie_id, details in self.movies.items():

            timings = ", ".join(details['timings'])

            available_seats = (
                details['capacity'] - details['booked_seats']
            )

            print(f"""
Movie ID       : {movie_id}
Movie Name     : {details['name']}
Language       : {details['language']}
Duration       : {details['duration']}
Price          : {details['price']}
Timings        : {timings}
Available Seats: {available_seats}
""")

    def book_ticket(self):

        self.view_movies()

        if not self.movies:
            return

        try:
            movie_id = input("Enter Movie ID to book: ")

            if not movie_id.isdigit():
                raise InvalidMovieIdError("Movie ID must be integer.")

            movie_id = int(movie_id)

            if movie_id not in self.movies:
                print("Invalid Movie ID.")
                return

            name = input("Enter your name: ")

            phone = input("Enter phone number (10 digits): ")

            if len(phone) != 10 or not phone.isdigit():
                raise InvalidPhoneNumberError(
                    "Phone number must be exactly 10 digits."
                )

            # Show Timings
            print("\nAvailable Timings:")

            for index, timing in enumerate(
                    self.movies[movie_id]['timings']):
                print(f"{index + 1}. {timing}")

            timing_choice = int(input("Select timing: "))

            if timing_choice < 1 or timing_choice > len(
                    self.movies[movie_id]['timings']):
                print("Invalid timing choice.")
                return

            selected_timing = self.movies[movie_id]['timings'][
                timing_choice - 1
            ]

            # Persons
            person = int(input("Enter number of persons: "))

            if person <= 0:
                print("Invalid number of persons.")
                return

            # Check Seat Capacity
            available_seats = (
                self.movies[movie_id]['capacity']
                - self.movies[movie_id]['booked_seats']
            )

            if person > available_seats:
                print(f"Only {available_seats} seats available.")
                return

            # Payment Methods
            print("\nPayment Methods")
            print("1. Cash")
            print("2. Credit Card (5% Discount)")
            print("3. Online Payment (5% GST)")

            payment_choice = input("Choose payment method: ")

            ticket_price = self.movies[movie_id]['price']

            total_price = ticket_price * person

            if payment_choice == "1":
                payment_method = "Cash"

            elif payment_choice == "2":
                payment_method = "Credit Card"
                total_price *= 0.95

            elif payment_choice == "3":
                payment_method = "Online Payment"
                total_price *= 1.05

            else:
                print("Invalid payment choice.")
                return

            # Update booked seats
            self.movies[movie_id]['booked_seats'] += person

            # Save Booking
            booking = {
                'name': name,
                'phone': phone,
                'movie': self.movies[movie_id]['name'],
                'timing': selected_timing,
                'persons': person,
                'payment_method': payment_method,
                'total_price': round(total_price, 2)
            }

            self.bookings.append(booking)

            print("\nBooking Successful!")
            print(f"Movie          : {booking['movie']}")
            print(f"Timing         : {selected_timing}")
            print(f"Persons        : {person}")
            print(f"Payment Method : {payment_method}")
            print(f"Total Price    : {round(total_price, 2)}")

        except Exception as e:
            print(e)

    def view_user_bookings(self):

        phone = input("Enter phone number: ")

        if len(phone) != 10 or not phone.isdigit():
            print("Invalid phone number.")
            return

        user_bookings = [
            booking for booking in self.bookings
            if booking['phone'] == phone
        ]

        if not user_bookings:
            print("No bookings found.")
            return

        print("\nYour Bookings:\n")

        for booking in user_bookings:
            print(booking)

    # ---------------- MENUS ---------------- #

    def admin_menu(self):

        while True:

            print("\n------ ADMIN MENU ------")
            print("1. Add Movie")
            print("2. Remove Movie")
            print("3. View All Bookings")
            print("4. Exit")

            try:
                choice = int(input("Enter choice: "))

                if choice == 1:
                    self.add_movie()

                elif choice == 2:
                    self.remove_movie()

                elif choice == 3:
                    self.view_all_bookings()

                elif choice == 4:
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Please enter valid number.")

    def user_menu(self):

        while True:

            print("\n------ USER MENU ------")
            print("1. View Movies")
            print("2. Book Ticket")
            print("3. View Your Bookings")
            print("4. Exit")

            try:
                choice = int(input("Enter choice: "))

                if choice == 1:
                    self.view_movies()

                elif choice == 2:
                    self.book_ticket()

                elif choice == 3:
                    self.view_user_bookings()

                elif choice == 4:
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Please enter valid number.")

    # ---------------- RUN SYSTEM ---------------- #

    def run(self):

        print("=" * 50)
        print("WELCOME TO MOVIE TICKET BOOKING SYSTEM".center(50))
        print("=" * 50)

        while True:

            role = input(
                "\nEnter role (admin/user/exit): "
            ).lower()

            if role == 'admin':
                self.admin_menu()

            elif role == 'user':
                self.user_menu()

            elif role == 'exit':
                print("Exiting System...")
                break

            else:
                print("Invalid input.")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":

    booking_system = Theatre_Ticket_Booking_System()
    booking_system.run()
