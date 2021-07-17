
class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def listofbooks(self):
        print("The books available in the library are : ")

        for book in self.books:
            print(">", book)

    def Availabilityofbook(self, bookname):

        if bookname in self.books:
            print(f"\n-----The book {bookname} is available and you can borrow it.-----")
        else:
            print(
                f"\n-----The book {bookname} Not available please try after some time/days.-----")

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(
                f"\n-->The book {bookname} is issued to you, Keep it safe and return it in time period of 30 days,")
            self.books.remove(bookname)
        else:
            print(
                f"\n-->The book {bookname} Not available please try after some time/days.")

    def returnbook(self, bookname):
        self.books.append(bookname)
        print(
            f"\n-->Thank you for returning {bookname} on time hopw you enjoyed it...")

    def donatebook(self, bookname):
        print(
            f"\n-->Thank You soo much for donating {bookname} to central library it will helpfull for the students...")
        self.books.append(bookname)
        


class Student():

    def availabiltyofbookstd(self):
        self.book = input(
            "\nEnter the book do you want to check wheather its available or not : ")
        return self.book

    def requestbook(self):
        self.book = input(
            "\nEnter the book do you want to take it with you for read : ")
        return self.book

    def returnbookstd(self):
        self.book = input("\nEnter the book do you want return : ")
        return self.book

    def donatebookstd(self):
        self.book = input("\nEnter the book which you want to donate : ")
        return self.book


if __name__ == '__main__':
    centralibrary = library(["Python", "C programming", "CPP programming", "Java", "HTML", "CSS"])
    student = Student()
    while(True):
        welcomemsg =""" 
        === Welcome To Central Library Created by Shiv ===

        Press the following number for the specific opration :
        1.List of Books
        2.To Check availability of book
        3.For borrw a book
        4.To return a book
        5.To donate a book
        6.For exit...
        """
        print(welcomemsg)
        a = int(input("Enter your number for the specific opration : "))
        if a == 1:
            centralibrary.listofbooks()
        elif a == 2:
            centralibrary.Availabilityofbook(student.availabiltyofbookstd())
        elif a == 3:
            centralibrary.borrowbook(student.requestbook())
        elif a == 4:
            centralibrary.returnbook(student.returnbookstd())
        elif a == 5:
            centralibrary.donatebook(student.donatebookstd())
        elif a == 6:
            print("Thanks for using central library,Have a great day ahead!")
            exit()
        else:
            print("Invalid choice")
