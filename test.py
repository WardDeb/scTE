chr_list = [str(k) for k in list(range(1, 50))] + ["X", "Y", "M"]

def readGtf(filename):
    raw = {}
    clean = {}
    if ".gz" in filename:
        o = gzip.open(filename, "rb")
    else:
        o = open(filename, "r")

    for l in o:
        if ".gz" in filename:
            l = l.decode("ascii")
        if l.startswith("#"):
            continue
        t = l.strip().split("\t")
        if t[2] == "exon" or t[2] == "UTR":

            if "chr" not in t[0]:
                chr = "chr" + t[0]
            chr = t[0]
            if chr.replace("chr", "") not in chr_list:
                continue
            left = int(t[3])
            riht = int(t[4])

            if "gene_name" not in t[8]:
                continue

            name = t[8].split('gene_name "')[1].split('";')[0]

            if name not in raw:
                raw[name] = []
            raw[name].append([chr, left, riht])

            if "protein_coding" not in l and "lincRNA" not in l:
               continue
            print(f"Exon hit CLEAN BITCH = {t}")
            if name not in clean:
                clean[name] = []

            clean[name].append([chr, left, riht])

    return raw, clean

readGtf("/data/manke/deboutte/dbg/references/T2T/T2T_UCSC.gtf")
