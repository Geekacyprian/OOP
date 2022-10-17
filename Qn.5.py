marks=input('Enter Score::>')
try:
    marks=float(marks)
    if marks<0.0 or marks>1.0:
        print('!!ERROR!!')
    elif marks>=0.9:
        print('A')
    elif marks>=0.8:
        print('B')
    elif marks>=0.7:
        print('C')
    elif marks>=0.6:
        print('D')
    elif marks<0.6:
        print('F')

except:
    print('***Stop***')
