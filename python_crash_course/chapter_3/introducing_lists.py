#3.1 Names
names = ["Alejandro","Veguitas","Hector","Damaris","Cony","Angelica","Ariana"]
print(names[0])
print(names[3])
print(names[6])
print(names[-3])

#3.2 Greetings
message = f"\nGracias por estar, {names[1]}"
print(message)
message = f"Gracias por estar, {names[5]}"
print(message)

#3.3 Your Own List
transportes = ["tesla Model Y", "honda navi"]
print(f"\nI would like to own a {transportes[1].upper()}")

#3.4 Guest list
guests = ["Veguitas", "Cony", "Ange", "Hector"]
init_guests = ["Veguitas", "Cony", "Ange", "Hector"]
print(f"\nHola {guests[0]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[1]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[2]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[3]}, te invito a mi cena. Espero puedas asistir")

#3.5 Changing guest list
print(f"\nNo podra asistir {guests[3]}")
guests[3] = "Ariana"
print(f"\nHola {guests[0]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[1]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[2]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[3]}, te invito a mi cena. Espero puedas asistir")

#3.6 More guests
print("\nHola chicos he encontrado una mesa mas grande")
guests.insert(0, "Damariss")
guests.insert(3, "Alejandro")
guests.append("Jose")
print(guests)

print(f"\nHola {guests[0]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[1]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[2]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[3]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[4]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[5]}, te invito a mi cena. Espero puedas asistir")
print(f"Hola {guests[6]}, te invito a mi cena. Espero puedas asistir")

#3.7 Shrinking guest list
print("\nHola chicos, lo siento pero solo podre invitar a dos personas xd")
popped_guests_1 = init_guests.pop()
print(f"Lo siento {popped_guests_1} pero no podras ir a la cena")
popped_guests_2 = init_guests.pop()
print(f"Lo siento {popped_guests_2} pero no podras ir a la cena")

print(f"Hola {init_guests[0]} aún estas invitado a la cena")
print(f"Hola {init_guests[1]} aún estas invitado a la cena")

del init_guests[0]
del init_guests[0]

print(init_guests)

#3.8 Seeing the world
places = ["barcelona", "ohio", "france", "canada", "japon"]
print(f"\n{places}")

print(f"Lugares sorteados alfabeticamente: {sorted(places)}")

print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

#3.9 Dinner guests
print(len(guests))
print(len(init_guests))
