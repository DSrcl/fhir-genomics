from os import path
from pysam import TabixFile, asTuple

SNP_FILE = path.join(path.dirname(path.abspath(__file__)), 'snps.sorted.txt.gz')

SNP_IDX = 1 
CHROM_IDX = 2
POS_IDX = 3

def get_snp_data(*args, **kwargs):
    return TabixFile(SNP_FILE, parser=asTuple()).\
            fetch(*args, **kwargs)

SNP_TABLE = {snp[SNP_IDX]: (snp[CHROM_IDX], snp[POS_IDX]) for snp in get_snp_data()}


def _slice(xs, offset, limit):
    '''
    safe version of xs[offset:offset+limit]
    return (sliced_collection, total_count)
    '''
    num_items = len(xs)
    offset = offset if offset < num_items else num_items
    bound = offset + limit
    bound = bound if bound < num_items else num_items
    return xs[offset:bound], num_items


def get_snps(chrom=None, start=None, end=None, offset=0, limit=100):
    # TODO: make this deterministic
    snps = [] 
    count = 0
    for snp in get_snp_data(chrom, start, end):
        if offset <= count < offset + limit:
            snps.append(snp[SNP_IDX]) 
        count += 1
    
    return snps, count


def get_coord(rsid):
    return SNP_TABLE[rsid] 
