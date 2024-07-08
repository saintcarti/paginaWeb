from .models import Camara

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar(self, camara):
        if camara.stock > -1:    
            if str(camara.idCamara) not in self.carrito.keys():
            
                self.carrito[str(camara.idCamara)] = {
                'idCamara': camara.idCamara,
                'nombreCamara': camara.nombreCamara,
                'precio': camara.precio,
                'cantidad': 1,
                'imagen': camara.imagen.url,
                'total': camara.precio,
            }
                camara.stock -= 1
                camara.save()
            else:
                for key, value in self.carrito.items():
                    if key == str(camara.idCamara):
                        if camara.stock > 0:
                            value["cantidad"] = value["cantidad"] + 1
                            value["precio"] = camara.precio
                            value["total"] = camara.precio * value["cantidad"]
                            camara.stock -= 1
                        break
            camara.save()
            self.guardar()

    def guardar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, camara):
        id = str(camara.idCamara)
        if id in self.carrito:
            camara.stock += self.carrito[id]["cantidad"]
            camara.save()
            del self.carrito[id]
            self.guardar()

    def restar(self, camara):
        camara.idCamara_str = str(camara.idCamara)
        for key, value in self.carrito.items():
            if key == camara.idCamara_str:
                    value["cantidad"] -= 1
                    value["total"] = int(value["total"]) - camara.precio
                    camara.stock += 1
                    camara.save()
                    if value["cantidad"]<1:
                        self.eliminar(camara)
                    break
        self.guardar()

    def limpiar(self):
        for key, value in self.carrito.items():
            camara = Camara.objects.get(idCamara=int(key))
            camara.stock += value["cantidad"]
            camara.save()
        self.session["carrito"] = {}
        self.session.modified = True


    def vaciar(self):
        for key , value in self.carrito.items():
            print("Entra a vaciar")
            camara = Camara.objects.get(idCamara=int(key))
            print(camara.stock) 
            if camara.stock <=0:
                camara.stock = 1
            camara.save()
        self.session["carrito"] = {}
        self.session.modified = True

