versionms = '1.1.0'
try:
    import pip
except:
    print('cài \'pip\' trong python để chạy math system')
    input()
    import sys
    sys.exit()
from datetime import datetime
import platform
import math
import sys
import os
try:
    import PyInstaller.__main__ as pyinstaller
except:
    os.system(f'{sys.executable} -m pip install PyInstaller')
sys.set_int_max_str_digits(1_000_000_000)

oo = 'hệ thông xử lý xong rồi, đang thoát ra...'
o = 'bạn muốn chọn số mấy?:   '
sd = 1

try:
    f = open('a', 'x', encoding='utf-8')
    f.write('     PYTHON CODE NUMBER GAME')
except:
    print('file \'a\' đã tồn tại, bạn có muốn xóa nó không?')
    while True:
        a = input('([Y (có)], [N (không)]):   ').strip().lower()
        if a == 'y':
            print('Chấp nhận thành công!')
            f = open('a', 'w', encoding='utf-8')
            f.write('     PYTHON CODE NUMBER GAME')
            break
        elif a == 'n':
            sys.exit(0)
        else:
            print('Chỉ được nhập \'Y\' hay \'N\'')
for i in range(3):
    f.write('  ')
f.close()

def pevp_xem_mknone():
    global sd
    f = open('a', 'a', encoding='utf-8')
    f.write(f'\n{sd}#')
    sd = sd + 1
    try:
        prv = int(input(o))
        if prv >= 1 and prv < 30:
            print(f'[xem số nguyên tố lớn nhất và nhỏ nhất có {prv} chữ số bắt đầu]')
            rnum = 10**prv-2
            rrnum = 10**(prv-1)
            sal = []
            for smalllarge in range(2):
                if prv == 1:
                    sal = [7, 2]
                    break
                if smalllarge == 1:
                    range_ = [rrnum+1, rnum, 2]
                else:
                    range_ = [rnum-1, rrnum, -2]
                for i in range(range_[0], range_[1], range_[2]):
                    if i % 2 == 0:
                        continue
                    testprime = True
                    for ii in range(3, int(math.sqrt(i))+1, 2):
                        if i % ii == 0:
                            testprime = False
                            break
                    if testprime:
                        sal.append(i)
                        break
            print(f'số nguyên tố lớn nhất có {prv} chữ số là {sal[0]}')
            print(f'số nguyên tố nhỏ nhất có {prv} chữ số là {sal[1]}')
            f.write(f'\n>>>[đang dò số nguyên tố lớn nhất và nhỏ nhất có {prv} chữ số]... kết quả: số nguyên tố lớn nhất là {sal[0]}')
            f.write(f'\n>>>[đang dò số nguyên tố lớn nhất và nhỏ nhất có {prv} chữ số]... kết quả: số nguyên tố nhỏ nhất là {sal[1]}')
        if prv < 0 or prv >= 30:
            print('số quá lớn để làm' if prv >= 30 else 'số quá nhỏ')
    except Exception as e:
        print('Lỗi: ' + str(e))
        f.write('\n(LỖI!)')
    print(oo)
    f.close()

def do_so_nguyen_to_tu_a_den_z_va_dem_mknone():
    global sd
    f = open('a', 'a', encoding='utf-8')
    f.write(f'\n{sd}#')
    sd = sd + 1
    zero2 = 0
    zero3 = 0
    try:
        az = int(input(o))
        if az >= 2:
            print(f'[dò số nguyên tố và số không nguyên tố từ 2 đến {az - 1} bắt đầu]')
            for i in range(2, az):
                num = True
                if i % 2 == 0 and i != 2:
                    num = False
                    print(f"{i} trong {az} không phải là số nguyên tố")
                    zero3 = zero3 + 1
                    continue
                if i == 2:
                    num = False
                    print(f'{i} trong {az} là số nguyên tố')
                if num:
                    for ii in range(3, int(math.sqrt(i) + 1), 2):
                        if i % ii == 0:
                            num = False
                            print(f"{i} trong {az} không phải là số nguyên tố")
                            zero3 = zero3 + 1
                            break
                if num:
                    print(f"{i} trong {az} là số nguyên tố")
                    zero2 = zero2 + 1
            print(f'có {zero2} số nguyên tố từ 2 đến {az - 1}')
            print(f'có {zero3} số không nguyên tố từ 2 đến {az - 1}')
            f.write(f"\n>>>[đang dò số nguyên tố và số không nguyên tố từ 2 đến {az - 1}]... kết quả: có tổng cộng {zero2} số nguyên tố")
            f.write(f"\n>>>[đang dò số nguyên tố và số không nguyên tố từ 2 đến {az - 1}]... kết quả: có tổng cộng {zero3} số không nguyên tố")
        else:
            print('số phải lớn hơn 1! Dưới 2 không phải là số nguyên tố, cũng không phải là số không nguyên tố')
            f.write("\n(number can't be smaller than 2)")
    except Exception as e:
        print('Lỗi: ' + str(e))
        f.write('\n(LỖI!)')
    print(oo)
    f.close()


