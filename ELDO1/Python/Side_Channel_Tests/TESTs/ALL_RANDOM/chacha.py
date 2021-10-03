def rotate(v, c):
    return ((v << c) & 0xffffffff) | v >> (32 - c)

def quarter_round(ciphertext, a, b, c, d):
    ciphertext[a] = (ciphertext[a] + ciphertext[b]) & 0xffffffff
    ciphertext[d] = rotate(ciphertext[d] ^ ciphertext[a], 16)
    ciphertext[c] = (ciphertext[c] + ciphertext[d]) & 0xffffffff
    ciphertext[b] = rotate(ciphertext[b] ^ ciphertext[c], 12)

    ciphertext[a] = (ciphertext[a] + ciphertext[b]) & 0xffffffff
    ciphertext[d] = rotate(ciphertext[d] ^ ciphertext[a], 8)
    ciphertext[c] = (ciphertext[c] + ciphertext[d]) & 0xffffffff
    ciphertext[b] = rotate(ciphertext[b] ^ ciphertext[c], 7)

def oneround(ciphertext):
	#input in order MSB to LSB
	#Even Rounds
	quarter_round(ciphertext, 0, 4,  8, 12)
	quarter_round(ciphertext, 1, 5,  9, 13)
	quarter_round(ciphertext, 2, 6, 10, 14)
	quarter_round(ciphertext, 3, 7, 11, 15)
	#Odd Round
	quarter_round(ciphertext, 0, 5, 10, 15)
	quarter_round(ciphertext, 1, 6, 11, 12)
	quarter_round(ciphertext, 2, 7,  8, 13)
	quarter_round(ciphertext, 3, 4,  9, 14)

def chacha20(ciphertext):
	for i in range(10):
		oneround(ciphertext)

def evenround(ciphertext):
	quarter_round(ciphertext, 0, 4,  8, 12)
	quarter_round(ciphertext, 1, 5,  9, 13)
	quarter_round(ciphertext, 2, 6, 10, 14)
	quarter_round(ciphertext, 3, 7, 11, 15)
