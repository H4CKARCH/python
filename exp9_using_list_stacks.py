class Stack:

    def __init__(self):
        self.stk = []
        self.top = -1

    def Push(self):
        val = int(input("Enter the value to push: "))

        self.stk.append(val)
        self.top = self.top + 1

        print(val, "Pushed into the stack")

    def Pop(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            val = self.stk.pop(self.top)
            self.top = self.top - 1
            print(val, "Popped from the stack")

    def Peek(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Topmost Element:", self.stk[self.top])

    def Display(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Elements in the Stack are:")

            new_lst = self.stk[::-1]

            for x in new_lst:
                print("|", x, "|")


StackObj = Stack()

while True:
    print("\n**** Operations On Stack ****")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        StackObj.Push()

    elif choice == 2:
        StackObj.Pop()

    elif choice == 3:
        StackObj.Peek()

    elif choice == 4:
        StackObj.Display()

    elif choice == 5:
        exit(0)

    else:
        print("Invalid Choice! Try Again")
