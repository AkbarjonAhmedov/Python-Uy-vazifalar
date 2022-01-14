# otam ={
#        'ism':'Azamjon',
#        'familiya':'Mamajonov',
#        't_yil':1951,
#        'kasbi':'Rentgenolog'
#        }
# print(f"Otam {otam['familiya'].title()} {otam['ism'].title()}\
#  {otam['t_yil']}-yil tug'ilgan.Tuman shoshilinch tez tibbiy yordam \
# bo'limida {otam['kasbi'].title()} bo'lib ishlagan")

# taom={
#       'otam':'osh',
#       'onam':'osh',
#       'opam':'o\'rama',
#       'akam':'shavla',
#       'men':'monti'     
#       }
# print(f"Otam {taom['otam']}ni, Onam ham {taom['onam']}ni yoqtirardilar.\
#  Men esa {taom['men']}ni juda yoqtirardim")


lugat={
       'integer':'butun son',
       'float':'o\'nlik son',
       'bool':'mantiqiy qiymat',
       'string':'matnli ma\'lumot',
       'dictionary':'lug\'at'
       }
soz=input('Biror soz kiriting: ')
if soz in lugat:
    print(lugat[soz])
else: print("Bunday so'z yo'q")
# print(lugat.get(soz,"Bunday so'z yo'q"))
















