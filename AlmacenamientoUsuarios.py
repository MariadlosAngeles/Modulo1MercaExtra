from Usuario import *


class AlmacenamientoUsuarios:

    listaUsuarios = []
    listaGeneralUsuarios = []
    listaGeneralPerfil = []

    def registrarUsuario(self, usuario):

        self.listaUsuarios.append(usuario)
        lista = []
        lista.append(usuario.documento)
        lista.append(usuario.nombre)
        lista.append(usuario.apellido)
        lista.append(usuario.telefono)
        lista.append(usuario.email)
        lista.append(usuario.password)
        lista.append(usuario.tipo)
        print(lista)
        print(usuario)
        #print(type(usuario))
        print("Tipo Usuario: ", usuario.tipo)
        if (usuario.tipo == 1):
            print("Ingresa a tipo 1")
            #   lista.append("Administrador")
        else:
            #  lista.append("Usuario")
            print("Ingresa a tipo 2")
        self.listaGeneralUsuarios.append(lista)

        print("***************")
        print(self.listaGeneralPerfil)

        print(f"Usuario {usuario.nombre} registrado con exito!")
        return f"Usuario {usuario.nombre} registrado con exito!"

    def eliminarUsuario(self, documento):
        print(documento)
        usuario = self.consultarUsuarioPorDocumento(documento)
        if(usuario != None):
            nombre = usuario.nombre
            for i in range(len(self.listaGeneralUsuarios)):
                lista = self.listaGeneralUsuarios[i]
                print("-->", lista)
                if(usuario.documento == lista[0]):
                    print("Elimina")
                    self.listaGeneralUsuarios.remove(lista)
                    self.listaUsuarios.remove(usuario)
                    break

        return f"El usuario {nombre} Se ha eliminado con exito!"

    def actualizarUsuario(self, miUsuario):
        usuario = self.consultarUsuarioPorDocumento(miUsuario.documento)
        mensaje = ""
        if(usuario != None):
            usuario.documento = miUsuario.documento
            usuario.nombre = miUsuario.nombre
            usuario.apellido = miUsuario.apellido
            usuario.telefono = miUsuario.telefono
            usuario.email = miUsuario.email
            usuario.password = miUsuario.password
            usuario.tipo = miUsuario.tipo
            self.actualizarListaGeneralUsuarios(usuario)
            mensaje = "Se ha actualizado el estudiante"
        else:
            mensaje = "El estudiante no se pudo actualizar"
        return mensaje

    def actualizarListaGeneralUsuarios(self, usuario):
        for i in range(len(self.listaGeneralUsuarios)):
            lista = self.listaGeneralUsuarios[i]
            print("-->", lista)
            if(usuario.documento == lista[0]):
                print("Actualiza")
                lista[1] = usuario.nombre
                lista[2] = usuario.apellido
                lista[3] = usuario.telefono
                lista[4] = usuario.email
                lista[5] = usuario.password
                if (usuario.tipo == 1):
                    print("Ingresa a tipo 1")
                    lista[6] = "Administrador"
                else:
                    lista[6] = "Usuario"
                    print("Ingresa a tipo 2")

                break

    def obtenerListaUsuarios(self):
        print(self.listaGeneralUsuarios)
        return self.listaGeneralUsuarios

    def obtenerListaPerfil(self):
        print(self.listaGeneralPerfil)
        return self.listaGeneralPerfil

    def consultarListaUsuarios(self):
        if(self.validaTamanioLista() == True):
            for i in range(len(self.listaUsuarios)):
                usuario = self.listaUsuarios[i]
                print(usuario)

        return self.listaUsuarios

    def consultarUsuarioPorDocumento(self, documento):
        usuario = None  # Se inicializa en none el usuario
        if(self.validaTamanioLista() == True):
            for user in self.listaUsuarios:
                if(user.documento == documento):
                    usuario = user  # se asigna el elemento encontrado al objeto usuario

        return usuario

    def obtenerCantidadUsuarios(self):
        return len(self.listaUsuarios)

    def validaTamanioLista(self):
        if(len(self.listaUsuarios) > 0):
            return True
        else:
            print("\n<<<< No han registrado estudiantes >>>")
            return False
