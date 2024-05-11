# create linear regression function

def getY(m, b, x):
    y = m*x + b
    return y

# testing

print(getY(1, 0, 7))
print(getY(5, 10, 3))

# calculate distance between the line and point

def calculate_error(m, b, point):
    xPoint = point[0]
    yPoint = point[1]
    yValue = getY(m, b, xPoint)
    diffY = yValue - yPoint
    return abs(diffY)

# testing. the line is: y = x
print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))

# testing. the line is: y = x - 1
print(calculate_error(1, -1, (3, 3)))

# testing. the line is: y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

# calculate total deviation
def calculate_all_error(m, b, dataPoints):
    totalError = 0
    for point in dataPoints:
        totalError += calculate_error(m, b, point)
    return totalError

# testing 
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
# the line is y = x
print(calculate_all_error(1, 0, datapoints))
# the line is y = x + 1
print(calculate_all_error(1, 1, datapoints))
# the line is y = x - 1
print(calculate_all_error(1, -1, datapoints))
# the line is y = -x + 1
print(calculate_all_error(-1, 1, datapoints))

possibleMS = [m/10 for m in range(-100, 101)]
print(possibleMS)