d=float(input("Distância em metros: "))
km=d/1000
hm=d/100
dam=d/10
dm=d*10
cm=d*100
mm=d*1000
print("Km: {} \nhm: {} \ndam: {} \ndm: {:.0f} \ncm: {:.0f} \nmm: {:.0f}".format(km,hm,dam,dm,cm,mm))
