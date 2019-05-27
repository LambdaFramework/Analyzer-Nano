#!/bin/python

from PhysicsTools.NanoAODTools.postprocessing.analysis.variables import branches_genall, branches_ana
import sys

var_template={}
variable={}
for ibranch in branches_ana: #branches_genall:
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()] = {}
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["title"] = ibranch.titleX() 
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["titleY"] = ibranch.titleY()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["nbins"] = ibranch.nbins()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["min"] = ibranch.mins()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["max"] = ibranch.maxs()
    var_template["%s[N]"%ibranch.name() if ibranch.dimen()==1 else "%s"%ibranch.name()]["log"] = ibranch.log()
    pass

#### GENProducer ####
#for v in ["nGenEle", "nGenMu", "nGenHad", "nGenJet", "nGenW", "nGenfsW", "nGenZ", "nGenH", "nGenfsH", "nGenWstar", "nGenRad", "nGenLL", "nGenL2JJ", "nRecoEle", "nRecoMu", "RecoMu_fromW12", "nRecoJet", "nRecoLL", "nRecoL2JJ" ]:
#    var_template[v] = {}
#    var_template[v]["title"] = v
#    var_template[v]["titleY"] = "Events/ XXX"
#    var_template[v]["nbins"] = 6
#    var_template[v]["min"] = -0.5
#    var_template[v]["max"] = 5.5
#    var_template[v]["log"] = True
    

for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(0, 3):
            ni = n.replace('[N]', "[%d]" % i)
            variable[ni] = v.copy()
            variable[ni]['title'] = variable[ni]['title'].replace('[N]', "%d" % i)
            variable[ni]['titleY'] = variable[ni]['titleY'].replace('XXX', "%s" % ( (variable[ni]['max'] - variable[ni]['min'])/variable[ni]['nbins'] ) )
    else:
        variable[n] = v
        variable[n]['titleY'] = variable[n]['titleY'].replace('XXX', "%s" % ( (variable[n]['max'] - variable[n]['min'])/variable[n]['nbins'] ) )

#for n, v in variable.iteritems():
#    print variable[n]['titleY']
#print "FOR variables definition, PLEASE REFER TO --> PhysicsTools.NanoAODTools.postprocessing.analysis.variables <-- "

## if you wanna write out variable to a files, use this
#import json

#with open('variable.txt', 'w') as json_file:
#    json.dump(variable, json_file)
