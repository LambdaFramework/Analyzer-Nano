class Dataset(object):

    def __init__(self, name, filename, nevent, xsec, kfactor, matcheff=1):
        self._name      = name
        self._filename  = filename
        self._nevent    = nevent
        self._xsec      = xsec
        self._kfactor   = kfactor
        self._matcheff  =  matcheff
    pass

    def name(self):
        return self._name
    def filename(self):
        return self._filename
    def nevent(self):
        return self._nevent
    def xsec(self):
        return self._xsec
    def kfactor(self):
        return self._kfactor
    def matcheff(self):
        return self._matcheff
    pass

Run2_16_nanov0 = [
    ## Data
    ### SingleMuon

    Dataset('data_obs'   ,"SingleMuonRun2016B-03Feb2017_ver1-v1",  2789243    ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016B-03Feb2017_ver2-v2",  158145722  ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016C-03Feb2017-v1"   ,  67441308   ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016D-03Feb2017-v1"   ,  98017996   ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016E-03Feb2017-v1"   ,  90984718   ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016F-03Feb2017-v1"   ,  65425108   ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016G-03Feb2017-v1"   ,  149916849  ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016H-03Feb2017_ver2-v1",  171134793  ,  1.0  ,  1.0 ),
    Dataset('data_obs'   ,"SingleMuonRun2016H-03Feb2017_ver3-v1",  4393222    ,  1.0  ,  1.0 ),
    ### SingleElectron
    Dataset('data_obs' ,"SingleElectronRun2016B-03Feb2017_ver1-v1",  1422819  ,  1.0  ,  1.0 ),
    Dataset('data_obs' ,"SingleElectronRun2016B-03Feb2017_ver2-v2",  246440440  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016B-03Feb2017_ver2-v2_1",  246440440  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016C-03Feb2017-v1"    ,  97259854  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016D-03Feb2017-v1"    ,  148167727  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016E-03Feb2017-v1"    ,  117321545  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016F-03Feb2017-v1"    ,  70593532  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016G-03Feb2017-v1"    ,  153363109  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016H-03Feb2017_ver2-v1",  126863489  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"SingleElectronRun2016H-03Feb2017_ver3-v1",  3191585  ,  1.0  ,  1.0  ),

    ### DoubleMuon
    Dataset('data_obs' ,"DoubleMuonRun2016B-03Feb2017_ver2-v2",  82535526  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016C-03Feb2017-v1",  27934629  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016D-03Feb2017-v1",  33861745  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016E-03Feb2017-v1",  28246946  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016F-03Feb2017-v1",  20329921  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016G-03Feb2017-v1",  45235604  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016H-03Feb2017_ver2-v1",  47693168  ,  1.0  ,  1.0  ),
    Dataset('data_obs' ,"DoubleMuonRun2016H-03Feb2017_ver3-v1",  1219644  ,  1.0  ,  1.0  ),

    ##DY
    Dataset('DYJetsToLL' ,"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1",  26156930  ,  9000  ,  1  ),
    Dataset('DYJetsToLL' ,"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v2",  49144270  ,  6025.0  ,  1.0  ),
    Dataset('DYJetsToLL_Pt' ,"DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext5-v1",  75457970  ,  78.325  ,  1.0  ),
    Dataset('DYJetsToLL_Pt' ,"DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext5-v1",  19575950  ,  3.31375  ,  1.0  ),
    Dataset('DYJetsToLL_Pt' ,"DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext2-v1",  604038  ,  0.451875  ,  1.0  ),
    Dataset('DYJetsToLL_Pt' ,"DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext2-v1",  597526  ,  0.054225  ,  1.0  ),

    ##WJets
    Dataset('WJetsToLNu' ,"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1",  21978040  ,  61530  ,  1.0  ),
    Dataset('WJetsToLNu_HT' ,"WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2-v1",  39617790  ,  3384.15  ,  1.395  ),
    Dataset('WJetsToLNu_HT' ,"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2-v1",  19914590  ,  738.36  ,  1.526  ),
    Dataset('WJetsToLNu_HT' ,"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1",  5796237  ,  92.295  ,  1.679  ),
    Dataset('WJetsToLNu_HT' ,"WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1",  14908340  ,  7.3836  ,  1.442  ),
    Dataset('WJetsToLNu_HT' ,"WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1",  10094300  ,  3691.18  ,  1.0  ),
    Dataset('WJetsToLNu_HT' ,"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1",  6069652  ,  3.19956  ,  1.442  ),

    ##TTbar-DiLep
    #Dataset('TTbar' ,"TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1",  23637880  ,  92.4177777778  ,  1.0  ),
    #Dataset('TTbar' ,"TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1",  50016940  ,  180.990976  ,  1.0  ),
    #Dataset('TTbar' ,"TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1",  48266350  ,  180.990976  ,  1.0  ),

    ##ST
    Dataset('ST' ,"ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v1",  1000000.0  ,  3.45  ,  1.0  ),
    Dataset('ST' ,"ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v1",  5922361  ,  27.1  ,  1.0  ),
    Dataset('ST' ,"ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v1",  11108070  ,  27.1  ,  1.0  ),
    Dataset('ST' ,"ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1-v1",  5425134.0  ,  19.99623375  ,  1.0  ),
    Dataset('ST' ,"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v1",  6933094  ,  35.85  ,  1.0  ),
    Dataset('ST' ,"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4-v1",  5435134  ,  20  ,  1.0  ),
    Dataset('ST' ,"ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1-v1",  5372991.0  ,  19.99623375  ,  1.0  ),
    Dataset('ST' ,"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4-v1",  5372991  ,  20  ,  1.0  ),

    ## WZ
    Dataset('WZ' ,"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1",  11887460  ,  4.4  ,  1.0  ),
    #Dataset('WZ' ,"WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8-v1",  11887460  ,  4.4  ,  1.0  ),

    ## WW
    Dataset('WW' ,"WW_TuneCUETP8M1_13TeV-pythia8-v1",  7981136  ,  118  ,  1.0  ),
    Dataset('WW' ,"WW_TuneCUETP8M1_13TeV-pythia8_ext1-v1",  7981136  ,  118  ,  1.0  ),

    ## WWJJ
    Dataset('WWJJ' ,"WpWpJJ_13TeV-powheg-pythia8_TuneCUETP8M1-v1",  146600  ,  0.03339  ,  1.0  ),
    Dataset('WWJJ' ,"WmWmJJ_13TeV-powheg-pythia8_TuneCUETP8M1-v1",  150000  ,  0.0110187  ,  1.0  ),

    ## ZZ
    #Dataset('ZZ' ,"ZZ_TuneCUETP8M1_13TeV-pythia8-v1",  1988088  ,  16.9  ,  1.0  ),
    #Dataset('ZZ' ,"ZZ_TuneCUETP8M1_13TeV-pythia8_ext1-v1",  1988088  ,  16.9  ,  1.0  ),
    Dataset('ZZ' ,"ZZTo2L2Nu_13TeV_powheg_pythia8-v1",  8655000  ,  0.564  ,  1.0  ),
    Dataset('ZZ' ,"ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1",  15345572  ,  3.22  ,  1.0  ),
    Dataset('ZZ' ,"ZZTo4L_13TeV-amcatnloFXFX-pythia8_ext1-v1",  10709784  ,  1.212  ,  1.0  ),

    ##ttV
    Dataset('ttV' ,"ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8-v1",  3389728  ,  0.0546  ,  1  ),
    Dataset('ttV' ,"ttHTobb_M125_13TeV_powheg_pythia8-v1",  3236762  ,  0.0754  ,  1  ),
    Dataset('ttV' ,"TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_ext1-v3",  236047  ,  0.204  ,  1.0  ),
    Dataset('ttV' ,"TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_ext1-v1",  1115478  ,  0.253  ,  1.0  ),

    ## WHWW
    Dataset('WHWWm' ,"HWminusJ_HToWW_M125_13TeV_powheg_pythia8-v1",  599796  ,  0.312  ,  1  ),
    Dataset('WHWWp' ,"HWplusJ_HToWW_M125_13TeV_powheg_pythia8-v1",  599796  ,  0.312  ,  1  ),
    #Dataset('WHWW' ,"HWminusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8-v1",  599796  ,  0.312  ,  1  ),
    #Dataset('WHWW' ,"HWplusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8-v1",  599796  ,  0.312  ,  1  ),

    ## VVV
    Dataset('VVV' ,"WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8-v1",  250000  ,  0.1651  ,  1.0  ),
    Dataset('VVV' ,"WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8-v1",  240000  ,  0.2086  ,  1.0  ),
    Dataset('VVV' ,"ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8-v1",  249237  ,  0.01398  ,  1.0  ),

    ##VGamma
    Dataset('VGamma' ,"WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext1-v1",  5048470  ,  586  ,  1.0  ),
    Dataset('VGamma' ,"ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1",  2307158  ,  131  ,  1.0  ),

    ##tZq
    #Dataset('tZq' ,"tZq_ll_4f_13TeV-amcatnlo-pythia8-v1",  13656784  ,  0.0758  ,  1.0  ),
    Dataset('tZq' ,"tZq_ll_4f_13TeV-amcatnlo-pythia8_ext1-v1",  200000  ,  0.0758  ,  1.0  ),

    ##Signal
    Dataset('Wm' ,"Wminushwwlvjj_M125_Madspin_Skim",  300000  ,  0.0069905587717  ,  1.0  ),
    Dataset('Wp' ,"Wplushwwlvjj_M125_Madspin_Skim",  300000  ,  0.0110211512166  ,  1.0  ),

]
