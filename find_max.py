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
        print('sayı: ' + str(sayı))
        if sayı > en_büyük_sayı:
            print('eğer sayı: ' + str(sayı) + ', büyükse, en_büyük_sayı: ' + str(en_büyük_sayı) + ' dan')
            en_büyük_sayı = sayı
            print('en_büyük_sayı: ' + str(en_büyük_sayı))
        else:
            print('eğer sayı: ' + str(sayı) + ', küçükse, en_büyük_sayı: ' + str(en_büyük_sayı) + ' dan, o zaman bir şey yapmadan devam ediyoruz')
    return en_büyük_sayı

sonuç = en_büyüğünü_bul(sayılarım)

print('sayılarından en büyük sayı ' + str(sonuç) + ' tır.')
