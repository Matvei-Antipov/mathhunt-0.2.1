# mathhunt Library

Mathhunt is a lightweight Python library designed for quick and efficient mathematical computations. It provides functions for calculating the volume and area of various geometric shapes, as well as distances between points in a Cartesian coordinate system.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Volume Calculation](#Volume-calculation)
  - [Area Calculation](#Area-calculation)
  - [Distance Calculation](#Distance-calculation)
  - [Mathematical function](#mathematical-function)
- [License](#license)

## Features

- **Volume Calculations**: Calculate the volume of shapes like cubes, spheres, cylinders, and more.
- **Area Calculations**: Calculate the area of shapes such as circles, triangles, rectangles, and polygons.
- **Distance Calculations**: Compute distances between points in a Cartesian coordinate system.
- **Error Handling**: Comprehensive error handling to ensure valid input types and values.
- **Mathematical Functions**: Use all mathematical functions required.

## Installation

```pip install fastmath```

## Usage

You should import module that you need to use from fastmath

For example you need to use sinus function. You should situate 

```from mathhunt import functions

print(functions.sinus(45, "deg"))```

Here you can see 2 arguments

##Volume-calculation

- The volume function calculates the volume of various 3D shapes  based on the provided shape type and corresponding metrics. It supports multiple geometric shapes and ensures input validation for accurate calculations.

**Parameters**
```*args (float)```: A variable-length argument list representing the necessary metrics for the specified shape (e.g., radius, height, side length). The number of arguments required depends on the shape type.

```type (str)```: A string that specifies the type of shape for which the volume is to be calculated. Supported types include:

'parallelepiped'
'cube'
'cylinder'
'sphere'
'cone'
'pyramid'
'tetrahedron'
'octahedron'
'icosahedron'
Returns
float: The calculated volume of the specified shape.
Raises
TypeError:

If any of the input metrics (*args) are not numbers (either int or float).
If the type parameter is not a string.
ValueError:

If the specified shape type is invalid (not one of the supported types).
If the number of arguments does not match the expected count for the specified shape type.
If any of the provided metrics are non-positive (less than or equal to zero).

**Examples of usage**

> Calculate the volume of a cube with side length 3
volume_cube = volume(3, type='cube')  # Returns: 27.0

> Calculate the volume of a cylinder with radius 2 and height 5
volume_cylinder = volume(2, 5, type='cylinder')  # Returns: 25.12

> Calculate the volume of a sphere with radius 4
volume_sphere = volume(4, type='sphere')  # Returns: 268.08

> Invalid usage example
```volume_invalid = volume(2, 3, type='invalid_shape')```
Raises ValueError

##Area-calculation
- The square function calculates the area of various 2D shapes based on the specified shape type and corresponding metrics. This function is designed to handle multiple geometric shapes and includes robust input validation for accurate area calculations.

**Parameters**
```*args (float):``` A variable-length argument list that represents the necessary metrics for the specified shape (e.g., side lengths, radius). The number of arguments required varies depending on the shape type.

```type (str):``` A string that specifies the type of shape for which the area is to be calculated. Supported types include:

'quadrate'
'rectangle'
'triangle_h' (triangle with base and height)
'triangle_s' (triangle with three sides)
'circle'
'trapezoid'
'rhombus'
'parallelogram'
'sector'
'ellipse'
'polygon'
'sphere' (note: typically, spheres are 3D; area may refer to the surface area calculation)
Returns
float: The function returns the calculated area of the specified shape.
Raises
TypeError:

If any of the input metrics (*args) are not numeric (i.e., not of type int or float).
If the type parameter is not a string.
ValueError:

If the specified shape type is invalid (not one of the recognized types).
If the number of provided arguments does not match the expected count for the specified shape type.
If any of the provided metrics are non-positive (i.e., less than or equal to zero).

**Example of usage**

> Calculate the area of a square with side length 4
area_square = square(4, type='quadrate')  # Expected output: 16.0

> Calculate the area of a rectangle with width 3 and height 5
area_rectangle = square(3, 5, type='rectangle')  # Expected output: 15.0

> Calculate the area of a triangle with base 4 and height 3
area_triangle_h = square(4, 3, type='triangle_h')  # Expected output: 6.0

> Calculate the area of a circle with radius 2
area_circle = square(2, type='circle')  # Expected output: 12.56

> Invalid usage example
area_invalid = square(3, type='invalid_shape')  
This will raise ValueError

##Distance-calculation
 -**Function: distance**
Calculates various types of distances based on the specified type and dimension.

**Parameters**
```*args (float):``` Coordinates or parameters required for distance calculation.
```type (str):``` The type of distance to calculate. Supported types include:
'dist_points'
'dist_point_line'
'dist_point_plane'
'dist_par_lines'
'dist_par_planes'
'dist_vectors'
'dist_manhattan'
'dist_cos'
'dist_Chebyshev'
dimension (str): The dimension of the space in which to calculate the distance. Acceptable values are:
'2d'
'3d'
'euclid'
Returns
float: The calculated distance based on the specified type and dimension.
Raises
TypeError: If any of the arguments are not numeric, or if type or dimension are not strings.
ValueError: If the type or dimension is invalid.

**Example of usage**

> Calculate distance between two points in 2D
dist = distance(0, 0, 3, 4, type='dist_points', dimension='2d')  # Output: 5.0

> Calculate Manhattan distance in 3D
manhattan_dist = distance(1, 2, 3, 4, 5, 6, type='dist_manhattan', dimension='3d')  # Output: 9.0

**Function: circumference**
Calculates the circumference of a circle.

Parameters
```r (float):``` The radius of the circle.
Returns
float: The calculated circumference of the circle.
Raises
TypeError: If the radius is not a number.

**Example of usage**

> Calculate the circumference of a circle with radius 5
circ = circumference(5)  # Output: 31.400000000000002


Here's an explanation for the distance, circumference, ```arc_length```, and ```vector_length``` functions from your Mathhunt library. This documentation will help users understand the purpose, parameters, return values, and potential exceptions raised by each function.

 -**Function: arc_length**
Calculates the length of an arc of a circle.

Parameters
```r (float):``` The radius of the circle.
```rad (float):``` The angle in radians.
Returns
float: The calculated arc length.
Raises
TypeError: If either r or rad is not a number.
ValueError: If the angle is out of the valid range.

**Example of usage**

> Calculate the length of an arc with radius 10 and angle π/2
```arc = arc_length(10, 1.5708)  # Output: 15.707999999999998```

 -**Function: vector_length**
Calculates the length of a vector.

*Parameters*
```*args (float):``` The components of the vector.
```dimension (str):``` The dimension of the vector, either '2d' or '3d'.
**Returns**
float: The calculated length of the vector.
**Raises**
TypeError: If any arguments are not valid numbers or if dimension is not a string.
ValueError: If dimension is invalid.

**Example of usage**

> Calculate the length of a 2D vector (3, 4)
```vec_length_2d = vector_length(3, 4, dimension='2d')  # Output: 5.0```

> Calculate the length of a 3D vector (1, 2, 2)
```vec_length_3d = vector_length(1, 2, 2, dimension='3d')  # Output: 3.0```

-##Mathematical-function