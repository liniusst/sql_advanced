from modules import Tevas
from session import session

tevas = session.query(Tevas).get(1)
tevas.vaikas.pavarde = "Naujapavardaitis"
session.commit()
