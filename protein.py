#!/usr/local/bin/python3

#script to determine and plot protein seq.
#Written by B189286
#------------------------------------------------------------------#

import os, sys, subprocess
print ("\nModules imported: os, sys, subprocess\n")

os.system('clear')
#___________________________________________________________________________#

#FUNCTION to get input from user
#Arguments will come in as a list from the dictionary of details provided

def user_entry(protein, taxonomic_group):
        import string
        print("You have provided the following details:\n\tProtein family: ",protein,"\n\tTaxonomic group: ",taxonomic_group)


#Store the output in an ordered dictionary

details={}
details["protein"] = input("Please enter the protein family: ")
details["taxonomic_group"] = input("Please enter the taxonomic group: ")

user_entry(*list(details.values()))

#Esearch using Edirect
mycommand1="esearch -db protein -query '{0}[organism] AND {1}[Protein name] NOT PARTIAL' | efetch -format fasta > {0}_esearch.fasta ".format(details["taxonomic_group"], details["protein"])
subprocess.call(mycommand1, shell = True)

#Print statement when files are downloaded
print("Sequences for {} protein in the {} taxonomic group are now downloaded!".format(details["protein"], details["taxonomic_group"]))

#Read the and count the file contents 
#Create function
#contents = open("{}_esearch.fasta".format(details["taxonomic_group"])).read
#print("\nIn your dataset, ")
#spec_no = seqcount({0}_esearch.fasta)
#print("The total number of species is: ", spec_no)

#Count the number of sequences in the FASTA file
#seqcount

#Create a list of different species - info taken from the header


#Align multiple sequences using Clustalo
#clustalo -i inputfile.fa

#Ask user if want info on alignment?
#infoalign

#Ask user to save and/or view conservation plot - plotcon
#SAVE
#plotcon -s format fasta .fa winsize=10 -graph ps
#SHOW
#plotcon -s format fasta .fa winsize=10 -graph x11
