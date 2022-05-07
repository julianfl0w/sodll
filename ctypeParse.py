from sodll import *
import json

goldenList = {
        "uint8_t [16]" : "c_ubyte *16"
        }

with open("alias2real.json", "r") as f:
    alias2name = json.loads(f.read())

for k, v in goldenList.items():
    t = getCtypeFromString(k, alias2name)
    if t != v:
        print("FAIL: got " + t + ", expected " + v)
    else:
        print(k + " success")
