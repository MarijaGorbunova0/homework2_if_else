from random import randint
# 1 Juku läheb kinno
# nimi = input("mis sinu nimi on?\n").capitalize()
# print("tere,", nimi)
# if nimi == "Juku":
#     print("me laheme kinno")
#     vanus = int(input("kui vana sa oled?"))
#     if vanus < 0 or vanus > 100:
#         pilet = "vale vanus"
#     elif vanus < 6:
#         pilet = "tasuta"
#     elif vanus <= 14:
#         pilet = "lastepilet"
#     elif vanus <= 65:
#         pilet = "täispilet"
#     elif vanus <= 100:
#         pilet = "sooduspilet"
#     print(pilet)
# else:
#     print("ei lähe")
# 2
# nimi1 = input("mis su ninmi on?")
# nimi2 = input("aga mis su nimi on")
# print(nimi1, nimi2, "te olete naabrid")
#3
# SeinaPikkus1 = int(input("kirjuta seina pikkus 1"))
# SeinaPikkus2 = int(input("kirjuta seina pikkus 2"))
# Põrand = SeinaPikkus1*SeinaPikkus2
# print("põranda pindala on", Põrand)
# user = input("Kas te tahate remonti teha?").capitalize()
# if user == "Jah":
#     hind = int(input("kui palju maksab ruutumetr?"))
#     PõrandaHind = hind*Põrand
#     print(PõrandaHind, "on maksab uus põrand")
#4
# Hind = randint(700,1000)
# print(Hind, "teie hind")
# if Hind > 700:
#     Hind = Hind-Hind*0.3
#     print(Hind)
#5
# Temperatuur = int(input("Kirjuta milline sul on temperatuur"))
# if Temperatuur <= 19:
#     otvet = "temperatuur on väiksem kui 19"
#     print(otvet)
# else:
#     print("temperatuur on suurem kui 18")
#6
# user = int(input("Kirjuta sinu pikkus"))
# if user < 160:
#     Pikkus = "sa oled väike"
# elif user > 180:
#     Pikkus = "sa oled Pikk"
# elif 179 > user > 160:
#     Pikkus = "noormalne pikkus"
#     print(Pikkus)
# else:
#     print("siin on mingi probleem")
#7
# userPikkus = int(input("Kirjuta sinu pikkus "))
# User = input("m või n: ")
# if User == "n":
#     if userPikkus < 150:
#         Pikkus = "sa oled väike"
#     elif userPikkus > 175:
#         Pikkus = "sa oled pikk"
#     else:
#         Pikkus = "normaalne pikkus"
# elif User == "m":
#     if userPikkus < 160:
#         Pikkus = "sa oled väike"
#     elif userPikkus > 185:
#         Pikkus = "sa oled pikk"
#     else:
#         Pikkus = "normaalne pikkus"
# else:
#     Pikkus = "vale sugu"
# print(Pikkus)
#8
# tooted = { #это словарь где рядом с продуктами сопоставлены их цены
#     "piim": randint(1, 5),
#     "sai": randint(1, 5),
#     "munad": randint(1, 10),
#     "keefir": randint(1, 6)
# }
#
# korv = [] #так как это корзина куда мы будем складывать продукты, то я решила сделать его списком
# pokupka1 = input("Kas sa tahad osta piima? jah või ei")
# if pokupka1.lower() == "jah":
#     korv.append("piim")
#
# pokupka2 = input("Kas sa tahad osta saia? jah või ei")
# if pokupka2.lower() == "jah":
#     korv.append("sai")
#
# pokupka3 = input("Kas sa tahad osta muned? jah või ei")
# if pokupka3.lower() == "jah":
#     korv.append("munad")
#
# pokupka4 = input("Kas sa tahad osta keefirit? jah või ei")
# if pokupka4.lower() == "jah":
#     korv.append("keefir")
# print("Teie ostukorv sisaldab", korv)

#9
# a = float(input("Sisesta külje pikkus a"))
# b = float(input("Sisesta külje pikkus b"))
# c = float(input("Sisesta külje pikkus c"))
# d = float(input("Sisesta külje pikkus d"))
# if a == b == c == d:
#     print("See on ruut")
# else:
#     print("See ei ole ruut")

#10
# number1 = float(input("Sisesta esimene number"))
# number2 = float(input("Sisesta teine number"))
# znak = input("Vali +, -, *, /")
# if znak == "+":
#     result = number1 + number2
#     print("Tulemus", result)
# elif znak == "-":
#     result = number1 - number2
#     print("Tulemus", result)
# elif znak == "*":
#     result = number1 * number2
#     print("Tulemus", result)
# elif znak == "/":
#     result = number1 / number2
#     print("Tulemus", result)
# else:
#     print("Vale operatsioon")

#11 я не понимаю задание

#12
# toode = float(input("Kirjuta toote hind"))
# if 10 <= toode <= 20:
#     skidkaProtsent = 0.1
# else:
#     skidkaProtsent = 0.2
#
# skidka = toode * skidkaProtsent
# lõpphind = toode - skidka
# print(lõpphind)
#13
# sugu = input("Sisesta oma sugu m voi n").lower()
# if sugu == "m":
#     vanus = int(input("Sisesta oma vanus"))
#     if 16 <= vanus < 18:
#         print("Oled sobiv kandidaat")
#     else:
#         print("Vabandame oled liiga noor või liiga vana")
# else:
#     print("Vabandame sa oled naine")
#14
# inimesi = int(input("Kirjuta inimeste arv"))
# kohtad = int(input("Kirjuta bussi kohtade arv"))
