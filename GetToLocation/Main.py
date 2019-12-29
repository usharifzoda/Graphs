import math

# Point class
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


# Main program
# Read in x and y for Point P
goal_point = Point()
print('Enter Point in X Axis: ')
goal_point.x = int(input())
print('Enter Point in Y Axis: ')
goal_point.y = int(input())

# Read in num of steps to be taken in X and Y directions
print('Enter Steps to take in X Direction: ')
x_dir = int(input())
print('Enter Steps to take in Y Direction: ')
y_dir = int(input())

# Read in num of steps to be taken (backwards) every 3 steps
print('Enter number of steps to take back after 3rd iteration: ')
num_back = int(input())
# Write dynamic programming algorithm

curr_point = Point()
curr_point.x = 0
curr_point.y = 0


previous_distance = 999
    #d = sqrt((x_p - x_1)^2 + (y_p - y_1)^2)
curr_distance = math.sqrt(math.pow(goal_point.x - curr_point.x,2) + math.pow(goal_point.y - curr_point.y,2))

i = 0
prev_point = Point()

while curr_distance < previous_distance:
    prev_point.x = curr_point.x
    prev_point.y = curr_point.y
    curr_point.x += x_dir
    curr_point.y += y_dir
    i += 1
    if i % 3 == 0:
        curr_point.x -= num_back
        curr_point.y -= num_back
    previous_distance = curr_distance
    curr_distance = math.sqrt(math.pow(goal_point.x - curr_point.x, 2) + math.pow(goal_point.y - curr_point.y, 2))
    print(curr_point.x, curr_point.y)
    print("\nCurrent Distance: ", curr_distance)
    print("Previous Distance: ", previous_distance)

# Output
print("\nClosest Point: ", prev_point.x, prev_point.y)

