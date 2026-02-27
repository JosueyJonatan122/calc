class Usuario:
    def __init__(self,nombre,cedula,tipo_usuario):
        self._nombre=nombre
        self._cedula=cedula
        self._tipo_usuario=tipo_usuario
        
    def get_nombre(self):
        return self._nombre
    
    def get_cedula(self):
        return self._cedula
    
    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def set_nombre(self,nuevo_nombre):
        self._nombre=nuevo_nombre
        
    def set_cedula(self,nueva_cedula):
        self._cedula=nueva_cedula
        
    def set_tipo_usuario(self,nuevo_tipo_usuario):
        self._tipo_usuario=nuevo_tipo_usuario
        
    def mostrar_info(self):
        return (f" Nombre: {self._nombre}\n" 
                f"cedula: {self._cedula}\n"
                f"Tipo_usuario: {self._tipo_usuario}")