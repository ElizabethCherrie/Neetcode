""""Task 6 Car Fleet
There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers position and speed, both of length n.
position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.
A car can not pass another car ahead of it. It can only catch up to another car and then
drive at the same speed as the car ahead of it.
A car fleet is a non-empty set of cars driving at the same position and same speed.
A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the destination,
then the car is considered to be part of the fleet.
Return the number of different car fleets that will arrive at the destination."""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for car in range(len(position)):
            time = (target - position[car]) / speed[car]
            cars.append([position[car], time])
        cars.sort(reverse = True)
        for car_pos, car_t in cars:
            stack.append(car_t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)