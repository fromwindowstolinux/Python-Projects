import func
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("Today is", now)

while True :
    user_input = input("Type: add / list / edit / done / exit \n> ")
    user_input = user_input.strip()
        
    if user_input.startswith("add"):

        add_book = user_input[4:] #input("Add book title: ") + "\n"
       
        books = func.read_input()
       
        books.append(add_book + "\n")

        func.write_input(books)
    
    elif user_input.startswith("list"):

        books = func.read_input()
        book_list = [book.strip("\n") for book in books]

        for index, book in enumerate(book_list):
            row = f"{index + 1} - {book}"
            print(row)
    
    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:]) #int(input("Input book number: "))
            print(number)
            number = number - 1
            
            books = func.read_input()
            new_title = input("Add book title: ")
            books[number] = new_title + "\n"

            func.write_input(books)

        except ValueError:
            print("Invalid command")
            continue

    elif user_input.startswith("done"):
        try:
            number = int(user_input[5:]) #int(input("Input completed book number: "))
            
            books = func.read_input()
            index = number-1
            book_done = books[index]
            books.pop(index)

            func.write_input(books)

            message = f"Finished reading {book_done}"
            print(message)

        except IndexError:
            print("Invalid number")
            continue

    elif user_input.startswith("exit"):
        break

    else:
        print("Incorrect command!")