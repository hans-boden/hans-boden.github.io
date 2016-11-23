# python3
"""
    make a function n(), which displays selected locals()
    usage:
        from shownames import *
        learn(locals())
    then call at times_
        n()
"""

lcls = None

def learn(dict):
    global lcls
    lcls = dict
    
def n():
    global lcls
    keys = [k for k in lcls.keys()
            if not k.startswith('_') and not k in ('lcls', 'n', 'ni', 'learn')]
    alvars = ["   {} ==> {}".format(k, lcls[k])
              for k in sorted(keys)]
    print( '\n'.join(alvars))
            
def ni():
    global lcls
    keys = [k for k in lcls.keys()
            if not k.startswith('_') and not k in ('lcls', 'n', 'ni', 'learn')]
    alvars = ["{:10d}    {} ==> {}".format(id(lcls[k]), k, lcls[k])
              for k in sorted(keys)]
    print( '\n'.join(alvars))
            
print("Begin with 'learn(locals()'")
print("Then show names with 'n()' or 'ni()' (to show IDs)")
