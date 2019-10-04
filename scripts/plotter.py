#! /usr/bin/env python

import os, multiprocessing, sys
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors, TEfficiency
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox
from multiprocessing import Pool, cpu_count
import time, os
from functools import partial
from collections import OrderedDict

from PhysicsTools.NanoAODTools.LambPlot.Utils.configs import Config
import PhysicsTools.NanoAODTools.LambPlot.Utils.color as col
from PhysicsTools.NanoAODTools.LambPlot.Utils.drawLambda import *
from PhysicsTools.NanoAODTools.postprocessing.data.vars.variables import br_all as variable
from PhysicsTools.NanoAODTools.LambPlot.Utils.selections import *
from PhysicsTools.NanoAODTools.LambPlot.Utils.alias import alias

if '%s' %os.getcwd().split('/')[-1] != 'LambPlot':
    print('EXIT: Please run the plotter in LambPlot folder')
    sys.exit()

########## SETTINGS ##########
import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
parser.add_option("-r", "--region", action="store", type="string", dest="region", default="")
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
#parser.add_option("-s", "--signal", action="store_true", default=False, dest="signal")
parser.add_option("-x", "--Statebox", action="store_true", default=False, dest="Statebox")
parser.add_option("-d", "--debug", action="store_true", default=False, dest="debug")
#parser.add_option("-u", "--User_cutflow", action="store_true", dest="cutflow", default=False)
parser.add_option("-V", "--PrintVar", action="store_true", dest="printVar", default=False)
#parser.add_option("-m", "--multiprocessing", action="store_true", dest="multiprocessing", default=False)
parser.add_option("-l", "--logy", action="store_true", dest="logy", default=False)
parser.add_option("-e", "--era", action="store", type="string", dest="dataset", default="Run2_2016_v4")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

if not options.Statebox:
    gStyle.SetOptStat(0)
else:
    gStyle.SetOptStat(1111111)

cfg = Config(options.dataset)
########## PLOTTER SETTINGS ##########
#NTUPLEDIR   = '/home/shoh/works/Projects/Analysis/LambdaNano/Run2_2016_v4-pilot/';
NTUPLEDIR = '/home/shoh/works/Projects/Analysis/LambdaNano/dataset16-v26-WH/';
PLOTDIR     = "plots/%s"%options.dataset
LUMI        = cfg.lumi() #41860. #35800. # pb-1 Inquire via brilcalc lumi --begin 272007 --end 275376 -u /pb #https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2016Analysis
#data = []
data        = ["data_obs"]
back        = [ "VVV", "ttV" , "WW", "VZ", "Vg", "ST", "WJetsToLNu", "TTbar", "DYJetsToLL" ]
cfg.register(data+back)
#back        = [ "tZq", "WWJJ", "VVV", "ttV" , "WW", "ZZ", "WZ", "Vg", "ST", "WJetsToLNu", "TTbar", "DYJetsToLL" ]
#sign        = ['whww','WHWW','VH']
sign=[]
BLIND       = True if options.blind else False
SIGNAL      = 1. #500. # rescaling factor 1/35800
RATIO       = 4 if not BLIND else 0 #4 # default=4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
POISSON     = False
selection=eval(cfg.era())['selection']
weight=eval(cfg.era())['weight']

#############################################
# Check files
check=True
filelist=cfg.getSamplelist()
for itag in data+back:
    for iroot in filelist[itag]['files']:
        if not os.path.exists(NTUPLEDIR+iroot+".root"):
            print col.FAIL+NTUPLEDIR+iroot+".root does not exit!", col.ENDC
            check=False
if not check:
    exit()
###############################################

def plot(var, cut, norm=False):

    PD = getPrimaryDataset(selection[cut])
    if cut in selection: plotdir = cut

    PROC=data+back if not BLIND else back
    print col.OKGREEN+"Primary Dataset    : "+col.ENDC, PD
    print col.OKGREEN+"CUT    : "+col.ENDC, selection[cut]
    print col.OKGREEN+"WEIGHT : "+col.ENDC, weight[cut]
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
            #Histlist[s].Scale(1./Histlist[s].Integral())
            Histlist[s].SetLineWidth(2)
            Histlist[s].SetFillStyle(0)

    if norm:
        sfnorm = hist['data_obs'].Integral()/hist['BkgSum'].Integral()
        for i, s in enumerate(back+['BkgSum']): hist[s].Scale(sfnorm)

    if len(data+back)>0:
        out = draw(Histlist, data if not BLIND else [], back, sign, SIGNAL, RATIO, POISSON, True if options.logy else (filter(lambda x:x.name()==var,variable)[0]).log())
        out[0].cd(1)
        drawCMS(LUMI, "Preliminary")
        drawRegion(cut)
        printTable(Histlist, sign)
    else:
        out = drawSignal(Histlist, sign, True if options.logy else (filter(lambda x:x.name()==var,variable)[0]).log())
        out[0].cd(1)
        drawCMS(LUMI, "Simulation")
        drawRegion(cut)

    out[0].Update()

    if gROOT.IsBatch():
            #pathname = PLOTDIR+"/Signal/"+cut if options.signal else PLOTDIR+"/"+plotdir
            pathname = PLOTDIR+"/"+plotdir
            if not os.path.exists(pathname): os.system('mkdir -p %s'%pathname)
            out[0].Print(pathname+"/"+var.replace('.', '_')+".png")
            out[0].Print(pathname+"/"+var.replace('.', '_')+".pdf")
    else:
        out[0].Draw()

    #if options.all:
    print col.WARNING+"PURGE OBJECTS IN MEMORY"+col.ENDC
    for process in Histlist:
        Histlist[process].Delete()

