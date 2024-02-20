from entities.geometry import CrossSection
from entities.physics import Material


class Beam:
    """class describing a beam

    Attributes:
        length (float): length of beam
        geom (Geomety): geometry of the cross section
        material (Material): matherial of beam
    """
    def __init__(self,
                 length: float,
                 geom: CrossSection,
                 material: Material) -> None:
        self.length = length
        self.geom = geom
        self.material = material
