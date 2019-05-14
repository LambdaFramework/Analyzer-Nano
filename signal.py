#! /usr/bin/env python

import os
import copy
import math
from array import array
from ROOT import gROOT, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText

from Analysis.ALPHA.drawUtils import *
from Analysis.ALPHA.variables import *
from Analysis.ALPHA.selectionsForAlpha import *
from Analysis.ALPHA.samples import samples

#gROOT.Macro('../Heppy/python/tools/functions.C')

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-b", "--bash", action="store_true", default=False, dest="runBash")
(options, args) = parser.parse_args()
if options.runBash: gROOT.SetBatch(True)

########## SETTINGS ##########
#gROOT.Macro('functions.C')
gStyle.SetOptStat(0)
LUMI        = 3990 # in pb-1
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
NTUPLEDIR   = '/lustre/cmsdata/pazzini/ALPHA/v6/Pruned/'

back = ["DYJetsToLL_HT"]
sign = ['XZZ_M600', 'XZZ_M800', 'XZZ_M1000', 'XZZ_M1200', 'XZZ_M1400', 'XZZ_M1600', 'XZZ_M1800', 'XZZ_M2000', 'XZZ_M2500', 'XZZ_M3000', 'XZZ_M3500', 'XZZ_M4000', 'XZZ_M4500']
colors = [616+4, 632, 800+7, 800, 416+1, 860+10, 600, 616, 921, 922]

massPoints = [600, 800, 1000, 1200, 1600, 1800, 2000, 3000, 3500, 4000, 4500]
channels = ['XVZmmlp', 'XVZmmhp', 'XVZeelp', 'XVZeehp']
color = {"XVZmmlp" : 634, "XVZmmhp" : 410, "XVZeelp" : 856, "XVZeehp" : 418}

def signal(var, cut, reg):
    
    signals = sign
    
    #if 'X.mass' in var:
        #variable[var]['nbins'] = 200 if not 'nn' in cut else 85
        #variable[var]['min'] = 500
        #variable[var]['max'] = 5000
    
    for i in range(5):
        for n, c in selection.iteritems():
            if n in cut: cut = cut.replace(n, c)
    
    for i, s in enumerate(signals):
        hist[s] = project('X_mass', cut, 'EventWeight', s, [], NTUPLEDIR)
        hist[s].Scale(LUMI)
        hist[s].SetLineWidth(2)
    
