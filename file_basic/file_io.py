"""
    file_io.py

    Sample ways to open files from Real Python Tutorial.

    line endings (I used Linux:
        Windows: \r\n
        Linux: \n
        Mac: \n
"""
import os

def basic_open_close():
    """ Basic open and close file. """
    file = open("test.txt")
    print("file is open!")
    file.close()
    print("file is closed")

def open_close_try():
    """
    Open and close file using try.
    Ensuring the file closes even with an error
    """
    file = open("test.txt")
    try:
        # do something with the file
        print("file is open!")
    finally:
        file.close()
        print("file is closed")

def open_close_with():
    """
    Open and close file using with.
    Ensures the file closes even with an error
    """
    with open("test.txt", "r") as file:
        # if no mode is given, so the default is read
        # it is better to provide the "r" and be more explicit
        print("file is open!")
    # file is automatically closed
    print("file is closed")

def read_file():
    """ Read a file. """
    with open("test.txt") as file:
        content = file.read(10)
        print(content)

def read_file_one_line():
    """ Read a file one line at a time. """
    with open("test.txt") as file:
        content = file.readline()
        print(content)

def read_file_two_lines():
    """ Read a file one line at a time. """
    with open("test.txt") as file:
        content = file.readline()
        print(content)
        content = file.readline()
        print(content)

def read_file_all_lines():
    """ Read a file all lines at a time. """
    with open("test.txt") as file:
        content = file.readlines()
        print(content)

def write_file():
    """ Write to a file. """
    with open("test_write.txt", "w") as file:
        print("file is open!")
        # this will delete file contents

def write_one_string_file():
    """ Write a string to a file. """
    with open("test_write.txt", "w") as file:
        content = "This is a test string.\n" # \n is a line ending for Linux\Mac
        file.write(content)
    # all data is written to the file at this point

def write_two_strings_file():
    """ Write a string to a file. """
    with open("test_write.txt", "w") as file:
        content = "This is a text string.\n" # \n is a line ending for Linux\Mac
        file.write(content)
        additional = "This is an another text string.\n"  # \n is a line ending for Linux\Mac
        file.write(additional)
    # all data is written to the file at this point

def write_lines_file():
    """ Write lines to a file. """
    with open("test_write.txt", "w") as file:
        content = ["This is a text string.\n", "This is an another text string.\n"]
        # content is a list of strings
        file.writelines(content)
    # all data is written to the file at this point

def write_multiple_lines_file():
    """ Write lines to a file. """
    with open("test_write.txt", "w") as file:
        content = ["This is a text string.\n", "This is an another text string.\n"]
        # content is a list of strings
        file.writelines(content)
        additional = ["This is a third text string.\n", "This is a fourth text string.\n"]
        file.writelines(additional)
    # all data is written to the file at this point

def copy_content_from_file_to_file():
    """ Copy content from one file to another. """
    with open("test_in.txt") as file_in, open("test_out.txt", "w") as file_out:
        content = file_in.readlines()
        for line in content:
            file_out.write(line.upper())

def append_string_file():
    """ Append to a file. """
    with open("test.txt", "a") as file:
        content = "A new ending for my text file.\n" # \n is a line ending for Linux\Mac
        file.write(content)

def join_folder_path():
    """ Get the folder path. """
    return os.path.split(os.path.realpath(__file__))

def menu() -> str:
    """ Menu of file operations. """
    return """
    1) Basic Open and Close
    2) Open and Close using Try
    3) Open and Close using With
    4) Read File Menu
    5) Write File Menu
    6) Append to File
    7) Get Folder Path
    0) Exit
    """

def menu_read_text() -> str:
    """ Menu of file operations. """
    return """
    1) Read File
    2) Read File One Line
    3) Read File Two Lines
    4) Read File All Lines
    0) Previous Menu
    """

def menu_write_text() -> str:
    """ Menu of file operations. """
    return """
    1) Write File
    2) Write One String to File
    3) Write Two Strings to File
    4) Write Lines to File
    5) Write Multiple Lines to File
    6) Copy Content from File to File
    0) Previous Menu
    """

def main_menu():
    """ Main menu function. """
    while True:
        print(menu())
        choice = input("Enter your choice: ")
        if choice == "1":
            basic_open_close()
        elif choice == "2":
            open_close_try()
        elif choice == "3":
            open_close_with()
        elif choice == "4":
            read_menu()
        elif choice == "5":
            write_menu()
        elif choice == "6":
            append_string_file()
        elif choice == "7":
            print(join_folder_path())
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


def read_menu():
    """ Main function. """
    while True:
        print(menu_read_text())
        choice = input("Enter your choice: ")
        if choice == "1":
            read_file()
        elif choice == "2":
            read_file_one_line()
        elif choice == "3":
            read_file_two_lines()
        elif choice == "4":
            read_file_all_lines()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def write_menu():
    """ Main function. """
    while True:
        print(menu_write_text())
        choice = input("Enter your choice: ")
        if choice == "1":
            write_file()
        elif choice == "2":
            write_one_string_file()
        elif choice == "3":
            write_two_strings_file()
        elif choice == "4":
            write_lines_file()
        elif choice == "5":
            write_multiple_lines_file()
        elif choice == "6":
            copy_content_from_file_to_file()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":

    main_menu()
