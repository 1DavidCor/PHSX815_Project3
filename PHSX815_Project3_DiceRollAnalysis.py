# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:23:13 2021

@author: d338c921
"""

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# main function for our dice roll analysis Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: \n -input_file [filename]")
        print
        sys.exit(1)

  
    if '-input_file' in sys.argv:
        p = sys.argv.index('-input_file')
        input_filename = str((sys.argv[p+1]))
        
    #read the .txt file
    rolls = np.loadtxt(input_filename, dtype = int)
    
    #store the size of the array 
    Nexp, num_rolls = rolls.shape
    
    #find the probability associated with each face in each experiment, and then in the whole set of experiments
    
    #A histogram with 6 bins and range = (1, 6), will count the number of times each face appears in each experiment
    #Ex: Histogram[0, :] = [0, 12, 35, 3, 0, 0] means we saw 1: 0 times, 2: 12 times, 3: 35 times, 4: 3 times, 5: 0 times, and 6: 0 times in Experiment #1
    #We can use this to create an array for the probabilities associated with each face in each experiment by dividing each Histogram[i,:] by num_rolls
    
    Histogram = np.ndarray((Nexp, 6), dtype = int)
    probs = np.ndarray((Nexp, 6), dtype = float)
    for i in range(Nexp):
        Histogram[i,:] = np.histogram(rolls[i, :], bins = 6, range = (1, 6))[0]
        probs[i, :] = Histogram[i,:] / num_rolls
    
    #How many rolls/experiments do we have to do to determine the probabilities within a certain confidence level???
    
    #fit a gaussian to a histogram of the probabilities for each face; store mu and sigma; use sigma as the uncertainty!!!
    mu_face = []
    sig_face = []
    for i in range(6):
        plt.figure()
        plt.xlabel("Probability")
        plt.ylabel("# of occurences")
        mu, sigma = stats.norm.fit(probs[:, i])
        plt.title("# of " + str(i+1) + " rolls")
        plt.xlim(mu - 3*sigma, mu + 3*sigma)
        plt.ylim(0, np.max(stats.norm.pdf(np.linspace(mu - 0.5, mu + 0.5, 100), mu, sigma)))
        mu_face = np.append(mu_face, mu)
        sig_face = np.append(sig_face, sigma)
        n, bins, patches = plt.hist(probs[:, i], bins = 100, range = (0, 1), density = True)
        plt.plot(np.linspace(mu - 0.5, mu + 0.5, 100), stats.norm.pdf(np.linspace(mu - 0.5, mu + 0.5, 100), mu, sigma))
        plt.axvline(mu, linestyle = "--", color = "r", label = "mean")
        plt.axvline(mu - sigma, linestyle = "--", color = "g", label = "mean +/- sigma")
        plt.axvline(mu + sigma, linestyle = "--", color = "g")
        plt.legend()
        plt.show()
        
    
    #Compare probabilities from individual experiments to those from the entire set
    prob_set = np.histogram(rolls, bins = 6, range = (1,6))[0] / num_rolls / Nexp
    plt.figure()
    plt.title("Probabilities of Rolling Each Face (Calc. for each Experiment)")
    plt.xlabel("Face #")
    plt.ylabel("Probability")
    plt.scatter(np.full(Nexp, 1), probs[:, 0])
    plt.scatter(np.full(Nexp, 2), probs[:, 1])
    plt.scatter(np.full(Nexp, 3), probs[:, 2])
    plt.scatter(np.full(Nexp, 4), probs[:, 3])
    plt.scatter(np.full(Nexp, 5), probs[:, 4])
    plt.scatter(np.full(Nexp, 6), probs[:, 5])
    plt.show()
    
    print("Probabilities and Uncertainties of Each Face: \n")
    print("Face 1: " + str(np.round(prob_set[0], 3)) + " +/- " + str(np.round(sig_face[0], 2)) + "\n")
    print("Face 2: " + str(np.round(prob_set[1], 3)) + " +/- " + str(np.round(sig_face[1], 2)) + "\n")
    print("Face 3: " + str(np.round(prob_set[2], 3)) + " +/- " + str(np.round(sig_face[2], 2)) + "\n")
    print("Face 4: " + str(np.round(prob_set[3], 3)) + " +/- " + str(np.round(sig_face[3], 2)) + "\n")
    print("Face 5: " + str(np.round(prob_set[4], 3)) + " +/- " + str(np.round(sig_face[4], 2)) + "\n")
    print("Face 6: " + str(np.round(prob_set[5], 3)) + " +/- " + str(np.round(sig_face[5], 2)) + "\n")
    ###Why does the highest probability face have the largest uncertainty/widest Gaussian???
    

   