from PhysicsTools.NanoAODTools.LambPlot.Utils.color import *
from PhysicsTools.NanoAODTools.plotConfiguration.WH_SS.Full2016nanov6.samples import samples
from PhysicsTools.NanoAODTools.plotConfiguration.WH_SS.Full2016nanov6.plot import groupPlot , plot

#from PhysicsTools.NanoAODTools.postprocessing.modules.analysis.datasets import *

import os

class Config(object):

    def __init__(self,era):

        #Analysis parameters
        self._era = era
        self._year = era.split('_')[-1]
        if self._year == '2016' : self._lumi = 35800. #pb-1
        if self._year == '2017' : self._lumi = 41500. #pb-1
        if self._year == '2018' : self._lumi = 68000. #pb-1
        self._groupPlot = {}

    def register(self,samples_):

        # build group list structure
        for i, igroup in enumerate(samples_):
            if igroup == 'DATA': continue
            species = groupPlot[igroup]['isSignal']
            #fil_samples = filter( lambda y : y in samples_ , groupPlot[igroup]['samples'] )
            #for itag in map( lambda x : samples[x]['name']  , fil_samples  ) : samplelist+=itag
            self._groupPlot[igroup]              = {}            
            self._groupPlot[igroup]['order']     = i
            self._groupPlot[igroup]['samples']   = groupPlot[igroup]['samples']
            self._groupPlot[igroup]['fillcolor'] = groupPlot[igroup]['color']
            self._groupPlot[igroup]['fillstyle'] = 1001 if species == 0 else 3003
            self._groupPlot[igroup]['linecolor'] = groupPlot[igroup]['color']
            self._groupPlot[igroup]['linewidth'] = 2
            self._groupPlot[igroup]['linestyle'] = 1
            self._groupPlot[igroup]['label']     = groupPlot[igroup]['nameHR']
            self._groupPlot[igroup]['weight']    = 1.
            self._groupPlot[igroup]['plot']      = True


        #DATA
        if 'DATA' in samples_:
            self._groupPlot['DATA'] ={}
            self._groupPlot[igroup]['order']     = 0
            self._groupPlot[igroup]['samples']   = samples['DATA']['name']
	    self._groupPlot[igroup]['fillcolor'] = plot['DATA']['color']
            self._groupPlot[igroup]['fillstyle'] = 1
            self._groupPlot[igroup]['linecolor'] = 0
            self._groupPlot[igroup]['linewidth'] = 2
            self._groupPlot[igroup]['linestyle'] = 1
            self._groupPlot[igroup]['label']     = plot['DATA']['nameHR']
            self._groupPlot[igroup]['weight']    = 1.
            self._groupPlot[igroup]['plot']      = True

        
        #BKGSUM
        self._groupPlot['BkgSum'] ={}
        self._groupPlot['BkgSum']['order']     = 0
        self._groupPlot['BkgSum']['samples']   = []
        self._groupPlot['BkgSum']['fillcolor'] = 1
        self._groupPlot['BkgSum']['fillstyle'] = 1001
        self._groupPlot['BkgSum']['linecolor'] = 1
        self._groupPlot['BkgSum']['linewidth'] = 2
        self._groupPlot['BkgSum']['linestyle'] = 1
        self._groupPlot['BkgSum']['label']     = 'MC. stat.'
        self._groupPlot['BkgSum']['weight']    = 1.
        self._groupPlot['BkgSum']['plot']      = True
        

    def era(self):
        return self._era
    def lumi(self):
        return self._lumi
    def getGroupPlot(self):
        return self._groupPlot

    def summary(self):

        print "-"*80
        print YELLOW+"Era configured : "+ENDC, OKGREEN+ self._year +ENDC
        print YELLOW+"Integrated luminosity configured : "+ENDC, OKGREEN+str( self._lumi ), " pb/-1"+ENDC
        #print YELLOW+"NTUPLE configured : "+ENDC, OKGREEN+ self._ntuple +ENDC
        #print col.YELLOW+"DATASET configured : "+col.ENDC, col.OKGREEN+ self._dataset +col.ENDC
        print "-"*80
