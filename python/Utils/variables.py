
variable = {}

var_template = {
    ## GLOBAL
    "event": {
      "title" : "event number",
      "nbins" : 10000000,
      "min" : 0,
      "max" : 1.e7,
      "log" : False,
    },
    "luminosityBlock": {
      "title" : "lumisection number",
      "nbins" : 2000,
      "min" : 0,
      "max" : 2000,
      "log" : False,
    },
    "run": {
      "title" : "run number",
      "nbins" : 7000,
      "min" : 254000,
      "max" : 261000,
      "log" : False,
    },
    "PV_npvs": {
      "title" : "number of reconstructed Primary Vertices",
      "nbins" : 100,
      "min" : -0.5,
      "max" : 99.5,
      "log" : True,
    },
    
    ##Flags
    "isOSmumu": {
        "title" : "isOSmumu",
        "nbins" : 2,
        "min" : -0.5,
        "max" : 1.5,
        "log" : True,
    },
    "isOSee": {
        "title" : "isOSee",
        "nbins" : 2,
        "min" : -0.5,
        "max" : 1.5,
        "log" : True,
    },
    "isOSemu": {
        "title" : "isOSemu",
        "nbins" : 2,
        "min" : -0.5,
        "max" : 1.5,
        "log" : True,
    },
    "isSSmumu": {
        "title" : "isSSmumu",
        "nbins" : 2,
        "min" : -0.5,
        "max" : 1.5,
        "log" : True,
    },
    "isSSee": {
        "title" : "isSSee",
        "nbins" : 2,
        "min" : -0.5,
        "max" : 1.5,
        "log" : True,
    },
    
    ## Tau
    "nTaulep" : {
        "title" : "number of Tau leptons",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "TauPt[N]":{
        "title" : "Tau Lepton [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },

    "TauEta[N]": {
        "title" : "Tau [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    "TauPhi[N]" : {
        "title" : "Tau [N] #phi",
        "nbins" : 10,
        "min" : 0.,
        "max" : 3.5,
        "log" : True,
    },
    "TauMass[N]" : {
        "title" : "Tau [N] mass (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 150,
        "log" : True,
    },
    
    ## Photon
    "nPho" : {
        "title" : "number of photons",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "PhoPt[N]":{
        "title" : "Photon [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "PhoEta[N]": {
        "title" : "Photon [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    "PhoPhi[N]" : {
        "title" : "Photon [N] #phi",
        "nbins" : 10,
        "min" : 0.,
        "max" : 3.5,
        "log" : True,
    },
    "PhoMass[N]" : {
        "title" : "Photon [N] mass (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 150,
        "log" : True,
    },

    ##Lepton
    "nLepton" : {
        "title" : "number of leptons",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "LepPt[N]":{
        "title" : "Lepton [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "LepEta[N]": {
        "title" : "Lepton [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    "LepPhi[N]" : {
        "title" : "Lepton [N] #phi",
        "nbins" : 10,
        "min" : 0.,
        "max" : 3.5,
        "log" : True,
    },
    "LepMass[N]" : {
        "title" : "Lepton [N] mass (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 150,
        "log" : True,
    },
    "LepIso03[N]" : {
        "title" : "Lepton [N] PFIso_{03}",
        "nbins" : 50,
        "min" : 0,
        "max" : 0.25,
        "log" : True,
    },
    "LepIso04[N]" : {
        "title" : "Lepton [N] PFIso_{04}",
        "nbins" : 50,
        "min" : 0,
        "max" : 0.25,
        "log" : True,
    },
    "LepSign[N]" : {
	"title" : "Lepton [N] Sign",
        "nbins" : 32,
        "min" : -16.5,
        "max" : 15.5,
        "log" : True,
    },
    "LepMediumId[N]": {
        "title" : "Muon [N] MediumId",
        "nbins" : 2,
        "min" : -0.5,
        "max" : 1.5,
        "log" : True,
    },
     "LepCutBased[N]": {
        "title" : "Electron [N] cutBased",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "LepMindRJet[N]": {
        "title" : "#Delta R(Lepton[N],jet_nearest)",
        "nbins" : 50,
        "min" : 0,
        "max" : 2,
        "log" : True,
    },
    ## HT
    "htpt": {
        "title" : "Hadronic Sum of Event Pt (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 2000,
        "log" : True,
        },
    "htphi": {
        "title" : "Hadronic Sum of Event #varphi",
        "nbins" : 50,
        "min" : -3.15,
        "max" : 3.15,
        "log" : True,
        },
    
    #MET
    "MET_pt": {
      "title" : "#slash{E}_{T} (GeV)",
      "nbins" : 25,
      "min" : 200,
      "max" : 1200,
      "log" : True,
    },
    "MET_phi": {
        "title" : "#slash{E}_{T} #varphi",
        "nbins" : 50,
        "min" : -3.15,
        "max" : 3.15,
        "log" : True,
        },
    #Clean Jet
    "nCJet": {
        "title" : "Number of cleaned jet",
        "nbins" : 13,
        "min" : -0.5,
        "max" : 12.5,
        "log" : True,
    },
    "CleanJetPt[N]": {
      "title" : "clean jet [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "CleanJetEta[N]": {
      "title" : "cleaned jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : True,
    },
    "CleanJetPhi[N]": {
      "title" : "cleaned jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : True,
    },
    "CleanJetMass[N]": {
      "title" : "cleaned jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : True,
    },
    "CleanJetchHEF[N]": {
      "title" : "clean jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "CleanJetneHEF[N]": {
      "title" : "clean jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    # Jets
    "nJet": {
        "title" : "Number of jet",
        "nbins" : 13,
        "min" : -0.5,
        "max" : 12.5,
        "log" : True,
    },
    "JetPt[N]": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "JetEta[N]": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : True,
    },
    "JetPhi[N]": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : True,
    },
    "JetMass[N]": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : True,
    },
    "JetchHEF[N]": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "JetneHEF[N]": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    #GEN
    "Zmass": {
        "title" : "m_{Z} (GeV)",
        "nbins" : 100,
        "min" : 0,
        "max" : 200,
        "log" : True,
    },
    "Zpt": {
        "title" : "Zpt (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "Zeta": {
        "title" : "Gen Z boson eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    #GEN W boson
    "nGenW" : {
        "title" : "number of Gen W boson",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "GenWpt[N]":{
        "title" : "Gen W boson [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "GenWeta[N]": {
        "title" : "Gen W boson [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    "GenWphi[N]" : {
        "title" : "Gen W boson [N] #phi",
        "nbins" : 10,
        "min" : 0.,
        "max" : 3.5,
        "log" : True,
    },
    "GenWmass[N]" : {
        "title" : "Gen W boson [N] mass (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 150,
        "log" : True,
    },
    "GenWsign[N]" : {
        "title" : "Gen W boson [N] Sign",
        "nbins" : 32,
        "min" : -16.5,
        "max" : 15.5,
        "log" : True,
    },
    ## Reco-matching
     "nGenL" : {
        "title" : "number of Match Gen Leptons",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "GenLpt[N]":{
        "title" : "Gen match lepton [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "GenLeta[N]": {
        "title" : "Gen match lepton [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    "GenLphi[N]" : {
        "title" : "Gen match lepton [N] #phi",
        "nbins" : 10,
        "min" : 0.,
        "max" : 3.5,
        "log" : True,
    },
    "GenLmass[N]" : {
        "title" : "Gen match lepton [N] mass (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 150,
        "log" : True,
    },
    "GenLsign[N]" : {
        "title" : "Gen match lepton [N] Sign",
        "nbins" : 32,
        "min" : -16.5,
        "max" : 15.5,
        "log" : True,
    },
    "nRecoL" : {
        "title" : "number of Match Reco Leptons",
        "nbins" : 5,
        "min" : -0.5,
        "max" : 4.5,
        "log" : True,
    },
    "RecoLpt[N]":{
        "title" : "Reco match lepton [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "RecoLeta[N]": {
        "title" : "Reco match lepton [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : True,
    },
    "RecoLphi[N]" : {
        "title" : "Reco match lepton [N] #phi",
        "nbins" : 10,
        "min" : 0.,
        "max" : 3.5,
        "log" : True,
    },
    "RecoLmass[N]" : {
        "title" : "Reco match lepton [N] mass (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 150,
        "log" : True,
    },
    "RecoLsign[N]" : {
        "title" : "Reco match lepton [N] Sign",
        "nbins" : 32,
        "min" : -16.5,
        "max" : 15.5,
        "log" : True,
    },
    #V
     "Vmass": {
        "title" : "V mass (GeV)",
        "nbins" : 100,
        "min" : 0,
        "max" : 200,
        "log" : True,
    },
    "Vpt": {
        "title" : "Vpt (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },

}

for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(0, 4):
            ni = n.replace('[N]', "[%d]" % i)
            variable[ni] = v.copy()
            variable[ni]['title'] = variable[ni]['title'].replace('[N]', "%d" % i)
    elif n.startswith('H.'):
        variable[n] = v
        variable[n.replace('H.', 'HMerged.')] = v.copy()
        variable[n.replace('H.', 'HResolved.')] = v.copy()
        variable[n.replace('H.', 'HResolvedHpt.')] = v.copy()
    elif n.startswith('X.'):
        variable[n] = v
        variable[n.replace('X.', 'XMerged.')] = v.copy()
        variable[n.replace('X.', 'XResolved.')] = v.copy()
        variable[n.replace('X.', 'XResolvedHpt.')] = v.copy()
    else:
        variable[n] = v

# For treealpha
for n, v in var_template.iteritems(): variable[n.replace('.', '_')] = v.copy()

