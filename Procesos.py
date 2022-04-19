from Usuario import *
from AlmacenamientoUsuarios import *

class Procesos:
    
    usuarioGlobal=None
    miAlmacenamientoUsuarios=AlmacenamientoUsuarios()
    '''
     def llenarListaUsuarios(self):
        miUsuario1=Usuario("111","maria","gonzalez","12345","maria@gmail.com","222",1)
        miUsuario2=Usuario("222","maria","cuellar","12345","mar@gmail.com","111",2)

        print()
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario1)
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario2)
    '''
   

    def registrarUsuarios(self,miUsuario):
        print("Usuario a registrar",miUsuario)
        return self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario)
    
    def actualizarUsuario(self,miUsuario):
        return self.miAlmacenamientoUsuarios.actualizarUsuario(miUsuario)

    def eliminarUsuario(self,documento):
        return self.miAlmacenamientoUsuarios.eliminarUsuario(documento)


    def consultarUsuario(self,documento):
        usuario=self.miAlmacenamientoUsuarios.consultarUsuarioPorDocumento(documento)

        if(usuario!=None):
            print(usuario)
        else:
            print(f"\nNo existe ningún estudiante con el documento {documento}")
            
        return usuario

    def obtenerListaUsuarios(self):
        lista=self.miAlmacenamientoUsuarios.obtenerListaUsuarios()  
        return lista 
    
    def obtenerListaPerfil(self):
        datoss=self.miAlmacenamientoUsuarios.obtenerListaPerfil()  
        return datoss 
    
    def consultarListaUsuarios(self):
        print("\n<<<<<<<<<<<<<<<<<- LISTA DE USUARIOS ->>>>>>>>>>>>>>>>>>>>")
        self.miAlmacenamientoUsuarios.consultarListaUsuarios()  
        print("\n*************************************************************\n")    
