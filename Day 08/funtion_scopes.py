def test_scopes():

    var = 2 #Function Scope Variable/ Local Variable
    global x
    x = 2

    print(f"Do i know this variable? {x}")

x = 1 #Global Scope

test_scopes()


print(x)