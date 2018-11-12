#! /usr/bin/env python                                                                                                                               
import os, multiprocessing, sys
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox
import time

cwd=os.getcwd()
sys.path.append(cwd+"/Utils/")
 
from drawUtils import *
from variables import *
from selections_SSLep import *
from samplesVH import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
gROOT.Macro('functions.C')
###############################################
NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/datav6-skim/"
LUMI        = 35800. # pb-1
data = ["data_obs"]
#back = [ "ttV", "WJetsToLNu", "TTbar-SL", "WW", "WZ", "ST", "TTbar-DiLep", "DYJetsToLL" ]
back = [ "ttV" , "WW" ,"WZ" , "TTbar-SL", "ST", "TTbar-DiLep", "WJetsToLNu" , "DYJetsToLL" ]
sign=[]
#############################################
#Variable
#var="Zmass"
var="MHTju_pt"
#Trigger
TRIGGER="(HLT_IsoMu22 || HLT_IsoMu22_eta2p1 || HLT_IsoTkMu22_eta2p1 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_Mu45_eta2p1 || HLT_Mu50)"
#Cut
cut=TRIGGER+"&& (Muon_charge[0]!=Muon_charge[1])"
#OPTION
BLIND=False
POISSON= False
SIGNAL      = 1.
RATIO       = 4
jobs        = []
############################################
ths1 = THStack ("Stacked","Stacked")
histcarrier={}
histlet={}
if var=="Zmass":
    VAR="invariantMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1])"
else:
    VAR=var
#############################################
start_time = time.time()
pd = getPrimaryDataset(cut)

##return the list of file under tag
if not BLIND:
    processes=data+back
elif BLIND:
    processes=back
for TAG in (processes):
    print "TAG : ", TAG
    #print samples['%s' %TAG]['files']
    ENUMLIST=[]
    if 'data' in TAG:
        for datalet in (samples['%s' %TAG]['files']):
            if datalet in pd:
                ENUMLIST.append(datalet)
    elif not 'data' in TAG:
        ENUMLIST=samples['%s' %TAG]['files']
    
    for num, bkgs in enumerate(ENUMLIST):
        print num, bkgs
        f = TFile.Open(NTUPLEDIR+bkgs+".root","READ")
        tree = f.Get("Events")
        gROOT.cd()
        #Define histograms
        nevents = sample[bkgs]['nevents']
        xs = sample[bkgs]['xsec']
        LumiMC = nevents/xs
        Weight = float(LUMI) / float(LumiMC)

        #Preserve first histogram
        if num==0:
            if variable[var]['nbins']>0: histlet[TAG] = TH1F(bkgs, ";"+variable[var]['title'], variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
            else: histlet[TAG]=TH1F(bkgs,";"+variable[var]['title'], len(variable[var]['bins'])-1, array('f', variable[var]['bins']))
            histlet[TAG].Sumw2()
            if 'data' in TAG:
                print "DATA, NO HLT : ", bkgs
                subcut= cut.replace(TRIGGER,"(1==1)")
                tree.Draw("%s >> %s" %(VAR,bkgs),"%s" %subcut)
            elif not 'data' in TAG:
                print "MC, With HLT"
                tree.Draw("%s >> %s" %(VAR,bkgs),"%s*(%s)" %(Weight,cut))
                if "WZ" in TAG:
                    c2=TCanvas("c2","c2")                                                                                         
                    tree.Draw("%s >> %s" %(VAR,bkgs),"%s*(%s)" %(Weight,cut))
                    c2.SaveAs("WZ.pdf") 
            print histlet[TAG].Print()
        #Preserve second histogram
        elif num>0:
            if variable[var]['nbins']>0: histcarrier[bkgs] = TH1F(bkgs, ";"+variable[var]['title'], variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
            else: histcarrier[bkgs]=TH1F(bkgs,";"+variable[var]['title'], len(variable[var]['bins'])-1, array('f', variable[var]['bins']))
            histcarrier[bkgs].Sumw2()
            if 'data' in TAG:
                print "DATA, NO HLT : ", bkgs
                subcut= cut.replace(TRIGGER,"(1==1)")
                tree.Draw("%s >> %s" %(VAR,bkgs),"%s" %subcut)
            elif not 'data' in TAG:
                print "MC, With HLT"
	        tree.Draw("%s >> %s" %(VAR,bkgs),"%s*(%s)" %(Weight,cut))
            #print "Check cloning PRIOR ", histcarrier[bkgs].Print()
            #gROOT.cd()
            hnew = histcarrier[bkgs].Clone(bkgs)
            #print "Check cloning POSTERIOR ",hnew.Print()
            histlet[TAG].Add(hnew)
    histlet[TAG].SetFillColor(samples[TAG]['fillcolor'])
    histlet[TAG].SetFillStyle(samples[TAG]['fillstyle'])
    histlet[TAG].SetLineColor(samples[TAG]['linecolor'])
    histlet[TAG].SetLineStyle(samples[TAG]['linestyle'])
    #ths1.Add(histlet[TAG])
    #return histlet
    

#c1=TCanvas("c1","c1")
#ths1.Draw()
#c1.SaveAs("test.pdf")

# Background sum                                                                                                                          
if len(back)>0:
    #If data_obs present, dummy BkgSum == first background process                                                                               
    histlet['BkgSum'] = histlet['data_obs'].Clone("BkgSum") if 'data_obs' in histlet else histlet[back[0]].Clone("BkgSum")
    histlet['BkgSum'].Reset("MICES")
    histlet['BkgSum'].SetFillStyle(3003)
    histlet['BkgSum'].SetFillColor(1)
    for i, s in enumerate(back): histlet['BkgSum'].Add(histlet[s])

if len(back)==0 and len(data)==0:
    for i, s in enumerate(sign):
        histlet[s].Scale(1./histlet[s].Integral())
        histlet[s].SetFillStyle(0)
        #hist[s].Rebin(2)                                                                                                                        

    #if norm:
    #    sfnorm = hist['data_obs'].Integral()/hist['BkgSum'].Integral()
    #    for i, s in enumerate(back+['BkgSum']): hist[s].Scale(sfnorm)

#PLOT
if len(data+back)>0:
    out = draw(histlet, data if not BLIND else [], back, sign, SIGNAL, RATIO, POISSON, variable[var]['log'])
else:
    out = drawSignal(histlet, sign, variable[var]['log'])

out[0].cd(1)
if len(data+back)>0:
    drawCMS(LUMI, "Preliminary")
else:
    drawCMS(LUMI, "Simulation")
#drawRegion(shortcut)
#drawAnalysis(channel)
out[0].Update()
print "HISTLET : ", histlet
if len(data+back)>0: printTable(histlet, sign)

out[0].Print("MHTju_pt.pdf")

print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
