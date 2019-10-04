###ANALYSIS
#1.) Signal
#--> Plot region, all variables
#--> Signal study (categorization), all variables
#--> HLT trigger
#2.) Backgrounds
#--> Plot Signal region, Plot control region ,all variables
#--> cutflow table
#--> S/b table too

import ROOT

# We prepare an input tree to run on
fileName = 'WWTo2L2Nu_13TeV-powheg-v1.root'
treeName = 'Events'
RDF = ROOT.ROOT.RDataFrame
d = RDF(treeName, fileName)
filtered1 = d.Filter('MHT_pt > 100', 'MHT cut')
filtered2 = filtered1.Filter('MET_pt > 200', 'MET cut')
filtered3 = filtered2.Filter('nLepton>0', 'nlep').Filter('Lepton_pt[0] > 50', 'lepton_pt 0 cut')
print('only newvar cut stats:')
#filtered3.Report()
print('All stats:')
allCutsReport = d.Report()
allCutsReport.Print()
