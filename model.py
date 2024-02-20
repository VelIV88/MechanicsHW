from abc import ABC, abstractmethod
from entities.physics import Material, ConcentratedLoad, DistributedLoad
from entities.constructions import Beam


class MechanicHomeWork(ABC):
    @abstractmethod
    def __init__(self,
                 beam: Beam,
                 material: Material,
                 concetrated_loads: list[ConcentratedLoad]) -> None:
        self.beam = beam
        self.material = material
        self.loads = concetrated_loads


class Stretching(MechanicHomeWork):
    def __init__(self,
                 beam: Beam,
                 material: Material,
                 concetrated_loads: list[ConcentratedLoad]) -> None:
        super().__init__(beam, material, concetrated_loads)
