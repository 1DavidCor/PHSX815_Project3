# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:23:12 2021

@author: d338c921
"""

# imports of external packages to use in our code
import sys
import numpy as np

# main function for our dice roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: \n -Nrolls [# of dice rolls] \n -Nexp [# of experiments] \n -output_file [filename]")
        print
        sys.exit(1)

  
    # default number of sample points
    num_rolls = 10
    
    #default number of experiments
    Nexp = 10
    
    #default: print instead of saving
    output_file = False

    # read the user-provided values from the command line (if there)
    if '-Nrolls' in sys.argv:
        p = sys.argv.index('-Nrolls')
        num_rolls = int(sys.argv[p+1])
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int((sys.argv[p+1]))
    if '-output_file' in sys.argv:
        p = sys.argv.index('-output_file')
        output_filename = str((sys.argv[p+1]))
        output_file = True
     
    #list of values to randomly select from i.e. the faces of the dice
    faces = [1, 2, 3, 4, 5, 6]
    
    #Use a random uniform distribution to choose probabilities for each side; make sure they sum to 1
    p1 = np.random.uniform(0.0, 1.0)
    p2 = np.random.uniform(0.0, 1.0 - p1)
    p3 = np.random.uniform(0.0, 1.0 - p1 - p2)
    p4 = np.random.uniform(0.0, 1.0 - p1 - p2 - p3)
    p5 = np.random.uniform(0.0, 1.0 - p1 - p2 - p3 - p4)
    p6 = 1.0 - p1 - p2 - p3 - p4 - p5
    
    #list of probabilities
    prob = [p1, p2, p3, p4, p5, p6]
    
    #shuffle the lsit of probabilities so it's not always faces 4, 5, 6 that have the smallest probabilities
    np.random.shuffle(prob)
    
    #print(prob)
    
    #roll the dice num_rolls times and repat the experiment Nexp times; store data in an array
    roll_array = np.random.choice(faces, size = (Nexp, num_rolls), p = prob)
    
    #print the dice rolls if an output file isn't specified; else save to teh specified .txt file
    if output_file == False:
        print(roll_array)
    else:
        np.savetxt(output_filename, roll_array)