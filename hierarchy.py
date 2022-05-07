import sys
import json

import logging
logger = logging.getLogger('dtfm')
#logger.setLevel(logging.DEBUG)
#
#handler = logging.StreamHandler(sys.stdout)
#handler.setLevel(logging.DEBUG)
#formatter = logging.Formatter('{{%(filename)s:%(lineno)d %(message)s}')
#handler.setFormatter(formatter)
#logger.addHandler(handler)


def hierarchize(path, name, indict):
    logger.debug("adding " + name)
    path += [name]
    newchild = {}
    newchild["name"] = name
    #newchild["descriptor"] = {}
    #newchild["descriptor"]["name"] = name
    if type(indict) == dict:
        for k, v in indict.items():
            newchild[k] = hierarchize(path, k,v)
            
    elif type(indict) == list:
        i = 0
        for item in indict:
            lname = "item_" + str(i)
            i+=1
            if type(item) == dict:
                for k, v in item.items():
                    if "name" in k.lower():
                        lname = v
                        
            newchild[lname] = hierarchize(path, lname, item)
    else:
        logger.debug(type(indict))
        newchild = indict
        if "VK_SHADER_STAGE_CALLABLE_BIT_KHR" in str(indict):
            logger.debug("SOB")
            #logger.debug(path)
            logger.debug(json.dumps(indict, indent=2))
            die
        
    return newchild

def dumpLevel(indict):
    with open("dump.txt", 'w+') as f:
        if type(indict) == dict:
            f.write(str(indict.keys()))
        elif type(indict) == list:
            
            for i, e in enumerate(indict):
                printstring = str(i) + ": "
                if type(e) == dict:
                    for k in e.keys():
                        if "name" in k:
                            printstring += e[k]
                f.write(printstring + "\n")
            
	
def showNode(indict, limit=10):
    logger.debug("type " + str(type(indict)))
    if type(indict) == dict:
        i = 0
        for k, v in indict.items():
            logger.debug(str(type(v)) + " : " + k)
            if i == limit:
                logger.debug("...")
                break
            i += 1
    elif type(indict) == list:
        logger.debug("length " + str(len(indict)))
        for i, e in enumerate(indict[:limit]):
            printstring = str(i) + ": "
            if type(e) == dict:
                for k in e.keys():
                    if "name" in k:
                        printstring += e[k]
            logger.debug(printstring)
    else:
        logger.debug(indict)

def followPath(indict, path):
    logger.debug("following path " + str(path))
    thisdict = indict
    for p in path:
        if type(thisdict) == dict:
            thisdict = thisdict[p]
        else:
            thisdict = thisdict[int(p)]
            

    return thisdict

def find(path, term, indict, exact=False):
    #logger.debug("searching " + str(path) + " for " + term)
    
    if type(indict) == dict:
        for k, v in indict.items():
            newpath = path + [k]
            potential = find(newpath, term, v)
            if (term ==k) or (term in k and not exact):
                #logger.debug("Found it in k")
                logger.debug(newpath)
                return newpath
            if potential != []:
                return potential
                
    elif type(indict) == list:
        for i, e in enumerate(indict):
            newpath = path + [str(i)]
            potential = find(newpath, term, e)
            if potential != []:
                return potential
            
    elif type(indict) == str:
        if (term ==indict) or (term in indict and not exact):
            logger.debug("Found it")
            return path
            
    #logger.debug("Didnt find it")
    return []

def spill2file(indict):
    with open("spill.txt", 'w+') as f:
        f.write(json.dumps(indict, indent=2))
    
def mainLoop(indict):
    
    
    lastdict = indict
    path = []
    nextStep = ""

    while(nextStep != "quit"):
        thisdict = followPath(indict, path)
        logger.debug("--------------------------------------------")
        formattedPath = "path: [\"" + "\"][\"".join(path) + "\"]" 
        logger.debug(formattedPath)
        showNode(thisdict)
        lastStep = nextStep
        nextStep = input ("Where do u wanna go (item, up, find, spill))? ")
        if nextStep == "":
            nextStep = lastStep
        elif nextStep == "up":
            path = path[:-1]
        elif nextStep.startswith("find"):
            path = find([], nextStep[5:], indict)
        elif nextStep.startswith("finde"):
            path = find([], nextStep[6:], indict, exact=True)
        elif nextStep == "spill":
            logger.debug(json.dumps(thisdict, indent=2))
        elif nextStep == "path":
            logger.debug(path)
        elif nextStep == "dump":
            dumpLevel(thisdict)
        else:
            if type(thisdict) == dict and nextStep in thisdict.keys():
                path += [nextStep]
            elif type(thisdict) == list:
                path += [nextStep]
            else:
                logger.debug("invalid step. partial match:")
                for k in thisdict.keys():
                    if nextStep in k:
                        logger.debug("  " + k)


if __name__ == "__main__":

    logger = logging.getLogger('dtfm')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('{%(filename)s:%(lineno)d %(message)s}')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    infile = sys.argv[1]
    with open(infile, 'r') as f:
        indict = json.loads(f.read())
        
    #h = hierarchize([], infile, indict)
    #
    #with open("adjust.json", 'w+') as f:
    #    f.write(json.dumps(h, indent=2))
    
    #logger.debug(h)
    mainLoop(indict)