def multiplot(cut, var, norm=False):
    plot(var,cut)

def cutflowV0(var, cut, norm=False):

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

def cutflow(cut, cutcat, norm=False):

    PD = getPrimaryDataset(cut[0])
    #if cut in selection: plotdir = cut
    PROC=data+back if not BLIND else back
    #print col.BOLD+"CUT : ", selection[cut]+col.ENDC

    if not sign:
        PDFrame=getEntires(cut, LUMI, PROC, PD, NTUPLEDIR, sign)
    else:
        PDFrame=getEntires(cut, LUMI, PROC+sign, PD, NTUPLEDIR, sign)

    if not os.path.exists(PLOTDIR+'/cutflow/'): os.system('mkdir -p '+PLOTDIR+'/cutflow/')
    PDFrame.to_html( PLOTDIR+'/cutflow/Signifiance_'+cutcat+'.html' if sign else PLOTDIR+'/cutflow/'+cutcat+'.html')
    print 'cutflow table save at '+PLOTDIR+'/cutflow/'

#VOI=['MHT_pt','nCleanJet','Lepton_pfRelIso03_all[0]','Lepton_pfRelIso03_all[1]','Lepton_pfRelIso03_all[2]','Lepton_pfRelIso03_all[3]','Mu_dz[0]','Mu_dz[1]','Mu_dxy[0]','Mu_dxy[1]','Ele_dz[0]','Ele_dz[1]','Ele_dxy[0]','Ele_dxy[1]']

def significanceStudy(cut, cutcat):

    PD = getPrimaryDataset(cut[0])
    #if cut in selection: plotdir = cut
    PROC=data+back if not BLIND else back

    DF=getEntires(cut, LUMI, PROC+sign, PD, NTUPLEDIR, sign)
    CF=DF.to_dict(into=OrderedDict)
    #Dict
    bkgs=CF['MC']
    if len(sign)>1:
        print "ERROR, only one signal is supported"
        sys.exit()
    signals=CF[sign[0]] #ONLY one signal

    dim = len(cut)
    significance = [0]*(dim+1)

    effs = {}
    GrAsym = {}
    yErrorUp = {}
    yErrorDown = {}
    GrAsym = TGraphAsymmErrors()

    for num, (i, j) in enumerate(bkgs.iteritems()):
        s = signals[i]
        b = j

        print "s = ", s
        print "b = ", b
        print "sqrt(b) = ",  math.sqrt(b)
        print "significance = ",  float(s/math.sqrt(b))
        significance[num] = float(s/math.sqrt(b))
        yErrorUp[num] = float(TEfficiency.ClopperPearson(math.sqrt(b),s,0.68, True) - significance[num])
        yErrorDown[num] = float(significance[num] - TEfficiency.ClopperPearson(math.sqrt(b),s,0.68, False))

        GrAsym.SetPoint(num,num+0.5,significance[num])
        GrAsym.SetPointError(num,0,0,yErrorUp[num],yErrorDown[num])

    for k, cs in enumerate(cut):
        GrAsym.GetHistogram().GetXaxis().Set(dim,0,dim);
        GrAsym.GetHistogram().GetXaxis().SetBinLabel(k+1, "%s" %cut[k])

    GrAsym.SetLineColor(2)
    GrAsym.SetLineWidth(3)
    GrAsym.SetMarkerStyle(8)
    GrAsym.SetMarkerColor(2)

    c1 = TCanvas("c1", "Signals Acceptance", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)

    gStyle.SetOptStat(0)

    #GrAsym.SetMaximum(1.3)
    #GrAsym.SetMinimum(0.)

    GrAsym.GetHistogram().GetXaxis().SetTitle("")
    GrAsym.GetHistogram().GetYaxis().SetTitle("Significance (S/#sqrt{B})")

    GrAsym.Draw("pa")
    drawCMS(LUMI, "Work In Progress")
    drawRegion(cutcat)

    if not os.path.exists(PLOTDIR+'/cutflow/'): os.system('mkdir -p '+PLOTDIR+'/cutflow/')
    DF.to_html( PLOTDIR+'/cutflow/Signifiance_'+cutcat+'.html' if sign else PLOTDIR+'/cutflow/'+cutcat+'.html')
    c1.Print( PLOTDIR+'/cutflow/Signifiance_'+cutcat+'.png')
    c1.Print( PLOTDIR+'/cutflow/Signifiance_'+cutcat+'.pdf')
    print 'cutflow table save at '+PLOTDIR+'/cutflow/'

    pass

