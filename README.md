# 5' End Read Accumulation Analysis

This repository contains a Python script (`5end_pileup.py`) designed to extract and quantify the accumulation of sequencing reads specifically at their 5' ends from aligned BAM files.

## Description

The script identifies the genomic coordinates of the 5' ends of sequencing reads and aggregates counts for these positions. It is particularly useful for analyses that require precise identification of transcription start sites (TSSs), such as promoter usage studies, metagene analyses, and transcription initiation assays.

## Requirements

- Python 3.x
- pysam
- pandas

Install dependencies using pip:

```bash
pip install pysam pandas
```

## Usage

```bash
python 5end_pileup.py <input_bam_file> <output_tsv_file>
```

### Arguments

- `<input_bam_file>`: Path to your input BAM file (sorted and indexed).
- `<output_tsv_file>`: Desired path for the output TSV file.

### Example

```bash
python 5end_pileup.py sample.bam sample_5prime_counts.tsv
```

## Output Format

The output is a tab-separated (TSV) file with columns:

| chrom | position | strand | count |
|-------|----------|--------|-------|
| chr1  | 123456   | +      | 42    |
| chr1  | 123789   | -      | 27    |
| chr2  | 987654   | +      | 55    |

## Author

[GyeungYun Kim]

## Cite
If you use this script in your research, please cite: Kim et al., Mol Cell, 2025.
