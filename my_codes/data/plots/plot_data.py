import numpy as np
import pylab
from Bio import SeqIO


def draw_line_plot(fasta_input_file, plot_title, plot_out_file, x_text, y_text):
    len_of_records = [len(rec.seq) for rec in SeqIO.parse(fasta_input_file, "fasta")]
    length, count = np.unique(len_of_records, return_counts=True)
    max_len = max(length)
    min_len = min(length)
    print(length)
    print(count)
    print("max_len: " + str(max_len))
    print("min_len: " + str(min_len))

    pylab.xlabel('Peptide Sequence Length')
    pylab.ylabel('Count of Peptides')
    pylab.title(plot_title)
    pylab.text(x_text, y_text, 'MAX_Length=' + str(max_len) + ' \n MIN_Length=' + str(min_len))
    pylab.grid()
    pylab.plot(length, count)
    pylab.savefig(plot_out_file)

    pylab.cla()
    pylab.clf()


def draw_all_plots():
    draw_line_plot('../split_data/ACP_40_pos.fasta', 'Plot of ACP Peptide Sequences With 40% cd-hit ',
                   'ACP_40_pos', 160, 70)
    draw_line_plot('../split_data/ACP_40_neg.fasta', 'Plot of non-ACP Peptide Sequences With 40% cd-hit ',
                   'ACP_40_neg', 160, 70)
    # -----------------------------
    draw_line_plot('../split_data/ACP_50_pos.fasta', 'Plot of ACP Peptide Sequences With 50% cd-hit ',
                   'ACP_50_pos', 160, 70)
    draw_line_plot('../split_data/ACP_50_neg.fasta', 'Plot of non-ACP Peptide Sequences With 50% cd-hit ',
                   'ACP_50_neg', 160, 70)
    # -----------------------------
    draw_line_plot('../split_data/ACP_60_pos.fasta', 'Plot of ACP Peptide Sequences With 60% cd-hit ',
                   'ACP_60_pos', 160, 70)
    draw_line_plot('../split_data/ACP_60_neg.fasta', 'Plot of non-ACP Peptide Sequences With 60% cd-hit ',
                   'ACP_60_neg', 160, 70)
    # -----------------------------
    draw_line_plot('../split_data/ACP_70_pos.fasta', 'Plot of ACP Peptide Sequences With 70% cd-hit ',
                   'ACP_70_pos', 170, 70)
    draw_line_plot('../split_data/ACP_70_neg.fasta', 'Plot of non-ACP Peptide Sequences With 70% cd-hit ',
                   'ACP_70_neg', 170, 70)
    # -----------------------------
    draw_line_plot('../split_data/ACP_80_pos.fasta', 'Plot of ACP Peptide Sequences With 80% cd-hit ',
                   'ACP_80_pos', 180, 80)
    draw_line_plot('../split_data/ACP_80_neg.fasta', 'Plot of non-ACP Peptide Sequences With 80% cd-hit ',
                   'ACP_80_neg', 180, 80)
    # -----------------------------
    draw_line_plot('../split_data/ACP_90_pos.fasta', 'Plot of ACP Peptide Sequences With 90% cd-hit ',
                   'ACP_90_pos', 190, 90)
    draw_line_plot('../split_data/ACP_90_neg.fasta', 'Plot of non-ACP Peptide Sequences With 90% cd-hit ',
                   'ACP_90_neg', 190, 90)
    # -----------------------------
    draw_line_plot('../split_data/ACP_100_pos.fasta', 'Plot of ACP Peptide Sequences With 100% cd-hit ',
                   'ACP_100_pos', 170, 70)
    draw_line_plot('../split_data/ACP_100_neg.fasta', 'Plot of non-ACP Peptide Sequences With 100% cd-hit ',
                   'ACP_100_neg', 170, 70)
    # -----------------------------
    draw_line_plot('../../../data/ACP_dataset/fasta/ACP_mixed_all_pos.fasta',
                   'Plot of Original ACP Peptide Sequences Length(no cd-hit)',
                   'Original_ACP_pos', 160, 70)
    draw_line_plot('../../../data/ACP_dataset/fasta/ACP_mixed_all_neg.fasta',
                   'Plot of Original non-ACP Peptide Sequences Length(no cd-hit)',
                   'Original_ACP_neg', 70, 150)
    # -----------------------------


draw_all_plots()
