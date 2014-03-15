#coding=utf-8
import math
import hashlib
import uuid
import time

__author__ = 'Gino'


#Short ID class
class ShortID(object):
     #Base alphabet
    ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = len(ALPHABET)
    MAXLEN = 6

    def encode_id(self, n):

        pad = self.MAXLEN - 1
        n = int(n + pow(self.BASE, pad))

        s = []
        t = int(math.log(n, self.BASE))
        while True:
            bcp = int(pow(self.BASE, t))
            a = int(n / bcp) % self.BASE
            s.append(self.ALPHABET[a:a + 1])
            n = n - (a * bcp)
            t -= 1
            if t < 0:
                break

        return "".join(reversed(s))

    def decode_id(self, n):

        n = "".join(reversed(n))
        s = 0
        l = len(n) - 1
        t = 0
        while True:
            bcpow = int(pow(self.BASE, l - t))
            s = s + self.ALPHABET.index(n[t:t + 1]) * bcpow
            t += 1
            if t > l:
                break

        pad = self.MAXLEN - 1
        s = int(s - pow(self.BASE, pad))

        return int(s)


#Base alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

''' number to short ID, encode and decode
    id_num: number(int) or ID(String)
    pad_up: set long for id
    passkey: set pass key
    encode 24 len number to 14 len id'''


def num_id_gen(id_num, pad_up=False, passkey=None):
    #according to type of id_num,determine that number to id or id to number
    to_num = False if type(id_num) in [int, long] else True
    index = ALPHABET
    #whether using passkey
    if passkey:
        i = list(index)
        passhash = hashlib.sha256(passkey).hexdigest()
        passhash = hashlib.sha512(passkey).hexdigest() if len(passhash) < len(index) else passhash
        p = list(passhash)[0:len(index)]
        index = ''.join(zip(*sorted(zip(p, i)))[1])
    base = len(index)

    #id decode to number
    if to_num:
        id_num = id_num[::-1]
        out = 0
        length = len(id_num) - 1
        t = 0
        while True:
            temp = int(pow(base, length - t))
            out += index.index(id_num[t:t + 1]) * temp
            t += 1
            if t > length:
                break

        # whether have padding bits
        if pad_up:
            pad_up -= 1
            if pad_up > 0:
                out -= int(pow(base, pad_up))

    #number encode to id
    else:
        # whether have padding bits
        if pad_up:
            pad_up -= 1
            if pad_up > 0:
                id_num += int(pow(base, pad_up))

        out = []
        t = int(math.log(id_num, base))
        while True:
            bcp = int(pow(base, t))
            a = int(id_num / bcp) % base
            out.append(index[a:a + 1])
            id_num -= (a * bcp)
            t -= 1
            if t < 0:
                break

        out = ''.join(out[::-1])

    return out


#encode uuid to slug(22 len)
def uuid2slug(uuid_str):
        return uuid.UUID(uuid_str).bytes.encode('base64').rstrip('=\n').replace('/', '_')


#decode slug(22 len) to uuid
def slug2uuid(slug):
    return str(uuid.UUID(bytes=(slug + '==').replace('_', '/').decode('base64')))


#convert uuid to 16 len string
def uuid2str(uuid_str):
    i = 1
    count = 0
    temp_str = uuid.UUID(uuid_str).hex
    # temp_list = [temp_str[i:i+2] for i in range(0, len(temp_str), 2)]
    # for temp in [int(elem.encode("hex")) for elem in uuid.UUID(uuid_str).hex]:
    for temp in temp_str:
        count += 1
        print(int(temp, 16))
        i *= (int(temp, 16) + 1)
    print(count)
    # return i
    return hex(i/10**10 - int(time.time() * 1000))[2:-1]


#core code of shortuuid
alphabet = list("23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
                            "abcdefghijkmnopqrstuvwxyz")
# Define our alphabet.
_alphabet = alphabet
_alpha_len = len(_alphabet)


def encode(uuid):
    """
    Encodes a UUID into a string (LSB first) according to the alphabet
    If leftmost (MSB) bits 0, string might be shorter
    """
    unique_id = uuid.int
    output = ""
    while unique_id:
        unique_id, digit = divmod(unique_id, _alpha_len)
        output += _alphabet[digit]
    return output


def decode(string):
    """
    Decodes a string according to the current alphabet into a UUID
    Raises ValueError when encountering illegal characters
    or too long string
    If string too short, fills leftmost (MSB) bits with 0.
    """
    number = 0
    for char in string[::-1]:
        number = number * _alpha_len + _alphabet.index(char)
    return uuid.UUID(int=number)