
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
    ## Electron
    "nElectron": {
      "title" : "number of electrons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "Electron_pt[N]": {
        "title" : "Electron [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "Electron_eta[N]": {
        "title" : "Electron [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : False,
    },
    "Electron_dxy[N]": {
        "title" : "Electron [N] d_{xy}",
        "nbins" : 50,
        "min" : -0.02,
        "max" : 0.02,
        "log" : True,
    },
    "Electron_pfRelIso03_all[N]": {
        "title" : "Electron [N] PFIso_{03}",
        "nbins" : 50,
        "min" : 0,
        "max" : 0.25,
        "log" : True,
    },
    
    ## Muon
    "nMuon": {
      "title" : "number of muons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "Muon_pt[N]": {
        "title" : "Muon [N] p_{T} (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "Muon_eta[N]": {
        "title" : "Muon [N] #eta",
        "nbins" : 30,
        "min" : -3,
        "max" : 3,
        "log" : False,
    },
    "Muon_dxy[N]": {
        "title" : "Muon [N] d_{xy}",
        "nbins" : 50,
        "min" : -0.02,
        "max" : 0.02,
        "log" : True,
    },
    "Muon_pfRelIso03_all[N]": {
        "title" : "Muon [N] PFIso_{03}",
        "nbins" : 50,
        "min" : 0,
        "max" : 0.25,
        "log" : True,
    },

    
    ## HT
    "MHTju_pt": {
        "title" : "MHTju_pt (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 2000,
        "log" : True,
        },
    "MHTju_phi": {
        "title" : "MHTju_phi #varphi",
        "nbins" : 50,
        "min" : -3.15,
        "max" : 3.15,
        "log" : False,
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
        "log" : False,
        },
    
    # Jets
    "nJet": {
        "title" : "Number of jet",
        "nbins" : 10,
        "min" : -0.5,
        "max" : 9.5,
        "log" : True,
    },
    "Jet_pt[N]": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "Jet_eta[N]": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : False,
    },
    "Jet_phi[N]": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "Jet_mass[N]": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "Jet_chHEF[N]": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet_neHEF[N]": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet_btagCSVV2[N]": {
      "title" : "jet [N] CSV2",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet_btagCMVA[N]": {
        "title" : "jet [N] CMVA",
        "nbins" : 50,
        "min" : 0,
        "max" : 1,
        "log" : False,
    },
    "Zmass": {
        "title" : "m_{Z} (GeV)",
        "nbins" : 100,
        "min" : 0,
        "max" : 300,
        "log" : True,
    },
    "Zpt": {
        "title" : "Zpt (GeV)",
        "nbins" : 50,
        "min" : 0,
        "max" : 500,
        "log" : True,
    },
    "Jet_jetId[N]":{
        "title" : "Jet_jetId",
        "nbins" : 10,
        "min" : 0,
        "max" : 10,
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

