#! /usr/bin/env pythonAA

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
from selections_SSLep import *

import color as col

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
parser.add_option("-z", "--Allsignal", action="store_true", default=False, dest="Allsignal")
parser.add_option("-x", "--Statebox", action="store_true", default=False, dest="Statebox")
parser.add_option("-d", "--debug", action="store_true", default=False, dest="debug")
parser.add_option("-a", "--analysis", action="store", type="string",  dest="analysis", default="VH")
parser.add_option("-u", "--User_cutflow", action="store_true", dest="cutflow", default=False)
parser.add_option("-V", "--PrintVar", action="store_true", dest="printVar", default=False)
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

if not options.Statebox:
    gStyle.SetOptStat(0)
else:
    gStyle.SetOptStat(1111111)
########## SETTINGS ##########

##############################
#NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/datav8-skim/" if options.analysis is 'VH' else "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/bbDMv2-skim/"
#NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/dataset-v17p1-VH/"
#NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/dataset-v15-signal/"
NTUPLEDIR   = "/Users/shoh/Projects/CMS/PhD/Analysis/SSL/dataset-v18-signal/"
PLOTDIR     = "plots/"
LUMI        = 35800. #41860. #35800. # pb-1 Inquire via brilcalc lumi --begin 272007 --end 275376 -u /pb #https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2016Analysis
data        = []
sign        = ['Wm','Wp']
if options.analysis=='VH':
    data        = ["data_obs"]
    back         = [ "tZq", "WWJJ", "VVV", "ttV" , "WW", "ZZ", "WZ", "VGamma", "ST", "WJetsToLNu_HT", "TTbar", "DYJetsToLL_HT" ]
#elif options.analysis=='signal':
#    sign        = ['wphww','wmhww']
#    back        = []
elif options.analysis=='bbDM':
    back = ["QCD" ,"VVIncl", "ST", "TTbar", "DYJetsToLL_Pt", "WJetsToLNu_HT" ,"ZJetsToNuNu_HT"]
    
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
    #signals        = [ "WHWW" ]
    #signals         = [ "VH" ]
    signals         = ['Wm','Wp']
    
    hist= ProjectDraw(var, cut, LUMI, signals, [], NTUPLEDIR)
    for i,s in enumerate(signals):
        print "s : ", s
        #hist[s].Scale(LUMI)
        hist[s].SetLineWidth(2)

    if not options.Statebox:
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
    if not options.Statebox: leg.Draw();
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
    pathname = "plots/Signal/"+cut
    if not os.path.exists(pathname): os.makedirs(pathname)
    c1.Print(pathname+"/"+var.replace('.', '_')+".png")
    c1.Print(pathname+"/"+var.replace('.', '_')+".pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")

    
def cutflow(var, cut, norm=False):

    PD = getPrimaryDataset(cut[0])
    #if cut in selection: plotdir = cut
    PROC=data+back if not BLIND else back
    #print col.BOLD+"CUT : ", selection[cut]+col.ENDC
    
    if not sign:
        Histlist=getEntires(var, cut, LUMI, PROC, PD, NTUPLEDIR)
    else:
        Histlist=getEntires(var, cut, LUMI, PROC+sign, PD, NTUPLEDIR)

    if len(data+back)>0:
        printTable_html(Histlist,sign)

VOI = [ 'Vmass' , 'Vpt' , 'PV_npvs' , 'htpt' , 'htphi' , 'LepPt[0]' , 'LepPt[1]' , \
        'LepSign[0]' , 'LepSign[1]' , 'nJet' , 'JetPt[0]' , 'JetPt[1]' , 'JetPt[2]' , \
        'JetEta[0]' , 'JetEta[1]' , 'JetEta[2]' , 'isOSmumu' , 'isOSee' , 'isOSemu' , 'isSSmumu' , 'isSSee' , \
        'Zpt' , 'nLepton' , 'JetchHEF[0]' , 'JetchHEF[1]' , 'JetneHEF[0]' , 'JetneHEF[1]', 'LepIso03[0]' , 'LepIso03[1]' ]

if options.all:
    #for region in [ 'OSemu' , 'OSmumu' ,'OSee' , 'SSmumu' ]:
    for region in [ 'OSemu' , 'OSee' , 'SSmumu' ]:
        print col.CYAN+"PLOTTING on : ",region+col.ENDC
        for VARS in VOI:  
            start_time = time.time()
            print col.OKGREEN+"PLOTTING on : ",VARS+col.ENDC
            plot(VARS,region)
            print("--- %s seconds ---" % (time.time() - start_time))
            print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
            print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
elif options.signal:
    print "Signal Study"
    signal(options.variable,options.cut)
elif options.printVar:
    print "Print all available variable specified"
    print VOI
elif options.Allsignal:
    print "Signal study All"
    for region in ['Reco-ee','Reco-mumu','Reco-emu','Gen-ee','Gen-mumu','Gen-emu','Reco-SSmumu','Gen-SSmumu']:
        for VARS in [ "S_RecoL1L2DeltaPhi" , "S_RecoL1L2Mass" , "S_RecoL1L2DeltaR" , "S_GenL1L2DeltaPhi" , "S_GenL1L2Mass" , "S_GenL1L2DeltaR" , \
                      "RecoLIso03[0]", "RecoLIso03[1]", "RecoLpt[0]", "RecoLeta[0]", "RecoLphi[0]", "RecoLsign[0]", \
                      "RecoLpt[1]", "RecoLeta[1]", "RecoLphi[1]", "RecoLsign[1]" \
                      "GenLpt[0]", "GenLeta[0]", "GenLphi[0]", "GenLsign[0]", "GenLpt[1]", "GenLeta[1]", "GenLphi[1]", "GenLsign[1]" ]:
            if 'Reco' in region:
                if 'Gen' in VARS: continue;
            elif 'Gen' in region:
                if 'Reco' in VARS: continue;
            signal(VARS,region)
elif options.cutflow:
    print "Cutflow table"
    if options.cut=="":
        print "ERROR: Please specify cut , python lambdaPlot.py -u -v VAR -c CUT "
        exit()
    
    if options.variable=="":
        var="PV_npvs"
    else:
        var=options.variable
        
    cutlet=[]
    tribit=[selection[options.cut].split(') && (')[0].split('((')[1]]
    cutseq=selection[options.cut].split(') && (')[2].split('))')[0].split('&&')
    cutlet = tribit + cutseq 
    #print tribit
    #print cutseq
    #print cutlet
    cutflow(var, cutlet)
else:
    start_time = time.time()
    print col.OKGREEN+"PLOTTING: ", options.variable+col.ENDC
    plot(options.variable, options.cut)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
    print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))