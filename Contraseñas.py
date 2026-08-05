import random
import string

print("=== GENERADOR DE CONTRASEÑAS ===")

# Le preguntamos al usuario de cuantos caracteres la quiere
longitud = int(input("¿De cuántos caracteres quieres la contraseña? "))

# Aquí están todas las letras, números y símbolos
letras = string.ascii_letters  # abc... ABC...
numeros = string.digits        # 123...
simbolos = string.punctuation  # !@#$...

# Juntamos todo
todo = letras + numeros + simbolos

# Creamos la contraseña escogiendo letras random
contraseña = "".join(random.choice(todo) for i in range(longitud))

print("Tu nueva contraseña segura es:")
print(contraseña)
print("¡No la compartas con nadie! 🤫")
