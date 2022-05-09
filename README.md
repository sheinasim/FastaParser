# FastaParser 
Extracts records from a fasta based on a list of fasta headers.

Dependencies:

* Python3 
* Biopython
* Python pandas

### Usage
  
> python fastaParser.py \<assembly.fasta\> \<records.txt\>

If no arguments are provided, the script will return help message.

## Outputs

* \{records file prefix\}\_records.fasta
* \{records file prefix\}\_records.lengths
* \{records file prefix\}\_remaining.fasta
* \{records file prefix\}\_remaining.lengths

### Citation

If this script is useful to you, please cite the following in your publication:

```
@software{FastaParser,
  author = {Sim, Sheina B.},
  title = {FastaParser},
  url = {https://github.com/sheinasim/FastaParser}
}
```

Sheina B. Sim  
USDA-ARS  
US Pacific Basin Agricultural Research Service  
Hilo, Hawaii, 96720 USA  
sheina.sim@usda.gov  

This script is in the public domain in the United States per 17 U.S.C. § 105
