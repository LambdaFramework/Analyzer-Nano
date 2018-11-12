from Misc import *
from re import sub

#dataset
triggerMET='(HLT_PFMETNoMu90_PFMHTNoMu90_IDTight||HLT_PFMETNoMu120_PFMHTNoMu120_IDTight)'
triggerEle25='(HLT_Ele25_WPTight_Gsf)'
triggerEle27='(HLT_Ele27_WPLoose_Gsf)'
triggerEle27eta2p1='(HLT_Ele27_eta2p1_WPLoose_Gsf)'
triggerEle105='HLT_Ele105_CaloIdVT_GsfTrkId'
triggerIsoMuo20='HLT_IsoMu20'
triggerIsoMuo22='HLT_IsoMu22'
triggerIsoMuo24='HLT_IsoMu24'
triggerIsoMuo27='HLT_IsoMu27'
#muonTrigger='(HLT_IsoMu22 || HLT_IsoMu22_eta2p1 || HLT_IsoTkMu22_eta2p1 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_Mu45_eta2p1 || HLT_Mu50)'
muonTrigger='(HLT_IsoMu22 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_Mu45_eta2p1 || HLT_Mu50)'
electronTrigger='(HLT_Ele25_WPTight_Gsf || HLT_Ele27_eta2p1_WPLoose_Gsf || HLT_Ele105_CaloIdVT_GsfTrkIdT)'
#HLT_Ele27_WPLoose_Gsf

#Preselection
#presel='nJet>2'
presel='Jet_pt>30 && Jet_jetId>0 && Jet_neEmEF>0.2 && Jet_chHEF>0.1 && Jet_puId>4 && fabs(Jet_eta)<2.5'
#presel='MHTju_pt>100'

#Composite Variables
ZWindow="60 < invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) && invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) < 120"
INVMuE="invariantMass(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0], Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])>15"
#INVMWZ="(invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) - )"

selection = {
    'Trigger' : tAND(muonTrigger,'1==1'),
    #CONTROL REGION
    ##DY+jets CR # this samples will be used both for Z+jets CR AND for di-muonic and di-electronic  tt CR )
    'OSmumu'    : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]!=Muon_charge[1]) && Muon_pt[0]>17 && Muon_pt[1]>8 && Muon_mediumId[0]>0 && Muon_mediumId[1]>0 && Muon_pfRelIso03_all[0]<0.1 && Muon_pfRelIso03_all[1]<0.1')),
    #'OSmumuhighpt'    : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]!=Muon_charge[1]) && Muon_pt[0]>25 && Muon_pt[1]>15 && Muon_pfRelIso03_all[0]<0.1')),
    'OSee'    : tAND(electronTrigger,tAND(presel,'(Electron_charge[0]!=Electron_charge[1]) && Electron_pt[0]>25 && Electron_pt[1]>17 && Electron_pfRelIso03_all[0]<0.15 && Electron_pfRelIso03_all[1]<0.15')),
    'OSemu'    : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]!=Electron_charge[0]) && Muon_pt[0]>22 && Electron_pt[0]>20 && Muon_pfRelIso03_all[0]<0.1 && Muon_mediumId[0]==1 && Electron_pfRelIso03_all[0]<0.1')),
    ## Di-leptonic tt -> e mu 
    'DiLepTT' : tAND(tAND(muonTrigger,tAND(presel,'Muon_pt[0]>24 && Electron_pt[0]>20')),INVMuE), ##INVMuE
    #SS muon
    'SSmumu'   : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]==Muon_charge[1]) && Muon_pt[0]>25 && Muon_pt[1]>15 && Muon_pfRelIso03_all[0]<0.1')), #HT30 > 50 ?
    #'SSmumu'   : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]==Muon_charge[1]) && Muon_mediumId[0]>0 && Muon_mediumId[1]>0 && Muon_pfRelIso03_all[0]<0.1')),
    'SSmumu1b'   : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]==Muon_charge[1]) && Muon_pt[0]>25 && Muon_pt[1]>15 && Muon_pfRelIso03_all[0]<0.1 && Jet_btagCSVV2[0]>0.8')),
    'SSmumu2b'   : tAND(muonTrigger,tAND(presel,'(Muon_charge[0]==Muon_charge[1]) && Muon_pt[0]>25 && Muon_pt[1]>15 && Muon_pfRelIso03_all[0]<0.1 && Jet_btagCSVV2[1]>0.8')),
    ## WZ CR
    #'WZ'      : tAND(tAND(muonTrigger,tAND(presel,'(nMuon > 2)'))),
    ## ZZ, Zgamma, Wgamma CR
    #'ZZ'      : tAND(muonTrigger,tAND(presel,'(nMuon==4 && Muon_pt[3]>5 && Muon_pfRelIso03_all[3]<0.2) || (nMuon==2 && nElectron>0 && Muon_pt[0]>20. && Muon_pfRelIso03_all[0]<0.1 && Muon_pt[1]>10 && Muon_pfRelIso03_all[1]<0.15 && Electron_pt[0]>25 && Electron_pfRelIso03_all[0]<0.1 )')),
}

weights = {
    
}
