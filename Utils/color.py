HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
YELLOW = '\033[33m'

#process color
scheme={
    #bkg
    'DYJetsToLL'    : { 'order' : 1  , 'fillcolor' : 418 , 'fillstyle' : 1001 , 'label' : 'Z(ll) + jets'                                     },
    'DYJetsToLL_HT' : { 'order' : 1  , 'fillcolor' : 418 , 'fillstyle' : 1001 , 'label' : 'Z(ll) + jets'                                     },
    'DYJetsToLL_Pt' : { 'order' : 2  , 'fillcolor' : 418 , 'fillstyle' : 1001 , 'label' : 'Z(ll) + jets'                                     },
    'WJetsToLNu'    : { 'order' : 3  , 'fillcolor' : 881 , 'fillstyle' : 1001 , 'label' : 'W(l#nu) + jets'                                   },
    'WJetsToLNu_HT' : { 'order' : 3  , 'fillcolor' : 881 , 'fillstyle' : 1001 , 'label' : 'W(l#nu) + jets'                                   },
    'TTbar'         : { 'order' : 4  , 'fillcolor' : 798 , 'fillstyle' : 1001 , 'label' : 't#bar{t}'                                         },
    'ST'      	    : { 'order' : 5  , 'fillcolor' : 801 , 'fillstyle' : 1001 , 'label' : 'ST'                                               },
    'VZ'      	    : { 'order' : 6  , 'fillcolor' : 602 , 'fillstyle' : 1001 , 'label' : 'VZ'                                               },
    'WW'      	    : { 'order' : 7  , 'fillcolor' : 41  , 'fillstyle' : 1001 , 'label' : 'WW'                                               },
    'Vg'      	    : { 'order' : 8  , 'fillcolor' : 42  , 'fillstyle' : 1001 , 'label' : 'Vg'                                               },
    'ttV'     	    : { 'order' : 9  , 'fillcolor' : 38  , 'fillstyle' : 1001 , 'label' : 'ttV'                                              },
    'VVV'     	    : { 'order' : 10 , 'fillcolor' : 46  , 'fillstyle' : 1001 , 'label' : 'VVV'                                              },
    'QCD'           : { 'order' : 11 , 'fillcolor' : 921 , 'fillstyle' : 1001 , 'label' : 'QCD'                                              },
    'tZq'           : { 'order' : 12 , 'fillcolor' : 30  , 'fillstyle' : 1001 , 'label' : 'tZq'                                              },
    'BkgSum'  	    : { 'order' : 0  , 'fillcolor' : 1   , 'fillstyle' : 1001 , 'label' : 'MC stat.'                                         },
    #signal
    'VH'            : { 'order' : 0  , 'fillcolor' : 3   , 'fillstyle' : 3003 , 'label' : 'VH'                                               },
    'WHWW'          : { 'order' : 0  , 'fillcolor' : 5   , 'fillstyle' : 3003 , 'label' : 'WHWW'                                             },
    'Whww'          : { 'order' : 0  , 'fillcolor' : 2   , 'fillstyle' : 3003 , 'label' : 'W^{#pm}H(l^{#pm}l^{#pm}#tilde{#nu}#tilde{#nu}jj)' },
    #data
    'data_obs'      : { 'order' : 0  , 'fillcolor' : 0   , 'fillstyle' : 1    , 'label' : 'Data'                                             },

}

