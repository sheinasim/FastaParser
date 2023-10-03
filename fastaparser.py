#!/usr/bin/python

import pandas as pd
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("fasta", help=".fasta file to parse.")
parser.add_argument("records", help="File containing fasta headers to isolate.")
args = parser.parse_args()

input_file = open(args.records, "r")
content = input_file.read()
content_list = content.split("\n")
input_file.close()

sequences_in_file = []
sequences_not_in_file = []

df_record_lengths = pd.DataFrame(columns=('record', 'length'))
for record in SeqIO.parse(args.fasta, "fasta"):
        df_record_lengths = df_record_lengths.append({'record' : record.name, 'length' : len(record.seq)}, ignore_index = True)
        if record.id.split(" ")[0] in content_list:
            sequences_in_file.append(record)
        else:
            sequences_not_in_file.append(record)
            
df1 = df_record_lengths[df_record_lengths['record'].isin(content_list)] 
df2 = df_record_lengths[~df_record_lengths['record'].isin(content_list)] 

outfile1 = args.records.split(".txt")[0] + "_records"
outfile2 = args.records.split(".txt")[0] + "_remaining"

SeqIO.write(sequences_in_file, outfile1 + ".fasta", "fasta")
SeqIO.write(sequences_not_in_file, outfile2 + ".fasta", "fasta")
df1.to_csv(outfile1 + ".lengths", index=False, sep='\t', header=True)
df2.to_csv(outfile2 + ".lengths", index=False, sep='\t', header=True)

print("fastaparser finished parsing.")
