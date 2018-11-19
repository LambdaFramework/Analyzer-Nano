#! /usr/bin/env pythonA

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
 
from drawLambda import *
from variables import *
#from selections_SSLep import *
#from samplesVH import *

import color as col

gStyle.SetOptStat(0)
gROOT.Macro('functions.C')

########## SETTINGS ##########
import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
parser.add_option("-r", "--region", action="store", type="string", dest="region", default="")
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
parser.add_option("-l", "--all", action="store_true", default=False, dest="all")
parser.add_option("-s", "--signal", action="store_true", default=False, dest="signal")
parser.add_option("-d", "--debug", action="store_true", default=False, dest="debug")
parser.add_option("-a", "--analysis", action="store", type="string",  dest="analysis", default="VH")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

if options.analysis=='VH':
    from selections_SSLep import *
    from samplesVH import *
    print col.OKGREEN+"VH analysis"+col.ENDC
elif options.analysis=='bbDM':
    from selections_bbDM import *
    from samplesbbDM import *
    print col.OKGREEN+"bbDM analysis"+col.ENDC
    
gStyle.SetOptStat(0)
########## SETTINGS ##########

##############################
#NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/datav8-skim/" if options.analysis is 'VH' else "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/bbDMv2-skim/"
NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/dataset-v10-VH/"
PLOTDIR     = "plots/"
LUMI        = 35800. # pb-1 Inquire via brilcalc lumi --begin 272007 --end 275376 -u /pb #https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2016Analysis
data        = ["data_obs"]
if options.analysis=='VH':
    #back        = [ "ttV" , "WW" ,"WZ" , "TTbar-SL", "ST", "TTbar-DiLep", "WJetsToLNu" , "DYJetsToLL" ]
    back        = [ "ttV" , "VV" , "VVV" , "WJetsToLNu_HT" , "TTbar-SL", "ST", "TTbar-DiLep", "DYJetsToLL" ] 
elif options.analysis=='bbDM':
    back = ["QCD" ,"VVIncl", "ST", "TTbar", "DYJetsToLL_Pt", "WJetsToLNu_HT" ,"ZJetsToNuNu_HT"]
sign        = []
SIGNAL      = 1. # rescaling factor 1/12900
RATIO       = 4 # default=4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
BLIND       = True if options.blind else False
POISSON     = False
#############################################

def plot(var, cut, norm=False):
    
    PD = getPrimaryDataset(selection[cut])
    if cut in selection: plotdir = cut

    PROC=data+back if not BLIND else back
    print col.BOLD+"CUT : ", selection[cut]+col.ENDC
    if not sign:
        Histlist=ProjectDraw(var, cut, LUMI, PROC, PD, NTUPLEDIR)
    else:
        Histlist=ProjectDraw(var, cut, LUMI, PROC+sign, PD, NTUPLEDIR)

    if len(back)>0:
        #If data_obs present, dummy BkgSum == first background process                                                                                                        
        Histlist['BkgSum'] = Histlist['data_obs'].Clone("BkgSum") if 'data_obs' in Histlist else Histlist[back[0]].Clone("BkgSum")
        Histlist['BkgSum'].Reset("MICES")
        Histlist['BkgSum'].SetFillStyle(3003)
        Histlist['BkgSum'].SetFillColor(1)
    for i, s in enumerate(back): Histlist['BkgSum'].Add(Histlist[s])

    if len(back)==0 and len(data)==0:
        for i, s in enumerate(sign):
            #Normalize signal to 1
            Histlist[s].Scale(1./Histlist[s].Integral())
            Histlist[s].SetFillStyle(0)

    if norm:
        sfnorm = hist['data_obs'].Integral()/hist['BkgSum'].Integral()
        for i, s in enumerate(back+['BkgSum']): hist[s].Scale(sfnorm)
        
    if len(data+back)>0:
        out = draw(Histlist, data if not BLIND else [], back, sign, SIGNAL, RATIO, POISSON, variable[var]['log'])
        out[0].cd(1)
        drawCMS(LUMI, "Preliminary")
        drawRegion(cut)
        printTable(Histlist, sign)
    else:
        out = drawSignal(Histlist, sign, variable[var]['log'])
        out[0].cd(1)
        drawRegion(cut)
        drawCMS(LUMI, "Simulation")
        
    out[0].Update()
    pathname = PLOTDIR+"/"+plotdir
    if gROOT.IsBatch():
        if not os.path.exists(pathname): os.makedirs(pathname)
        out[0].Print(pathname+"/"+var.replace('.', '_')+".png")
        out[0].Print(pathname+"/"+var.replace('.', '_')+".pdf")
    else:
        out[0].Draw()
    #out[0].Print("MHTju_pt.pdf")

    if options.all:
        print col.WARNING+"PURGE OBJECTS IN MEMORY"+col.ENDC
        for process in Histlist:
            Histlist[process].Delete()

