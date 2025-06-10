


def formatted_strings():
    """This function shows different ways to include formatted strings"""
    name = "Joby"
    Company = "Google"

    s1 = "Welcome %s to the headquarters of %s" %(name, Company) # oldest
    s2 = "Welcome {0} to the headquarters of {1}".format(name, Company) # middle
    s3 = f"Welcome {name} to the headquarters of {Company}" #new after 3.6

    print(s1)
    print(s2)
    print(s3)

    # we can include operation, functions or expressions call and all in f strings
    a = "ABC"
    l = f'Lower case of {a} is {a.lower()}'
    print(l)

if __name__ == "__main__":
    formatted_strings()