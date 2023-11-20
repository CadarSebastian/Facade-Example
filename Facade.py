# Definirea unui sistem complex
class SubsystemA:
    def operation_a(self):
        return "Subsystem A operation"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B operation"

# Facade care oferă o interfață simplificată
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        result = []
        result.append(self.subsystem_a.operation_a())
        result.append(self.subsystem_b.operation_b())
        return "\n".join(result)

# Utilizarea Facade
def client_code(facade):
    print(facade.operation())

# Exemplu de utilizare
if __name__ == "__main__":
    facade = Facade()
    client_code(facade)
