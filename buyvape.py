# fehlend:
# Donnerstag: alm, ma, Sch
# Dienstag: Sc
# Mittwoch: darstellendes Spiel
# Freitag: Spanisch, Pi
import json


def sabber(day,less,ma,teach,fach,etea,eles,lass):
    if ma == "Vertretung":
        if len(fach) < 4:
            stra = "Am " , day , " habt ihr in der ", less, ". Stunde " , fach , " ", " bei " , etea, " anstatt ", teach
        else:
            stra = "Am " , day , " habt ihr in der ", less, ". Stunde anstatt " , fach , " ", eles, " bei " , etea, " anstatt ", teach
    else:
        stra = "Am " , day , " habt ihr in der ", less, ". Stunde " , fach , " ", ma , " bei " , teach
    stra = ''.join(stra)
    return stra



def main(ta,day,teach,less,fach,etea,eles,lass):
    daylist = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]

    with open("/home/noyavy/dsbapibutonly4me/ml.json", "r") as f:
        data = json.load(f)
        data = data["Data"][dayindex]
    try:
        print(data[less], teach, hex(id(data[less])), hex(id(teach)), hex(id("KröK")))
        if data[less] == teach:
            ne = sabber(day,less,ta,teach,fach,etea,eles,lass)
            print(ne)
    except Exception as e:
        print(e)

    try:
        return ne
    except:
        return False
