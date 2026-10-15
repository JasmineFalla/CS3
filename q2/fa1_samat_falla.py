# Jasmine Kaylee M. Falla
# Formative Assessment No. 1


class Publication:
    # Initialize the shared title and author attributes.
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Return the publication's title and author.
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # Update the publication's title and author.
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # Display the publication's shared information.
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")




class Book(Publication):
    # Initialize inherited attributes and validate the page count.
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.__validation_message = None
        self.set_number_of_pages(number_pages)

    # Return the book's page count.
    def get_number_of_pages(self):
        return self.__number_of_pages

    # Validate the page count and record any initial error.
    def set_number_of_pages(self, number_pages):
        if (
            isinstance(number_pages, int)
            and not isinstance(number_pages, bool)
            and number_pages > 0
        ):
            self.__number_of_pages = number_pages
        else:
            self.__validation_message = (
                "Number of pages must be positive."
            )

    # Display any validation message before the book's information.
    def display_info(self):
        if self.__validation_message:
            print(self.__validation_message)
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")




class Magazine(Publication):
    # Initialize inherited attributes and validate the issue number.
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    # Return the magazine's issue number.
    def get_issue_number(self):
        return self.__issue_number

    # Accept only positive integers as valid issue numbers.
    def set_issue_number(self, issue_number):
        if (
            isinstance(issue_number, int)
            and not isinstance(issue_number, bool)
            and issue_number > 0
        ):
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")

    # Reuse the parent's display method and show the issue number.
    def display_info(self):
        super().display_info()
        print(f"Issue number : {self.__issue_number}")


# Create two Publication objects with different information.
publication1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)
publication2 = Publication(
    "World Discoveries",
    "James Rivera"
)

# Create two Book objects and demonstrate page-count validation.
book1 = Book("The Hobbit", "J.R.R. Tolkien", -5)
book1.set_number_of_pages(310)

book2 = Book("Noli Me Tangere", "Jose Rizal", 480)

# Create two Magazine objects with valid issue numbers.
magazine1 = Magazine(
    "National Geographic",
    "Various Authors",
    202
)
magazine2 = Magazine(
    "Science Today",
    "Alex Morgan",
    12
)


# Display the information of all six objects.
print("Publication Information:")
publication1.display_info()
print()
publication2.display_info()

print("\nBook Information:")
book1.display_info()
print()
book2.display_info()

print("\nMagazine Information:")
magazine1.display_info()
print()
magazine2.display_info()