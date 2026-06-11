class   FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

festival1 = FestivalMusical("Lollapalooza", "Estados Unidos", "Rock")

festival2 = FestivalMusical("Tomorrowland", "Bélgica", "Música electrónica")

print(festival1.nombre)  # Salida: Lollapalooza   

festival1.nombre = "Festival de Música"

print(festival1.nombre)  # Salida: Festival de Música   

print(festival2.pais)   