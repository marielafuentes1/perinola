import pytest
from Jugador import Jugador


def test_constructor_sin_fichas():
   j = Jugador("b")
   assert(j.nombre == "b" )
   assert(j.fichas == 5)

def test_constructor_con_fichas():
   j = Jugador("b" , 8)
   assert(j.nombre == "b" )
   assert(j.fichas == 8)

def test_dar_ficha():
   j = Jugador("b", 10)
   j.darFicha(5)
   assert(j.fichas == 15)  
 
def test_dar_ficha_sin_ficha():
   j = Jugador("b", 10)
   j.darFicha()
   assert(j.fichas == 11)


def test_sacar_ficha_error():
   j = Jugador("b", 10)
   with pytest.raises(ValueError):
       j.sacarFicha(11)
