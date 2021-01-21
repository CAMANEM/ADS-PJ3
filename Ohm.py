class Ohm:
    """
    Clase encargada de calcular voltaje, amperaje y resitancia del circuito.
    """
    cooperResistivity = 0.0000000171
    def __init__(self):
        super().__init__()

    @staticmethod
    def Resistance(voltage, intensity):
        """
        Calcula la resistencia presente en el voltaje e intensidad (amperaje) de entrada.

        Entrada: voltaje (int o float) e intensidad (int o float).
        Salida: resistencia (float).
        """
        if ((isinstance(intensity, int) or isinstance(intensity, float)) and (isinstance(voltage, int) or isinstance(voltage, float))):
            return voltage / intensity
        else:
            print("Error de entrada en 'Resistance'. El formato de entrada debe ser entero o de coma flotante.")

    @staticmethod
    def Voltage(intensity, resistance):
        """
        Calcula el voltage de salida para la intensidad (amperaje) y resistencia de entrada.

        Entrada: intensidad (int o float) y resistencia (int o float).
        Salida: voltaje (float).
        """
        if ((isinstance(intensity, int) or isinstance(intensity, float)) and (isinstance(resistance, int) or isinstance(resistance, float))):
            return intensity * resistance
        else:
            print("Error de entrada en 'Voltage'. El formato de entrada debe ser entero o de coma flotante.")

    @staticmethod
    def Intensity(voltage, resistance):
        """
        Calcula la intensidad (amperaje) considerando el voltaje y resistencia presentes.

        Entrada: vontaje (int o float) y resistencia (int o float).
        Salida: intensidad (float).
        """
        if ((isinstance(voltage, int) or isinstance(voltage, float)) and (isinstance(resistance, int) or isinstance(resistance, float))):
            return voltage / resistance
        else:
            print("Error de entrada en 'Intensity'. El formato de entrada debe ser entero o de coma flotante.")

    @staticmethod
    def CableOutput(lenght, thickness, voltage, intensity):
        """
        Calcula la salida (voltaje, amperaje y potencia) del cable.
        
        Entradas: largo del cable [metros] (int o float), grosor [metros cuadados] (int o float), voltaje (int o float) e intensidad (int o float).
        Salidas: lista con todos los elementos float [voltaje, amperaje, potencia].
        """

        voltageDrop = (2 * intensity * lenght * Ohm.cooperResistivity) / 1000
        voltage -= voltageDrop
        power = voltage * intensity
        
        return [voltage, intensity, power]