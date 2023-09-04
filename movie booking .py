#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Movie:
    def __init__(self, title, showtimes, seats_per_showtime, information):
        self.title = title
        self.showtimes = showtimes
        self.seats_per_showtime = seats_per_showtime
        self.available_seats = {
            showtime: [i for i in range(1, seats_per_showtime + 1)]
            for showtime in showtimes
        }
        self.information = information

    def display_showtimes(self):
        print(f"Showtimes for {self.title}:")
        for showtime in self.showtimes:
            print(showtime)

    def display_information(self):
        print(f"Information for {self.title}:")
        print(self.information)

    def book_ticket(self, showtime, seat_number):
        if showtime in self.showtimes:
            if seat_number in self.available_seats[showtime]:
                self.available_seats[showtime].remove(seat_number)
                print(f"Ticket booked for {self.title}, Showtime: {showtime}, Seat: {seat_number}")
            else:
                print("Seat is already booked.")
        else:
            print("Invalid showtime.")


# In[2]:



def main():
    # Create recent Tamil movies with information
    movie1_info = "A thrilling action movie with a star-studded cast."
    movie1 = Movie("Master", ["10:00 AM", "1:00 PM", "4:00 PM"], 50, movie1_info)

    movie2_info = "A heartwarming family drama set in a village backdrop."
    movie2 = Movie("Kadaikutty Singam", ["11:00 AM", "2:00 PM", "5:00 PM"], 40, movie2_info)

    # Display available showtimes and information
    movie1.display_showtimes()
    movie1.display_information()

    movie2.display_showtimes()
    movie2.display_information()

    while True:
        print("\nSelect a movie (1 for Master, 2 for Kadaikutty Singam, 0 to exit):")
        choice = input()
        if choice == '0':
            break
        elif choice == '1':
            selected_movie = movie1
        elif choice == '2':
            selected_movie = movie2
        else:
            print("Invalid choice. Please try again.")
            continue

        selected_movie.display_showtimes()

        showtime = input("Select a showtime: ")
        if showtime not in selected_movie.showtimes:
            print("Invalid showtime. Please try again.")
            continue

        try:
            seat_number = int(input("Enter the seat number: "))
            selected_movie.book_ticket(showtime, seat_number)
        except ValueError:
            print("Invalid seat number. Please enter a valid seat number.")


# In[ ]:



if __name__ == "__main__":
    main()


# In[ ]:




