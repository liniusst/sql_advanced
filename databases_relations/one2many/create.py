from modelis import Tevas, Vaikas
from session import session

vaikas = Vaikas(vardas="Vaikas 1", pavarde="Vaikaitis 1")
vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")
tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")
tevas.vaikai.append(vaikas)
tevas.vaikai.append(vaikas2)
session.add(tevas)
session.commit()
