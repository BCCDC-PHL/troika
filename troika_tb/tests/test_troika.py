import sys, pathlib, pandas, pytest, numpy
import argparse
import logging
from unittest.mock import patch

from troika_tb.RunTroika import Troika


def create_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--input_file', '-i', default = '')
        parser.add_argument('--detect_species', '-d',action = 'store_true')
        parser.add_argument('--resistance_only', action = 'store_true')
        parser.add_argument("--Singularity", "-S", action="store_true")
        parser.add_argument('--profiler_singularity_path', '-ps', default = 'docker://mduphl/mtbtools')
        parser.add_argument('--snippy_singularity_path', '-ss', default = 'docker://mduphl/snippy:v4.4.3')
        parser.add_argument("--workdir", "-w", default=f"{pathlib.Path.cwd().absolute()}")
        parser.add_argument("--resources", "-r", default=f"{pathlib.Path(__file__).parent }")
        parser.add_argument("--jobs", "-j", default=8)
        parser.add_argument('--profiler_threads', '-t', default=1)
        parser.add_argument('--kraken_threads', '-kt', default = 4)
        parser.add_argument('--kraken_db', '-k', default='')
        parser.add_argument('--snippy_threads', '-st', default = 8)
        parser.add_argument('--mode', '-m', default='normal', choices=['mdu', 'normal'])
        parser.add_argument('--positive_control', '-pc', default='')
        parser.add_argument('--db_version', default='')
        parser.add_argument('--min_cov', '-mc', default=40)
        parser.add_argument('--min_aln','-ma', default=80)
        args = parser.parse_args()
        return args

def test_3_cols():
        '''
        return True when correct number of columns
        '''
        args = create_args()
        detect_obj = Troika(args)
        tab = pandas.DataFrame({'A':[1], 'B':[2], 'C':[3]})
        assert detect_obj.three_cols(tab)


def test_2col_dimensions():
        '''
        return False when wrong number of columns present
        '''
        args = create_args()
        detect_obj = Troika(args)
        tab = pandas.DataFrame({'A':[1], 'B':[2]})
        assert detect_obj.three_cols(tab) == False


def test_path_exists():
        '''
        test that path_exists returns True
        '''
        args = create_args()
        p = pathlib.Path('troika_tb','tests', 'troika.txt')
        detect_obj = Troika(args)
        assert detect_obj.path_exists(p)

