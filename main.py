meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
            "LMAO" : "Es una manera de reirse pero mas fuerte",
            "GHOSTEAR" : "Mirar perfiles (creo)"
            "FOLLOW" : "Seguir a alguien, puede ser en redes como en la vida real"
            }
print("Buenos Días/Tardes/Noches, Bienvenido a el diccionario para Boomers xd")    

for i in range(5):   
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")            
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No se encontró la palabra en la base de datos.")
        
print("Sigue aprendiendo y anímate a poner mas cosas ^^ ")
