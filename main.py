import random

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class BookRecommendationSystem:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def recommend_book(self, genre):
        recommended_books = []
        for book in self.books:
            if book.genre.lower() == genre.lower():
                recommended_books.append(book)
        if recommended_books:
            recommended_book = random.choice(recommended_books)
            print("Recommended Book:")
            print(f"Title: {recommended_book.title}")
            print(f"Author: {recommended_book.author}")
            print(f"Genre: {recommended_book.genre}")
        else:
            print("No books found in the specified genre.")

def main():
    recommendation_system = BookRecommendationSystem()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    book3 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
    book4 = Book("Pride and Prejudice", "Jane Austen", "Romance")

    recommendation_system.add_book(book1)
    recommendation_system.add_book(book2)
    recommendation_system.add_book(book3)
    recommendation_system.add_book(book4)

    genre = input("Enter a genre to get a book recommendation: ")
    recommendation_system.recommend_book(genre)

if __name__ == "__main__":
    main()
