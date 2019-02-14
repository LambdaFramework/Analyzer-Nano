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
#cleanedJet==1
#cleanedMuon
#cleanedElectron
#JetMuon_MindR
#JetElectron_MindR
presel='1==1' ## OSmumu, OSem show agreement
#presel='( (Jet_nElectrons>0 && Jet_nMuons>0) && ( (Jet_electronIdx1[0]!=-1) && Muon_mediumId[Jet_electronIdx1[0]]>0 && Muon_pt[Jet_electronIdx1[0]]>30 )   )'
#presel='MHTju_pt>100'
#presel='Jet_nElectrons==0 && Jet_nMuons==0 && Jet_puId>4 && Jet_jetId>0 && Jet_pt>30 && fabs(Jet_eta)<2.5'
#presel='Muon_mediumId>0 && Electron_cutBased>0'
#presel='Jet_pt>30 && Jet_jetId>0 && Jet_neEmEF>0.2 && Jet_chHEF>0.1 && Jet_puId>4 && fabs(Jet_eta)<2.5'

#Composite Variables
#ZWindow="60 < invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) && invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) < 120"
#INVMuE="invariantMass(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0], Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])>15"
#INVMWZ="(invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1]) - )"

selection = {
    'Trigger' : tAND(muonTrigger,'1==1'),
    #CONTROL REGION
    ##DY+jets CR # this samples will be used both for Z+jets CR AND for di-muonic and di-electronic  tt CR )
    'OSmumu'    : tAND(muonTrigger,tAND(presel,'nLepton==2 && abs(LepSign[0])+abs(LepSign[1])==26 && (LepSign[0]+LepSign[1])==0 && LepPt[0]>17 && LepPt[1]>8 && LepIso03[0]<0.15 && LepIso03[1]<0.15')),
    'OSee'    : tAND(electronTrigger,tAND(presel,'nLepton==2 && abs(LepSign[0])+abs(LepSign[1])==22 && (LepSign[0]+LepSign[1])==4 && LepPt[0]>25 && LepPt[1]>17 && LepIso03[0]<0.15 && LepIso03[1]<0.15')),
    'OSemu'   : tAND(muonTrigger,tAND(presel,'nLepton==2 && abs(LepSign[0])+abs(LepSign[1])==24 && abs(LepSign[0]-LepSign[1])==2 && LepPt[0]>20 && LepPt[1]>24')),
    'SSmumu'   : tAND(muonTrigger,tAND(presel,'nLepton==2 && abs(LepSign[0]+LepSign[1])==26 && LepPt[0]>25 && LepPt[1]>15 && LepIso03[0]<0.1')),
}


weights = {
    
}
