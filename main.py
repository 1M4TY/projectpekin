# Jhairo Sobarzo, Estudiante del Insuco de Valparaiso.
# Matías Gutiérrez, Estudiante del Insuco de Valparaiso.
# Inicio: 19 de agosto de 2021.

# Intro
input("Hola, soy steve")
print()
input("te guiare por este pequeño tutorial")
print()
input("aunque solo soy una IA diseñada para satisfacer tu ganas de jugar videojuegos.")
print()
input("Ahora debes elegir entre una de estas opciones:" )
print()
  print (" (1) Obtener 10 monedas")
  print (" (2) Robar 100 monedas")
  print()
  op_monedas = int(input("¿Que eliges? "))
  print()
  if op_monedas == 1 :
      print ("Aaawww, que lindo quiere que le regale 10 monedas, pero eso no sera tan facil deberas decirme algo pequeño y sencillo")
      res_capital = input ("\n\t¿Cual es la capital de China?\n")
      if str(res_capital) == "pekin":
        print ("\nMuy bien, Usted sabe bastante :) ...")
      else:
        print ("\nUsted no es muy inteligente al parecer :( ...")
  else:
    if op_monedas == 2 :
      print ("Aaaah, eres un ladronsuelo algo astuto, pero  la ves imbecil, para robarle a la persona que te da una opción de continuar con tu vida, aun que es algo ficticio, ¿pero acaso no lo has hecho en la vida real?")
