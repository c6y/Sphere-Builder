# Sphere Builder

Render an isometric sphere with slices. The slice count, camera pitch (also called 'tilt'), and camera roll, can all be set. Made with DrawBot/Python.

### Examples:

![Spherebuilder](media/sphere_12s_30p_0r.svg)  
*12 slices, camera pitch 30°*
<!-- ![Spherebuilder](media/sphere@12@30@0.png)  
*12 slices, camera pitch 30°* -->

![Spherebuilder](media/sphere_24s_15p_0r.svg)  
*24 slices, camera pitch 15°*
<!-- ![Spherebuilder](media/sphere@24s@15@0.png)  
*24 slices, camera pitch 15°* -->

![Spherebuilder](media/sphere_6s_50p_15r.svg)  
*6 slices, camera pitch 50°, camera roll 15°*
<!-- ![Spherebuilder](media/sphere@6s@15@45.png)  
*6 slices, camera pitch 15°, camera roll 45°* -->

![Spherebuilder](media/sphere_2s_30p_63.435r.svg)  
*1 slice, camera pitch 30°, camera roll 63.435°*

### Math:

##### Calculate factors for Y and Z projection:

![Spherebuilder](media/Isometry-Projection-Geometry-03k3.gif)  
*Isometric projection geometry with a camera pitch of 30°. For projection, the y-axis is scaled by 0.87x and the z-axis by 0.5x.*

```processing
// Calculating the sides of a triangle
angleA = 90;
angleB = cameraPitch;
angleC = angleA - angleB;
sideA = 1; // normalized hypotenuse
sideB = sideA * sin(radians(angleC));
sideC = sideA * sin(radians(angleB));
```
