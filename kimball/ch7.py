# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:05:36 2017

@author: Wu
"""

#%%
#7.1
import unicodedata
mystery='\U0001f4a9'
print(unicodedata.name(mystery))

#7.2
pop_bytes=mystery.encode('utf8')
print(pop_bytes)

#7.3
pop_string=pop_bytes.decode('utf8')
print(pop_string==mystery)

#7.4
print('''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.
''' % ('roast beff', 'ham', 'head', 'clam'))

#7.5
letter='''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}'''

#7.6
response={'salutation':'Mr.','name':'Smith','product':'ICBMs','verbed':'malfunctioned',
          'room':'arsenal','animals':'personnel','amount':'quantity','percent':0.01,
          'spokesman':'Donald Trump','job_title':'U.S. President'}

print(letter.format(**response))

#7.7
mammoth='''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

import re
#7.8
print(re.findall('\s(c[a-z]+)[\.,]*?\s',mammoth))

#7.9
print(re.findall('\s(c[a-z]{1,3})[\.,]*?\s',mammoth))

#7.10
print(re.findall('\s([a-zA-Z\']*?r)[\.,]*?\s',mammoth))

#7.11
print(re.findall('\s([^ ]*?[aeiouAEIOU]{3}[a-zA-Z\']*?)[\.,]*?\s',mammoth))

#7.12
import binascii
gif=binascii.unhexlify(bytes('47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b',encoding='ascii'))

#7.13
print(True if re.match(bytes('GIF89a', encoding='ascii'),gif) else False)

#7.14
import struct
#note : the width and height in GIF seems to be stored as litter-endian 2-Byte unsigned integer, which will correctly unpack to (1,1)
print('width if big-endian: {}'.format(struct.unpack('>h',gif[6:8])))
print('height if big-endian {}'.format(struct.unpack('>h',gif[8:10])))
