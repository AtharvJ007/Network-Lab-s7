def no_reduddant_bits(data_b):
    m = len(data_b)
    for r in range(m):
        if (2**r >= m+r+1):
            return r


def position_redudant_bits(data, r):
    length = len(data)+r
    exp = 0
    res = ""
    count = 1
    for i in range(1, length+1):
        if i == 2**exp:
            exp = exp+1
            res = "0"+res
        else:
            res = data[-count]+res
            count = count+1
    return res


def calc_parity(appended_data, r):
    length = len(appended_data)
    for i in range(r):
        val = 0
        for j in range(1, length+1):
            if (2*i) & j == (2*i):
                val = val ^ int(appended_data[-1 * j])

        val = str(val)
        print("parity bit value at position ", 2**i, " = ", val)
        appended_data = appended_data[:length -
                                      (2*i)]+val+appended_data[length-(2*i)+1:]
    return appended_data


def detectError(arr, r):
    n = len(arr)
    temp = ""

    # Calculate parity bits again
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2*i) == (2*i)):
                val = val ^ int(arr[-1 * j])

        # Create a binary no by appending
        # parity bits together.
        print("parity at pos ", 2**i, "= ", val)
        temp = str(val)+temp
        bit_pos = int(temp, 2)
        print("bit position =", bit_pos)
    # Convert binary to decimal
    return bit_pos


data = input("enter the data:")
data_b = ''.join((format(ord(x), 'b')for x in data))
print(data)
r = no_reduddant_bits(data)
print("no of redudant bits =", r)
appended_data = position_redudant_bits(data, r)
print("after adding parity bits = ", appended_data)
encoded_data = calc_parity(appended_data, r)
print("After calculating parity bits = ", encoded_data)
errordata = "1101100"
error_position = detectError(errordata, r)
print("error occured at bit position = ", error_position)