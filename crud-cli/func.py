FILEPATH = "inputs.txt"


# read text file and return list of books
def read_input(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        books_local = file_local.readlines()
    return books_local

# write book title in the text file
def write_input(books_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(books_arg)


if __name__ == "__main__":
    print(read_input())