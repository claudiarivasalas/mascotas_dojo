from ninja import Ninja
from dojo_pets import Mascota, Perro, Gato

perrito = Perro("cacho", "perro","galletas", 100, 50 )

gatito = Gato("Cucho", "gato", "Atun", 100, 50 )

Ninja1 = Ninja("Sailor", "Moon","xx", "Galletas", perrito)
Ninja2 = Ninja("Sailor", "Moon","xx", "Galletas", gatito)

Ninja1.alimentar();
print(Ninja1.nombre, Ninja1.apellido, "alimentando a:", perrito.nombre)

Ninja2.alimentar();
print(Ninja2.nombre, Ninja2.apellido, "alimentando a:", gatito.nombre)
