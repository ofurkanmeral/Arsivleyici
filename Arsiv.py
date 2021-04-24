import shutil
import os
import sys
liste=list()
konum=os.listdir(os.getcwd())


for iter3 in konum:
    x=iter3.split("_")
    liste.append(x[0])
liste=list(set(liste))
for iter2 in liste:
    print(iter2)


#pathim="C:\\Users\Onur Furkan Meral\Desktop"
for iter in liste:
    try:
        #yol=os.path.join(pathim,iter)
        os.mkdir(iter)

    except:
        print(iter +"adlı klasör oluşturulamadı")


yeni=os.listdir(os.getcwd())
"""
for iter5 in range(0,10):
    dosyalar=os.listdir(os.getcwd())
    klasor=os.listdir(os.getcwd())
    if(klasor in dosyalar):
        print("calıstı")
        shutil.move(dosyalar[iter5], klasor[iter5])#ilki dosyalar ikincisi taşınacak yer
    
"""
dosyalar=os.listdir(os.getcwd())
klasor=os.listdir(os.getcwd())
for iter5 in liste:
    for iter6 in yeni:
        try:
            if(iter5 in iter6):
                print("calıstı")
                shutil.move(iter6, iter5)#ilki dosyalar ikincisi taşınacak yer
        except:
            print(iter6+" isimli dosya taşınamadı")
            pass
