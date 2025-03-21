import random
 # Preguntas para el juego
questions = [
     "¿Qué función se usa para obtener la longitud de una cadena en Python?",
     "¿Cuál de las siguientes opciones es un número entero en Python?",
     "¿Cómo se solicita entrada del usuario en Python?",
     "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
     "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
 # Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
     ("size()", "len()", "length()", "count()"),
     ("3.14", "'42'", "10", "True"),
     ("input()", "scan()", "read()", "ask()"),
     (
         "// Esto es un comentario",
         "/* Esto es un comentario */",
         "-- Esto es un comentario",
         "# Esto es un comentario",
     ),
     ("=", "==", "!=", "==="),
     ]
 # Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
score = 0
 # El usuario deberá contestar 3 preguntas
 
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
for preg, opcion, rta in questions_to_ask:     
     # Se muestra la pregunta y las respuestas posibles
     print(preg)
     for i, answer in enumerate(opcion):    
         print(f"{i + 1}. {answer}")
     # El usuario tiene 2 intentos para responder correctamente
     for intento in range(2):
         user_answer = input("RESPUESTA: ")
         #asegurar nro ingresado
         if(user_answer in ["1","2","3","4"]):
            user_answer = int(user_answer)-1 
         else:
             print("ingrese un nro entre 1 y 4")
             exit(1)      
     # Se verifica si la respuesta es correcta
         if user_answer == rta:
             print("¡Correcto!")
             score+=1
             break
     else:
     # Si el usuario no responde correctamente después de 2 intentos,
     # se muestra la respuesta correcta
         print("Incorrecto. La respuesta correcta es:")
         print(opcion[rta])
         score-=0.5
 
#tu puntaje final es:
print(f"Tu puntaje es: {score}")
print("")