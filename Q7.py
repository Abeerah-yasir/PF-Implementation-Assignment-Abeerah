def calculate_total_and_average(pf, ic, cg):
    total = pf+ic+cg
    average = total/3
    return total, average
roll_no = 100
pf = 80
ic = 90
cg = 85
total,average = calculate_total_and_average(pf, ic, cg)
print("Roll number:",roll_no)
print("Marks in pf =",pf)
print("Marks in ic =",ic)
print("Marks in cg =",cg)
print("Tottal =",total)
print("Average =",average)