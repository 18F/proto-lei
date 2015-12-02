import cherrypy
from GenerateProtoLEI import get_proto_lei
import json
import csv

class ProtoLEI(object):
    def __init__(self):


        self.info = {}

        reader = csv.reader(open('results/protoLEI_DUNS_mapping.csv'))

        self.DUNSs = {}
        self.protoLEIs = {}
        for row in reader:
            protoLEI = row[4]
            DUNS = row[3]

            if protoLEI not in self.DUNSs:
                self.DUNSs[protoLEI] = DUNS

            if DUNS not in self.protoLEIs:
                self.protoLEIs[DUNS] = protoLEI

            name = row[0]
            address = row[1]
            postal_code = row[2]
            self.info[protoLEI] = {"name": name, "address": address, \
                "postal-code": postal_code}

        reader = csv.reader(open('results/protoLEI_preLEI_mapping.csv'))
        
        self.preLEIs = {}
        for row in reader:
            protoLEI = row[4]
            preLEI = row[3]

            if preLEI not in self.preLEIs:
                self.preLEIs[protoLEI] = preLEI

            if preLEI not in self.protoLEIs:
                self.protoLEIs[preLEI] = protoLEI

            name = row[0]
            address = row[1]
            postal_code = row[2]
            self.info[protoLEI] = {"name": name, "address": address, \
                "postal-code": postal_code}

        print "%d entities found." % len(self.info)

    @cherrypy.expose
    def index(self):
        return "I'm Alive! Hit get_id to generate Ids."

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_id(self, entity_name=None, entity_zip=None, duns=None, protoLEI=None, preLEI=None):        
        if protoLEI is None:
            lookup_id = preLEI if preLEI is not None else duns    
            if lookup_id in self.protoLEIs:
                protoLEI = self.protoLEIs[lookup_id]
            else:
                if entity_name is not None and entity_zip is not None:
                    protoLEI = get_proto_lei(entity_name, "", entity_zip)
                else:
                    return {"success1": False}

        result = {}
        result["protoLEI"] = protoLEI

        if protoLEI in self.preLEIs:
            result["preLEI"] = self.preLEIs[protoLEI]

        if protoLEI in self.DUNSs:
            result["DUNS"] = self.DUNSs[protoLEI]
        
        return result
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_info(self, protoLEI):
        if protoLEI in self.info:
            return self.info[protoLEI]
        else:
            return {"success": False}

if __name__ == '__main__':
   cherrypy.quickstart(ProtoLEI())