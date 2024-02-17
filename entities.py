class Point:
    """class describing a point in a Cartesian coordinate system

    Args:
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

    Args:
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

    Args:
        name (str): type of the section shape
    """
    def __init__(self, name: str, params: dict) -> None:

        self.name = name
        self.size_params = params


class Beam:
    """class describing a beam

    Args:
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

    Args:
        coordinate (Point): coordinates of the application of force
        value (float): magnitude of the force
        """
    def __init__(self, coordinate: Point, value: float, angle: float) -> None:
        self.coord = coordinate
        self.value = value
