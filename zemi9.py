from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from io import StringIO


def dotmatrix(f1,f2,win):
    record1=next(SeqIO.parse(f1,"fasta"))
    record2=next(SeqIO.parse(f2,"fasta"))


    Seq1 =record1.seq
    Seq2 =record2.seq


    len1 = len(Seq1)-win+1
    len2 = len(Seq2)-win+1

    width = 500
    height = 500

    image = np.zeros((height,width))


    hash = {}
    for x in range(len(Seq1)-win+1):
        sub1 = Seq1[x:x+win]
        if sub1 not in hash:
            hash[sub1]=[]
        hash[sub1].append(x)
    for y in range(len2):
        sub2 = Seq2[y:y+win]
        py = int(y/len2*height)
        if sub2 in hash:
            for x in hash[sub2]:
                px = int(x/len1*width)
                image[py,px] = 1

    plt.imshow(image,extent=(1,len1,len2,1),cmap="Grays")
    st.pyplot(plt)


st.title("Dot matrix")


file1=st.sidebar.file_uploader("Sequence file 1:")
file2=st.sidebar.file_uploader("Sequence file 2:")

win = st.sidebar.slider("Window size:",4,100,10)


from io import StringIO

if file1 and file2:
    with StringIO(file1.getvalue().decode("utf-8")) as f1,\
        StringIO(file2.getvalue().decode("utf-8")) as f2:
        dotmatrix(f1,f2,win)