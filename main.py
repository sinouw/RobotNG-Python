from robot import Robot
from robot_ng import RobotNG
from point import Point

# ******************************************** #
# Robot Class Test
# ******************************************** #

# Initialiser Instance 1
robot1 = Robot(4, 10, "est")
# Afficher Instance 1
robot1.afficher(prefix="robot1 = ")

# Initialiser Instance 2
robot2 = Robot(15, 7, "sud")
# Afficher Instance 2
robot2.afficher(prefix="robot2 = ")

# Pivoter Instance 1
robot1.pivoter()
# Afficher Instance 1
robot1.afficher(prefix="robot1 = ")

# Avancer Instance 2
robot2.avancer()
# Afficher Instance 2
robot2.afficher(prefix="robot2 = ")
# Pivoter Instance 2
robot2.pivoter()
# Afficher Instance 2
robot2.afficher(prefix="robot2 = ")

# ******************************************** #
# RobotNg Class Test
# ******************************************** #

# Créer le chemin

# Liste globale des points
pointsList = []

p1 = Point(6, 1)
p2 = Point(4, 3)
p3 = Point(3, 4)
p4 = Point(1, 3)
p5 = Point(5, 5)

# Affecter les points a la liste
pointsList = [p1, p2, p3, p4, p5]

# Instancer robotNG1 de la classe RobotNG
robotNG1 = RobotNG(2, 1, "nord")
# Afficher robotNG1
robotNG1.afficher(prefix="robotNG1 = ")
# Detecter Le Trajet robotNG1
robotNG1.trajet(pointsList)
