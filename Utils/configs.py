from PhysicsTools.NanoAODTools.LambPlot.Utils.color import *
from PhysicsTools.NanoAODTools.postprocessing.modules.datasets import *
import os

class Config(object):

    def __init__(self,era):

        #Analysis parameters
        self._year = era.split('_')[1]
        self._lumi = datasets['%s' %era.split('_')[1]]['lumi']


    def register(self,samples):
        self._samples=samples
        
        #Cosmetics
        self._samplelist ={}
        for isample in self._samples:
            self._samplelist[isample]={}
            self._samplelist[isample]['order']=0 if isample=='data_obs' else schemebkg[isample]['order']
            self._samplelist[isample]['files']=map(lambda x : x.filename(), filter(lambda x : x.name()==isample , list(datasets[era]['data']) + list(datasets[era]['mc']) ))
            self._samplelist[isample]['fillcolor']= scheme[isample]['fillcolor']
            self._samplelist[isample]['fillstyle']= scheme[isample]['fillstyle']
            self._samplelist[isample]['linecolor']= scheme[isample]['fillcolor']
            self._samplelist[isample]['linewidth']= 2
            self._samplelist[isample]['linestyle']=1
            self._samplelist[isample]['label']= scheme[isample]['label']
            self._samplelist[isample]['weight']=1.
            self._samplelist[isample]['plot']=True
            
        #for idataset in datasets[era]['data']:
        #    sample['%s'%idataset.filename()] ={}
        #    sample['%s'%idataset.filename()]['nevents'] = idataset.nevent()
        #    sample['%s'%idataset.filename()]['xsec'] = idataset.xsec()
        #    sample['%s'%idataset.filename()]['kfactor'] = idataset.kfactor()
        #    sample['%s'%idataset.filename()]['matcheff'] = idataset.matcheff()
        #for idataset in datasets[era]['mc']:
        #    sample['%s'%idataset.filename()] ={}
        #    sample['%s'%idataset.filename()]['nevents'] = idataset.nevent()
        #    sample['%s'%idataset.filename()]['xsec'] = idataset.xsec()
        #    sample['%s'%idataset.filename()]['kfactor'] = idataset.kfactor()
        #    sample['%s'%idataset.filename()]['matcheff'] = idataset.matcheff()


    def lumi(self):
        return self._lumi
    def getSamplelist(self):
        return self._samples

    def summary(self):

        print "-"*80
        print YELLOW+"Era configured : "+ENDC, OKGREEN+ self._year +ENDC
        print YELLOW+"Integrated luminosity configured : "+ENDC, OKGREEN+str( self._lumi ), " pb/-1"+ENDC
        print YELLOW+"NTUPLE configured : "+ENDC, OKGREEN+ self._ntuple +ENDC
        #print col.YELLOW+"DATASET configured : "+col.ENDC, col.OKGREEN+ self._dataset +col.ENDC
        print "-"*80
    
