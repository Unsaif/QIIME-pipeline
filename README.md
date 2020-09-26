# QIIME_pipeline
The QIIME Pipeline is a tool that uses QIIME2 to produce compatible input for mgPipe

# SYSTEM REQUIREMENTS
To run the QIIME Pipeline and its supporting python scripts requires:

* A modern Linux operating system.
* Python3 or greater.
* QIIME2 
    
# INSTALLATION

The QIIME Pipeline is hosted on GitHub

The QIIME Pipeline source code and executables can be obtained via two different methods:

Either clone the repository using git:

`git clone https://github.com/Unsaif/QIIME-pipeline`

Or download and extract the zip file using the 'Download ZIP' link of the GitHub project page.

No further installation is necessary. The program can be run from within the cloned repository or from the location that the zip was extracted to.

This document will assume that the QIIME Pipeline is located in your home directory in a folder named `/home/your_username/QIIME-pipeline`. This location will be referred to from hereon in as 'QIIMEPIPELINEDIR'.
If you have placed QIIME Pipeline in a different location, use that path in place of 'QIIMEPIPELINEDIR'.

# Downloading a classifier

Before the QIIME Pipeline can be used a classifier must be downloaded. 

At the time of release, this classifier is the 13_8 from [Greengenes](http://greengenes.secondgenome.com/) formatted as a QIIME2 artifact.

If you already have these files, place a copy of them into the QIIMEPIPELINEDIR/files_needed_for_MbT directory.
If you do not have these files, they can be downloaded automatically as part of the following step.

Change to the QIIMEPIPELINEDIR/files_needed_for_MbT directory.
Execute the command:
wget
`-o "gg-13-8-99-nb-classifier.qza"
"https://data.qiime2.org/2018.11/common/gg-13-8-99-nb-classifier.qza"`

# RUNNING THE QIIME PIPELINE

To run the pipeline, accession codes of individuals of interest are needed. This can be contained in a file of .txt, .tsv or .csv format.

What is necessary in the file of one of these formats is that there is a column named "accession" along with the codes of individuals underneath. 

The pipeline is capable of dealing with both single-end and paired-end. It will have to be specified in the command line which one is being dealt with. 

To run the pipeline using a file described above, and saving the output in the pipeline directory which will be labeled "the file's name + _output" for single-end (1) or paired-end (2):

`path_to_qiime_pipeline_folder/pipeline -a path_to_accession_file/accession.csv -o 1`

If running from within the pipeline directory:

`./pipeline -a path_to_accession_file/accession.csv -o 1`

# OUTPUT

The output of the QIIME Pipeline is a directory named "name of the accession file" + "_output" situated in the QIIME Pipeline directory and it consists of ten files:

* The relative abundance tables on a species and genus level: **QIIME2_MbT_Species.tsv** & **QIIME2_MbT_Genus.tsv**, respectively.
    
* Taxonomic tables up to the species and genus level: **taxon_table_species.tsv** & **taxon_table_species.tsv**, respectively.
    
* A file containing a list of genera whose respective taxonomic group only contained information up to the genus level: **dropped_genera.tsv**.
    
* The taxonomy table file and feature table file used to create the output files: **taxonomy.tsv** & **feature-table.tsv**, respectively.

* A file containing the total reads for each sample: **total_reads.tsv**
    
* Finally, two files that relay for each found species and genera, if they are absent, present or have a been renamed as a synonym in AGORA: **absent_present_species.tsv** & **absent_present_genus.tsv**.
