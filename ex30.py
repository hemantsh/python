# Exercise 30: Custom Context Manager (with statement)
# Practice Problem: Write a class that acts as a context manager for handling a database-style connection 
#     (Don’t do actual database connection, simply printing “Connected” and “Disconnected”). Use the with statement to ensure the connection is closed even if an error occurs.

# Exercise Purpose: Managing resources like files, network sockets, or database connections is risky. 
#     If you forget to close them, you get memory leaks. Context managers automate this using the __enter__ and __exit__ magic methods.

class DBContext :
    def __init__(self) :
        pass

    def __enter__(self) :
        print("Connecting to DB....")
        return self

    def __exit__(self, extype, exval, extb) :
        print("Closing Connection ...")
        print(f"{extype} {exval} {extb}")
        return False

try :
    with DBContext() as con :
        print("Process Using connection")
        raise Exception("Error message")
except Exception as e:
    print(e)
    