def xem_a_co_phai_la_so_nguyen_to_ko_mknone():
    global sd
    f = open('a', 'a', encoding='utf-8')
    f.write(f'\n{sd}#')
    sd = sd + 1
    prime = True
    try:
        bz = int(input(o))
        if bz >= 2:
            print(f'[dò xem số {bz} là số nguyên tố hay không bắt đầu]')
            i = 2
            if bz % 2 == 0:
                prime = False
            if prime:
                for i in range(3, int(math.sqrt(bz) + 1), 2):
                    if bz % i == 0:
                        prime = False
                        break
            if bz == 2:
                prime = True
            if prime:
                print(f"{bz} là số nguyên tố")
                f.write(f"\n>>>[đang dò xem số {bz} là số nguyên tố hay không]... kết quả: {bz} là số nguyên tố")
            else:
                print(f"{bz} không phải là số nguyên tố (chia hết cho {i})")
                f.write(f"\n>>>[đang dò xem số {bz} là số nguyên tố hay không]... kết quả: {bz} không phải là số nguyên tố (chia {i} dư {bz % i})")
        else:
            print('số phải lớn hơn 1! Dưới 2 không phải là số nguyên tố, cũng không phải là số không nguyên tố')
            f.write("\n(number can't be smaller than 2)")
    except Exception as e:
        print('Lỗi: ' + str(e))
        f.write('\n(LỖI!)')
    print(oo)
    f.close()


def xem_a_chia_dc_cho_b_ko_va_xem_so_du_mknone():
    global sd
    f = open('a', 'a', encoding='utf-8')
    f.write(f'\n{sd}#')
    sd = sd + 1
    try:
        cz = int(input(o))
        czz = int(input(f'bạn cần lấy số {cz} chia cho số gì?:  '))
        print(f'[dò xem số {cz} có chia được cho số {czz} không bắt đầu]')
        zero = cz % czz
        if zero == 0:
            print(f'{cz} chia hết cho {czz} (chia dư {zero})')
            f.write(f'[đang dò xem số {cz} có chia được cho số {czz} không]... kết quả: {cz} chia hết cho {czz}')
            f.write(f'[đang dò xem số {cz} có chia được cho số {czz} không]... kết quả: {cz} chia cho {czz} dư {zero}')
        else:
            print(f'{cz} không chia hết cho {czz} (chia dư {zero})')
            f.write(f'[đang dò xem số {cz} có chia được cho số {czz} không]... kết quả: {cz} không chia hết cho {czz}')
            f.write(f'[đang dò xem số {cz} có chia được cho số {czz} không]... kết quả: {cz} chia cho {czz} dư {zero}')
    except Exception as e:
        print('Lỗi: ' + str(e))
        f.write('\n(LỖI!)')
    print(oo)
    f.close()


