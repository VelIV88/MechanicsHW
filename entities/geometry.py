class Point:
    """class describing a point in a Cartesian coordinate system

    Attributes:
        x (float): the x coordinate
        y (float): the y coordinate
        z (float): the z coordinate
    """
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z


class CrossSection:
    """class describing the geometric characteristics of the cross section

    Attributes:
        name (str): type of the section shape
        params (dict): size values for different shapes
    """
    def __init__(self, name: str, params: dict) -> None:

        self.name = name
        self.size_params = params
