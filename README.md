# Proto LEI

This code generates and tests Proto-LEI, a shim designed for gradual adoption of GLEI from DUNS. 

In addition to serving as a reference implementation, the project also generates files which correlate vendor information (name, address, zip code) with DUNS and pre-LEI codes.

## Setup

To run server, use:
```
>>> python app.py
```

### Examples
http://127.0.0.1:8080/get_id?entity_name=TheDevil&entity_zip=66666
http://127.0.0.1:8080/get_id?entity_name=Hutchin Hill Capital, LP&entity_zip=19808
http://127.0.0.1:8080/get_id?entity_name=DELOITTE CONSULTING LLP&entity_zip=223143456
http://127.0.0.1:8080/get_id?duns=019121586
http://127.0.0.1:8080/get_id?protoLEI=000018E0SWMLN672G495
http://127.0.0.1:8080/get_id?preLEI=004L5FPTUREIWK9T2N63
http://127.0.0.1:8080/get_id?entity_name=NBA Properties, Inc.&entity_zip=10022-5910
http://127.0.0.1:8080/get_info?protoLEI=00001813U30B8X05CW53