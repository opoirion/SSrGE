"""
config file for SNV calling pipeline

"""
# Project name. Used to create folder
PROJECT_NAME = 'jones_pancreatic_cancer'
# type of the dataset (human or mouse). Used to select reference genomes
CELL_TYPE = 'HUMAN'
# valid sequencing machine for picard tools:
# ILLUMINA, SLX, SOLEXA, SOLID, 454, LS454, COMPLETE, PACBIO,
# IONTORRE NT, CAPILLARY, HELICOS, UNKNOWN
PLATEFORM = 'ILLUMINA'
# Read length used to create star index for reference genome
STAR_INDEX_READ_LENGTH = 50

############ FOLDER ARCHITECTURE  ####################################
#Alias to define the GLOBAL_DATA_ROOT, OUTPUT_ROOT and PROG_ROOT
# (could be overloaded using reference paths)
USER = 'opoirion'
# Alias to define the root folder for reference data
# (could be overloaded using reference paths)
GLOBAL_DATA_ROOT = '/data/{0}/'.format(USER)
# Alias to define the output folder
OUTPUT_ROOT = '/home/{0}/data/'.format(USER)
# Alias to define the folder containing softwares.
# (could be overloaded using reference paths)
PROG_ROOT = '/home/{0}/prog/'.format(USER)
# Absolute path for the .soft file (dataset description) from NCBI
SOFT_PATH = "{0}/{1}/{1}.soft".format(GLOBAL_DATA_ROOT, PROJECT_NAME)
######################################################################

############ STANDART VARIABLE #######################################
TYPE_VAR = {
    'HUMAN': {
        # gtf file containing annotated human genes
        'ANNOTATION_PATH': "{0}/Illumina_hg19/Annotation/genes.gtf"\
        .format(GLOBAL_DATA_ROOT),
        # folder which will contains the STAR index using human genome
        'STAR_INDEX_PATH': "{0}/Illumina_hg19/Sequences/STARindex"\
        .format(GLOBAL_DATA_ROOT),
        # human reference fasta (.fa) file
        'REF_GENOME': "{0}/Illumina_hg19/Sequences/WholeGenomeFasta/genome.fa"\
        .format(GLOBAL_DATA_ROOT),
        # Reference human genome used
        'ORGANISM': 'hg19',
        # reference variant database used. The last version can be downloaded from:
        # ftp://ftp.ncbi.nih.gov/snp/organisms/ (human_9607_b{version}_p2)
        'DBSNP': "{0}/Illumina_hg19/vcf/dbsnp_138.hg19.vcf"\
        .format(GLOBAL_DATA_ROOT),\
        'VCF_RESOURCES': [
            # Other reference variant resources.
            # Can be downloaded from ftp://ftp.broadinstitute.org/bundle/2.8/hg19
            "{0}/Illumina_hg19/vcf/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf"\
            .format(GLOBAL_DATA_ROOT),
            # Indel variant reference database
            # can be downloaded from ftp://ftp.broadinstitute.org/bundle/2.8/hg19
            "{0}/Illumina_hg19/vcf/1000G_phase1.indels.hg19.sites.vcf"\
            .format(GLOBAL_DATA_ROOT),
            ]
    },
    'MOUSE': {
        # gtf file containing annotated mouse genes
        'ANNOTATION_PATH': "{0}/Mus_musculus/UCSC/mm10/Annotation/genes.gtf"\
        .format(GLOBAL_DATA_ROOT),
        # folder which will contains the STAR index using mouse genome
        'STAR_INDEX_PATH': "{0}/Mus_musculus/UCSC/mm10/Sequence/STARindex"\
        .format(GLOBAL_DATA_ROOT),
        # Mouse reference fasta (.fa) file
        'REF_GENOME': "{0}/Mus_musculus/UCSC/mm10/Sequence/WholeGenomeFasta/genome.fa"\
        .format(GLOBAL_DATA_ROOT),
        # Reference mouse genome used
        'ORGANISM': 'mm10',
        # reference variant database used. This version can be downloaded from:
        # ftp://ftp-mouse.sanger.ac.uk/REL-1303- SNPs_Indels-GRCm38/.
        'DBSNP': "{0}/Mus_musculus/vcf/mgp.v3.snps.rsIDdbSNPv137_ordered.vcf"\
        .format(GLOBAL_DATA_ROOT),
        # reference indel variant database used. This version can be downloaded from:
        # ftp://ftp-mouse.sanger.ac.uk/REL-1303- SNPs_Indels-GRCm38/.
        # Mouse VCF files must be sorted toward the sequence dictionnary of the mouse reference genome using SortVCF function from picard-tools
        'VCF_RESOURCES': [
            "{0}/Mus_musculus/vcf/mgp.v3.indels.rsIDdbSNPv137_ordered.vcf"\
            .format(GLOBAL_DATA_ROOT)
            ]
    }
}
######################################################################

