def distance(*args: float, type: str, dimension: str) -> float:
    """
    Calculate various types of distances based on type and dimension.

    Parameters:
        *args (float): Coordinates or parameters for distance calculation.
        type (str): Distance type (e.g., 'dist_points', 'dist_manhattan').
        dimension (str): Dimension of space ('2d', '3d', 'euclid').

    Returns:
        float: Calculated distance.

    Raises:
        TypeError: If inputs are of incorrect type.
        ValueError: If the type or dimension is invalid.
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [distances] : Input error! Arguments must be numbers!")
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [distances] : Input error! Type must be a string!")
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [distances] : Input error! Dimension must be a string!")

    valid_types = [
        "dist_points", "dist_point_line", "dist_point_plane", "dist_par_lines",
        "dist_par_planes", "dist_vectors", "dist_manhattan", "dist_cos", "dist_Chebyshev"
    ]
    valid_dimensions = ["2d", "3d", "euclid"]

    if dimension not in valid_dimensions:
        raise ValueError("[mathhunt] : [distances] : Dimension must be one of: " + ", ".join(valid_dimensions))
    if type not in valid_types:
        raise ValueError("[mathhunt] : [distances] : Type must be one of: " + ", ".join(valid_types))

    if type == "dist_points":
        if dimension == "2d":
            return (((args[2] - args[0]) ** 2) + ((args[3] - args[1]) ** 2)) ** 0.5
        elif dimension == "3d":
            return (((args[3] - args[0]) ** 2) + ((args[4] - args[1]) ** 2) + ((args[5] - args[2]) ** 2)) ** 0.5
    elif type == "dist_point_line" and dimension == "2d":
        return abs((args[0] * args[3]) + (args[1] * args[4]) + args[2]) / (((args[0]) ** 2 + (args[1]) ** 2) ** 0.5)
    elif type == "dist_point_plane" and dimension == "3d":
        return abs((args[0] * args[4]) + (args[1] * args[5]) + (args[2] * args[6]) + args[3]) / (((args[0]) ** 2 + (args[1]) ** 2 + (args[2]) ** 2) ** 0.5)
    elif type == "dist_par_lines" and dimension == "2d":
        return abs(args[5] - args[2]) / (((args[0]) ** 2 + (args[1]) ** 2) ** 0.5)
    elif type == "dist_par_planes" and dimension == "3d":
        return abs(args[7] - args[3]) / (((args[0]) ** 2 + (args[1]) ** 2 + (args[2]) ** 2) ** 0.5)
    elif type == "dist_vectors":
        if dimension == "euclid":
            return (((args[3] - args[0]) ** 2) + ((args[4] - args[1]) ** 2) + ((args[5] - args[2]) ** 2)) ** 0.5
    elif type == "dist_manhattan":
        if dimension == "2d":
            return abs(args[2] - args[0]) + abs(args[3] - args[1])
        elif dimension == "3d":
            return abs(args[3] - args[0]) + abs(args[4] - args[1]) + abs(args[5] - args[2])
    elif type == "dist_cos" and dimension == "2d":
        cos = ((args[0] * args[2]) + (args[1] * args[3])) / (((args[0] ** 2 + args[1] ** 2) ** 0.5) * ((args[2] ** 2 + args[3] ** 2) ** 0.5))
        return 1.0 - cos
    elif type == "dist_Chebyshev":
        if dimension == "2d":
            return max(abs(args[2] - args[0]), abs(args[3] - args[1]))
        elif dimension == "3d":
            return max(abs(args[3] - args[0]), abs(args[4] - args[1]), abs(args[5] - args[2]))

    raise ValueError("[mathhunt] : [distances] : Unexpected error in calculations.")


def circumference(r: float) -> float:
    """
    Calculate the circumference of a circle.

    Parameters:
        r (float): Radius of the circle.

    Returns:
        float: Circumference of the circle.

    Raises:
        TypeError: If the radius is not a number.
    """
    if not isinstance(r, (int, float)):
        raise TypeError("[mathhunt] : [distances] : Input error! Radius must be a number!")
    return 2 * 3.14 * r


def arc_length(r: float, rad: float) -> float:
    """
    Calculate the length of an arc.

    Parameters:
        r (float): Radius of the circle.
        rad (float): Angle in radians.

    Returns:
        float: Arc length.

    Raises:
        TypeError: If inputs are not numbers.
        ValueError: If the angle is out of the valid range.
    """
    if not isinstance(r, (int, float)):
        raise TypeError("[mathhunt] : [distances] : Input error! Radius must be a number!")
    if not isinstance(rad, (int, float)):
        raise TypeError("[mathhunt] : [distances] : Input error! Angle must be a number!")
    if not (-6.2832 <= rad <= 6.2832):
        raise ValueError("[mathhunt] : [distances] : Angle must be in the range [-2π, 2π]")
    return r * rad


def vector_length(*args: float, dimension: str) -> float:
    """
    Calculate the length of a vector.

    Parameters:
        *args (float): Vector components.
        dimension (str): Dimension of the vector ('2d' or '3d').

    Returns:
        float: Length of the vector.

    Raises:
        TypeError: If inputs are not valid numbers or dimension is not a string.
        ValueError: If the dimension is invalid.
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [distances] : Input error! Arguments must be numbers!")
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [distances] : Input error! Dimension must be a string!")

    if dimension == "2d":
        return (args[0] ** 2 + args[1] ** 2) ** 0.5
    elif dimension == "3d":
        return (args[0] ** 2 + args[1] ** 2 + args[2] ** 2) ** 0.5
    else:
        raise ValueError("[mathhunt] : [distances] : Dimension must be '2d' or '3d'")