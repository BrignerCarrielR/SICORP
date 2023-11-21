class Opciones:
    def __init__(self):
        pass
    def genero(self):
        GENERO= (('M', 'Masculino'),('F', 'Femenino'),)
        return GENERO
    
    def estadoPermiso(self):
        ESTADOPER= (('En Curso', 'En Curso'),('Finalizado', 'Finalizado'),)
        return ESTADOPER
    
    def estado_entidad(self):
        ESTADOEN= (('Vigente', 'Vigente'),('No Vigente', 'No Vigente'),)
        return ESTADOEN

    def sector(self):
        SECTOR= (('Privado', 'Privado'),('Publico', 'Publico'),)
        return SECTOR

    def sistema(self):
        SISTEMA= (('Financiero', 'Financiero'),('No Financiero', 'No Financiero'),)
        return SISTEMA

    def perido(self):
        PERIODO= (('Indefinido', 'Indefinido'),('Definido', 'Definido'),)
        return PERIODO


    