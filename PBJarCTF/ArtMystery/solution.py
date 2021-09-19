crc_table = None

def make_crc_table():
  global crc_table
  crc_table = [0] * 256
  for n in range(256):
    c = n
    for k in range(8):
        if c & 1:
            c = 0xedb88320 ^ (c >> 1)
        else:
            c = c >> 1
    crc_table[n] = c

make_crc_table()

"""
/* Update a running CRC with the bytes buf[0..len-1]--the CRC
should be initialized to all 1's, and the transmitted value
is the 1's complement of the final running CRC (see the
crc() routine below)). */
"""
def update_crc(crc, buf):
  c = crc
  for byte in buf:
    c = crc_table[int((c ^ byte) & 0xff)] ^ (c >> 8)
  return c

# /* Return the CRC of the bytes buf[0..len-1]. */
def crc(buf):
  return update_crc(0xffffffff, buf) ^ 0xffffffff

# Width is 6, 7
# Height is 10, 11
IHDR = [0x49,0x48,0x44,0x52,0x00,0x00,0x00,0x00,0x00,
                     0x00,0x00,0x00,0x08,0x06,0x00,0x00,0x00]
checksum = 0x60444CB6

import sys
for w in range(1000):
    IHDR[7] += 1
    if IHDR[7] == 256:
        IHDR[7] = 0
        IHDR[6] += 1
    for h in range(1000):
        IHDR[11] += 1
        if IHDR[11] == 256:
            IHDR[11] = 0
            IHDR[10] += 1
        if (hex(crc(IHDR))== hex(checksum)):
            print(IHDR)
            for n in IHDR:
                print(hex(n))
            print(hex(checksum))
            sys.exit()
    IHDR[10] = 0
    IHDR[11] = 0

