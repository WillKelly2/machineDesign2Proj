

from matplotlib.rcsetup import all_backends


def beamReadin(directory,beamFN):
    f = open(directory,'r') #reads in with type _io.TextIOWrapper which is a not super usable object

    f = f.read() #The read function returns f as a str which has much more usability

    #print(type(f)) #debug

    #print(f) #debug 
    li = list(f.split("\n"))
    equationLines = ["1"]
    for line in li:
        if line.find("[") == 1:
            equationLines.append(line)
    equationLines = equationLines[1:]
    validVfns = ["1"]
    validTfns = ["1"]
    for line in equationLines:
        if line.find("v(x)") !=-1:
            validVfns.append(line)
        elif line.find("dv/dx(x)")!=-1:
            validTfns.append(line)

    validVfns = validVfns[1:]
    validTfns = validTfns[1:]
    rangedeqT = ["1"]
    for line in validTfns:
        currline = list(line.split(" "))
        for i in range(len(currline)):
            try:
                currline.remove("")
            except:
                continue
        newline = [currline[1],currline[3],' '.join(currline[6:])]
        rangedeqT.append(newline)
    rangedeqT = rangedeqT[1:]
    rangedeqV = ["1"]
    for line in validVfns:
        currline = list(line.split(" "))
        for i in range(len(currline)):
            try:
                currline.remove("")
            except:
                continue
        newline = [currline[1],currline[3],' '.join(currline[6:])]
        rangedeqV.append(newline)
    rangedeqV = rangedeqV[1:]
    #f.close()

    out = open('allbeamFNs.py','a')
    out.write('def '+beamFN+'(x):\n')
    out.write('    vy = 0.0\n')
    out.write('    vz = 0.0\n')
    out.write('    Ty = 0.0\n')
    out.write('    Tz = 0.0\n')
    a = int(len(rangedeqV)/2)
    for i in range(int((len(rangedeqV))/2)):
        if i == 0:
            out.write('    if x>='+rangedeqV[i][0]+' and x <='+rangedeqV[i][1]+':\n')
            out.write('        vy = '+rangedeqV[i][2]+'\n')
            out.write('        vz = '+rangedeqV[i+a][2]+'\n')
            out.write('        Ty = '+rangedeqT[i][2]+'\n')
            out.write('        Tz = '+rangedeqT[i+a][2]+'\n')
        else:
            out.write('    elif x>='+rangedeqV[i][0]+' and x <='+rangedeqV[i][1]+':\n')
            out.write('        vy = '+rangedeqV[i][2]+'\n')
            out.write('        vz = '+rangedeqV[i+a][2]+'\n')
            out.write('        Ty = '+rangedeqT[i][2]+'\n')
            out.write('        Tz = '+rangedeqT[i+a][2]+'\n')
    out.write('    else:\n        raise "x bound out of range"\n    return vy,vz,Ty,Tz\n\n')
    out.close()

if __name__ == '__main__':
    s =open('allbeamFNs.py','w')
    s.close()
    beamReadin('./pdfs/singularityFNs1.txt','beam1')
    beamReadin('./pdfs/singularityFNs2.txt','beam2')
    beamReadin('./pdfs/singularityFNs3.txt','beam3')
    beamReadin('./pdfs/singularityFNs4.txt','beam4')
    import allbeamFNs
    print("Beam 1 characteristics at 6in (vy,vz,Ty,Tz) ",allbeamFNs.beam1(6))
    print("Beam 1 characteristics at 15in (vy,vz,Ty,Tz) ",allbeamFNs.beam1(15))
    print("Beam 1 characteristics at 22in (vy,vz,Ty,Tz) ",allbeamFNs.beam1(22))
    #print("Beam 1 characteristics at 27in(vy,vz,Ty,Tz) ",allbeamFNs.beam1(27))
    print("Beam 2 characteristics at 10in (vy,vz,Ty,Tz) ",allbeamFNs.beam2(10))
    print("Beam 3 characteristics at 3in (vy,vz,Ty,Tz) ",allbeamFNs.beam3(3))
    print("Beam 4 characteristics at 3in (vy,vz,Ty,Tz) ",allbeamFNs.beam4(3))
    