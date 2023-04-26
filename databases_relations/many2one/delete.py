from modules import Vaikas, Tevas
from session import session

tevas = session.query(Tevas).get(1)
vaikas1 = tevas.vaikai[0]
tevas.vaikai.remove(vaikas1)
session.commit()
