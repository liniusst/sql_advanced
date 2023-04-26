from modules import Vaikas, Tevas
from session import session

vaikas = Vaikas(vardas="naujas vaikas", pavarde="Tevaika")
tevas = session.query(Tevas).get(1)
tevas.vaikas = vaikas
session.commit()
