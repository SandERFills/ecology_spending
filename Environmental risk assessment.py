inputData={ "Sn":167,
            "Alph":1.1,
            "Se":98,
            "Betta":1,
            "M0":12.8,
            "LvL":4,
            "Vb":4100,
            "A0":180}

def defineAlphaScale(alpha):
    n=1
    i=1
    if alpha <=1:
        return 1
    elif alpha >1:
        while i<int(alpha):           
            n+=0.1
            i+=1
        return float(n)
def defineBettaScale(betta):
    n=1
    i=1
    if betta <=1:
        return 1
    elif betta >1:
        while i<=int(betta):           
            n+=0.1
            i+=1
        return float(n)
def defineclassScale(classLvL):
    if classLvL==1:
        return 2
    elif classLvL == 2:
        return 1.5
    elif classLvL ==3:
        return 1
    elif classLvL ==4:
        return 0.5
print(defineclassScale(inputData["LvL"]))
print(defineAlphaScale(inputData["Alph"]))
print(defineBettaScale(inputData["Betta"]))
def defCalcResult(dataArray):
    """Функция принимает хэш-таблицу формата json"""
    classScale=defineclassScale(dataArray["LvL"])
    alphaScale=defineAlphaScale(dataArray["Alph"])
    bettaScale=defineBettaScale(dataArray["Betta"])
    re=0.02*(alphaScale*dataArray["Sn"]+bettaScale*dataArray["Se"]+classScale*dataArray["M0"]+classScale*dataArray["Vb"]+classScale*dataArray["A0"])
    return re
print(defCalcResult(inputData))