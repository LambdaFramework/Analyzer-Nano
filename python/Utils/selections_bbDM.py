from Misc import *
from re import sub

#dataset
triggerMET='( HLT_PFMETNoMu120_PFMHTNoMu120_IDTight )'
#HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight
#HLT_PFMETNoMu90_PFMHTNoMu90_IDTight
triggerEle25='(HLT_Ele25_WPTight_Gsf)'
triggerEle27='(HLT_Ele27_WPLoose_Gsf)'
triggerEle27eta2p1='(HLT_Ele27_eta2p1_WPLoose_Gsf)'
triggerEle105='HLT_Ele105_CaloIdVT_GsfTrkId'
triggerIsoMuo20='HLT_IsoMu20'
triggerIsoMuo22='HLT_IsoMu22'
triggerIsoMuo24='HLT_IsoMu24'
triggerIsoMuo27='HLT_IsoMu27'
muonTrigger='(HLT_IsoMu22 || HLT_IsoMu22_eta2p1 || HLT_IsoTkMu22_eta2p1 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_Mu45_eta2p1 || HLT_Mu50)'
electronTrigger='(HLT_Ele25_WPTight_Gsf || HLT_Ele27_eta2p1_WPLoose_Gsf || HLT_Ele105_CaloIdVT_GsfTrkIdT)'
#HLT_Ele27_WPLoose_Gsf

#Preselection
#presel='nJet>2'
presel='1==1'

#Composite Variables
ZWindow="60 < invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) && invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) < 120"
INVMuE="invariantMass(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0], Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])>15"

#triggerMET && isZtoMM && Lepton1.isMuon && Lepton2.isMuon && ((Lepton1.pt>30 && Lepton1.isTight && Lepton1.pfIso04<0.15 && Lepton2.pt>10 && \
#Lepton2.isLoose && Lepton2.pfIso04<0.25)||(Lepton1.pt>10 && Lepton1.isLoose && Lepton1.pfIso04<0.25 && Lepton2.pt>30 && Lepton2.isTight && Lepton2.pfIso04<0.15)) && V.mass > 70 && V.mass<110

selection = {
    'Trigger' : tAND(triggerMET,'1==1'),
    'ZmmINC' : tAND(tAND(triggerMET,'nMuon>2 && Muon_pt[0]>30 && Muon_pt[1]>10 && Muon_pfRelIso04_all[0]<0.15 && Muon_pfRelIso04_all[0]<0.25'),ZWindow),
}

weights = {
    
}
