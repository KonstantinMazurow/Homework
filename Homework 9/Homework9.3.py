class Car:

    def __init__(self, color=None, type_car=None, year=None):
        self.color = color
        self.type_car = type_car
        self.year = year

    def start_car(self) -> str:
        print(str('{0} car, {1} type, {2} release - started'.
              format(self.color, self.type_car, self.year)))

    def stop_car(self) -> str:
        print(str('{0} car, {1} type, {2} release - stoped'.
              format(self.color, self.type_car, self.year)))

    def set_year(self, year: int) -> None:
        self.year = year

    def set_type_car(self, type_car: str) -> None:
        self.type_car = type_car

    def set_color(self, color: str) -> None:
        self.color = color
