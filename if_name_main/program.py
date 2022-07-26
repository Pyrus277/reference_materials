import test

from test import user
# ^This line is still gonna run thru all the lines of test.py

# If you run a file directly, then 
#       __name__ == __main__
# If that same file is called by another program by way
# of an import statement, however, then 
#       __name__ == the name of the file (minus extension)
print(f'Game File: {__name__}')

def run():
    print('Game Starts')

# Using this line, we can test if a file is being run directly, or 
# being imported.

if __name__ == '__main__':
    run()

# It can act like a little gatekeeper, keeping the code within only
# accessible if you run the file directly. Other files importing this
# file will not have access to that segment of code. 