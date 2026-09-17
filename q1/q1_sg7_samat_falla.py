class Glassware:
    def __init__(self, name):
        self.name = name


class Beaker(Glassware):
    def __init__(self, capacity):
        super().__init__("Beaker")
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} ({self.capacity} mL)"


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker(100),
            Beaker(250),
            Beaker(500),
            Beaker(1000),
            Beaker(2000)
        ]

    def show_beakers(self):
        for beaker in self.beakers:
            print(beaker)



tray = Tray()

tray.show_beakers()

del tray