# # class Ota:
# #     def __init__(self, fullname):
# #         self.fullname = fullname
# #         self.__money = 0
# #
# #     def pul_solish(self):
# #         pass
# #
# #     def info(self):
# #         print(f"Egasi: {self.fullname}")
# #         print(f"Puli: {self.__money}")
# #
# # o1 = Ota("Aliyev VAli")
# # o1.info()


# # #1-misol
# # class Kitob:
# #     def __init__(self, nomi, narxi):
# #         self.nomi = nomi
# #         self.narxi = narxi
# #         self.__narxi = 0
# #
# #     def chegirma(self, toza_narx):
# #         self.__narxi -= toza_narx
# #
# #
# #     def info(self):
# #         print(f"Nomi: {self.nomi}")
# #         print(f"Narxi: {self.__narxi}")
# #
# # k1 = Kitob("O'tkan kunlar", "300" )
# # k1.info()


# # #2-misil
# # class Talaba:
# #     def __init__(self, fullname, ball):
# #         self.fullname = fullname
# #         self.ball = ball
# #         self.__ball = 0
# #
# #     def ball_qosh(self, qiymat):
# #         self.__ball += qiymat
# #
# #     def info(self):
# #         print(f"ismi: {self.fullname}")
# #         print(f"bali: {self.ball}")
# #
# # t1 = Talaba("Dilnura", "100")
# # t1.info()


# # #3-misol
# # class BamkHisob:
# #     def __init__(self, egasi, balans):
# #         self.egasi = egasi
# #         self.balans = balans
# #         self.__balans = 0
# #
# #     def pul_qosh(self, summa):
# #         self.__balans += summa
# #
# #     def pul_yech(self, summa):
# #         self.__balans -= summa
# #
# #     def info(self):
# #         print(f"egasi: {self.egasi}")
# #         print(f"Balansi: {self.balans}")
# #
# # b1 = BamkHisob("Sevinch", "200")
# # b1.info()


# # #4-misol
# # class Telefon:
# #     def __init__(self, model, batareya):
# #         self.model = model
# #         self.batareya = batareya
# #         self.__batareya = 0
# #
# #     def zaryad_qil(self, foiz):
# #         self.__batareya += foiz
# #
# #     def foydalan(self, foiz):
# #         self.__batareya -= foiz
# #
# #     def info(self):
# #         print(f"Modeli: {self.model}")
# #         print(f"Batargiyasi: {self.__batareya}")
# #
# # t1 = Telefon("iphone", "80")
# # t1.info()

# # #5-misol
# # class Avtomobil:
# #     def __init__(self, model, tezlik):
# #         self.model = model
# #         self.tezlik = tezlik
# #         self.__tezlik = 0
# #
# #     def tezlashtir(self, qiymat):
# #         self.__tezlik += qiymat
# #
# #     def sekinlashtir(self, qiymat):
# #         self.__tezlik -= qiymat
# #
# #     def info(self):
# #         print(f"Modeli: {self.model}")
# #         print(f"Tezligi: {self.__tezlik}")
# #
# # a1 = Avtomobil("Malibu", "120")
# # a1.info()


# #6-misol
# class Ishchi:
#     def __init__(self, fullname, oylik):
#         self.fullname = fullname
#         self.oylik = oylik
#         self.__oylik = 0

#     def oshirish(self, qiymat):
#         self.__oylik += qiymat

#     def kamaytir(self, qiymat):
#         self.__oylik -= qiymat

#     def info(self):
#         print(f"ismi: {self.fullname}")
#         print(f"oyligi: {self.__oylik}")

# i1 = Ishchi("Aziza", "2mln")
# i1.info()

# # #7-misol
# # class Dokon:
# #     def __init__(self, nomi, kassa):
# #         self.nomi = nomi
# #         self.kassa = kassa
# #         self.__kassa = 0
# #
# #     def sotuv(self, summa):
# #         self.__kassa += summa
# #
# #     def harajat(self, summa):
# #         self.__kassa -= summa
# #
# #     def info(self):
# #         print(f"nomi: {self.nomi}")
# #         print(f"kassa: {self.__kassa}")
# #
# # d1 = Dokon("Supermarket", "12 000 000")
# # d1.info()

# # # 8-misol
# # class Bak:
# #     def __init__(self, sigim, yoqilgi):
# #         self.sigim = sigim
# #         self.yoqilgi = yoqilgi
# #
# #     def quyish(self, litr):
# #         self.yoqilgi += litr
# #
# #     def sarflash(self, litr):
# #         self.yoqilgi -= litr
# #
# #     def info(self):
# #         print(self.sigim, self.yoqilgi)
# #
# # b1 = Bak(120, 230)
# # b1.info()
# #
# #
# # # 9-misol
# # class Kurs:
# #     def __init__(self, nomi, student_soni):
# #         self.nomi = nomi
# #         self.student_soni = student_soni
# #
# #     def qoshish(self):
# #         self.student_soni += 1
# #
# #     def ayirish(self):
# #         self.student_soni -= 1
# #
# #     def info(self):
# #         print(self.nomi, self.student_soni)
# #
# #
# # # 10-misol
# # class Stadion:
# #     def __init__(self, nomi, muxlislar):
# #