def dem_xem_a_co_bao_nhieu_uoc_so_va_noi_ra_tung_uoc_so_mknone():
    global sd
    f = open('a', 'a', encoding='utf-8')
    f.write(f'\n{sd}#')
    sd = sd + 1
    zero = 0
    try:
        dz = int(input(o))
        print(f'dò xem các số từ 1 đến {dz} có phải là ước số của số {dz} và xem có bao nhiêu ước số của số {dz} bắt đầu')
        for i in range(1, dz + 1):
            if dz % i == 0:
                print(f'{i} là ước số của {dz}')
                f.write(f'\n[đang dò xem các số từ 1 đến {dz} có phải là ước số của số {dz} và xem có bao nhiêu ước số của số {dz}]... kết quả: {i} là ước số của {dz}')
                zero = zero + 1
        print(f'{dz} có {zero} ước số')
        f.write(f'\n[đang dò xem các số từ 1 đến {dz} có phải là ước số của số {dz} và xem có bao nhiêu ước số của số {dz}]... kết quả: có {zero} số là ước số của {dz}')
    except Exception as e:
        print('Lỗi: ' + str(e))
        f.write('\n(LỖI!)')
    print(oo)
    f.close()


def may_tinh_td_congtru_nhanchia_luythua_canbachai_canbacx_don_gian_mknone():
    global sd
    az = ''

    def r(gggg, ggggg):
        if int(ggggg ** (1 / gggg)) == float(ggggg ** (1 / gggg)):
            return int(ggggg ** (1 / gggg))
        else:
            return ggggg ** (1 / gggg)

    f = open('a', 'a', encoding='utf-8')
    f.write(f'\n{sd}#')
    sd = sd + 1
    zero2 = '''cách dùng máy tính dùng máy tính cơ bản:
-các số trong máy tính: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [ví dụ: 1, 34, 5019, 0012]
-các phép toán học: [dấu cộng (+): +, dấu trừ (-): -, dấu nhân (x): x, dấu chia(:, x/y): :, dấu lũy thừa(^, xʸ): ^, dấu căn bậc y cho x(ʸ√x): r(y, x)], [ví dụ: 1 + 2 - -3 + 4, 55 ^ 234 x 2 ^ 1221, 24 : 4, r(33, 330)]
-dấu thập phân: [.], [ví dụ: 1.5, 4554.98707, 1960.00100, 10.5 x 4.599]
-dấu ngoặc đơn: [()], [ví dụ: (1) x 344 x (0 + 111 + 112), r((55 x 55), (34 - 4)), 20 ^ 30  (4 x 1)]
-cách dùng máy tính: [nếu muốn ra đáp án: điền số hoặc phép tính không có dấu bằng, ví dụ: 1 + 3 (kết quả là: 4), 2222 + 4445.4 = (LỖI)]
-những số đặc biệt: [số Pi (π): pp, số Phi - tỉ lệ vàng (φ): ph, số Euler (e): e]
-những lưu ý quan trọng: [phải gõ dấu bằng, vì nếu không thì máy tính sẽ lỗi (ví dụ: 1 + 1 (LỖI), 1 + 1 = (đáp án: 2))]
-trợ giúp, thoát ra: [trợ giúp: h()]
-tóm lại: [chỉ được dùng các ký tự: "123456789+-0,.():^xrpeh= "]'''
    zero3 = '1234567890,.()+-:^xrpeh= '

    def zero4():
        nonlocal az
        if az == 'h()':
            print(zero2)
            f.write('[đang kích hoạt máy tính cơ bản]... kết quả: hướng dẫn ' + zero2)
        az = az.replace('  ', ' ').replace('   ', ' ')
        zero5 = az.replace('x', '*').replace(':', '/').replace('^', '**').replace('=', '')
        pp = math.pi
        ph = (1 + 5 ** 0.5) / 2
        e = math.e
        if '=' in az and '==' not in az:
            zero6 = eval(zero5, {'__builtins__': []}, {'pp': pp, 'ph': ph, 'e': e, 'r': r})
            print(f'{az}{zero6}')
            f.write(f"[đang kích hoạt máy tính cơ bản]... kết quả: đáp án hiện ra của '{az}' là {zero6}")
        else:
            print('ghi \'=\' ở cuối cùng để tính')
    print(f'[kích hoạt máy tính cơ bản bắt đầu]')
    try:
        az = input('Tính: ')
        if all(zero in zero3 for zero in az):
            zero4()
        else:
            print("phép tính của bạn có lẽ không đúng, nhập 'h()' để thử lại sau")
            print(f"[đang kích hoạt máy tính cơ bản]... kết quả: nothing")
    except Exception as e:
        print('Lỗi: ' + str(e))
        f.write('\n(LỖI!)')
    print(oo)
    f.close()


