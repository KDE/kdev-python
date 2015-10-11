
# Try redefining a built-in function with a different return type,
# it should be possible to import that but it should not replace the existing
# open() function
def open():
    return 3