from Usuario import *

class Almacenamiento:

    listaUsuarios=[]
    listaGeneralUsuarios=[]

    def registrarUsuario(self,usuarios):
        
        self.listaUsuarios.append(usuarios)
        lista=[]
        lista.append(usuarios.documento)
        lista.append(usuarios.nombre)
        lista.append(usuarios.apellido)
        lista.append(usuarios.telefono)
        lista.append(usuarios.email)
        lista.append(usuarios.password)
        lista.append(usuarios.tipo)
        self.listaGeneralUsuarios.append(lista)
        print(lista)
        print(usuarios)

        print(f"Usuario {usuarios.nombre} registrado con exito!")
        return f"Usuario {usuarios.nombre} registrado con exito!"
    
    def eliminarUsuario(self,documento):
        print(documento)
        usuarios=self.consultarEstudiantePorDocumento(documento)
        if(usuarios!=None):
            nombre=usuarios.nombre
            for i in range(len(self.listaGeneralUsuarios)):
                lista=self.listaGeneralUsuarios[i]
                print("-->",lista)
                if(usuarios.documento==lista[0]):
                    print("Elimina")
                    self.listaGeneralUsuarios.remove(lista)
                    self.listaUsuarios.remove(usuarios)
                    break
        
        return f"El usuario {nombre} Se ha eliminado con exito!"

    def actualizarUsuario(self,miUsuario):
        usuarios=self.consultarEstudiantePorDocumento(miUsuario.documento)
        mensaje=""
        if(usuarios!=None):

            usuarios.documento=miUsuario.documento
            usuarios.nombre=miUsuario.nombre
            usuarios.apellido=miUsuario.apellido
            usuarios.telefono=miUsuario.telefono
            usuarios.email=miUsuario.email
            usuarios.password=miUsuario.password
            usuarios.tipo=miUsuario.tipo
            self.actualizarListaGeneral(usuarios)
            mensaje="Se ha actualizado el estudiante"
        else:
            mensaje="El estudiante no se pudo actualizar"
        return mensaje

    def actualizarListaGeneral(self,usuarios):
        for i in range(len(self.listaGeneralUsuarios)):
            lista=self.listaGeneralUsuarios[i]
            print("-->",lista)
            if(usuarios.documento==lista[0]):
                print("Actualiza")
                lista[1]=usuarios.documento
                lista[2]=usuarios.nombre
                lista[3]=usuarios.apellido
                lista[4]=usuarios.telefono
                lista[5]=usuarios.email
                lista[6]=usuarios.password
                lista[7]=usuarios.tipo
                break


    def obtenerListaEstudiantes(self):
        print(self.listaGeneralUsuarios)
        return self.listaGeneralUsuarios

    def consultarListaEstudiantes(self):
        if(self.validaTamanioLista()==True):
            for i in range(len(self.listaUsuarios)):
                usuarios=self.listaUsuarios[i]
                usuarios.imprimirDatos()
        
        return self.listaUsuarios


    def consultarEstudiantePorDocumento(self,documento):
        usuarios=None #Se inicializa en none el estudiante
        if(self.validaTamanioLista()==True):
            for user in self.listaUsuarios:
                if(user.documento==documento):
                    usuarios=user # se asigna el elemento encontrado al objeto estudiante
        
        return usuarios


        

    def obtenerCantidadEstudiantes(self):
        return len(self.listaUsuarios)

    
    def validaTamanioLista(self):
        if(len(self.listaUsuarios)>0):
            return True
        else:
            print("\n<<<< No han registrado estudiantes >>>")
            return False




