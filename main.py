#
# class Talaba:
#     def __init__(self,ism,familiya, tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#     def getinfo(self):
#         return f"{self.ism} {self.familiya}  "
#     def getname(self):
#         return self.ism
#
#     def tanishtir(self):
#         return f"Ismin {self.ism} {self.familiya} tug'ilgan yilim {self.tyil}"
#
# talaba1=Talaba("olim","olimov", 2000)
# talaba2=Talaba("husan","hasanov",2007)
# #
# #
# #
# # print(talaba2.getname())
#
# class Fan():
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.talabalarsoni=0
#         self.talabalar=[]
#
#
#     def getstudents(self):
#         return self.talabalarsoni
#     def addstudent(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalarsoni+=1
#
#
#
#
#
# matem=Fan("oliy matematika")
# print(matem.talabalarsoni)
# print(talaba1.ism)
# matem.addstudent(talaba1)
# print(matem.talabalarsoni)
# matem.addstudent(talaba2)
# print(matem.talabalarsoni)
# print(matem.nomi)
# print(matem.talabalar)
# #
# from faker import Faker
# fake=Faker()
# print(fake.name())

import os
print(os.listdir())


