# create linear regression function

def getY(m, b, x):
    y = m*x + b
    return y

# testing

print(getY(1, 0, 7))
print(getY(5, 10, 3))