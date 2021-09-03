from Bio import SeqIO


def count_data_by_id(file_name, class_label):
    count = 0
    query = "|" + class_label
    for seq_record in SeqIO.parse(open(file_name, mode='r'), 'fasta'):

        if query in seq_record.id:
            count += 1

    return count


# --------------------------------------------
file_in = '../../data/ACP_dataset/fasta/ACP-Mixed-40.fasta'
file_out = 'gene_seq_out.fasta'
# --------------------------------------------
print("ACP (1) count data: " + str(count_data_by_id(file_in, "1")))
print("non-ACP (0) count data: " + str(count_data_by_id(file_in, "0")))
