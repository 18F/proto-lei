import csv
from GenerateProtoLEI import get_proto_lei

reader = csv.reader(open('data/FY15_vendors.csv', 'rb'))

similar_entities = {}
vendors = {}

i = 0
for row in reader:
#for i in range(100000):
#	row = next(reader)

	if i == 0:
		header = row
	else:
		vendor_name = row[header.index('vendorname')]
		address = row[header.index('streetaddress')]
		zipcode = row[header.index('zipcode')]
		
		duns = row[header.index('dunsnumber')]
		protoLEI = get_proto_lei(vendor_name, address, zipcode)
		
		key = (protoLEI, duns)
		if key not in vendors:
			vendors[key] = (vendor_name, address, zipcode, duns, protoLEI)

	i += 1

writer = csv.writer(open('results/protoLEI_DUNS_mapping.csv', 'wb'))
writer.writerow(('Vendor Name', 'Address', 'Zip Code', 'DUNS Number', 'ProtoLEI'))

for key in vendors:
	writer.writerow(vendors[key])

duns_dict = {}
proto_lei_dict = {}

protoLEI_duplicates = []
duns_duplicates = []

for key in vendors:
	if key[1] not in duns_dict:
		duns_dict[key[1]] = vendors[key]
	else:
		protoLEI_duplicates.append(duns_dict[key[1]])
		protoLEI_duplicates.append(vendors[key])

	if key[0] not in proto_lei_dict:
		proto_lei_dict[key[0]] = vendors[key]
	else:
		duns_duplicates.append(proto_lei_dict[key[0]])
		duns_duplicates.append(vendors[key])

protoLEI_duplicates.sort(key=lambda tup: tup[3])
duns_duplicates.sort(key=lambda tup: tup[4])


writer = csv.writer(open('results/different_protoLEI_same_duns.csv', 'wb'))
writer.writerow(('Vendor Name', 'Address', 'Zip Code', 'DUNS Number', 'ProtoLEI'))

for row in protoLEI_duplicates:
	writer.writerow(row)

writer = csv.writer(open('results/different_duns_same_lei.csv', 'wb'))
writer.writerow(('Vendor Name', 'Address', 'Zip Code', 'DUNS Number', 'ProtoLEI'))

for row in duns_duplicates:
	writer.writerow(row)


print "%d vendors found." % len(vendors)

