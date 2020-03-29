#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import Drain

input_dir  = '../logs/Hadoop/'  # The input directory of log file
output_dir = 'Drain_result/'  # The output directory of parsing results
# log_file   = 'hadoop-fu_chen-secondarynamenode-sense01.log'  # The input log file name
# log_file   = 'yarn-fu_chen-resourcemanager-sense01.log'  # The input log file name
log_file   = 'hadoop-hdfs-datanode-mesos-01.log'  # The input log file name
# log_file   = 'test.log'  # The input log file name
log_format = '<Date> <Time>,<Pid> <Level> <Component>: <Content>'  # HDFS log format11011
# Regular expression list for optional preprocessing (default: [])
regex      = [
    r'blk_(|-)[0-9]+' , # block id
    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
    r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
]
st         = 0.5  # Similarity threshold
depth      = 4  # Depth of all leaf nodes

parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
parser.parse(log_file)