def signal(var, cut):
    hist={}
    signals        = [ "WHWW" ]
    
    hist= ProjectDraw(var, cut, LUMI, signals, [], NTUPLEDIR)
    for i,s in enumerate(signals):
        print "s : ", s
        #hist[s].Scale(LUMI)
        hist[s].SetLineWidth(2)

    leg = TLegend(0.7, 0.9-0.035*len(signals), 0.9, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001                                                                                                                                                            
    leg.SetFillColor(0)
    for i, s in enumerate(signals):
        #print "hist[s] : ", hist[s].Print()
        #print "sample[s]['label'] : ", sample[s]['label']
        leg.AddEntry(hist[s], samples[s]['label'], "l")

    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd().SetLogy() if variable[var]['log'] else c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    hmax = 0.
    for i, s in enumerate(signals):
        if hist[s].GetMaximum() > hmax: hmax = hist[s].GetMaximum()
    hist[signals[0]].SetMaximum(hmax*1.2)
    #if not variable[var]['log']: hist[signals[0]].SetMinimum(0.)
    
    for i, s in enumerate(signals):
        hist[s].Draw("HIST" if i==0 else "SAME, HIST")
    leg.Draw()
    drawCMS(-1, "Simulation")
    drawRegion(cut)
    #drawAnalysis(channel)

    if 'X' in var and 'mass' in var:
        mean = {}
        width = {}
        for i, s in enumerate(signals):
            amean = hist[s].GetXaxis().GetBinCenter(hist[s].GetMaximumBin())
            sigma = hist[s].GetRMS()
            hist[s].Fit("gaus", "Q0", "SAME", amean/sigma, amean*sigma) #(i+1)*1000-(i+1)*400, (i+1)*1000+(i+1)*400) 
            hist[s].GetFunction("gaus").SetLineWidth(3)
            hist[s].GetFunction("gaus").SetLineColor(hist[s].GetLineColor())
            #mean[s] = hist[s].GetFunction("gaus").GetParameter(1)
            #width[s] = hist[s].GetFunction("gaus").GetParameter(2)
            mean[s] = amean
            width[s] = sigma
            
        print "Mass (GeV)",
        for i, s in enumerate(signals): print " &", s.replace("ZZhllbb_M", ""), "\t",
        print " \\\\"
        print "\\hline"
        print "Mean (GeV)",
        for i, s in enumerate(signals): print " & %.0f\t" % mean[s],
        print " \\\\"
        print "Width (GeV)",
        for i, s in enumerate(signals): print " & %.1f\t" % width[s],
        print " \\\\"
        print "Res (\\%)",
        for i, s in enumerate(signals): print " & %.1f\t" % (100.*width[s]/mean[s], ),
        print " \\\\"
        #    print "%s\t& %.1f\t& %.1f\t& %.1f%% \\\\" % (s.replace("ZZhToLLM", ""), hist[s].GetFunction("gaus").GetParameter(1), hist[s].GetFunction("gaus").GetParameter(2), 100*hist[s].GetFunction("gaus").GetParameter(2)/hist[s].GetFunction("gaus").GetParameter(1))
    pathname = "plots/Signal/"
    if not os.path.exists(pathname): os.makedirs(pathname)
    c1.Print(pathname+"/"+var.replace('.', '_')+".png")
    c1.Print(pathname+"/"+var.replace('.', '_')+".pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")

    

if options.all:
    for region in ['OSemu','OSmumu','SSmumu']:
        print col.CYAN+"PLOTTING on : ",region+col.ENDC
        #for VARS in [ 'Zmass' , 'Zpt' , 'PV_npvs' , 'MHTju_pt' , \
        #              'nMuon' , 'Muon_pt[0]' , 'Muon_pt[1]' , 'Muon_pt[2]' , \
        #              'nElectron' , 'Electron_pt[0]' , 'Electron_pt[1]' , 'Electron_pt[2]' , \
        #              'nJet' , 'Jet_pt[0]' , 'Jet_pt[1]' , 'Jet_pt[2]' , \
        #              #'Muon_eta[0]' , 'Muon_eta[1]' , 'Muon_eta[2]' , \
        #              #'Electron_eta[0]' , 'Electron_eta[1]' , 'Electron_eta[2]' , \
        #              #'Jet_eta[0]' , 'Jet_eta[1]'	, 'Jet_eta[2]' ,	\
        #              'Muon_pfRelIso03_all[0]' , 'Muon_pfRelIso03_all[1]' , 'Muon_pfRelIso03_all[2]' , \
        #              'Electron_pfRelIso03_all[0]' , 'Electron_pfRelIso03_all[1]' , 'Electron_pfRelIso03_all[2]' , \
        #              'Jet_btagCSVV2[0]' , 'Jet_btagCSVV2[1]' , 'Jet_btagCSVV2[2]' , \
        #              'Jet_btagCMVA[0]' , 'Jet_btagCMVA[1]' , 'Jet_btagCMVA[2]'  , \
        #              'Electron_dxy[0]' , 'Electron_dxy[1]' , 'Electron_dxy[2]' , \
        #              'Muon_dxy[0]' , 'Muon_dxy[1]' , 'Muon_dxy[2]' \
        #]:
        for VARS in [ 'Zmass' , 'Zpt' , 'PV_npvs' , 'MHTju_pt' , 'Muon_pt[0]' , 'Muon_pt[1]' , 'Muon_pt[2]' , \
                      'Muon_pfRelIso03_all[0]' , 'Muon_pfRelIso03_all[1]' , 'Muon_pfRelIso03_all[2]', \
                      'Electron_pt[0]' , 'Electron_pt[1]' , 'Electron_pt[2]', \
                      'Electron_pfRelIso03_all[0]' , 'Electron_pfRelIso03_all[1]' , 'Electron_pfRelIso03_all[2]' , \
                      'nJet' , 'Jet_pt[0]' , 'Jet_pt[1]' , 'Jet_pt[2]' ]:
            start_time = time.time()
            print col.OKGREEN+"PLOTTING on : ",VARS+col.ENDC
            plot(VARS,region)
            print("--- %s seconds ---" % (time.time() - start_time))
            print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
            print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
elif options.signal:
    print "Signal Study"
    signal(options.variable,options.cut)
else:
    start_time = time.time()
    print col.OKGREEN+"PLOTTING: ", options.variable+col.ENDC
    plot(options.variable, options.cut)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
    print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
