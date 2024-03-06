# Open ASA files
fc = open("1ASY_C.asa")
clines = fc.readlines()
fc.close()

fp = open("1ASY_P.asa")
plines = fp.readlines()
fp.close()

fr = open("1ASY_R.asa")
rlines = fr.readlines()
fr.close()

cplines = []
crlines = []

for i in clines:
    if len(i[17:20].strip()) == 3:
        cplines.append(i)
    else:
        crlines.append(i)

if len(plines) == len(cplines) and len(rlines) == len(crlines):
    pass
else:
    raise ValueError("Corrupted File")

p_int = []
p_int_atoms = 0
p_int_res = []

p_area = 0

for i in range(len(plines)):
    if int(plines[i][6:11].strip()) == int(cplines[i][6:11].strip()) and plines[i][21] == cplines[i][21]:
        da = round(float(plines[i][54:62].strip()) - float(cplines[i][54:62].strip()), 3)
        if da > 0:
            p_int.append(plines[i][:62] + cplines[i][54:62] + str(da).rjust(8, " "))
            p_int_atoms += 1
            p_area += da
            temp_residue = plines[i][21:28].strip()
            if temp_residue not in p_int_res:
                p_int_res.append(temp_residue)

p_int_resnum = len(p_int_res)

fp_int = open("1asy_P.int", 'w')

for each in p_int:
    fp_int.write(each + '\n')

fp_int.close()

r_int = []
r_int_atoms = 0
r_int_res = []

r_area = 0

for i in range(len(rlines)):
    if int(rlines[i][6:11].strip()) == int(crlines[i][6:11].strip()) and rlines[i][21] == crlines[i][21]:
        da = round(float(rlines[i][54:62].strip()) - float(crlines[i][54:62].strip()), 3)
        if da > 0:
            r_int.append(rlines[i][:62] + crlines[i][54:62] + str(da).rjust(8, " "))
            r_int_atoms += 1
            r_area += da
            temp_residue = rlines[i][21:28].strip()
            if temp_residue not in r_int_res:
                r_int_res.append(temp_residue)

r_int_resnum = len(r_int_res)

fr_int = open("1asy_R.int", 'w')

for each in r_int:
    fr_int.write(each + '\n')

fr_int.close()

print('Category\tProtein\tRNA')
print('-' * 50)
print('Int Area\t' + str(round(p_area, 3)) + '\t' + str(round(r_area, 3)))
print('Int Atoms\t' + str(p_int_atoms) + '\t\t' + str(r_int_atoms))
print('Int Residues\t' + str(p_int_resnum) + '\t\t' + str(r_int_resnum))