'''

    if 'mumu' in cut:
        print col.OKGREEN+var+" : "+col.ENDC+ \
            "Inv( "+col.OKGREEN+"Muon^(+/-)"+col.ENDC+" , "+col.FAIL+"Muon^(-/+)"+col.ENDC+" )" if 'OS' in cut else \
            "Inv( "+col.OKGREEN+"Muon^(+/-)"+col.ENDC+" , "+col.OKGREEN+"Muon^(+/-)"+col.ENDC+" )"
    elif 'ee' in cut:
        print col.OKGREEN+var+" : "+col.ENDC+ \
            "Inv( "+col.OKGREEN+"Electron^(+/-)"+col.ENDC+" , "+col.FAIL+"Electron^(-/+)"+col.ENDC+" )" if 'OS' in cut else \
            "Inv( "+col.OKGREEN+"Electron^(+/-)"+col.ENDC+" , "+col.OKGREEN+"Electron^(+/-)"+col.ENDC+" )"
    elif 'emu' in cut:
        print col.OKGREEN+var+" : "+col.ENDC+ \
	    "Inv( "+col.OKGREEN+"Electron^(+/-)"+col.ENDC+" , "+col.FAIL+"Muon^(-/+)"+col.ENDC+" )" if 'OS' in cut else \
            "Inv( "+col.OKGREEN+"Electron^(+/-)"+col.ENDC+" , "+col.OKGREEN+"Muon^(+/-)"+col.ENDC+" )"

    if 'C_' in var:
        ##Leptonic final state
        if var=='C_deltaRll':
            print col.WARNING+"Compute composite variable C_deltaRll"+col.ENDC
            VAR="deltaR(Lepton_eta[0],Lepton_phi[0],Lepton_eta[1],Lepton_phi[1])"
            print col.WARNING+VAR+col.ENDC
        elif var=='C_deltaPhill':
            print col.WARNING+"Compute composite variable C_deltaPhill"+col.ENDC
            VAR="deltaPhi(Lepton_phi[0],Lepton_phi[1])"
        elif var=='C_deltaEtall':
            print col.WARNING+"Compute composite variable C_deltaEtall"+col.ENDC
            VAR="deltaEta(Lepton_eta[0],Lepton_eta[1])"
        ##Hadronic final state
        elif var=='C_deltaRjj':
            print col.WARNING+"Compute composite variable C_deltaRjj"+col.ENDC
            VAR="deltaR(CleanJet_eta[0],CleanJet_phi[0],CleanJet_eta[1],CleanJet_phi[1])"
            print col.WARNING+VAR+col.ENDC
        elif var=='C_deltaPhijj':
            print col.WARNING+"Compute composite variable C_deltaPhijj"+col.ENDC
            VAR="deltaPhi(CleanJet_phi[0],CleanJet_phi[1])"
        elif var=='C_deltaEtajj':
            print col.WARNING+"Compute composite variable C_deltaEtajj"+col.ENDC
            VAR="deltaEta(CleanJet_eta[0],CleanJet_eta[1])"
        ##Invariant mass of V
        elif var=='C_Vllmass':
            print col.WARNING+"Compute composite variable C_Vllmass"+col.ENDC
            VAR="invariantMass(Lepton_pt[0],Lepton_eta[0],Lepton_phi[0],Lepton_mass[0],Lepton_pt[1],Lepton_eta[1],Lepton_phi[1],Lepton_mass[1])"
            print col.WARNING+VAR+col.ENDC
        elif var=='C_Vjjmass':
            print col.WARNING+"Compute composite variable C_Vjjmass"+col.ENDC
            VAR="invariantMass(CleanJet_pt[0],CleanJet_eta[0],CleanJet_phi[0],CleanJet_mass[0],CleanJet_pt[1],CleanJet_eta[1],CleanJet_phi[1],CleanJet_mass[1])"
            print col.WARNING+VAR+col.ENDC
        ##Invariant pt of V
        elif var=='C_Vllpt':
            print col.WARNING+"Compute composite variable C_Vllpt"+col.ENDC
            VAR="invariantMassPt(Lepton_pt[0],Lepton_eta[0],Lepton_phi[0],Lepton_mass[0],Lepton_pt[1],Lepton_eta[1],Lepton_phi[1],Lepton_mass[1])"
            print col.WARNING+VAR+col.ENDC
        elif var=='C_Vjjpt':
            print col.WARNING+"Compute composite variable C_Vjjpt"+col.ENDC
            VAR="invariantMassPt(CleanJet_pt[0],CleanJet_eta[0],CleanJet_phi[0],CleanJet_mass[0],CleanJet_pt[1],CleanJet_eta[1],CleanJet_phi[1],CleanJet_mass[1])"
            print col.WARNING+VAR+col.ENDC
    else:
        print col.OKGREEN+var+col.ENDC
'''
