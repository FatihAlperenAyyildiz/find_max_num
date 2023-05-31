print('İçlerinden en büyüğünü bulmak istediğiniz sayıları teker teker girin\nve bitirmek istediğinizde herhangi bir harf girin:')

try:
    sayılarım = []
 
    while True:
        sayılarım.append(int(input()))
except:
    print(sayılarım)

def en_büyüğünü_bul(sayılar):
    en_büyük_sayı = float('-inf')
    for sayı in sayılar:
        if sayı > en_büyük_sayı:
            en_büyük_sayı = sayı
    return en_büyük_sayı

sonuç = en_büyüğünü_bul(sayılarım)

print('sayılarından en büyük sayı ' + str(sonuç) + ' tır.')