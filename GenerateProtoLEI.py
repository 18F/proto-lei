from hashlib import md5
from math import floor

base_36_digits = []
base_36_digits.extend([str(i) for i in range(10)])
#base_36_digits.extend(map(chr, range(97, 123)))
base_36_digits.extend(map(chr, range(65, 91)))

def get_md5(string):
	m = md5()
	m.update(string)
	return long(m.hexdigest(), 16)

def get_checksum(string):
	data = long(
        "".join({"0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9",
                 "A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15", "G":"16", "H":"17", "I":"18",
                 "J":"19", "K":"20", "L":"21", "M":"22", "N":"23", "O":"24", "P":"25", "Q":"26", "R":"27",
                 "S":"28", "T":"29", "U":"30", "V":"31", "W":"32", "X":"33", "Y":"34", "Z":"35"
                 }[c] for c in string)
               )
	return str(98 - ((data * 100) % 97) % 97)

def print_in_base_36(number):
	digit = base_36_digits[(number % 36)]
	next_number = int(floor(number / 36))
	if next_number > 0:
		return print_in_base_36(next_number) + digit
	else:
		return digit

def get_unique_hash(string):
	md5_digest = get_md5(string)
	base_36_str = print_in_base_36(md5_digest)
	return "".join(list(base_36_str)[:12])

def normalize_entity_string(vendor_name, address, zipcode):
	zipcode = ''.join([d for d in zipcode if d.isdigit()][:5])

	normalized_vendor_name = vendor_name.lower() \
								.replace('incorporated', 'inc') \
								.replace('inc.', 'inc') \
								.replace('l.p.', 'lp') \
								.replace(',', ' ')

	normalized_address = address.lower() \
							.replace('street', 'st') \
							.replace('drive', 'dr') \
							.replace('road', 'rd') \
							.replace('rd.', 'rd') \
							.replace(',', ' ')

	normalized_entity_string = normalized_vendor_name + normalized_address + zipcode
	normalized_entity_string = ''.join(normalized_entity_string.split())
	return normalized_entity_string

def get_proto_lei(vendor_name, address, zipcode):
	normalized_entity_string = normalize_entity_string(vendor_name, address, zipcode)
	print "Input data normal form: %s" % normalized_entity_string
	prehash = '000018' + get_unique_hash(normalized_entity_string) 
	checksum = get_checksum(prehash)
	proto_lei = prehash + checksum
	return proto_lei

if __name__ == '__main__':
	proto_lei = get_proto_lei("18F Incorporated", "1800 F Street NW", "06510-12312")
	print "Proto LEI: %s" % proto_lei
