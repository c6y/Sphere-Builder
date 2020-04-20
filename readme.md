# eBoy Spherebuilder

Render an isometric sphere with slices. Camera angle and rotation can be set.

![Spherebuilder ](spherebuilder-window.png)
*Rendered sphere at 30 degrees*

![Iso View Geometry](ISO-view-geometry.png)
*Projections of z and y axes to isometric camera view*

```java
// Calculating the sides of a triangle
angleA = 90;
angleB = cameraAngle; // any angle between 0 and 90
angleC = angleA - angleB;
sideA = 1; // hypotenuse is normalized
sideB = sideA * sin(radians(angleC));
sideC = sideA * sin(radians(angleB));
```
