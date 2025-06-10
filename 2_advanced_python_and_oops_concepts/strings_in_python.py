def fun():
    print(chr(65))
    print(ord('a'))

    multi_line_string = """
    This
    is an example 
    of multiline string"""

    print(multi_line_string)

    #raw strings
    # we can use \characters to skip or avoid quotes and for special things liek \n or \t
    # if not wanted use raw string or like \\n, or \\t
    
    r1 = "c:\project\name.py"

    #this is a raw string
    r2 = r"c:\project\name.py"

    print("normal string: " + r1)
    print("raw string: " + r2)

if __name__ == '__main__':
    fun()