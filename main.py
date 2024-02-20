from model import Stretching
from entities.constructions import Beam
from entities.geometry import CrossSection, Point
from entities.physics import Force, Material


def main() -> None:
    squard = CrossSection("sqard", {})
    steel = Material("steel", 2 * 10**11, 0.3, 250 * 10**6)
    straight_rod = Beam(2.2, squard, steel)
    force_coord = Point(0, 0, 1.1)
    loads = [Force(force_coord, 0, 0, 1000)]
    new_hw = Stretching(straight_rod, steel, loads)

    print(new_hw)


if __name__ == "__main__":
    main()
