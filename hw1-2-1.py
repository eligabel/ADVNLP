import sys
from collections import Counter
from math import log2
import statistics
from scipy.stats import entropy
import fileinput


#This boilerplate provides a rough structure for your code You are free to change it
#as you wish. You are in fact encouraged to do so, with the exception of the main
#function. Please do not change the main function.

def input_file(filename):
	f = open(filename, "r")
	dirtytxt = f.readlines()
	f.close()
	return dirtytxt
#britishtxt = "The sun never set on the British Empire because the British Empire is in the East and the sun sets in the West. Queen Victoria was the longest queen. She sat on a thorn for 63 years. He reclining years and finally the end of her life were exemplatory of a great personality. Her death was the final event which ended her reign."
#def read_txt(file):
#	f = open(file, "r")
#	dirtytxt = f.read()
#	f.close()
#	return dirtytxt

#def clean_vartext(txt):
#	dirtytxt = read_txt(txt)
#	words = [word.lower() for word in dirtytxt]
	#Define Characters we're interested in
#	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	#Create dictionary
#	letters = Counter()
	#Update dictionary
#	for char in words:
#		if char in alphabet:
#			letters.update(char)
	#return
#	return letters

def clean_text(file):
	#Cleans the text according to the problem description
	#Begin by reading the non-cleaned text
	dirtytxt = input_file(file)
	#Lowercase
	words = [word.lower() for word in dirtytxt]
	#Define Characters we're interested in
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	#Create dictionary
	letters = Counter()
	#Update dictionary
	for char in words:
		if char in alphabet:
			letters.update(char)
	#return
	return letters

def learn_distribution():
	letters = clean_text(file)
	frequencies = letters.values()
	total = sum(frequencies)
	distribution = {}
	for letter, count in letters.items():
		probability = count/total
		distribution[letter] = probability

	# You should learn the distribution as a dictionary
	return distribution

#def learn_vardistribution(txt):
#	letters = clean_vartext(txt)
#	frequencies = letters.values()
#	total = sum(frequencies)
#	distribution = {}
#	for letter, count in letters.items():
#		probability = count/total
#		distribution[letter] = probability

# You should learn the distribution as a dictionary
#	return distribution

def expectation(file):
	"""Return expectation of distribution"""
	distribution = learn_distribution(file)
	#0-25 numbers assigned to letters, create new dictionary, calculate expectation, variance, and entropy from said dictionary
	assignedVar = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
	expected = {}
	for letter, probability in distribution.items():
		for letter, frequency in assignedVar.items():
			expV = probability*frequency
			expected[letter] = expV
	return expected
	#formula for expected value is P(x)*n, or probability of x multiplied by number of time x occurs.  So, need the probability of a letter occuring multiplied by the number of times
	#said letter occurs (the value, v, which corresponds with the key, k)
	#need to multiply v by the x, which is this case is the frequency of the key.  Therorectical equation: expEquation = (v)*(x)


def variance(file):
	#calculate variance of the expected values
	expDic = expectation(file)
	dataL = []
	for letter, expV in expDic.items():
		dataL.append(expV)
	print(dataL)
	var = statistics.variance(dataL)
	return var

def entropyFunc(file):
	distribution = learn_distribution(file)
	pk = []
	for letter, probability in distribution.items():
		pk.append(probability)
	ent = entropy(pk, base=2)
	return ent

def KL(txt1, txt2):
	dist1 = learn_distribution(txt1)
	pk = []
	dist2 = learn_distribution(txt2)
	qk = []
	for letter, probability in dist1.items():
		if probability == 0:
			probability = 0.0001
			pk.append(probability)
		else:
			pk.append(probability)
	for letter, probability in dist2.items():
		if probability == 0:
			probability = 0.0001
			qk.append(probability)
		else:
			qk.append(probability)
	kldiv = entropy(pk, qk, base=2)
	return kldiv


def p1():
	print(expectation("newcomp.txt"))
	print(variance("newcomp.txt"))
	print(entropyFunc("newcomp.txt"))

def p2():

	"""This problem should print the KL divergence of the two distributions in problem 2"""
	print(KL("newcomp.txt","britishtxt"))

def p3(input_file_name):
	"""This function should read the contents of the input file_name and identify the
	language of the text contained in it and print the name of the language"""
	#premise here is that the KL divergence should be smaller between the english sample text and the english test text than the KL divergence betweent the enlgish sample text and the polish text
	# On this basis, pseudocode looks something like this:
	 KL1 = KL("english_sample.txt")
	 KL2 = KL("polish_sample.txt")
	 if KL1<KL2
		print("The text is English")
	 if KL1>KL2
		print("The text is Polish")
	 else
		print("The text is unidentifiable")


if __name__ == "__main__":
    if sys.argv[1] == '1':
        p1()
    elif sys.argv[1] == '2':
        p2()
    else:
        p3(sys.argv[1])
