from datetime import date
import time

class PC:

    def __init__(self, marca, modelo, procesador, memoria_ram, almacenamiento, estado="Pendiente de revisión", averia="", fecha_entrada=None, fecha_salida=None):
        """
        Constructor de la clase PC.

        Parámetros:
            marca (str): Marca del ordenador.
            modelo (str): Modelo del ordenador.
            procesador (int): Número de núcleos del procesador.
            memoria_ram (int): Capacidad de memoria RAM en GB.
            almacenamiento (int): Capacidad de almacenamiento en GB.
            estado (str): Estado actual del ordenador ("Pendiente de revisión", "En reparación", "Reparado").
            averia (str): Descripción de la avería (opcional).
            fecha_entrada (date): Fecha de entrada del ordenador al taller (opcional).
            fecha_salida (date): Fecha de salida del ordenador del taller (opcional).
        """
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.estado = estado
        self.averia = averia
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def reparar(self, averia):
        """
        Simula la reparación del ordenador.

        Parámetros:
            averia (str): Descripción de la avería.

        Retorno:
            None.
        """
        self.averia = averia
        self.estado = "En reparación"
        # Simulación del proceso de reparación (puede ser un simple delay)
        time.sleep(2)
        self.estado = "Reparado"
        self.fecha_salida = date.today()

    def mostrar_informacion(self):
        """
        Muestra la información del ordenador.
        """
        print(f"**Información del ordenador:**")
        print(f"- Marca: {self.marca}")
        print(f"- Modelo: {self.modelo}")
        print(f"- Procesador: {self.procesador} núcleos")
        print(f"- Memoria RAM: {self.memoria_ram} GB")
        print(f"- Almacenamiento: {self.almacenamiento} GB")
        print(f"- Estado: {self.estado}")
        if self.averia:
            print(f"- Avería: {self.averia}")
        if self.fecha_entrada:
            print(f"- Fecha de entrada: {self.fecha_entrada}")
        if self.fecha_salida:
            print(f"- Fecha de salida: {self.fecha_salida}")

    def get_estado(self):
        """
        Devuelve el estado del ordenador.

        Retorno:
            str: Estado del ordenador.
        """
        return self.estado

    def set_estado(self, nuevo_estado):
        """
        Cambia el estado del ordenador.

        Parámetros:
            nuevo_estado (str): Nuevo estado del ordenador.

        Retorno:
            None.
        """
        self.estado = nuevo_estado


# Creación de 5 instancias de la clase PC
pc1 = PC("Asus", "VivoBook 15", 8, 16, 512)
pc2 = PC("Lenovo", "IdeaPad 3", 6, 8, 256)
pc3 = PC("HP", "Pavilion 14", 4, 4, 128)
pc4 = PC("Acer", "Aspire 5", 8, 12, 512)
pc5 = PC("Dell", "Inspiron 15", 6, 8, 256)

# Simulación de la reparación de 3 ordenadores
pc1.reparar("Pantalla rota")
pc3.reparar("Batería agotada")
pc5.reparar("Teclado no funciona")

# Impresión de la información de los ordenadores antes y después de la reparación
for pc in [pc1, pc3, pc5]:
    print(f"**Información antes de la reparación:**")
    pc.mostrar_informacion()
    print()
    pc.reparar("Simulación de reparación")
    print(f"**Información después de la reparación:**")
    pc.mostrar_informacion()
    print
