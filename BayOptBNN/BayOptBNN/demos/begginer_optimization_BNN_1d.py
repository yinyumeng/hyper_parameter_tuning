# Copyright (c) 2015, Javier Gonzalez
# Copyright (c) 2015, the GPy Authors (see GPy AUTHORS.txt)
# Licensed under the BSD 3-clause license (see LICENSE.txt)


"""
This is a simple demo to demonstrate the use of Bayesian optimization with BO_BNN with some simple options. Run the example by writing:

import BO_BNN
BO_demo_1d = BO_BNN.demos.begginer_optimization_1d()

As a result you should see:

- A plot with the model and the current acquisition function
- A plot with the diagnostic plots of the optimization.
- An object call BO_demo_1d that contains the results of the optimization process (see reference manual for details). Among the available results you have access to the GP model via

>> BO_demo_1d.model

and to the location of the best found location writing.

BO_demo_1d.x_opt

"""

def begginer_optimization_1d(plots=True):

    import BayOptBNN
    from numpy.random import seed
    seed(1234)
    
    # --- Objective function
    objective_true  = BayOptBNN.fmodels.experiments1d.forrester()              # true function
    objective_noisy = BayOptBNN.fmodels.experiments1d.forrester(sd= .25)       # noisy version
    bounds = [(0,1)]                                                        # problem constrains 

    # --- Problem definition and optimization
    BO_demo_1d = BayOptBNN.methods.BayesianOptimizationBNN(f=objective_noisy.f,   # function to optimize
                                                    bounds=bounds,          # box-constrains of the problem
                                                    acquisition='EI')       # Selects the Expected improvement
    # Run the optimization for 15 iterations
    max_iter = 15                                                           

    print '-----'
    print '----- Running demo. It may take a few seconds.'
    print '-----'
    
    # Run the optimization                                                  
    BO_demo_1d.run_optimization(max_iter,                                   # evaluation budget
                                    eps=10e-6)                              # stop criterion
                            

    # --- Plots
    if plots:
        objective_true.plot()
        BO_demo_1d.plot_acquisition("bnn_acquisition_final.pdf")
        BO_demo_1d.plot_convergence("bnn_covergence_final.pdf")
    BO_demo_1d.save_report()
        
    return BO_demo_1d

if __name__=='__main__':
    begginer_optimization_1d()