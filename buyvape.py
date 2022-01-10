# fehlend:
# Donnerstag: alm, ma, Sch
# Dienstag: Sc
# Mittwoch: darstellendes Spiel
# Freitag: Spanisch, Pi

def sabber(day,less,ma,teach):
    stra = "Am " , day , " habt ihr in der ", less, ". Stunde " , ma , " bei " , teach
    stra = ''.join(stra)
    return stra
def main(ta,day,teach,less):
    if day == "Montag":
        if teach == "MonP":
            if less == "2":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "ObeI":
            if less == "3" or less == "4" or less == "3 - 4":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "ScJu":
            if less == "5" or less == "6" or less == "5 - 6":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
    if day == "Dienstag":
        if teach == "MesD":
            if less == "1" or less == "2" or less == "1 - 2":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "Sant":
            if less == "3":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "PirL":
            if less == "4":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "KleS" or teach == "FuhL" or teach == "ScJu":
            if less == "5":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
    if day == "Mittwoch":
        if teach == "PirL":
            if less == "1" or less == "2" or less == "1 - 2":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "SerD" or teach == "FuhL":
            if less == "3":
                print("alarm")
                print(entry)
                finall.append(entry)
        if teach == "SteU" or teach == "ScHe" or teach == "BenG" or teach == "VoiJ" or teach == "LorL":
            if less == "4" or less == "5" or less == "4 - 5":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "CosK":
            if less == "6":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "HahS":
            if less == "8":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
    if day == "Donnerstag":
        if teach == "KleS" or teach == "FuhL":
            if less == "0":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "CosK":
            if less == "1" or less == "2" or less == "1 - 2":
                print("alarm")
                print(entry)
                finall.append(entry)
        if teach == "LanJ" or teach == "MutR" or teach == "KoSi" or teach == "PreM":
            if less == "3" or less == "4" or less == "3 - 4":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "HahS" or teach == "FuhL" or teach == "SerD":
            if less == "5" or less == "6" or less == "5 - 6":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "EssH" or teach == "SteK":
            if less == "7" or less == "8" or less == "7 - 8":
                print("alarm")
                print(entry)
                finall.append(entry)
    if day == "Freitag":
        if teach == "KleS" or teach == "FuhL":
            if less == "1" or less == "2" or less == "1 - 2":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "OkaS":
            if less == "3" or less == "4" or less == "3 - 4":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "ElmC":
            finall.append(entry)
            if less == "5" or less == "6" or less == "5 - 6":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
        if teach == "KröK" or teach == "BenG" or teach == "MayA" or teach == "LehA" or teach == "RüsU":
            if less == "7" or less == "8" or less == "7 - 8":
                print("alarm")
                ne = sabber(day,less,ta,teach)
                print(ne)
    try:
        return ne
    except:
        return False
