#Namespace

def outer():
    outer_num = 100
    print(id(outer_num))

    #global keyword allows us to modify the global variable from within a function
    #global keyword is bad practice
    global global_number
    global_number = 101
    print("Global number: ", global_number)

    def inner():
        inner_num = 200
        print("Inner number: ", inner_num)

        #this outer num is different from the outer_num in the outer function
        #it has a different id, it's a new object in memory
        outer_num = 500
        print(id(outer_num))
        print("Outer number: ", outer_num)
    inner()

global_number = 300
print("Global number before calling outer function: ", global_number)


outer()


