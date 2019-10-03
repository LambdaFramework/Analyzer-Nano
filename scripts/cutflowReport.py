import ROOT

#def fill_tree(treeName, fileName):
#    tdf = ROOT.ROOT.RDataFrame(10000)
#    tdf.Define("MHT_pt", "(double) tdfentry_")\
#       .Define("MET_pt", "(double) tdfentry_")\
#       .Define("Lepton_pt", "(double) tdfentry_").Snapshot(treeName, fileName)
#       #.Define("events","(int) tdfentry_ * tdfentry_").Snapshot(treeName, fileName)
    
# We prepare an input tree to run on
fileName = 'WWTo2L2Nu_13TeV-powheg-v1.root'
treeName = 'Events'
#fill_tree(treeName, fileName)
# We read the tree from the file and create a RDataFrame, a class that
# allows us to interact with the data contained in the tree.

RDF = ROOT.ROOT.RDataFrame
d = RDF(treeName, fileName)
# ## Define cuts and create the report
# An optional string parameter name can be passed to the Filter method to create a named filter.
# Named filters work as usual, but also keep track of how many entries they accept and reject.
filtered1 = d.Filter('MHT_pt > 100', 'MHT cut')
filtered2 = filtered1.Filter('MET_pt > 200', 'MET cut')
filtered3 = filtered2.Filter('nLepton>0', 'nlep').Filter('Lepton_pt[0] > 50', 'lepton_pt 0 cut')

#augmented1 = filtered2.Define('newvar', 'Lepton_pt[0] / MHT_pt')
#filtered3 = augmented1.Filter('newvar < .5','newvar cut')
# Statistics are retrieved through a call to the Report method:
# when Report is called on the main RDataFrame object, it retrieves stats for
# all named filters declared up to that point. When called on a stored chain
# state (i.e. a chain/graph node), it retrieves stats for all named filters in
# the section of the chain between the main RDataFrame and that node (included).
# Stats are printed in the same order as named filters have been added to the
# graph, and refer to the latest event-loop that has been run using the relevant
# RDataFrame.
print('only newvar cut stats:')
#filtered3.Report()
print('All stats:')
allCutsReport = d.Report()
allCutsReport.Print()
