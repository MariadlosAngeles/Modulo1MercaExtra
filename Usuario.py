class Usuario:

    def __init__(self,documento=None,nombre=None,apellido=None,telefono=None,email=None,password=None,tipo=None):
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.email=email
        self.password=password
        self.tipo=tipo

    def __str__(self) -> str:
        datos="\n<<<<<<<<<<<<< DATOS USUARIO >>>>>>>>>>>>>>>\n"
        datos+=f"Documento: {self.documento} , Nombre: {self.nombre}, Apellido: {self.apellido}\n"
        datos+=f"Telefono: {self.telefono} , email:{self.email}\n"
        datos+=f"Contraseña: {self.password},tipo:{self.tipo}\n"

        return datos
