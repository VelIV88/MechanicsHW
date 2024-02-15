
class Material:

    def __init__(
            self,
            young_module: float,
            poisson_ratio: float, allowable_stress: float
            ) -> None:
        self.young_module = young_module
        self.poisson_ratio = poisson_ratio
        self.allowable_stress = allowable_stress


class Beam:

    def __init__(self, length: float, form: str, material: Material) -> None:
        self.length = length
        self.form = form
        self.material = material


class Force:

    def __init__(self, coordinate: str, value: float, angle: float) -> None:
        self.coord = coordinate
        self.value = value
        self.angle = angle