def plotsignal(var, cut):
    hist={}

    ## Project into histogram
    hist= ProjectDraw(var, cut, LUMI, signals, [], NTUPLESIG)
    for i,s in enumerate(signals):
        print "s : ", s
        hist[s].SetLineWidth(2)

    ## We need the legends
    if not stats:
        leg = TLegend(0.7, 0.9-0.035*len(signals), 0.9, 0.9)
    else:
        leg = TLegend(0.4, 0.9-0.035*len(signals), 0.6, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(1001) #1001
    leg.SetFillColor(0)
    for i, s in enumerate(signals):
        leg.AddEntry(hist[s], samples[s]['label'], "l")

    # declare a canvas for this shit
    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd().SetLogy() if variable[var]['log'] else c1.cd()
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)

    hmax = 0.
    ## Define a suitable height for the histogram taking into account of other signal samples
    for i, s in enumerate(signals):
        if hist[s].GetMaximum() > hmax: hmax = hist[s].GetMaximum()
    if not variable[var]['log']:
        hist[signals[0]].SetMaximum(hmax*1.2)
        hist[signals[0]].SetMinimum(0.)
    else:
        hist[signals[0]].SetMaximum(hmax*6)

    ### after that you fucking draw this shit
    for i, s in enumerate(signals):
        hist[s].Draw("HIST" if i==0 else "SAMES, HIST")
        if stats:
            c1.GetPad(0).Update()
            if i==1:
                lof = hist[s].GetListOfFunctions()
                statbox = lof.FindObject('stats')
                statbox.SetX1NDC(0.779026); statbox.SetX2NDC(0.979401)
                statbox.SetY1NDC(0.593168); statbox.SetY2NDC(0.754658)
    leg.Draw()

    if var.split('_')[0] in ['R','nR']:
        fol="RECO"
    elif var.split('_')[0] in ['G','nG']:
        fol="GEN"
    else:
        fol="ANALYSIS"

    drawCMS(LUMI, fol+" Simulation ")
    #drawRegion(cut)
    #drawAnalysis(channel)

#
#    if variable[var]['log'] and not "X_mass" in var:
#        c1.GetPad(0).SetLogy()

    ## Fitting the mass shape of the variables

    if ('RecoLL' in var or 'RecoL2JJ' in var) and 'mass[0]' in var:
        fitOption="Q0"
        mean = {}
        width = {}
        for i, s in enumerate(signals):
            amean = hist[s].GetXaxis().GetBinCenter(hist[s].GetMaximumBin())
            sigma = hist[s].GetRMS()
            hist[s].Fit("gaus", "%s" %fitOption, "SAME", amean/sigma, amean*sigma) #(i+1)*1000-(i+1)*400, (i+1)*1000+(i+1)*400)
            hist[s].GetFunction("gaus").SetLineWidth(3)
            hist[s].GetFunction("gaus").SetLineColor(hist[s].GetLineColor())
            mean[s] = hist[s].GetFunction("gaus").GetParameter(1)
            width[s] = hist[s].GetFunction("gaus").GetParameter(2)
            #mean[s] = amean
            #width[s] = sigma
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

        #hist[s].Draw()
    #c1.Print("plots/Signal/"+channel+".pdf")
    #c1.Print("plots/Signal/"+channel+".png")
    if not os.path.exists('plots/Signal/'+fol+'/'): os.system('mkdir -p plots/Signal/'+fol+'/')
    c1.Print("plots/Signal/"+fol+'/'+var+".pdf")
    c1.Print("plots/Signal/"+fol+'/'+var+".png")

    print col.WARNING+"PURGE OBJECTS IN MEMORY"+col.ENDC
    for process in hist:
        hist[process].Delete()

    #c1.Delete()
    #if not options.runBash: raw_input("Press Enter to continue...")
    pass