print('math system')
print(f'version {versionms}')
print('Cảm ơn bạn đã dùng sản phẩm của chúng tôi')
print('BẮT ĐẦU HỆ THỐNG')
print(f'Cảm ơn: {os.path.expanduser('~')} đã dùng sản phẩm của tôi')
print(f'(\t<Thông tin>\n{sys.executable}: {sys.version}; {'MacOS' if platform.system() == 'Darwin' else platform.system()} system version {platform.version()}; OS type name: {os.name}; run at {datetime.now().strftime("%Y/%m/%d - %H:%M:%S (%f)")})')
f = open('a', 'w', encoding='utf-8')
f.write(f'\t\t\t<Thông tin>\n{sys.executable}: {sys.version}; {'MacOS' if platform.system() == 'Darwin' else platform.system()} system version {platform.version()}; OS type name: {os.name}; run at {datetime.now().strftime("%Y/%m/%d - %H:%M:%S (%f)")}')
f.close()
for i in range(3):
    print('   ')
for i in range(2):
    print('----------------------------------'*3)
for i in range(1):
    print(" ")

helpcmd = u"""\
các chế độ:
a == xem các số nguyên tố từ 2 đến n - 1
b == kiểm tra số đó có phải số nguyên tố không
c == xem n có bao nhiêu ước số
d == xem a có chia hết cho b không
e == máy tính cơ bản
f == xem số nguyên tố lớn nhất và nhỏ nhất có n chữ số
help == trợ giúp
file == xem lịch sử dùng
cls == xóa hết văn bản của cửa sổ
del == xóa lịch sử file
ver == vesion math system
app == đóng gói file
quit == thoát ra
exit == thoát ra\
"""
cofileakhong = True
if __name__ == '__main__':
    while True:
        try:
            chaycode = input().strip().lower()
            if not cofileakhong:
                with open('a', 'w', encoding='utf-8'):
                    pass
                cofileakhong = True
            if chaycode == 'a':
                do_so_nguyen_to_tu_a_den_z_va_dem_mknone()
            elif chaycode == 'b':
                xem_a_co_phai_la_so_nguyen_to_ko_mknone()
            elif chaycode == 'c':
                dem_xem_a_co_bao_nhieu_uoc_so_va_noi_ra_tung_uoc_so_mknone()
            elif chaycode == 'd':
                xem_a_chia_dc_cho_b_ko_va_xem_so_du_mknone()
            elif chaycode == 'e':
                may_tinh_td_congtru_nhanchia_luythua_canbachai_canbacx_don_gian_mknone()
            elif chaycode == 'f':
                pevp_xem_mknone()
            elif chaycode == 'file':
                f = open('a', 'r', encoding='utf-8')
                ffff = f.read()
                print(f"\"{ffff}\"")
                f.close()
            elif chaycode == 'cls':
                os.system('cls' if os.name == 'nt' else 'clear')
            elif chaycode == 'help':
                print(helpcmd)
            elif chaycode == 'del':
                os.remove('a')
                print(oo)
                cofileakhong = False
            elif chaycode == 'quit' or chaycode == 'exit':
                input('Press Enter To Exit')
                os.remove('a')
                sys.exit(0)
                os._exit(0)
            elif chaycode == 'app':
                if __file__[-3:] == '.py' or __file__[-4:] == '.pyw':
                    pyinstaller.run(['--onefile', __file__])
                    print('nếu file được đống gói bị xóa, hãy kiểm tra nó trong phần mềm antivirus\n(ví dụ: McAFee, ms-defender, bitdefender, avast software,...)')
                else:
                    print('file đã được đóng gói, file extension bị đổi, hoặc file bị nén không có chức năng đóng gói 1 file')
            elif chaycode == 'ver':
                print(versionms)
            elif chaycode == '':
                pass
            else:
                print('ghi \'help\' để trợ giúp')
        except Exception as e:
            if type(e).__name__ == 'SystemExit':
                sys.exit(0)
            print(type(e).__name__ + ': ' + str(e))