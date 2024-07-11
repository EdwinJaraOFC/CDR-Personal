import time
import random

class VirtualMachine:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources
        self.running = False
        self.failed = False

    def iniciar(self):
        if not self.failed:
            self.running = True
            print(f"VM {self.name} ha sido iniciada.")
        else:
            print(f"No se puede iniciar VM {self.name} debido a un fallo.")

    def detener(self):
        self.running = False
        print(f"VM {self.name} ha sido detenida.")

    def reiniciar(self):
        if not self.failed:
            self.detener()
            time.sleep(1)  # Simula el tiempo de reinicio
            self.iniciar()
            print(f"VM {self.name} ha sido reiniciada.")
        else:
            print(f"No se puede reiniciar VM {self.name} debido a un fallo.")

    def fallar(self):
        self.failed = True
        self.running = False
        print(f"VM {self.name} ha fallado.")

    def recuperar(self):
        self.failed = False
        print(f"VM {self.name} ha sido recuperada.")

class Hypervisor:
    def __init__(self):
        self.vms = []

    def agregar_vm(self, vm):
        self.vms.append(vm)
        print(f"VM {vm.name} ha sido añadida al hipervisor.")

    def iniciar_vm(self, name):
        vm = self.buscar_vm(name)
        if vm:
            vm.iniciar()

    def detener_vm(self, name):
        vm = self.buscar_vm(name)
        if vm:
            vm.detener()

    def reiniciar_vm(self, name):
        vm = self.buscar_vm(name)
        if vm:
            vm.reiniciar()

    def fallar_vm(self, name):
        vm = self.buscar_vm(name)
        if vm:
            vm.fallar()

    def recuperar_vm(self, name):
        vm = self.buscar_vm(name)
        if vm:
            vm.recuperar()

    def asignar_recursos(self):
        for vm in self.vms:
            if vm.running and not vm.failed:
                vm.resources = random.randint(1, 100)
                print(f"Recursos asignados a VM {vm.name}: {vm.resources}")

    def balancear_carga(self):
        total_recursos = sum(vm.resources for vm in self.vms if vm.running and not vm.failed)
        if total_recursos > 0:
            promedio_recursos = total_recursos // len([vm for vm in self.vms if vm.running and not vm.failed])
            for vm in self.vms:
                if vm.running and not vm.failed:
                    vm.resources = promedio_recursos
                    print(f"Recursos balanceados para VM {vm.name}: {vm.resources}")

    def buscar_vm(self, name):
        for vm in self.vms:
            if vm.name == name:
                return vm
        print(f"VM {name} no encontrada.")
        return None

# Ejemplo de ejecución del simulador de hipervisor
if __name__ == "__main__":
    # Crear el hipervisor
    hypervisor = Hypervisor()

    # Crear y agregar VMs al hipervisor
    vm1 = VirtualMachine("VM1", 50)
    vm2 = VirtualMachine("VM2", 30)
    vm3 = VirtualMachine("VM3", 70)

    hypervisor.agregar_vm(vm1)
    hypervisor.agregar_vm(vm2)
    hypervisor.agregar_vm(vm3)

    # Iniciar VMs
    hypervisor.iniciar_vm("VM1")
    hypervisor.iniciar_vm("VM2")

    # Asignación de recursos
    hypervisor.asignar_recursos()

    # Simulación de fallo y recuperación
    hypervisor.fallar_vm("VM2")
    hypervisor.recuperar_vm("VM2")
    hypervisor.reiniciar_vm("VM2")

    # Balanceo de carga
    hypervisor.balancear_carga()

    # Parar VMs
    hypervisor.detener_vm("VM1")
    hypervisor.detener_vm("VM2")
    hypervisor.detener_vm("VM3")
