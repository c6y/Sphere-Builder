# Sphere Builder

Render an isometric sphere with slices. The slice count, camera pitch (also called 'tilt'), and camera roll, can all be set. Made with DrawBot/Python.

![Spherebuilder](media/sphere_12s_30p_0r.svg)  
*12 slices, camera pitch 30°*

![Spherebuilder](media/sphere_24s_15p_0r.svg)  
*24 slices, camera pitch 15°*

![Spherebuilder](media/sphere_6s_50p_15r.svg)  
*6 slices, camera pitch 50°, camera roll 15°*

![Spherebuilder](media/sphere_2s_30p_63.435r.svg)  
*1 slice, camera pitch 30°, camera roll 63.435°*

![Spherebuilder](media/Isometry-Projection-Geometry-03k3.gif)  
*Isometric projection geometry with a camera pitch of 30°. When projecting to a 2d plane, the y-axis is scaled by 0.87x and the z-axis by 0.5x. The x-axis is not scaled. These are the values we actually work with when making pixel art (and usually are not aware of). Using Geometry, it is easy to calculate the translation to 2D, once we have the camera pitch, the depth and the height of the original object.*
