def rp_calculator(grades):
    result = 0
    l = []
    for x in grades.values():
        l.append(x)

    for i in range(2):
        if l[i] == "A(H1)": result += 10
        elif l[i] == "B(H1)": result += 8.75
        elif l[i] == "C(H1)": result += 7.5
        elif l[i] == "D(H1)": result += 6.75
        elif l[i] == "E(H1)": result += 5
        elif l[i] == "S(H1)": result += 2.5

    if "H1" in l[5]:
        for i in range(2, 6):
            if l[i] == "A" or l[i] == "A(H2)": result += 20
            elif l[i] == "B" or l[i] == "B(H2)": result += 17.5
            elif l[i] == "C" or l[i] == "C(H2)": result += 15
            elif l[i] == "D" or l[i] == "D(H2)": result += 12.5
            elif l[i] == "E" or l[i] == "E(H2)": result += 10
            elif l[i] == "S" or l[i] == "S(H2)": result += 5
            elif l[i] == "A(H1)": result += 10
            elif l[i] == "B(H1)": result += 8.75
            elif l[i] == "C(H1)": result += 7.5
            elif l[i] == "D(H1)": result += 6.75
            elif l[i] == "E(H1)": result += 5
            elif l[i] == "S(H1)": result += 2.5
    else:

        h1 = l[2]
        pos = 2
        for i in range(3, 5):
            if l[i] <= h1:
                pos = i
                h1 = l[i]
        if l[5][0] < h1:
            pos = 5



        for i in range(2, 6):
            if i == pos:
                if l[i] == "A" or l[i] == "A(H2)": result +=10
                elif l[i] == "B" or l[i] == "B(H2)": result += 8.75
                elif l[i] == "C" or l[i] == "C(H2)": result += 7.5
                elif l[i] == "D" or l[i] == "D(H2)": result += 6.75
                elif l[i] == "E" or l[i] == "E(H2)": result += 5
                elif l[i] == "S" or l[i] == "S(H2)": result += 2.5
            else:
                if l[i] == "A" or l[i] == "A(H2)": result += 20
                elif l[i] == "B" or l[i] == "B(H2)": result += 17.5
                elif l[i] == "C" or l[i] == "C(H2)": result += 15
                elif l[i] == "D" or l[i] == "D(H2)": result += 12.5
                elif l[i] == "E" or l[i] == "E(H2)": result += 10
                elif l[i] == "S" or l[i] == "S(H2)": result += 5

    return result
