class Cliente:
    def __init__(self, id, nombre, telefono):
        
        self.id = id
        
        
        self.nombre = nombre
        
        
        self.telefono = telefono

    def __str__(self):
        
        return f"{self.id} - {self.nombre} ({self.telefono})"
