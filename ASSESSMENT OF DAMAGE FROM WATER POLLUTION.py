V=260
KWATER=1.7
KU=1
variant={
    "Nitroamon":0.79,
    "Fenol":0.094,
    "oil product":24,
    "PAV":0.102,
    "Fosfat":0.026,
    "Expsubstances":17.3,
    "BPK":40.4,
    "Iron":1.62,
    "Coper":0.055}
PDK={"Nitroamon":1,
    "Fenol":0.0018,
    "oil product":0.05,
    "PAV":0.09,
    "Fosfat":0.29,
    "Expsubstances":6.67,
    "BPK":3.33,
    "Iron":1,
    "Coper":0.0018}
HBLI={"Nitroamon":6875.8,
    "Fenol":2749700,
    "oil product":54994,
    "PAV":5499.4,
    "Fosfat":13751.6,
    "Expsubstances":3658,
    "BPK":905.2,
    "Iron":27497,
    "Coper":2749700}
def mi(ci):
    mi=[]
    for key in ci:
        mi.append(ci[key]*V*0.001)
    return mi
def pn(paynormshedding,mnormi):
    pn=[]
    for i in range(len(mnormi)):
        pn.append(paynormshedding[i]*mnormi[i]*0.001) 
    return pn
def mnormi(pdk):
    mni=[]
    for key in pdk:
        mni.append(pdk[key]*V*0.001)
    return mni
def overnormsehdding(pnormshedding,mi,mnormi):
    pch=[]
    mibig=0
    for i in range(len(mi)):
        if mi[i]>mnormi[i]:
            pch.append(5*pnormshedding[i]*(mi[i]-mnormi[i])*0.001)
        else:
            mibig=mnormi[i]
            pch.append(5*pnormshedding[i]*(mibig-mnormi[i])*0.001)
    return pch
def paynormshedding(nbi,kwater,ku):
    pyni=[]
    for key in nbi:
        pyni.append(nbi[key]*kwater*ku)
    return pyni

print("Мi=",mi(variant))
print("Пуднi=",paynormshedding(HBLI,KWATER,KU))
print("mнi=",mnormi(PDK))
print("Пн=",pn(paynormshedding(HBLI,KWATER,KU),mnormi(PDK)))
print("Выброс сверхнормы",overnormsehdding(paynormshedding(HBLI,KWATER,KU),mi(variant),mnormi(PDK)))