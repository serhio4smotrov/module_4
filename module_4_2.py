def test_function():
    def inner_function():
        print('Я в области видимости test_function')
    inner_function()
test_function()
#inner_function() эту функцию нельзя вызвать вне функции, в которой она описана, то есть вне test_function