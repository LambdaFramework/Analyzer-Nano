#!/bin/python

from PhysicsTools.NanoAODTools.postprocessing.analysis.variables import branches_all
import sys

var_template={}
variable={}
for ibranch in branches_all:
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()] = {}
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["title"] = ibranch.titleX() 
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["titleY"] = ibranch.titleY()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["nbins"] = ibranch.nbins()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["min"] = ibranch.mins()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["max"] = ibranch.maxs()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["log"] = ibranch.log()
    pass

#print varDict['RecoLL_phi[N]']

for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(0, 4):
            ni = n.replace('[N]', "[%d]" % i)
            variable[ni] = v.copy()
            variable[ni]['titleX'] = variable[ni]['titleX'].replace('[N]', "%d" % i)
    else:
        variable[n] = v

for n, v in variable.iteritems():
    print n
print "FOR variables definition, PLEASE REFER TO --> PhysicsTools.NanoAODTools.postprocessing.analysis.variables <-- "

## if you wanna write out variable to a files, use this
#import json

#with open('variable.txt', 'w') as json_file:
#    json.dump(variable, json_file)
