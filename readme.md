# eBoy Spherebuilder

Render an isometric sphere with slices. Camera angle and rotation can be set.

![Spherebuilder](media/sphere@12@30@0.png)
*12 slices, camera pitch 30°*

![Spherebuilder](media/sphere@24s@15@0.png)
*24 slices, camera pitch 15°*

![Spherebuilder](media/sphere@6s@15@45.png)
*6 slices, camera pitch 15°, camera roll 45°*

![Spherebuilder](media/sphere@1s@30@63.435.png)
*1 slice, camera pitch 30°, camera roll 63.435°*

![Iso View Geometry](media/ISO-view-geometry.png)
*Projections of z and y axes to isometric camera view*

```java
// Calculating the sides of a triangle
angleA = 90;
angleB = cameraPitch; // 'pitch' same as 'tilt'
angleC = angleA - angleB;
sideA = 1; // normalized hypotenuse
sideB = sideA * sin(radians(angleC));
sideC = sideA * sin(radians(angleB));
```