def significancev0(cutlist, labellist):

    basecut=labellist[0]
    dim = len(cutlist)
    significance = [0]*(dim+1)

    file = {}
    tree = {}
    effs = {}
    hist = {}
    GrAsym = {}
    yErrorUp = {}
    yErrorDown = {}
    totEve=0
    GrAsym = TGraphAsymmErrors()
    cuts=""

    for j, c in enumerate(cutlist):
        s=0. ; b=0.
        cuts+=cutlist[0] if j==0 else " && "+cutlist[j]
        print "cuts = ", cuts
        for num1,v in enumerate(signals):
            #print "Signal = ", v
            for num2,filename in enumerate(samples[v]['files']):
                #print "Signal rootfile read = ",  filename
                file[filename] = TFile(NTUPLESIG + filename + ".root", "READ") # Read TFile
                tree[filename] = file[filename].Get("Events") # Read TTree
                nevents = float(sample[filename]['nevents'])
                xs = float(sample[filename]['xsec'])*float(sample[filename]['kfactor'])
                LumiMC = nevents/xs
                Weight = float(LUMI) / float(LumiMC)

                sig_entries = tree[filename].GetEntries(cuts)
                #print "s = ", float(sig_entries) * float(Weight)
                s+= float(sig_entries) * float(Weight)
            print "TOT SIG = ", s

        for num1,k in enumerate(back):
            #print "backgrounds = ", k
            for num2,filename in enumerate(samples[k]['files']):
                #print "backgrounds rootfile read = ",  filename
                file[filename] = TFile(NTUPLEDIR + filename + ".root", "READ") # Read TFile
                tree[filename] = file[filename].Get("Events") # Read TTree
                nevents = float(sample[filename]['nevents'])
                xs = float(sample[filename]['xsec'])*float(sample[filename]['kfactor'])
                LumiMC = nevents/xs
                Weight = float(LUMI) / float(LumiMC)

                bkg_entries = tree[filename].GetEntries(cuts)
                #print "b = ", float(bkg_entries) * float(Weight)
                b+= float(bkg_entries) * float(Weight)
            print "TOT BKG = ", b

        ##End of cutlist
        #COMPUTE
        #print "s = ", s
        #print "b = ", b
        #print "sqrt(b) = ",  math.sqrt(b)
        #print "significance = ",  float(s/math.sqrt(b))
        significance[j] = float(s/math.sqrt(b))
        yErrorUp[j] = float(TEfficiency.ClopperPearson(math.sqrt(b),s,0.68, True) - significance[j])
        yErrorDown[j] = float(significance[j] - TEfficiency.ClopperPearson(math.sqrt(b),s,0.68, False))
        GrAsym.SetPoint(j,j+0.5,significance[j])
        GrAsym.SetPointError(j,0,0,yErrorUp[j],yErrorDown[j])

    for k, cs in enumerate(labellist):
        GrAsym.GetHistogram().GetXaxis().Set(dim,0,dim);
        GrAsym.GetHistogram().GetXaxis().SetBinLabel(k+1, "%s" %labellist[k])

    GrAsym.SetLineColor(2)
    GrAsym.SetLineWidth(3)
    GrAsym.SetMarkerStyle(8)
    GrAsym.SetMarkerColor(2)

    c1 = TCanvas("c1", "Signals Acceptance", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)

    gStyle.SetOptStat(0)

    #GrAsym.SetMaximum(1.3)
    #GrAsym.SetMinimum(0.)

    GrAsym.GetHistogram().GetXaxis().SetTitle("")
    GrAsym.GetHistogram().GetYaxis().SetTitle("Significance (S/#sqrt{B})")

    GrAsym.Draw("pa")
    drawCMS(LUMI, "Work In Progress")
    drawRegion(basecut)

    if not os.path.exists('plots/Signal/Significance/'): os.system('mkdir -p plots/Signal/Significance/')
    c1.Print("plots/Signal/Significance/Sigf_SB_" + basecut + ".png")
    c1.Print("plots/Signal/Significance/Sigf_SB_" + basecut + ".pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")
    pass

###########################################

if __name__ == "__main__":

    start_time = time.time()
    if options.variable =="" and not options.printVar:
        parser.print_help()
        print(col.WARNING+'Example:'+col.ENDC)
        print(col.WARNING+'python scripts/plotter.py -v MHT_pt -r OSmumu -e Run2_2016_v4'+col.ENDC)
        sys.exit(1)

    if options.printVar:
        print(col.OKGREEN+'Predefined Variables for plotting'+col.ENDC)
        print(map(lambda x: x.name(), br_all)+list(alias.keys()))
        print(col.OKGREEN+'Predefined region for plotting'+col.ENDC)
        print(selection.keys())
        sys.exit(1)

    cfg.summary()
    gROOT.Macro('%s/scripts/functions.C' %os.getcwd())
    print col.OKGREEN+"PLOTTING variable ",options.variable+col.ENDC

    if options.cut != "":
        print col.CYAN+"with Cuts : ",options.cut+col.ENDC
        plot( options.variable , options.cut )
    else:
        print col.CYAN+"In selection region : ",options.region+col.ENDC
        plot( options.variable , options.region )

    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
    print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
