class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user's email address has been changed")
        return self.email

    def __repr__(self):
        return("User: " + self.name + " Email: " + self.email)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_sum = 0
        for value in self.books.values():
            rating_sum += value
        return rating_sum/len(self.books.values())

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        print("This book's isbn has been changed")
        self.isbn = new_isbn

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        rating_sum = 0
        for rating in self.ratings:
            rating_sum += rating
        return rating_sum/len(self.ratings)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title + " ISBN: " + str(self.isbn)

class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater(object):

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] +=1
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("A user with this email already exists!")
        username = name.replace(" ", "")
        username = User(name, email)
        self.users[email] = username
        try:
            for book in user_books:
          	     TomeRater.add_book_to_user(book, email, rating=None)
        except TypeError:
            pass

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        times_book_read = float("-inf")
        for book in self.books.keys():
            if self.books[book] > times_book_read:
                times_book_read = self.books[book]
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        highest_average_rating = float("-inf")
        for book in self.books.keys():
            if book.get_average_rating() > highest_average_rating:
                highest_average_rating = book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        highest_average_rating = float("-inf")
        for user in self.users.values():
            if user.get_average_rating() > highest_average_rating:
                highest_average_rating = user.get_average_rating()
                most_positive_user = user
        return most_positive_user
