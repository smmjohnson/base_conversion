'''
Created by: Sarah Johnson
Updated: 6/11/20

Description:
    A series of functions to convert between binary, decimal, octal, and hexadecimal bases.
'''

def bin_to_dec(bin_num):
    '''
    Parameter:
        bin_num is a number in base 2
    Returns the equivalent of dec_num in base 10
    '''
    num = [str(i) for i in str(bin_num)]
    num.reverse()
    sum = 0
    for i in range(len(num)):
        sum += (int(num[i]) * 2**i)   
    return sum

def dec_to_oct(dec_num):
    '''
    Parameter:
        dec_num is a number in base 10
    Returns the equivalent of dec_num in base 8
    '''
    nums = []
    while True:
        div = dec_num//8
        partial = (dec_num/8)-div #decimal portion of number/8
        rem = partial*8
        nums.append(str(int(rem)))
        if div == 0:
            nums.reverse()
            return ''.join(nums)
        dec_num = div
    
def oct_to_dec(oct_num):
    '''
    Parameter:
        dec_num is a number in base 10
    Returns the equivalent of dec_num in base 8
    '''
    num = [i for i in str(oct_num)]
    num.reverse()
    sum = 0
    for i in range(len(num)):
        sum += (int(num[i])*(8**i))
    return sum
    
    
def dec_to_hex(dec_num):
    '''
    Parameter:
        dec_num is a number in base 10
    Returns the equivalent of dec_num in base 8
    '''
    hex_dict = {'10':'A',
                '11':'B',
                '12':'C',
                '13':'D',
                '14':'E',
                '15':'F'}
                
    hex = []
    while True:            
        div = dec_num//16 
        partial = dec_num/16-div
        rem = partial*16
        hex.append(str(int(rem)))
        if dec_num == 0:
            break
        dec_num = div
    if hex[-1] == '0':
        hex.pop()
    hex.reverse()
    for i in range(len(hex)):
        if int(hex[i]) > 9:
            hex[i] = hex_dict[hex[i]]
    
    return ''.join(hex)

def oct_to_hex(oct_num):
    '''
    Parameter:
        oct_num is a number in base 8
    Returns the equivalent of dec_num in base 16
    '''
    return dec_to_hex(oct_to_dec(oct_num))
    
def hex_to_dec(hex_num):
    '''
    Parameter:
        hex_num is a number in base 16
    Returns the equivalent of dec_num in base 10
    '''
    hex_dict = {'A':'10',
                'B':'11',
                'C':'12',
                'D':'13',
                'E':'14',
                'F':'15'}
    num = [str(i) for i in str(hex_num).upper()]
    num.reverse()
    sum = 0
    for i in range(len(num)):
        if num[i] in hex_dict:
            digit = int(hex_dict[num[i]])
        else:
            digit = int(num[i])
        sum += (digit * (16**i))
    return sum

    
    