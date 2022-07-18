from direccion import Direccion
from cuenta import Cuenta

class Cliente(object):

    def __init__(self, **cuenta):
        self.cuenta = Cuenta(**cuenta)
    
    def gestionarDatos(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['dni']
        self.direccion = Direccion(**datos['direccion'])
    
    def puedeCrearChequera(self):
        return False

    def puedeTenerTarjetaDeCredito(self):
        return False

    def puedeComprarDolar(self):
        return False

    def tieneCuentaCorriente(self):
        return False

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return True


class ClienteClassic(Cliente):
    def __init__(self, **cliente):
        Cliente.__init__(**cliente)

    def puedeCrearChequera(self):
        return False

    def puedeTenerTarjetaDeCredito(self):
        return False

    def puedeComprarDolar(self):
        return False

    def tieneCuentaCorriente(self):
        return False

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return True

class ClienteGold(Cliente):
    def __init__(self, **cliente):
        Cliente.__init__(**cliente)

    def puedeCrearChequera(self):
        return True

    def puedeTenerTarjetaDeCredito(self):
        return True

    def puedeComprarDolar(self):
        return True

    def tieneCuentaCorriente(self):
        return True

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return True

class ClienteBlack(Cliente):
    def __init__(self, **cliente):
        Cliente.__init__(**cliente)

    def puedeCrearChequera(self):
        return True

    def puedeTenerTarjetaDeCredito(self):
        return True

    def puedeComprarDolar(self):
        return True

    def tieneCuentaCorriente(self):
        return True

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return True
