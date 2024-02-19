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


class Material:
    """class describing the mechanical characteristics of a material

    Attributes:
        name (str): material mark name
        younge_module (float): Young's modulus of tension of the material
        poisson_ratio (float): Poisson's ratio of the material
        allowable_stress (float): Permissible tensile stresses of the material
    """
    def __init__(self,
                 name: str,
                 young_module: float,
                 poisson_ratio: float,
                 allowable_stress: float) -> None:
        self.name = name
        self.young_module = young_module
        self.poisson_ratio = poisson_ratio
        self.allowable_stress = allowable_stress


class Geomety:
    """class describing the geometric characteristics of the cross section

    Attributes:
        name (str): type of the section shape
        params (dict): size values for different shapes
    """
    def __init__(self, name: str, params: dict) -> None:

        self.name = name
        self.size_params = params


class Beam:
    """class describing a beam

    Attributes:
        length (float): length of beam
        geom (Geomety): geometry of the cross section
        material (Material): matherial of beam
    """
    def __init__(self,
                 length: float,
                 geom: Geomety,
                 material: Material) -> None:
        self.length = length
        self.geom = geom
        self.material = material


class Force:
    """class for describing mechanical force

    Attributes:
        coordinate (Point): coorinate to which force is applied
        value_x (float): magnitude of the force projected on the x-axis
        value_y (float): magnitude of the force projected on the y-axis
        value_z (float): magnitude of the force projected on the z-axis
        """
    def __init__(self,
                 coordinate: Point,
                 value_x: float,
                 value_y: float,
                 value_z: float) -> None:
        self.coordinate = coordinate
        self.value_x = value_x
        self.value_y = value_y
        self.value_z = value_z


class Pressure:
    """class for describing a distributed load

    Attributes:
        intensity_x (float): intensity distributed load projected on the x-axis
        intensity_y (float): intensity distributed load projected on the y-axis
        intensity_z (float): intensity distributed load projected on the z-axis
        start (Point): coordinates of the beginning of the distributed load
        end (Point): coordinates of the ending of the distributed load
    """
    def __init__(self,
                 intensity_x: float,
                 intensity_y: float,
                 intensity_z: float,
                 start: Point,
                 end: Point) -> None:
        self.intensity_x = intensity_x
        self.intensity_y = intensity_y
        self.intensity_z = intensity_z
        self.start = start
        self.end = end


class Moment:
    """class for describing mechanical moment of force

    Attributes:
        coordinate (Point): coordinate to which force moment is applied
        value_x (float): magnitude of moment of force relative to the x axis
        value_y (float): magnitude of moment of force relative to the y axis
        value_z (float): magnitude of moment of force relative to the z axis
        """
    def __init__(self,
                 coordinate: Point,
                 value_x: float,
                 value_y: float,
                 value_z: float) -> None:
        self.coordinate = coordinate
        self.value_x = value_x
        self.value_y = value_y
        self.value_z = value_z
