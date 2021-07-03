from point import Point


class Robot:
    nom = "Robot"
    version = 0

    def __init__(self):
        self.position = Point()
        self.orientation = "nord"

    def __init__(self, x, y, orientation):
        self.position = Point(x, y)
        self.orientation = "nord est sud ouest".split().index(orientation)

    def avancer(self):
        """Avancer d'une case dans la orientation."""
        # mettre à jour self.position.x
        if self.orientation == 1:  # est
            self.position.x += 1
        elif self.orientation == 3:  # ouest
            self.position.x -= 1
        # mettre à jour self.position.y
        if self.orientation == 0:  # nord
            self.position.y += 1
        elif self.orientation == 2:  # sud
            self.position.y -= 1

    def pivoter(self):
        """Pivoter ce robot de 90° vers la droite."""
        self.orientation = (self.orientation + 1) % 4

    def afficher(self, *, prefix):
        print(
            prefix
            + "({}, {})>{}".format(
                self.position.x,
                self.position.y,
                "nord est sud ouest".split()[self.orientation],
            )
        )
