import readchar

while True:
    key = readchar.readkey()


    if key == "\x00\x48": 
        print("Saliendo...")
        break
    else:
        print(f"Tecla presionada: {key}")