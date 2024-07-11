class DNS:
    """
    Implementación de un Servicio de DNS Dinámico
    Objetivo: Implementa un servicio de DNS dinámico en Python que pueda gestionar múltiples
    registros, incluyendo registros A, CNAME y MX, y simular resoluciones de nombres de dominio.
    """
    def __init__(self):
        self.records = {
            'A': {},
            'CNAME': {},
            'MX': {}
        }

    def agregar_registro(self, tipo_registro, nombre, valor):
        if tipo_registro in self.records:
            self.records[tipo_registro][nombre] = valor
        else:
            print(f"Tipo de registro {tipo_registro} no soportado")

    def eliminar_registro(self, tipo_registro, nombre):
        if tipo_registro in self.records and nombre in self.records[tipo_registro]:
            del self.records[tipo_registro][nombre]
        else:
            print(f"Registro {nombre} no encontrado en los registros {tipo_registro}")

    def actualizar_registro(self, tipo_registro, nombre, valor):
        if tipo_registro in self.records and nombre in self.records[tipo_registro]:
            self.records[tipo_registro][nombre] = valor
        else:
            print(f"Registro {nombre} no encontrado en los registros {tipo_registro}")

    def resolver(self, nombre):
        if nombre in self.records['A']:
            return self.records['A'][nombre]
        elif nombre in self.records['CNAME']:
            cname = self.records['CNAME'][nombre]
            return self.resolver(cname)
        elif nombre in self.records['MX']:
            return self.records['MX'][nombre]
        else:
            return None

    def __str__(self):
        return str(self.records)

# Simulación de la CLI
def main():
    dns = DNS()
    while True:
        comando = input("Ingrese comando (agregar, eliminar, actualizar, resolver, salir): ")
        if comando == 'agregar':
            tipo_registro = input("Ingrese tipo de registro (A, CNAME, MX): ")
            nombre = input("Ingrese nombre: ")
            valor = input("Ingrese valor: ")
            dns.agregar_registro(tipo_registro, nombre, valor)
        elif comando == 'eliminar':
            tipo_registro = input("Ingrese tipo de registro (A, CNAME, MX): ")
            nombre = input("Ingrese nombre: ")
            dns.eliminar_registro(tipo_registro, nombre)
        elif comando == 'actualizar':
            tipo_registro = input("Ingrese tipo de registro (A, CNAME, MX): ")
            nombre = input("Ingrese nombre: ")
            valor = input("Ingrese nuevo valor: ")
            dns.actualizar_registro(tipo_registro, nombre, valor)
        elif comando == 'resolver':
            nombre = input("Ingrese nombre a resolver: ")
            ip = dns.resolver(nombre)
            if ip:
                print(f"IP para {nombre} es {ip}")
            else:
                print(f"{nombre} no encontrado")
        elif comando == 'salir':
            break
        else:
            print("Comando inválido")

if __name__ == "__main__":
    main()
