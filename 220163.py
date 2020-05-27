a = []
f = (2500,5000,2000,3500,4000,3000,1500)
h=0
while True:
    b = input('**TINZZ Shop******\n\nNIKE ลด 20% [1]\nAdidas ลด 30% [2]\nReebok ลด 70% [3]\nรถเข็น [4]\nออก [5]\n')
    b = b.lower()
    if b == '1':
        c = input('ยี่ห้อสินค้า\n[1]NIKE air max ราคา 2,500\n[2]NIKE air froce ราคา 5,000\n[3]NIKE air ราคา 2,000\n')
        if c == '1':
            a.append('NIKE air max : 2,500 : 20% : 2,000')
            g = f[0]-((f[0]*20)/100) #h += 2000
            h += g
        elif c == '2':
            a.append('NIKE air froce : 5,000 : 20% : 4,000')
            g = f[1]-((f[1]*20)/100) #h += 4000
            h += g
        elif c == '3':
            a.append('NIKE air : 2,000 : 20% : 1,600')
            g = f[2]-((f[2]*20)/100) #h += 1600
            h += g
        print('\nสิ้นค้าเข้าสู่ตะกร้าแล้ว\n')
    elif b == '2':
        c = input('[1]OZWEEGO ราคา 3,500\n[2]Continental 80 ราคา 4,000 \n[3]Gazelle Shoes ราคา 3,000 \n')
        if c == '1':
            a.append('OZWEEGO : 3,500 : 30% : 2,450')
            g = f[3]-((f[3]*20)/100) #h += 2450
            h += g
        elif c == '2':
            a.append('Continental 80 : 4,000 : 30% : 2,800')
            g = f[4]-((f[4]*20)/100) #h += 2800
            h += g
        elif c == '3':
            a.append('Gazelle Shoes : 3,000 : 30% : 2,100')
            g = f[5]-((f[5]*20)/100) #h += 2100
            h += g
        print('\nสิ้นค้าเข้าสู่ตะกร้าแล้ว\n')
    elif b == '3':
        c = input('[1]Interval 96 ราคา 2,500\n[2]LIQUIFECT LS AP ราคา 3,000\n[3]LIQUIFECT LS AD ราคา 1,500\n')
        if c == '1':
            a.append('OZWEEGO : 2,500 : 70% : 750')
            g = f[0]-((f[0]*20)/100) #h += 750
            h += g
        elif c == '2':
            a.append('LIQUIFECT LS AP : 3,000 : 70% : 900')
            g = f[6]-((f[5]*20)/100) #h += 900
            h += g
        elif c == '3':
            a.append('LIQUIFECT LS AD : 1,500 : 70% : 450')
            g = f[2]-((f[6]*20)/100) #h += 450
            h += g
        print('\nสินค้าเข้าสู่รถเข็นแล้ว\n')
    elif b == '4':
        for x in a:
            y = x.split(":")
            print('สินค้า {0[0]:-<15} ราคา {0[1]:-<10} ส่วนลด {0[2]:-<10} จ่ายจริง{0[3]:-<10}'.format(y))
            continue
        print('------------------------------------------------------ราคารวม',h)
        print('\n')
    elif b == '5':
        break