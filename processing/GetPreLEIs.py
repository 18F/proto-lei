import csv
from GenerateProtoLEI import get_proto_lei

reader = csv.reader(open('../data/pleiFull_20151126.csv', 'rb'))

similar_entities = {}
vendors = {}

def has_numbers(inputString):
	return any(char.isdigit() for char in inputString)
i = 0
for row in reader:
#for i in range(100000):
#	row = next(reader)

	if i == 0:
		header = row
	else:
		vendor_name = row[header.index('RegisteredName')]
		address1 = row[header.index('RegisteredAddress1')]
		address2 = row[header.index('RegisteredAddress2')]
		address3 = row[header.index('RegisteredAddress3')]

		for address in [address1, address2, address3]:
			if has_numbers(address):
				break

		zipcode = row[header.index('RegisteredPostalCode')]
		
		preLEI = row[header.index('LegalEntityIdentifier')]
		protoLEI = get_proto_lei(vendor_name, address, zipcode)
		
		key = (protoLEI, preLEI)
		if key not in vendors:
			vendors[key] = (vendor_name, address, zipcode, preLEI, protoLEI)

	i += 1

writer = csv.writer(open('../results/protoLEI_preLEI_mapping.csv', 'wb'))
writer.writerow(('Vendor Name', 'Address', 'Zip Code', 'PreLEI', 'ProtoLEI'))

for key in vendors:
	writer.writerow(vendors[key])

print "Found %d entities." % len(vendors)