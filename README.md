# Lambda
Nanoaod Plotter

## Setup With NanoAODTools tools
```
# Standalone
cd NanoAODTools/python
git clone git@github.com:LambdaFramework/LambPlot.git
# or checkout dfdev to use RDataFrame, ITS FAST
# git clone git@github.com:LambdaFramework/LambPlot.git -b dfdev

# CMSSW
cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python
git clone git@github.com:LambdaFramework/LambPlot.git
# or checkout dfdev to use RDataFrame, ITS FAST
# git clone git@github.com:LambdaFramework/LambPlot.git -b dfdev
```

## Plotting command

Consults ```python scripts/plotter.py```

```
python scripts/plotter.py -v MHT_pt -r OSmumu -e Run2_2016_v4
```
