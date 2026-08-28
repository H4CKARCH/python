class OverloadDemo:
    # sum method with default as None for parameters
    def sum(self, a=None, b=None, c=None):

        # When three parameters are passed
        if a is not None and b is not None and c is not None:
            s = a + b + c
            print("Sum = ", s)

        # When two parameters are passed
        elif a is not None and b is not None:
            s = a + b
            print("Sum = ", s)


# Create object
od = OverloadDemo()

# Calling sum with two parameters
od.sum(8, 9)

# Calling sum with three parameters
od.sum(8, 9, 10)
