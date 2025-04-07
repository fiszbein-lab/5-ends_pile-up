import pysam
import pandas as pd
import argparse

def extract_five_prime_counts(bam_filename, output_filename):
    # Open BAM file
    bamfile = pysam.AlignmentFile(bam_filename, "rb")
    
    five_prime_counts = {}

    # Iterate over reads and count 5' positions
    for read in bamfile.fetch():
        # Skip second read of paired-end (we only want the first read)
        if read.is_secondary or not read.is_proper_pair:
            continue
        
        # Capture the 5' end based on the strand and first read in pair
        chrom = read.reference_name
        strand = "-" if read.is_reverse else "+"
        five_prime = read.reference_end - 1 if read.is_reverse else read.reference_start

        key = (chrom, five_prime, strand)
        five_prime_counts[key] = five_prime_counts.get(key, 0) + 1

    bamfile.close()

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(five_prime_counts, orient="index", columns=["count"])
    df.index = pd.MultiIndex.from_tuples(df.index, names=["chrom", "position", "strand"])
    df.reset_index(inplace=True)

    # Save output
    df.to_csv(output_filename, sep="\t", index=False)
    print(f"5' read accumulation counts saved to: {output_filename}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Extract 5' read accumulation from a BAM file")
    parser.add_argument("bamfile", help="Input BAM file")
    parser.add_argument("outfile", help="Output file (TSV format)")

    args = parser.parse_args()
    
    # Run extraction function
    extract_five_prime_counts(args.bamfile, args.outfile)