#    if not var == "X_mass": sign = ['XZZ_M1000', 'XZZ_M1400', 'XZZ_M2000', 'XZZ_M3000', 'XZZ_M4000']
#    hmax = 0.
#    file = {}
#    tree = {}
#    hist = {}
#    for i, s in enumerate(sign):
#        file[s] = TFile(NTUPLEDIR + sample[s]['files'][0] + ".root", "READ") # Read TFile
#        tree[s] = file[s].Get(reg) # Read TTree
#        if "X_mass" in var: hist[s] = TH1F(s, ";"+variable[var]['title'], 250, 0, 5000)
#        elif variable[var]['nbins']>0: hist[s] = TH1F(s, ";"+variable[var]['title'], variable[var]['nbins']*5, variable[var]['min'], variable[var]['max']) # Init histogram
#        else: hist[s] = TH1F(s, ";"+variable[var]['title'], len(variable[var]['bins'])-1, array('f', variable[var]['bins']))
#        hist[s].Sumw2()
#        tree[s].Project(s, var, cut)
#        if hist[s].Integral() > 0: hist[s].Scale(1./hist[s].Integral())
#        hist[s].SetFillColor(sample[s]['fillcolor'])
#        hist[s].SetFillStyle(0)
#        hist[s].SetLineColor(sample[s]['linecolor'])
#        hist[s].SetLineStyle(sample[s]['linestyle'])
#        hist[s].SetLineWidth(2)
#        hist[s].GetXaxis().SetTitleOffset(hist[s].GetXaxis().GetTitleOffset()*1.2)
#        hist[s].GetYaxis().SetTitleOffset(hist[s].GetYaxis().GetTitleOffset()*1.2)
#        if hist[s].GetMaximum() > hmax: hmax = hist[s].GetMaximum()
#    
    leg = TLegend(0.7, 0.9-0.035*len(signals), 0.9, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for i, s in enumerate(signals):
        leg.AddEntry(hist[s], sample[s]['label'], "l")
    
    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
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
    drawRegion(channel)
    drawAnalysis(channel)
    
#    
#    if variable[var]['log'] and not "X_mass" in var:
#        c1.GetPad(0).SetLogy()

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
    
    c1.Print("plots/Signal/"+channel+".pdf")
    c1.Print("plots/Signal/"+channel+".png")
    if not options.runBash: raw_input("Press Enter to continue...")



def btag():
    nbins = 500
    xmin = 0.
    xmax = 1.
    sel = "Z_pt>200 && Z_mass>70 && Z_mass<110 && fatjet1_pt>200 && (fatjet1_prunedMass>95 && fatjet1_prunedMass<130)"
    add = "fatjet1_CSV>0. && fatjet1_CSV1>0. && fatjet1_CSV2>0."
    
    tree = TChain("XZZ")
    for j, ss in enumerate(sample[back[0]]['files']):
        tree.Add(NTUPLEDIR + ss + ".root")
    bb = TH1F("bb", ";CSV;Arbitrary units", nbins, xmin, xmax)
    qq = TH1F("qq", ";CSV;Arbitrary units", nbins, xmin, xmax)
    bb12 = TH2F("bb12", ";CSV1;CSV2;Arbitrary units", nbins, xmin, xmax, nbins, xmin, xmax)
    qq12 = TH2F("qq12", ";CSV1;CSV2;Arbitrary units", nbins, xmin, xmax, nbins, xmin, xmax)
    tree.Project("bb", "fatjet1_CSV", sel+" && "+add+" && fatjet1_flavour==5")
    tree.Project("qq", "fatjet1_CSV", sel+" && "+add+" && fatjet1_flavour!=5")
    tree.Project("bb12", "fatjet1_CSV2:fatjet1_CSV1", sel+" && "+add+" && fatjet1_flavour==5")
    tree.Project("qq12", "fatjet1_CSV2:fatjet1_CSV1", sel+" && "+add+" && fatjet1_flavour!=5")
    #bb12.Draw("LEGO2")
    
    bb.Scale(1./bb.Integral())
    qq.Scale(1./qq.Integral())
    bb12.Scale(1./bb12.Integral())
    qq12.Scale(1./qq12.Integral())
    
    fatjet = TGraph(nbins)
    subjet = TGraph(nbins)
    loose = TGraph(2)
    medium = TGraph(2)
    tight = TGraph(2)
    
    fatjet.SetLineColor(633) #kRed+1
    fatjet.SetLineWidth(3)
    subjet.SetLineColor(418) #kGreen+2
    subjet.SetLineWidth(3)
    loose.SetMarkerStyle(29)
    loose.SetMarkerSize(2.)
    medium.SetMarkerStyle(23)
    medium.SetMarkerSize(2.)
    tight.SetMarkerStyle(20)
    tight.SetMarkerSize(2.)
    
    leg = TLegend(0.25, 0.7, 0.6, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    leg.AddEntry(fatjet, "fat-jet b-tagging", "l")
    leg.AddEntry(subjet, "sub-jet b-tagging", "l")
    leg.AddEntry(loose, "Loose WP", "p")
    leg.AddEntry(medium, "Medium WP", "p")
    leg.AddEntry(tight, "Tight WP", "p")
    
    for i in range(0, nbins):
        fatjet.SetPoint(i, 1.-bb.Integral(0, i), 1.-qq.Integral(0, i))
        subjet.SetPoint(i, 1.-bb12.Integral(0, i, 0, i), 1.-qq12.Integral(0, i, 0, i))
    
    lbin = bb12.GetXaxis().FindBin(0.605)
    mbin = bb12.GetXaxis().FindBin(0.890)
    tbin = bb12.GetXaxis().FindBin(0.970)
    loose.SetPoint(0, 1.-bb.Integral(0, lbin), 1.-qq.Integral(0, lbin))
    medium.SetPoint(0, 1.-bb.Integral(0, mbin), 1.-qq.Integral(0, mbin))
    tight.SetPoint(0, 1.-bb.Integral(0, tbin), 1.-qq.Integral(0, tbin))
    loose.SetPoint(1, 1.-bb12.Integral(0, lbin, 0, lbin), 1.-qq12.Integral(0, lbin, 0, lbin))
    medium.SetPoint(1, 1.-bb12.Integral(0, mbin, 0, mbin), 1.-qq12.Integral(0, mbin, 0, mbin))
    tight.SetPoint(1, 1.-bb12.Integral(0, tbin, 0, tbin), 1.-qq12.Integral(0, tbin, 0, tbin))
    
    c3 = TCanvas("c3", "sub-jet b-tagging", 800, 600)
    c3.cd()
    c3.GetPad(0).SetTopMargin(0.06)
    c3.GetPad(0).SetRightMargin(0.05)
    c3.GetPad(0).SetTicks(1, 1)
    c3.GetPad(0).SetLogy()
    subjet.SetTitle(";b-jet efficiency;udsg-jet efficiency")
    subjet.GetXaxis().SetRangeUser(0., 1.)
    #subjet.GetYaxis().SetRangeUser(5e-3, 1.)
    subjet.Draw("AL")
    fatjet.Draw("SAME, L")
    loose.Draw("SAME, P")
    medium.Draw("SAME, P")
    tight.Draw("SAME, P")
    leg.Draw()
    c3.Print("plots/Signal/ROC.pdf")
    c3.Print("plots/Signal/ROC.png")
    
    raw_input("Press Enter to continue...")



def efficiency(cutlist, labellist):
    basecut = ""
    
    if "isZtoEE" in cutlist[0]: basecut = "isZtoEE"
    elif "isZtoMM" in cutlist[0]: basecut = "isZtoMM"

    ncuts = len(cutlist)
    
    file = {}
    tree = {}
    effs = {}
    for i, s in enumerate(sign):
        file[s] = TFile(NTUPLEDIR + sample[s]['files'][0] + ".root", "READ") # Read TFile
        tree[s] = file[s].Get("ntuple/tree") # Read TTree
        effs[s] = [0]*(ncuts+1)
        for j, c in enumerate(cutlist):
            n = tree[s].GetEntries(cutlist[j])
            d = tree[s].GetEntries(basecut)
            effs[s][j] = float(n)/(d)
    
    line = []
    for j, c in enumerate(cutlist):
        line.append( TGraph(ncuts) )
        line[j].SetTitle(";m_{X} (GeV);Efficiency")
        for i, s in enumerate(sign):
            mass = int( ''.join(x for x in s if x.isdigit()) )
            line[j].SetPoint(i, mass, effs[s][j])
        line[j].SetMarkerStyle(20)
        line[j].SetMarkerColor(colors[j])
        line[j].SetLineColor(colors[j])
        line[j].SetLineWidth(3)
        line[j].GetXaxis().SetTitleOffset(line[j].GetXaxis().GetTitleOffset()*1.2)
        line[j].GetYaxis().SetTitleOffset(line[j].GetYaxis().GetTitleOffset()*1.2)
    
    leg = TLegend(0.6, 0.2, 0.9, 0.6)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for i, c in enumerate(cutlist):
        leg.AddEntry(line[i], labellist[i], "lp")
    
    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    line[0].GetXaxis().SetTitle("m_{X} (GeV)")
    line[0].GetYaxis().SetTitle("Efficiency")
    line[0].GetYaxis().SetRangeUser(0., 1.)
    
    for i, s in enumerate(cutlist):
        line[i].Draw("APL" if i==0 else "SAME, PL")
    leg.Draw()
    drawCMS(-1, "Simulation")
    
    c1.Print("plots/Signal/Efficiency_" + basecut + ".png")
    c1.Print("plots/Signal/Efficiency_" + basecut + ".pdf")
    if not options.runBash: raw_input("Press Enter to continue...")




def significance(precut, cutlist, labellist, testname):

    var = "X_mass"
    ncuts = len(cutlist)
    
    
    file = {}
    tree = {}
    hist = {}
    effs = {}
    psig = {}
    
    # Create and fill MC histograms
    for i, s in enumerate(back+sign):
        nevts = 0
        tree[s] = TChain("XZZ")
        for j, ss in enumerate(sample[s]['files']):
            tree[s].Add(NTUPLEDIR + ss + ".root")
            tfile = TFile(NTUPLEDIR + ss + ".root", "READ")
            nevts += tfile.Get("Counters/Counter").GetBinContent(0)
            tfile.Close()
        hist[s] = []
        effs[s] = []
        for j, c in enumerate(cutlist):
            ss = s + "_%d" % j
            if variable[var]['nbins']>0: hist[s].append( TH1F(ss, ";"+variable[var]['title'], variable[var]['nbins']*5, variable[var]['min'], variable[var]['max']) ) # Init histogram
            else: hist[s].append( TH1F(ss, ";"+variable[var]['title'], len(variable[var]['bins'])-1, array('f', variable[var]['bins'])) )
            hist[s][j].Sumw2()
            effs[s].append( tree[s].Project(ss, var, "eventWeight*("+c+")") / float(nevts) )
            hist[s][j].SetFillColor(sample[s]['fillcolor'])
            hist[s][j].SetFillStyle(sample[s]['fillstyle'])
            hist[s][j].SetLineColor(sample[s]['linecolor'])
            hist[s][j].SetLineStyle(sample[s]['linestyle'])
            if not 'Data' in s: hist[s][j].Scale(LUMI)
            if 'ZZh' in s: hist[s][j].Scale(1.e-2) # Scale to 10 fb
    
    
    hist['BkgSum'] = []
    for j, c in enumerate(cutlist):
        name = 'BkgSum' + "_%d" % j
        hist['BkgSum'].append( hist[back[0]][0].Clone(name) )
        hist['BkgSum'][j].Reset("MICES")
        hist['BkgSum'][j].SetFillStyle(0)
        for i, s in enumerate(back): # Add hist to BkgSum and stack
            hist['BkgSum'][j].Add(hist[s][j])
    
#    for j, c in enumerate(cutlist):
#        c1 = TCanvas("c1", "Signals", 800, 600)
#        c1.cd()
#        hist['BkgSum'][j].Draw("H")
#        for i, s in enumerate(sign): hist[s][j].Draw("SAME, H")
#        if not options.runBash: raw_input("Press Enter to continue...")
    
    for i, s in enumerate(sign):
        psig[s] = [0]*(ncuts+1)
        mass = float( ''.join(x for x in s if x.isdigit()) )
        amean = hist[s][j].GetMean()
        rms = hist[s][j].GetRMS()
        #print hist[s][j].GetName(), amean, rms
        cbin = hist[s][j].FindBin(amean)
        lbin = hist[s][j].FindBin(amean - 2*rms)
        hbin = hist[s][j].FindBin(amean + 2*rms)
        for j, c in enumerate(cutlist):
            n = hist[s][j].Integral(lbin, hbin)
            d = hist['BkgSum'][j].Integral(lbin, hbin)
            psig[s][j] = effs[s][j]/(1.+math.sqrt(d)) #2.*(math.sqrt(n+d) - math.sqrt(d))
    
    line = []
    for j, c in enumerate(cutlist):
        line.append( TGraph(ncuts) )
        line[j].SetTitle(";m_{X} (GeV);Significance")
        line[j].SetTitle("")
        for i, s in enumerate(sign):
            mass = int( ''.join(x for x in s if x.isdigit()) )
            line[j].SetPoint(i, mass, psig[s][j])
        line[j].SetMarkerStyle(20)
        line[j].SetMarkerColor(colors[j])
        line[j].SetLineColor(colors[j])
        line[j].SetLineWidth(3)
        line[j].GetXaxis().SetTitleOffset(line[j].GetXaxis().GetTitleOffset()*1.2)
        line[j].GetYaxis().SetTitleOffset(line[j].GetYaxis().GetTitleOffset()*1.2)
    
    leg = TLegend(0.12, 0.8-0.04*ncuts, 0.55, 0.8)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for i, c in enumerate(cutlist):
        leg.AddEntry(line[i], labellist[i], "lp")
    
    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    #line[0].GetYaxis().SetRangeUser(0., 1.)
    line[0].GetXaxis().SetTitle("m_{X} (GeV)")
    line[0].GetYaxis().SetTitle("Punzi FOM = #varepsilon_{s}/(1+#sqrt{B})") #"Q = 2(#sqrt{S+B}-#sqrt{B}) ")
    for i, s in enumerate(cutlist):
        line[i].Draw("APL" if i==0 else "SAME, PL")
    leg.Draw()
    drawCMS(LUMI, "Simulation")
    
    c1.Print("plots/Signal/sign_"+testname+".png")
    c1.Print("plots/Signal/sign_"+testname+".pdf")
    if not options.runBash: raw_input("Press Enter to continue...")


#signal("X_tmass", "XZZnnbbSR", "SR")
#signal("X_mass", "XWhenbbSR", "WCR")
#signal("X_tmass", "XWhmnbbSR", "WCR")
signal("X.mass", "XVZmmlpSR", "ntuple/tree")
#signal("X_mass", "XZZmmbbSR", "XZZ")


#signal("lepton1_pt", Lcut, "XZZ")
#signal("lepton2_pt", Lcut, "XZZ")
#signal("Z_pt", Lcut, "XZZ")
#signal("fatjet1_pt", Lcut, "XZZ")
#signal("fatjet1_mass", PreLep+" && "+Zcut, "XZZ")
#signal("fatjet1_tau21", PreLep+" && "+Zcut, "XZZ")
#signal("fatjet1_prunedMass", PreLep+" && "+Zcut+" && fatjet1_pt>200", "XZZ")
#signal("fatjet1_softdropMass", PreLep+" && "+Zcut+" && fatjet1_pt>200", "XZZ")
#signal("fatjet1_prunedMassCorr", PreLep+" && "+Zcut+" && fatjet1_pt>200", "XZZ")
#signal("fatjet1_softdropMassCorr", PreLep+" && "+Zcut+" && fatjet1_pt>200", "XZZ")
#btag()


#Ecuts = [TriEle, TriEle+" && "+PreEle, TriEle+" && "+PreEle+" && "+Zcut, TriEle+" && "+PreEle+" && "+Zcut+" && "+Hcut, TriEle+" && "+PreEle+" && "+Zcut+" && "+Hcut+" && "+Bcut]
#Mcuts = [TriMuo, TriMuo+" && "+PreMuo, TriMuo+" && "+PreMuo+" && "+Zcut, TriMuo+" && "+PreMuo+" && "+Zcut+" && "+Hcut, TriMuo+" && "+PreMuo+" && "+Zcut+" && "+Hcut+" && "+Bcut]
#Lcuts = [TriLep, PreLep, PreLep+" && "+Zcut, PreLep+" && "+Zcut+" && "+Hcut, PreLep+" && "+Zcut+" && "+Hcut+" && "+Bcut]
#Llabs = ["Trigger", "Id + Iso", "Z cand", "H mass", "b-tag"]
##efficiency(Lcuts, Llabs, "XZZ")


#Scut = "isZtoLL && "+PreLep+" && "+Zcut

# Mass
#Scuts = [Scut, Scut+" && (fatjet1_softdropMass>90 && fatjet1_softdropMass<145)", Scut+" && (fatjet1_softdropMass>90 && fatjet1_softdropMass<140)", Scut+" && (fatjet1_softdropMass>95 && fatjet1_softdropMass<140)", Scut+" && (fatjet1_softdropMass>95 && fatjet1_softdropMass<135)", Scut+" && (fatjet1_softdropMass>95 && fatjet1_softdropMass<130)", Scut+" && (fatjet1_softdropMass>100 && fatjet1_softdropMass<135)", Scut+" && (fatjet1_softdropMass>100 && fatjet1_softdropMass<130)"]
#Scuts = [Scut, Scut+" && (fatjet1_prunedMass>90 && fatjet1_prunedMass<145)", Scut+" && (fatjet1_prunedMass>90 && fatjet1_prunedMass<140)", Scut+" && (fatjet1_prunedMass>95 && fatjet1_prunedMass<140)", Scut+" && (fatjet1_prunedMass>95 && fatjet1_prunedMass<135)", Scut+" && (fatjet1_prunedMass>95 && fatjet1_prunedMass<130)", Scut+" && (fatjet1_prunedMass>100 && fatjet1_prunedMass<135)", Scut+" && (fatjet1_prunedMass>100 && fatjet1_prunedMass<130)"]
#Slabs = ["no cut (pruned)", "90<m_{j}<145 GeV", "90<m_{j}<140 GeV", "95<m_{j}<140 GeV", "95<m_{j}<135 GeV", "95<m_{j}<130 GeV", "100<m_{j}<135 GeV", "100<m_{j}<130 GeV"]
#Scuts = [Scut, Scut+" && (fatjet1_prunedMassCorr>90 && fatjet1_prunedMassCorr<135)", Scut+" && (fatjet1_prunedMassCorr>90 && fatjet1_prunedMassCorr<140)", Scut+" && (fatjet1_prunedMassCorr>95 && fatjet1_prunedMassCorr<135)", Scut+" && (fatjet1_prunedMassCorr>100 && fatjet1_prunedMassCorr<130)", Scut+" && (fatjet1_prunedMassCorr>105 && fatjet1_prunedMassCorr<135)", Scut+" && (fatjet1_prunedMassCorr>105 && fatjet1_prunedMassCorr<140)", Scut+" && (fatjet1_prunedMassCorr>105 && fatjet1_prunedMassCorr<145)"]
#Slabs = ["no cut (pruned)", "90<m_{j}<135 GeV", "90<m_{j}<140 GeV", "95<m_{j}<135 GeV", "100<m_{j}<130 GeV", "105<m_{j}<135 GeV", "105<m_{j}<140 GeV", "105<m_{j}<145 GeV"]
#significance(Scut, Scuts, Slabs, Sname)


#Scut = "isZtoLL && "+PreLep+" && "+Zcut+" && "+Hcut

## Btag
#Scuts = [Scut, Scut+" && fatjet1_CSV>0.605", Scut+" && fatjet1_CSV>0.890", Scut+" && fatjet1_CSV>0.970", Scut+" && fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605", Scut+" && fatjet1_CSV1>0.890 && fatjet1_CSV2>0.890", Scut+" && fatjet1_CSV1>0.970 && fatjet1_CSV2>0.970"] #, Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV>0.605)"
#Slabs = ["No b-tag", "fat-jet CSVL", "fat-jet CSVM", "fat-jet CSVT", "sub-jet CSVLL", "sub-jet CSVMM", "sub-jet CSVTT"] #, "sub/fat-jet CSVLL/L"
#Sname = "btagDefault"
#significance(Scut, Scuts, Slabs, Sname)

## Switch Sub/Fat-jet
#Scuts = [Scut, Scut+" && fatjet1_CSV>0.605", Scut+" && fatjet1_CSV>0.890", Scut+" && fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605", Scut+" && fatjet1_CSV1>0.890 && fatjet1_CSV2>0.890", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV>0.605)", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.890 && fatjet1_CSV2>0.890 : fatjet1_CSV>0.890)"]
#Slabs = ["No b-tag", "fat-jet CSVL", "fat-jet CSVM", "sub-jet CSVLL", "sub-jet CSVMM", "sub/fat-jet CSVLL/L", "sub/fat-jet CSVMM/M"]
#Sname = "btagSubFat"
#significance(Scut, Scuts, Slabs, Sname)

## Btag Ultraloose
#Scuts = [Scut, Scut+" && fatjet1_CSV>0.3", Scut+" && fatjet1_CSV>0.605", Scut+" && fatjet1_CSV1>0.3 && fatjet1_CSV2>0.3", Scut+" && fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.3 && fatjet1_CSV2>0.3 : fatjet1_CSV>0.3)", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV>0.605)"]
#Slabs = ["No b-tag", "fat-jet CSVU", "fat-jet CSVL", "sub-jet CSVUU", "sub-jet CSVLL", "sub/fat-jet CSVUU/U", "sub/fat-jet CSVLL/L"]
#Sname = "btagUltra"
#significance(Scut, Scuts, Slabs, Sname)

## Btag asymm
#Scuts = [Scut, Scut+" && fatjet1_CSV>0.605", Scut+" && fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV>0.605)", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)", Scut+" && fatjet1_CSV>0.3", Scut+" && fatjet1_CSV1>0.3 && fatjet1_CSV2>0.3", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.3 && fatjet1_CSV2>0.3 : fatjet1_CSV>0.3)", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.3 && fatjet1_CSV2>0.3 : fatjet1_CSV1>0.3 || fatjet1_CSV2>0.3)"]
#Slabs = ["No b-tag", "fat-jet CSVL", "sub-jet CSVLL", "sub/fat-jet CSVLL/L", "sub-jet CSVL(L)", "fat-jet CSVU", "sub-jet CSVUU", "sub/fat-jet CSVUU/U", "sub-jet CSVU(U)"]
#Sname = "btagAsymm"
#significance(Scut, Scuts, Slabs, Sname)

## Btag dR
#Scuts = [Scut, Scut+" && (fatjet1_dR>0.2 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)", Scut+" && (fatjet1_dR>0.25 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)", Scut+" && (fatjet1_dR>0.3 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)", Scut+" && (fatjet1_dR>0.35 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)", Scut+" && (fatjet1_dR>0.4 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)", Scut+" && (fatjet1_dR>0.5 ? fatjet1_CSV1>0.605 && fatjet1_CSV2>0.605 : fatjet1_CSV1>0.605 || fatjet1_CSV2>0.605)"]
#Slabs = ["No b-tag", "sub-jet CSVL(L) #Delta R=0.2", "sub-jet CSVL(L) #Delta R=0.25", "sub-jet CSVL(L) #Delta R=0.3", "sub-jet CSVL(L) #Delta R=0.35", "sub-jet CSVL(L) #Delta R=0.4", "sub-jet CSVL(L) #Delta R=0.5"]
#Sname = "btagDR"
#significance(Scut, Scuts, Slabs, Sname)

##Scut = "isZtoLL && "+PreLep+" && "+Zcut+" && "+Hcut+" && "+Bcut

## Tau21
#Scuts = [Scut, Scut+" && fatjet1_tau21<0.3", Scut+" && fatjet1_tau21<0.4", Scut+" && fatjet1_tau21<0.45", Scut+" && fatjet1_tau21<0.5", Scut+" && fatjet1_tau21<0.55", Scut+" && fatjet1_tau21<0.6", Scut+" && fatjet1_tau21<0.7"]
#Slabs = ["no cut", "#tau_{21}<0.3", "#tau_{21}<0.4", "#tau_{21}<0.45", "#tau_{21}<0.5", "#tau_{21}<0.55", "#tau_{21}<0.6", "#tau_{21}<0.7"]
#Sname = "tau21"
#significance(Scut, Scuts, Slabs, Sname)

