from Dataset import *

era = Run2_16_nanov0

samples = {
    'data_obs' : {
        'order' : 0,
        'files' : [ x.filename() for x in era if x.name() == 'data_obs' ],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToLL' : {
        'order' : 1,
        'files' : [ x.filename() for x in era if x.name() == 'DYJetsToLL' ],
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToLL_HT' : {
            'order' : 1,
            'files' : [ x.filename() for x in era if x.name() == 'DYJetsToLL_HT' ],
            'fillcolor' : 418,
            'fillstyle' : 1001,
            'linecolor' : 418,
            'linewidth' : 2,
            'linestyle' : 1,
            'label' : "Z(ll) + jets",
            'weight': 1.,
            'plot': True,
    },
    'DYJetsToLL_Pt' : {
        'order' : 2,
        'files' : [ x.filename() for x in era if x.name() == 'DYJetsToLL_Pt' ],
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
        },
    'WJetsToLNu' : {
        'order' : 3,
        'files' : [ x.filename() for x in era if x.name() == 'WJetsToLNu' ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W(l#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'WJetsToLNu_HT' : {
        'order' : 3,
        'files' : [ x.filename() for x in era if x.name() == 'WJetsToLNu_HT' ],
	    'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W(l#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'TTbar' : {
        'order' : 4,
        'files' : [ x.filename() for x in era if x.name() == 'TTbar' ],
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",#, single t
        'weight': 1.,
        'plot': True,
    },
    'TTbar-DiLept' : {
        'order' : 4,
        'files' : [ x.filename() for x in era if x.name() == 'TTBar-DiLept' ],
        'fillcolor' : 41,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t} di-lept",#, single t
        'weight': 1.,
        'plot': True,
    },
    'TTbar-SL' : {
        'order' : 4,
        'files' : [ x.filename() for x in era if x.name() == 'TTbar-SL' ],
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t} sing.lept",
        'weight': 1.,
        'plot': True,
    },
    'ST' : {
        'order' : 5,
        'files' : [ x.filename() for x in era if x.name() == 'ST' ],
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Single-t",
        'weight': 1.,
        'plot': True,
        },
    'WZ' : {
        'order' : 7,
        'files' : [ x.filename() for x in era if x.name() == 'WZ' ],
        'fillcolor' : 602,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "WZ",
        'weight': 1.,
        'plot': True,
        },
     'WW' : {
        'order' : 9,
        'files' : [ x.filename() for x in era if x.name() == 'WW' ],
        'fillcolor' : 7,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W+W-",
        'weight': 1.,
        'plot': True,
        },
    'ZZ' : {
        'order' : 8,
        'files' : [ x.filename() for x in era if x.name() == 'ZZ' ],
        'fillcolor' : 9,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ZZ",
        'weight': 1.,
        'plot': True,
        },
    'VV' : {
        'order' : 8,
        'files' : [ x.filename() for x in era if x.name() == 'VV' ],
        'fillcolor' : 9,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "WW, WZ, ZZ",
        'weight': 1.,
        'plot': True,
    },
    'ttH' : {
        'order' : 10,
        'files' : [ x.filename() for x in era if x.name() == 'ttH' ],
        'fillcolor' : 30,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ttH",
        'weight': 1.,
        'plot': True,
        },
    'ttV' : {
        'order' : 10,
        'files' : [ x.filename() for x in era if x.name() == 'ttV' ],
        'fillcolor' : 38,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ttW,ttZ,ttH",
        'weight': 1.,
        'plot': True,
        },
    'VVV' : {
        'order' : 11,
        'files' : [ x.filename() for x in era if x.name() == 'VVV' ],
        'fillcolor' : 46,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "WWW,WWZ,ZZZ",
        'weight': 1.,
        'plot': True,
        },
    'WWJJ' : {
        'order' : 9,
        'files' : [ x.filename() for x in era if x.name() == 'WWJJ' ],
        'fillcolor' : 8,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W+W+,W-W-",
        'weight': 1.,
        'plot': True,
        },
    'VGamma' : {
        'order' : 6,
        'files' : [ x.filename() for x in era if x.name() == 'VGamma' ],
        'fillcolor' : 42,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W#gamma,Z#gamma",
        'weight': 1.,
        'plot': True,
        },
    #Signal
    'WHWWm' : {
        'order' : 1001,
        'files' : [ x.filename() for x in era if x.name() == 'WHWW' ],
        'fillcolor' : 623,
        'fillstyle' : 3005,
        'linecolor' : 632,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "WmHWW",
        'weight': 1.,
        'plot': True,
        },
    'WHWWp' : {
        'order' : 1001,
        'files' : [ x.filename() for x in era if x.name() == 'WHWW' ],
        'fillcolor' : 623,
        'fillstyle' : 3005,
        'linecolor' : 632,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "WpHWW",
        'weight': 1.,
        'plot': True,
        },
    'QCD' : {
        'order' : 6,
        'files' : [ x.filename() for x in era if x.name() == 'QCD' ],
	    'fillcolor' : 921,
        'fillstyle' : 1001,
        'linecolor' : 921,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "multijet",
        'weight': 1.,
        'plot': True,
    },
    'tZq' : {
        'order' : 12,
        'files' : [ x.filename() for x in era if x.name() == 'tZq' ],
        'fillcolor' : 30,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "tZq",
        'weight': 1.,
        'plot': True,
    },
    ## Signal
    'Wm': {
        'order' : 0,
        'files' : [ x.filename() for x in era if x.name() == 'Wm' ],
        'fillcolor' : 2,
        'fillstyle' : 3003,
        'linecolor' : 2,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W^{-}H(l^{-}l^{-}#tilde{#nu}#tilde{#nu}jj)",
        'weight': 1.,
        'plot': True,
        },
    'Wp': {
        'order' : 0,
        'files' : [ x.filename() for x in era if x.name() == 'Wp' ],
        'fillcolor' : 4,
        'fillstyle' : 3003,
        'linecolor' : 4,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W^{+}H(l^{+}l^{+}#nu#nujj)",
        'weight': 1.,
        'plot': True,
    },
    # Dummy entry for background sum
    'BkgSum' : {
        'order' : 0,
        'files' : [],
        'fillcolor' : 1,
        'fillstyle' : 3003,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "MC stat.",
        'weight': 1.,
        'plot': True,
    },
}
