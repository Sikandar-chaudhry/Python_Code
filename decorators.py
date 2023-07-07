def announce(f):
    def wrapper():
        print("\nFunction is about to run...")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, World")
    
hello()