############ MOUSE/ HUMAN ############################################
REF_GENOME = TYPE_VAR[CELL_TYPE]['REF_GENOME']
ANNOTATION_PATH = TYPE_VAR[CELL_TYPE]['ANNOTATION_PATH']
STAR_INDEX_PATH = TYPE_VAR[CELL_TYPE]['STAR_INDEX_PATH']
ORGANISM = TYPE_VAR[CELL_TYPE]['ORGANISM']
DBSNP = TYPE_VAR[CELL_TYPE]['DBSNP']
VCF_RESOURCES = TYPE_VAR[CELL_TYPE]['VCF_RESOURCES']
######################################################################

############# DATASET ###############################################
# Absolute path for fastq files.
# Fastq files must be organised using one folder for one SRX experiment
FASTQ_PATH = "{0}/{1}/fastq/".format(GLOBAL_DATA_ROOT, PROJECT_NAME)
# output path
PATH_OUTPUT = "{0}/{1}/".format(OUTPUT_ROOT, PROJECT_NAME)
#specific string pattern that a folder name must match
SPECIFIC_FILENAME_PATTERN = ""
# Used aligner (star / bismark (RRBS read alignment))
USED_ALIGNER = 'star'
# Are the reads from the bislufite pipeline ?
ARE_READS_BISULFITE = False
#####################################################################

############# SOFTWARE ###############################################
# Available java version. Must be > 1.8
JAVA = "{0}/jdk1.8.0_77/bin/java".format(PROG_ROOT)
# Max memory used by Java
JAVA_MEM = "-Xmx110g"
# GATK folder where can be found GATK software
GATK_DIR = "{0}/GATK/".format(PROG_ROOT)
# picard-tools software
PICARD_DIR = "{0}/picard-tools-2.1.1/".format(PROG_ROOT)
# Perl
PERL = 'perl'
# BS-Snper (SNP calling for bisulfite reads)
BSSNPER = '{0}/BS-Snper/BS-Snper.pl'.format(PROG_ROOT)
# STAR aligner software
PATH_STAR_SOFTWARE = "{0}/STAR/bin/Linux_x86_64_static/STAR"\
                          .format(PROG_ROOT)
# fastqc software [OPTIONAL]
FASTQC = "fastqc"
# snpEff software (vcf annotation) [OPTIONAL]
SNPEFF = '{0}/snpEff/snpEff.jar'.format(PROG_ROOT)
# required snpEff databases (vcf annotation) [OPTIONAL]
SNPEFF_DICT = {'MOUSE': 'GRCm38.82',
               'HUMAN': 'GRCh37.75'}
SNPEFF_DB = SNPEFF_DICT[CELL_TYPE]
######################################################################

#############  STAR #################################################
# Number of threads used when using STAR aligner
STAR_THREADS = 12
# output path for STAR results
OUTPUT_PATH_STAR = PATH_OUTPUT + "/star/"
#####################################################################

############ SNV CALLING PIPELINE ###################################
# output path for SNVs inferred
OUTPUT_PATH_SNV =  PATH_OUTPUT + '/snv_pipeline_results/'
# Number of SNV calling processes launched in parallel
NB_PROCESS_SNV = 3
####################################################################

############ COMPUTE DISTANCE MATRIX [OPTIONAL] ##############################
# software to infer gene expressions count with raw count for each single cells
# [OPTIONAL]
FEATURE_COUNT = "featureCounts"
# path for gene expression matrices [OPTIONAL]
MATRIX_OUTPUT_PATH = "{0}/{1}/expression_profile/"\
                     .format(OUTPUT_ROOT, PROJECT_NAME)
###############################################################################
