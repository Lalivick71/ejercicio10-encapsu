#crear una clase Atleta, que tenga su nombre, apellido, altura, peso y teléfono. Decidir que atributos deben ser públicos y cuales privados. Crear los métodos get y set que crea necesarios.

clase atleta:
  def__init__(self,nombre,apellido,altura,peso,telefono):
  self.nombre=nombre
  self.apellido=apellido
  self.altura=altura
  self._peso=peso
  self._telefono=telefono
def get_altura(self):
    return self._altura
def get_peso(self):
    return self._peso
def get_telefono(self):
    return self._telefono
def set_altura(self,altura):
    self._altura=altura 
def set_peso(self, peso)
    self._peso=peso
def set_telefono(self,telefono):
    self._telefono=telefono
def __str__(self):
    return atleta:" + self.nombre +"" + self.apellido 
atleta1 =atleta("leon","sanchez",1,80, 50, 42198870)
print (atleta1)
print(atleta1.nombre)
