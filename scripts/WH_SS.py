'''
    if len(args) == 0 and not options.multiprocessing and not options.cutflow:
        print "None argument provided, plotting on all variables in ", VOI
        if options.cut=="":
            for region in [ 'OSmumu', 'OSee', 'OSemu', 'SSemu', 'SSmumu', 'SSee' ]:
                print col.CYAN+"PLOTTING on : ",region+col.ENDC
                for VARS in VOI:
                    start_time = time.time()
                    print col.OKGREEN+"PLOTTING on : ",VARS+col.ENDC
                    plot(VARS,region)
                    print("--- %s seconds ---" % (time.time() - start_time))
                    print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
                    print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
        else:
            print col.CYAN+"PLOTTING on : ",options.cut+col.ENDC
            for VARS in VOI:
                start_time = time.time()
                print col.OKGREEN+"PLOTTING on : ",VARS+col.ENDC
                plot(VARS,options.cut)
                print("--- %s seconds ---" % (time.time() - start_time))
                print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
                print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
    elif options.printVar:
        print "Print all available variable specified"
        print [ var for var in variable ]
    elif options.cutflow:
        print "Cutflow table"
        if options.cut=="":
            print "ERROR: Please specify cut , python lambdaPlot.py VAR -u -c CUT "
            exit()

        cutlet = selection[options.cut].split(' && ')
        #cutflow(cutlet,options.cut)
        significanceStudy(cutlet,options.cut)
    elif options.multiprocessing and len(args) == 0:
        print col.OKGREEN+"core available : ", cpu_count(),", which means ", cpu_count()," processes can be distributedly processed in parallel."+col.ENDC
        #Region=[ 'OSmumu', 'OSee', 'OSemu', 'SSemu', 'SSmumu', 'SSee', 'WZCR', 'VgCR' ]
        Region=[ 'OSmumu', 'OSee', 'OSemu', 'SSemu', 'SSmumu', 'SSee', 'WZCR' ]
        start_time = time.time()
        for voi in VOI:
            p = Pool(processes=8)
            plotter=partial(multiplot,var=voi)
            #result = p.map(partial(plot, var=voi), Region)
            result = p.map(plotter, Region)
        p.close()
        p.join()
        print "multiprocessing complete, with time taken : "
        print("--- %s seconds ---" % (time.time() - start_time))
        print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
        print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
    else:
        start_time = time.time()
        print col.OKGREEN+"PLOTTING: ", args[0]+col.ENDC
        print col.CYAN+"PLOTTING on : ",options.cut+col.ENDC
        plot(args[0], options.cut)
        print("--- %s seconds ---" % (time.time() - start_time))
        print("--- %s minutes ---" % ( (time.time() - start_time)/60. ))
        print("--- %s hours ---" % ( (time.time() - start_time)/3600. ))
'''
