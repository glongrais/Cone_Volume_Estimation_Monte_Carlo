import math
import random

def pointsDistance(x1, x2, y1, y2):
    return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

def computeConeFormula(radius, height):
    return (1/3)*(math.pi*radius*radius*height)

def computeConeMonteCarlo(radius, height, points):
    total_points = 0
    points_in = 0
    for _ in range(points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        z = random.uniform(0, height)
        height_pourcent = 1.0-(z/height)
        dist = pointsDistance(0, x, 0, y)
        tmp_radius = radius*height_pourcent
        if dist <= tmp_radius:
            points_in += 1
        total_points += 1
    return (4*radius*radius*height)*(points_in/total_points)

def main():

    radius = 200
    height = 80
    points = 10000
    print(computeConeFormula(radius, height))
    print(computeConeMonteCarlo(radius, height, points))


if __name__ == "__main__":
    main()