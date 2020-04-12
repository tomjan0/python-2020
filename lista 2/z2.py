""" Program kodujący i dekodujący w base64 """


import sys

SIGNS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def style_bin_len(bin_num, target_len):
    """funcja dodaje 0 do liczby binarnej, aby miała określoną długość"""
    if len(bin_num) != target_len:
        return '0' * (target_len - len(bin_num)) + bin_num
    return bin_num


def dec_to_bin(num, target_len):
    """funckja zamienia liczbe dziesiętną na binarną o zadanej długości"""
    return style_bin_len(bin(num).replace('0b', ''), target_len)


def encode(filename):
    """funkcja kodująca zadany plik do formatu Base64"""
    bit_form = ''
    with open(filename, "r+") as fin:
        content = fin.read()
        for byte in bytes(content, 'ascii'):
            bit_form += str(dec_to_bin(byte, 8))
    diff = len(bit_form) % 6
    if diff != 0:
        bit_form += '0' * (6 - diff)
    encoded = ''
    for i in range(0, len(bit_form), 6):
        sign = bit_form[i:i + 6]
        encoded += SIGNS[int(sign, base=2)]
    return encoded


def decode(filename):
    """funkcja deodująca zadany plik z formatu Base64"""
    decoded = ''
    with open(filename, "r+") as fin:
        content = fin.read()
        bit_form = ''
        for letter in content:
            bit_form += dec_to_bin(SIGNS.index(letter), 6)
        diff = len(bit_form) % 8

        if diff != 0:
            bit_form = bit_form[:-diff]

        for i in range(0, len(bit_form), 8):
            sign = int(bit_form[i:i + 8], base=2)
            decoded += chr(sign)
    return decoded


def main():
    """main"""
    try:
        if sys.argv[1] == '--encode':
            with open('encoded.txt', "w+") as fout:
                fout.write(encode(sys.argv[2]))
            print(encode(sys.argv[2]))
        elif sys.argv[1] == '--decode':
            with open('decoded.txt', "w+") as fout:
                fout.write(decode(sys.argv[2]))
            print(decode(sys.argv[2]))
        else:
            print('zła opcja')
    except IndexError:
        print('brak danych')
    except FileNotFoundError:
        print("Błędna nazwa pliku")


if __name__ == '__main__':
    main()
