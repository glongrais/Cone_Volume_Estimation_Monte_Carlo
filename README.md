# Cone Volume Estimation with Monte Carlo

The [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method) is based on the principle of repeated random sampling to determine numerical results. In this short example I used this method to determine the volume of a cone.

## Principle

The general idea of this simulation is to place the cone in a rectangular parallelepiped where the edges of the base of the rectangular parallelepiped are equal to ```` 2*(radius of the cone's base) ````. And the height of the parallelepiped is equal at the height of the cone.  

Then I generated a large enough amount of random points inside the parallelepiped and checked how many of them were inside the cone. 
I can then compute the ratio of points inside the cone compared to the total number of point:   
```` ratio = (points inside the cone)/(total number of points) ````.  

Finally the volume of the cone is found by multiplying this ratio with the volume of the parallelepiped:  
```` Volume cone = (Volume parallelepiped)*ratio````
