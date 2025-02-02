[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
![push master](https://github.com/BCCDC-PHL/troika/actions/workflows/push_master.yml/badge.svg)



# Troika

Detection of resistance mechanisms in _Mycobacterium tuberculosis_ is dependent upon identification of SNPs that may confer decreased susceptibility to anti-mycobacterial drugs. Troika is a pipeline, which calls SNPs for both phylogenetic analysis and determination of AST. Troika leverages high quality tools, including [Snippy](https://github.com/tseemann/snippy) and [TB-profiler](https://github.com/jodyphelan/TBProfiler) and its related database to detect resistance conferring mutations from Illumina read data and filters these results for reporting for public health and clinical use. The [upstream repository](https://github.com/MDU-PHL/troika) was created and designed for use in Australia, and this fork has been created to adapt Troika for use at the [BCCDC Public Health Laboratory](http://www.bccdc.ca/our-services/service-areas/bccdc-public-health-laboratory).


### Motivation

There are many tools and databases available, however, for the purposes of reporting genomic AST for _M. tuberculosis_ in the context of public health and clinical use in Australia customisation is required. Rather than reinventing the wheel, Troika leverages a high quality database and a detection tool which is highly customisable. 


## Pipeline

Troika is designed for batch reporting of AST in _M. tuberculosis_ isolates generated from Illumina reads and phylogenetic analysis and clustering to identify potentially related isolates. This pipeline is in use at MDU Victoria Australia for Tuberculosis surveillance and AST reporting.

### Installation

#### Conda (Recomended)

TO COME

#### PyPi

```
pip3 install git+https://github.com/BCCDC-PHL/troika.git
```

### Running Troika

#### input

Input for troika is a tab-delimited file containing three columns (no header) `<sample_name> <path_to_read1> <path_to_read2>`

```
troika -h

usage: troika_tb.py [-h] [-v] [--input_file INPUT_FILE] [--detect_species]
                    [--resistance_only] [--Singularity]
                    [--profiler_singularity_path PROFILER_SINGULARITY_PATH]
                    [--snippy_singularity_path SNIPPY_SINGULARITY_PATH]
                    [--workdir WORKDIR] [--resources RESOURCES] [--jobs JOBS]
                    [--profiler_threads PROFILER_THREADS]
                    [--kraken_threads KRAKEN_THREADS] [--kraken_db KRAKEN_DB]
                    [--snippy_threads SNIPPY_THREADS] [--mode {mdu,normal}]
                    [--positive_control POSITIVE_CONTROL]
                    [--db_version DB_VERSION] [--min_cov MIN_COV]
                    [--min_aln MIN_ALN]

Troika - a pipeline for phylogenentic analysis, detection and reporting of
genomic AST in Mtb If an arg is specified in more than one place, then
commandline values override environment variables which override defaults.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --input_file INPUT_FILE, -i INPUT_FILE
                        Input file tab-delimited file 3 columns isolate_id
                        path_to_r1 path_to_r2 (default: )
  --detect_species, -d  Set if you would like to detect species - note if not
                        set troika may include non-tuberculosis species in the
                        analysis. (default: False)
  --resistance_only     If detection of resistance mutations only is needed.
                        Phylogeny will not be performed. (default: False)
  --Singularity, -S     If singularity is to be used for troika. (default:
                        False)
  --profiler_singularity_path PROFILER_SINGULARITY_PATH, -ps PROFILER_SINGULARITY_PATH
                        URL for TB-profiler singularity container. (default:
                        docker://mduphl/mtbtools)
  --workdir WORKDIR, -w WORKDIR
                        Working directory, default is current directory
                        (default: /home/khhor/dev/troika_tb)
  --resources RESOURCES, -r RESOURCES
                        Directory where templates are stored (default:
                        troika_tb)
  --jobs JOBS, -j JOBS  Number of jobs to run in parallel. (default: 8)
  --profiler_threads PROFILER_THREADS, -t PROFILER_THREADS
                        Number of threads to run TB-profiler (default: 1)
  --kraken_threads KRAKEN_THREADS, -kt KRAKEN_THREADS
                        Number of threads for kraken (default: 4)
  --kraken_db KRAKEN_DB, -k KRAKEN_DB
                        Path to DB for use with kraken2, if no DB present
                        speciation will not be performed. [env var:
                        KRAKEN2_DEFAULT_DB] (default: None)
  --snippy_threads SNIPPY_THREADS, -st SNIPPY_THREADS
                        Number of threads for snippy (default: 8)
  --mode {mdu,normal}, -m {mdu,normal}
                        If running for MDU service use 'mdu', else use
                        'normal' (default: normal)
  --positive_control POSITIVE_CONTROL, -pc POSITIVE_CONTROL
                        Path to positive control - REQUIRED if running for MDU
                        service (default: )
  --db_version DB_VERSION
                        The version of database being used. (default:
                        TBProfiler-20190820)
  --min_cov MIN_COV, -mc MIN_COV
                        Minimum coverage for quality checks, isolates with
                        coverage below this threshold will not be used in the
                        analysis. (default: 40)
  --min_aln MIN_ALN, -ma     MIN_ALN
                        Minimum alignment for phylogenetic analysis,
                        alignments lower than this threshold will not be
                        included in the calculation of core-genome. (default:
                        80)
```

