class Turno:
    def __init__(self, id, cliente_id, peluquero_id, fecha, hora):
        
        self.id = id
        
        
        self.cliente_id = cliente_id
        
        
        self.peluquero_id = peluquero_id
        
        
        self.fecha = fecha
        
        
        self.hora = hora

    def __str__(self):
        return f"Turno {self.id}: Cliente {self.cliente_id}, Peluquero {self.peluquero_id}, {self.fecha} {self.hora}"
