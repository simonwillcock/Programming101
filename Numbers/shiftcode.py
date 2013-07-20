# Encode and decode a shift encryption
import string as str
def decode(string):
	decoded_string = ""
	for c in string:
		if c.isalpha() == True:
			decoded_string += chr(ord(c) + 2)
		else:
			decoded_string += c
	return decoded_string

def decode_better(string):
	frm = "abcdefghijklmnopqrstuvwxyz"
	to = "cdefghijqlmnopqrstuvwxyzab"
	trans_table = str.maketrans(frm,to)
	return string.translate(trans_table)

print(decode_better("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))
print(decode_better("http://www.pythonchallenge.com/pc/def/map.html"))