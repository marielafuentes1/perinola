from apuesta import Apuesta

def test_constructor():
    a= Apuesta()
    assert(a.fichas == 0 )

def test_poner_fichas():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    assert apuesta.fichas == 5, "Error: Debería haber 5 fichas"
    apuesta.ponerFicha()
    assert apuesta.fichas == 6, "Error: Debería haber 6 fichas"

def test_tomar_fichas():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    apuesta.tomarFicha(2)
    assert apuesta.fichas == 3, "Error: Debería haber 3 fichas"

  
    try:
        apuesta.tomarFicha(5)
        assert False, "Error: Debería haber lanzado un ValueError"
    except ValueError:
        pass  
    
def test_tomar_todas():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    total_tomadas = apuesta.tomarTodas()
    assert total_tomadas == 5, "Error: Debería haber tomado 5 fichas"
    assert apuesta.fichas == 0, "Error: Debería estar vacía después de tomar todas las fichas"

def test_tiene_ficha():
    apuesta = Apuesta()
    apuesta.ponerFicha(3)
    assert apuesta.tieneFicha(2) == True, "Error: Debería tener al menos 2 fichas"
    assert apuesta.tieneFicha(4) == False, "Error: No debería tener 4 fichas"

def test_esta_vacia():
    apuesta = Apuesta()
    assert apuesta.estaVacia() == True, "Error: Debería estar vacía"
    apuesta.ponerFicha(3)
    assert apuesta.estaVacia() == False, "Error: No debería estar vacía"
    apuesta.tomarTodas()
    assert apuesta.estaVacia() == True, "Error: Debería estar vacía después de quitar todas las fichas"
