def rotate(v, c):
    return ((v << c) & 0xffffffff) | v >> (32 - c)

def quarter_round(x, a, b, c, d):
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 16)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 12)

    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 8)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 7)

def oneround(x):
	#input in order MSB to LSB
	#Even Rounds
	quarter_round(x, 0, 4,  8, 12)
	quarter_round(x, 1, 5,  9, 13)
	quarter_round(x, 2, 6, 10, 14)
	quarter_round(x, 3, 7, 11, 15)
	#Odd Round
	quarter_round(x, 0, 5, 10, 15)
	quarter_round(x, 1, 6, 11, 12)
	quarter_round(x, 2, 7,  8, 13)
	quarter_round(x, 3, 4,  9, 14)
def evenround(x):
	quarter_round(x, 0, 4,  8, 12)
	quarter_round(x, 1, 5,  9, 13)
	quarter_round(x, 2, 6, 10, 14)
	quarter_round(x, 3, 7, 11, 15)
def chacha(x):
	for i in range(10):
		oneround(x)
