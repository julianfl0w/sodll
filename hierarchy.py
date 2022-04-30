import sys
import json

def hierarchize(name, indict):
    newchild = {}
    #newchild["descriptor"] = {}
    #newchild["descriptor"]["name"] = name
    
    if type(indict) == dict:
        for k, v in indict.items():
            newchild[k] = hierarchize(k,v)
            
    elif type(indict) == list:
        i = 0
        for item in indict:
            if type(item) == dict:
                for k, v in item.items():
                    if "name" in k.lower():
                        name = v
            else:
                name = "item_" + str(i)
                i+=1
            newchild[name] = hierarchize(name, item)
    else:
        newchild = indict
        
    return newchild
                    
        
	
def showNode(indict):
    if type(indict) == dict:
        for k, v in indict.items():
            print(str(type(v)) + " : " + k)
    elif type(indict) == list:
        for e in indict:
            print(e)
    else:
        print(indict)

def followPath(indict, path):
    thisdict = indict
    for p in path:
        thisdict = thisdict[p]

    return thisdict

def mainLoop(indict):
    
    
    lastdict = indict
    path = []
    nextStep = ""

    while(nextStep != "quit"):
        thisdict = followPath(indict, path)
        formattedPath = "[\"" + "\"][\"".join(path) + "\"]" 
        print(formattedPath)
        showNode(thisdict)
        nextStep = input ("Where do u wanna go (item, up))? ")
        if nextStep == "up":
            path = path[:-1]
        elif nextStep == "path":
            print(path)
        else:
            if type(thisdict) == dict and nextStep in thisdict.keys():
                path += [nextStep]
            else:
                print("invalid step")


if __name__ == "__main__":
    
    infile = sys.argv[1]
    with open(infile, 'r') as f:
        indict = json.loads(f.read())
        
    h = hierarchize(infile, indict)
    #print(h)
    mainLoop(h)
