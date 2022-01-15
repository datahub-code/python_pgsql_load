# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from dbconfig import DB_DETAILS

def main():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


