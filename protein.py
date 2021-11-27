#!/usr/local/bin/python3

#script to determine and plot protein seq.
#Written by B189286
#------------------------------------------------------------------#

import os, sys, subprocess
print ("\nModules imported: os, sys, subprocess\n")

os.system('clear')
#___________________________________________________________________________#

#Function to get input from user
#Arguments will come in as a list from the dictionary of details provided

#Create a function
def user_entry(protein, taxonomic_group):
        import string
        print("You have provided the following details:\n\tProtein family: ",protein,"\n\tTaxonomic group: ",taxonomic_group)


#Store the output in an ordered dictionary

details={}
details["protein"] = input("Please enter the protein family: ")
details["taxonomic_group"] = input("Please enter the taxonomic group: ")

user_entry(*list(details.values()))

#Esearch using Edirect
#NB ASK USER IF THEY WANT FULL/AND PARTIAL SEQUENCES??????***************
mycommand1="esearch -db protein -query '{0}[organism] AND {1}[Protein name] NOT PARTIAL' | efetch -format fasta > {0}_esearch.fasta ".format(details["taxonomic_group"], details["protein"])
subprocess.call(mycommand1, shell = True)

#Print statement when files are downloaded
print("Sequences for {} protein in the {} taxonomic group are now downloaded!".format(details["protein"], details["taxonomic_group"]))

#Ask the user if they would like to continue and count the number of sequences were retrieved?
count_seq=input("Would you like to proceed and count the number of sequences retrived? [Yes/No]").upper()

if count_seq=="YES":
	print("The total number of sequences in the FASTA file is: ")
	command2='open("{}_esearch.fa".format(details["taxonomic_group"]).read()'
	subprocess.call(command2, shell=True)
	command3='seqcount("{}_esearch.fa".format(details["taxonomic_group])
	subprocess.call(command3, shell=True)

if count_seq=="NO":
	print("Session ended.")
	sys.exit()

#Create a list of different species - info taken from the header??????????######

#Ask the user if they want to continue and align the sequences
#clustalo -i inputfile.fa
#subprocess.call("clustalo -i {0}_esearch.fa -o {}_clustalo.fa -v".format(details["taxonomic_group"], shell=True)
alig_seq=("Would you like to coninue and align the sequences?[Yes/No]").upper()

if align_seq=="YES":
	print("Sequences are split and then aligned.")
	command4='("{}_esearch.fa".format(details["taxonomic_group]).split">" > esearch_split.fa)
	subprocess.call(command4, shell, True)
	#clustalo: align multiple sequences
	command5='clustalo -i esearch_split.fa -o prot_clust.msf -t protein --outfmt msf -v
	subprocess.call(command5, shell=True)

if align_seq=="NO":
	print("Session ended.")
	sys.exit()

#Ask user if want info on alignment?
#infoalign

#Ask the user if they would like to create a conservation plot?
con_plot=("Would you like to display the coservation plot?[Yes/No]").upper()

if con_plot=="Yes":
	print("Conservation plot displayed.")
	command6='plotcon -sformat msf prot_clust.msf -winsize 4 -graph x11'
	subprocess.call(command6, shell=True)

elif con_plot=="No":
	print("Instead of displaying the plot, would you like to save it?[Yes/No]").upper()
	if yes: 
		print("Conservation plot saved to file")
		command7='plotcon -sformat msf prot_clust.msf -winsize 4 -graph ps'
		subprocess.call(command7, shell=True)
	else:
        	print("Session ended.")
        	sys.exit()

#Ask the user if they want to create individual files of each sequence?
ind_seqfile=("Would you like to create files for each sequence? This is required if you want to scan the sequences for known motifs. [Yes/No]")

if ind_seqfile="Yes":
	print("Individual files created")
	command8='seqretsplit FILE.fa'
	subprocess.call(command8, shell=True)
if ind_seqfile="No":
	print("Session ended.")
        sys.exit()

#scan protein sequences with motifs from PROSITE for known motifs
#??????????????????????????


#os.environ[]



