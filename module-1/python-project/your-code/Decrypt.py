class Decrypt_c():
    def __init__(self, mensaje,rand_num,codificacion):
        self.msj   = mensaje
        self.r_num = rand_num
        self.codif = codificacion

    def desencripta_mensaje(self):
        desencriptacion = ''
        for i in self.msj:
            indice = self.codif.find(i)
            n_indice = (indice-self.r_num)%len(self.codif)
            desencriptacion += self.codif[n_indice]
        return desencriptacion
