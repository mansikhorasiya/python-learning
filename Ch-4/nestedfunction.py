def outer_function():
    x=1 #variable in the outer function

    def inner_function():
        y=2 #variable in the inner function
        result=x + y
        return result
    return inner_function()
output=outer_function()
print(output)