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
muonTrigger='(HLT_IsoMu22 || HLT_IsoMu22_eta2p1 || HLT_IsoTkMu22_eta2p1 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_Mu45_eta2p1 || HLT_Mu50)'
#muonTrigger='(HLT_IsoMu22 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_Mu45_eta2p1 || HLT_Mu50)'
electronTrigger='(HLT_Ele25_WPTight_Gsf || HLT_Ele27_eta2p1_WPLoose_Gsf || HLT_Ele105_CaloIdVT_GsfTrkIdT)'

#Preselection
presel='1==1'

#Composite Variables
#ZWindow="60 < invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) && invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) < 120"
#INVMuE="invariantMass(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0], Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])>15"
#INVMWZ="(invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) - )"

selection = {
    'Trigger' : tAND(muonTrigger,'1==1'),
    #CONTROL REGION
    'OSmumu'    : tAND(muonTrigger,tAND(presel,'isOSmumu && LepPt[0]>30 && LepPt[1]>15 && LepIso03[0]<0.15 && LepIso03[1]<0.15')),
    'OSee'    : tAND(electronTrigger,tAND(presel,'isOSee && LepPt[0]>25 && LepPt[1]>17 && LepIso03[0]<0.15 && LepIso03[1]<0.15')),
    'OSemu'   : tAND(muonTrigger,tAND(presel,'isOSemu && LepPt[0]>20 && LepPt[1]>24 && Vmass>15')),
    'SSmumu'   : tAND(muonTrigger,tAND(presel,'isSSmumu && LepPt[0]>25 && LepPt[1]>15 && LepIso03[0]<0.1')),
}


weights = {
    
}
