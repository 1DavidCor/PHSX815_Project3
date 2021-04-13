# PHSX815_Project3

For Project 3, I have chosen to study the probabilities associated with rolling a six-sided dice.  If youwere to roll a dice enough times, you should be able to calculate the probability associated with eachface of the dice to a certain degree of certainty. Even in a dice where each face has a different probability, you should still beable to estimate the true probabilities for each face if you roll the dice enough times. For this project, I have created a program to roll a biased dice a certain nnumber of times as well as a program which takes these results and computes the probability of rolling each side.

DiceRoll.py:
This program is used to simulate a dice rolling experiment.  The script accepts user input for -Nrolls,the  number  of  times  the  biased  dice  is  rolled  in  each  experiment,  and  -Nexp,  the  total  number  ofexperiments.  Thus, the biased dice I developed is rolled a total number ofN rolls∗N exptimes. 

%run DiceRolls.py -Nrolls 50 -Nexp 100 -output_file rolls.txt

DiceRollAnalysis.py:
This portion of the project receives the .txt file storing the results of the experimental dice rolls as input and uses histograms to count the number of rolls associated with each face to estimate the probability of the biased die landing on each face. The script fits a Gaussian to the histopgram of probabilities of each face. The mean of the each Gaussian distribution represents the probability of each face we determined earlier, and the standard deviation is then the uncertainty associated with each probability measurement.

%run DiceRollAnalysis.py -input_file rolls.txt
