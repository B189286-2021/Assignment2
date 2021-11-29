#!/usr/local/bin/python3

#script to determine and plot protein seq.
#Written by B189286
#------------------------------------------------------------------#

import os, sys, subprocess
print ("\nModules imported: os, sys, subprocess\n")

os.system('clear')
#___________________________________________________________________________#




#___________________________________________________________________________#

#---------------------------SECTION ONE-------------------------------------#

#------------------------CONSERVATION PLOT---------------------------------#

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
mycommand1="esearch -db protein -query '{0}[organism] AND {1}[Protein name] NOT PARTIAL' | efetch -format fasta > {0}_esearch.fasta ".format(details["taxonomic_group"], details["protein"])
subprocess.call(mycommand1, shell = True)

#Print statement when files are downloaded
print("Sequences for {} protein in the {} taxonomic group are now downloaded!".format(details["protein"], details["taxonomic_group"]))


#_______________________________________________________________________________________________#


#Ask the user if they would like to continue and count the number of sequences were retrieved?
count_seq=input("Would you like to proceed and count the number of sequences retrived? [Yes/No]").upper()

if count_seq=="YES":
	print("The total number of sequences in the FASTA file is: ")
	command2='open("{0}_esearch.fa".format(details["taxonomic_group"]).read()'
	subprocess.call(command2, shell=True)
	command3='seqcount("{0}_esearch.fa".format(details["taxonomic_group"])
	subprocess.call(command3, shell=True)

if count_seq=="NO":
	print("Session ended.")
	sys.exit()

#Ask the user if they want to continue and align the sequences
#sequences must first be split (seqretsplit???) and then aligned usilng clustalo
alig_seq=("Would you like to coninue and align the sequences?[Yes/No]").upper()

if align_seq=="YES":
	print("Sequences were split and then aligned.")
	command4='("{0}_esearch.fa".format(details["taxonomic_group"]).split">" > esearch_split.fa)'
	subprocess.call(command4, shell, True)
	#clustalo: align multiple sequences
	command5='clustalo -i esearch_split.fa -o prot_clust.msf -t protein --outfmt msf --maxnumseq=1001 --threads=4 -v'
	subprocess.call(command5, shell=True)

if align_seq=="NO":
	print("Session ended.")
	sys.exit()

#Ask user if want info on alignment?
#infoalign
info_align=("Would you like to create a file with information on the alignement?"[Yes/No"]).upper()

if info_align=="YES":
	print("Alginment info file created")
	command6='infoalign prot_clust.msf > info_align.fa'
	subrocess.call(command6, shell=True)

if info_alig=="NO":
	print("Exiting programme.")
	sys.exit()

#Ask the user if they would like to create a conservation plot?
con_plot=("Would you like to display the coservation plot?[Yes/No]").upper()

if con_plot=="Yes":
	print("Conservation plot displayed.")
	command7='plotcon -sformat msf prot_clust.msf -winsize 4 -graph x11'
	subprocess.call(command7, shell=True)

elif con_plot=="No":
	print("Instead of displaying the plot, would you like to save it?[Yes/No]").upper()
	if yes: 
		print("Conservation plot saved to file")
		command8='plotcon -sformat msf prot_clust.msf -winsize 4 -graph ps'
		subprocess.call(command8, shell=True)
	else:
        	print("Session ended.")
        	sys.exit()

#______________________________________________________________________________#

#----------------------------SECTION TWO---------------------------------------#

#--------------------------SCAN FOR KNOWN MOTIFS------------------------------#

#_____________________________________________________________________________#

#Ask the user if they want to scan the sequences for known motifs?
#individual files of each sequence required for this.
ind_seqfile=("Would you like to create files for each sequence? This is required if you want to scan the sequences for known motifs. [Yes/No]")

if ind_seqfile=="YES":
	print("Individual files created")
	command9='seqretsplit {0}_esearch.fa seqoutall > {0}_esearch.seq.fa'
	subprocess.call(command9, shell=True)
	command10='patmatmotifs -full -sequence {0}_esearch.seq.fa -sformat fasta'
	subprocess.call(command10, shell=True)
if ind_seqfile=="NO":
	print("Session ended.")
        sys.exit()

#________________________________________________________________________________#

#-------------------------------SECTION THREE-----------------------------------#

#-------------------------DETERMINE SECONDARY STRUCTURE--------------------------#

#________________________________________________________________________________#


#Ask user if they want to predict secondary protein structure? 

pred_struc=("Would you like to predict the secondary protein structure?[Yes/No]").upper()

if pre_dstruc=="YES":
	print("File created with info on secondary protein structure")
	command11='garnier {0}_esearch.seq.fa  > {0}.garnier'
	subprocess.call(command11, shell=True)

if pred_struc=='NO':
	print("Exiting programe")
	sys.exit()

#Ask the user if they want to get aa summary:

aa_plot=("Would you like to save or generate a plot displaying the amino acid properties of your protein? Them graplh will appear on screen.[Yes/No]").upper()

if aa_plot=="YES":
	print("Would you like to print or save it?[P/S]).upper()
	command12='pepinfo {0}_esearch.seq.fa  -sprotein1 -graph x11'
	subprocess.call(command12, shell=True)

if aa_plot=="NO":
	print("Exiting programe")
	sys.exit()
