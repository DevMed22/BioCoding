import tkinter
import customtkinter
import numpy as np
import bisect

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("500x500")
app.title('BioCoding app')
# prog.minsize("300x300")
tabview = customtkinter.CTkTabview(app,
                                   width=450,
                                   height=450,
                                   corner_radius=10)
tabview.pack(padx=10, pady=10)

tab_1 = tabview.add("tab 1")
tab_2 = tabview.add("tab 2")
tab_3 = tabview.add("tab 3")
tab_4 = tabview.add("tab 4")
tab_5 = tabview.add("tab 5")
tab_6 = tabview.add("tab 6")
tab_7 = tabview.add("tab 7")

tabview.set("tab 1")


# ----------------tab_1-----------#
def GC_Content():
    seq = entry_1.get()
    l = len(seq)
    num_G = seq.count("G")
    num_C = seq.count("C")
    total = num_C + num_G
    gc_count = total / l

    textbox = customtkinter.CTkTextbox(tab_1, width=400, height=100)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"GC Content:   {gc_count}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


def Complement():
    seq = entry_1.get()
    dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
    s = list(seq)
    for i in range(len(seq)):
        s[i] = str(dic[s[i]])
    s = "".join(s)

    textbox = customtkinter.CTkTextbox(tab_1, width=400, height=100)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{s}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


def Reverse():
    seq = entry_1.get()
    s = "".join(list(reversed(seq)))

    textbox = customtkinter.CTkTextbox(tab_1, width=400, height=100)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{s}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


def Reverse_Complement():
    seq = entry_1.get()
    dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
    s = list(seq)
    for i in range(len(seq)):
        s[i] = str(dic[s[i]])
    s = "".join(s)
    seq_2 = "".join(list(reversed(s)))

    textbox = customtkinter.CTkTextbox(tab_1, width=400, height=100)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{seq_2}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


label_1 = customtkinter.CTkLabel(master=tab_1,
                                 text="Main algorithms",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_1.pack(pady=12, padx=10)
label_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

entry_1 = customtkinter.CTkEntry(master=tab_1,
                                 placeholder_text="Enter the Gene Seq",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
entry_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

button_1 = customtkinter.CTkButton(master=tab_1,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="GC Content",
                                   command=GC_Content)
button_1.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

button_2 = customtkinter.CTkButton(master=tab_1,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="Complement",
                                   command=Complement)
button_2.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

button_3 = customtkinter.CTkButton(master=tab_1,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="Reverse",
                                   command=Reverse)
button_3.place(relx=0.2, rely=0.65, anchor=tkinter.CENTER)

button_4 = customtkinter.CTkButton(master=tab_1,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="Reverse Complement",
                                   command=Reverse_Complement)
button_4.place(relx=0.7, rely=0.65, anchor=tkinter.CENTER)


# ------------------------tab_2-------------------#
def translation():
    seq = entry_2.get()

    dic = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
           "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
           "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
           "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
           "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
           "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
           "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
           "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
           "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
           "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
           "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
           }
    x = ''
    for i in range(0, len(seq), 3):
        if dic[seq[i:i + 3]] != "*":
            x = x + dic[seq[i:i + 3]]

    textbox = customtkinter.CTkTextbox(tab_2, width=400, height=100)
    textbox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{str(x)}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


# ------------------------------------------
label_2 = customtkinter.CTkLabel(master=tab_2,
                                 text="Translation",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_2.pack(pady=12, padx=10)
label_2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

entry_2 = customtkinter.CTkEntry(master=tab_2,
                                 placeholder_text="Enter the Gene Seq",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
entry_2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

tran_bt = customtkinter.CTkButton(master=tab_2,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=8,
                                  text="Gene Translation",
                                  command=translation)
tran_bt.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# ------------------------tab_3-------------------#

def match():
    seq1 = seq1_entry.get()
    sub_seq = sub_seq_entry.get()

    x = -1
    for i in range(len(seq1) - len(sub_seq) + 1):
        if sub_seq == seq1[i:i + len(sub_seq)]:
            x = i
    textbox = customtkinter.CTkTextbox(tab_3, width=400, height=100)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{str(x)}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


def Badchars():
    seq1 = seq1_entry.get()
    sub_seq = sub_seq_entry.get()

    table = np.zeros([4, len(sub_seq)])
    row = ["C", "G", "A", "T"]
    for i in range(4):
        num = -1
        for j in range(len(sub_seq)):
            if row[i] == sub_seq[j]:
                table[i, j] = -1
                num = -1
            else:
                num += 1
                table[i, j] = num
    x = -1
    i = 0
    while (i < len(seq1) - len(sub_seq) + 1):
        if sub_seq == seq1[i:i + len(sub_seq)]:
            x = i
        else:
            for j in range(i + len(sub_seq) - 1, i - 1, -1):
                if seq1[j] != sub_seq[int(j - i)]:
                    k = row.index(seq[j])
                    i += table[k, j - i]
                    break
        i = int(i + 1)

    textbox = customtkinter.CTkTextbox(tab_3, width=400, height=100)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{x}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


# ------------------------------------------
label_2 = customtkinter.CTkLabel(master=tab_3,
                                 text="Matching , Bad characters",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_2.pack(pady=12, padx=10)
label_2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

seq1_entry = customtkinter.CTkEntry(master=tab_3,
                                    placeholder_text="Enter the Gene Seq",
                                    width=240,
                                    height=30,
                                    border_width=2,
                                    corner_radius=10)
seq1_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

sub_seq_entry = customtkinter.CTkEntry(master=tab_3,
                                       placeholder_text="Enter the Gene Sub Seq",
                                       width=240,
                                       height=30,
                                       border_width=2,
                                       corner_radius=10)
sub_seq_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

match_bt = customtkinter.CTkButton(master=tab_3,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="Match",
                                   command=match())
match_bt.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)

bad_bt = customtkinter.CTkButton(master=tab_3,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="BadChars",
                                 command=Badchars)
bad_bt.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)


# ------------------------tab_4-------------------#

def IndexSorted():
    seq = seq_entry.get()
    ln = int(ln_entry.get())
    index = []
    for i in range(len(seq) - ln + 1):
        index.append((seq[i:i + ln], i))
    index.sort()
    textbox = customtkinter.CTkTextbox(tab_4, width=400, height=170)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{str(index)}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


def query():
    seq = seq_entry.get()
    ln = int(ln_entry.get())
    index = []
    for i in range(len(seq) - ln + 1):
        index.append((seq[i:i + ln], i))
    index.sort()

    t = seq[1][0:-1]
    p = p_entry.get()
    keys = [r[0] for r in index]
    st = bisect.bisect_left(keys, p[:len(keys[0])])

    en = bisect.bisect(keys, p[:len(keys[0])])
    hits = index[st:en]
    l = [h[1] for h in hits]
    offsets = []
    for i in l:
        if t[i:i + len(p)] == p:
            offsets.append(i)

    textbox = customtkinter.CTkTextbox(tab_4, width=400, height=170)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{hits}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


# ------------------------------------------
label_2 = customtkinter.CTkLabel(master=tab_4,
                                 text="Index Sorting",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_2.pack(pady=12, padx=10)
label_2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

seq_entry = customtkinter.CTkEntry(master=tab_4,
                                   placeholder_text="Enter the Gene Seq",
                                   width=240,
                                   height=30,
                                   border_width=2,
                                   corner_radius=10)
seq_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

ln_entry = customtkinter.CTkEntry(master=tab_4,
                                  placeholder_text="Enter the Gene Length",
                                  width=240,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
ln_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

p_entry = customtkinter.CTkEntry(master=tab_4,
                                 placeholder_text="Choose Index for query",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
p_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

sort_bt = customtkinter.CTkButton(master=tab_4,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=8,
                                  text="Index Sort",
                                  command=IndexSorted)
sort_bt.place(relx=0.2, rely=0.55, anchor=tkinter.CENTER)

query_bt = customtkinter.CTkButton(master=tab_4,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="Query",
                                   command=query)
query_bt.place(relx=0.7, rely=0.55, anchor=tkinter.CENTER)

# ------------------------tab_5-------------------#

def IndexSorted():
    seq = seq_entry.get()
    ln = int(ln_entry.get())
    index = []
    for i in range(len(seq) - ln + 1):
        index.append((seq[i:i + ln], i))
    index.sort()
    textbox = customtkinter.CTkTextbox(tab_4, width=400, height=170)
    textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{str(index)}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


def overlap():
    a = a_entry.get()
    b = b_entry.get()
    min_len = int(min_ln_entry.get())
    j = len(a) - 1
    count = 0
    for i in range(len(b) - 1, -1, -1):
        if a[j] == b[i]:
            count += 1
            j -= 1
        else:
            count = 0
            j = len(a) - 1
            if a[j] == b[i]:
                count += 1
                j -= 1
    if count >= min_len:
        textbox = customtkinter.CTkTextbox(tab_5, width=400, height=170)
        textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

        textbox.insert("0.0", f"Overlap: {count}")  # insert at line 0 character 0
        textbox.configure(state="disabled")  # configure textbox to be read-only
    else:
        textbox = customtkinter.CTkTextbox(tab_5, width=400, height=170)
        textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

        textbox.insert("0.0", f"No overlap")  # insert at line 0 character 0
        textbox.configure(state="disabled")  # configure textbox to be read-only



# ------------------------------------------
label_2 = customtkinter.CTkLabel(master=tab_5,
                                 text="Overlapping",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_2.pack(pady=12, padx=10)
label_2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

a_entry = customtkinter.CTkEntry(master=tab_5,
                                   placeholder_text="Sequence 1",
                                   width=240,
                                   height=30,
                                   border_width=2,
                                   corner_radius=10)
a_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

b_entry = customtkinter.CTkEntry(master=tab_5,
                                  placeholder_text="Sequence 2",
                                  width=240,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
b_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

min_ln_entry = customtkinter.CTkEntry(master=tab_5,
                                 placeholder_text="Minimum length",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
min_ln_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

overlap_bt = customtkinter.CTkButton(master=tab_5,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=8,
                                  text="Overlap",
                                  command=overlap)
overlap_bt.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

# ------------------------tab_6-------------------#
def table():
    T = t_entry.get()
    l=[]
    for i in range(len(T)):
        l.append(T[i:])
    l2 = l.copy()
    l.sort()
    dec = {}
    for i in range(len(l)):
        dec[l[i]] = i
    table = []
    for i in range(len(l)):
        table.append([l2[i], i, dec[l2[i]]])

    textbox = customtkinter.CTkTextbox(tab_6, width=400, height=100)
    textbox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"{str(table)}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


# ------------------------------------------
# label_2 = customtkinter.CTkLabel(master=tab_2,
#                                  text="Translation",
#                                  width=120,
#                                  height=25,
#                                  corner_radius=8,
#                                  font=("Roboto", 20))
# label_2.pack(pady=12, padx=10)
# label_2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

t_entry = customtkinter.CTkEntry(master=tab_6,
                                 placeholder_text="Enter the Gene Seq",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
t_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

table_bt = customtkinter.CTkButton(master=tab_6,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=8,
                                  text="Create the table",
                                  command=table)
table_bt.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# ------------------------tab_7-------------------#
def cal_dist():
    seq1 = seq1_entry.get()
    seq2 = seq2_entry.get()

    tag = 3
    dic = {}
    for i in range(0, len(seq1) - tag):
        dic[seq1[i:i + tag]] = dic.get(seq1[i:i + tag], 0) + 1

    dic2 = {}
    for i in range(0, len(seq2) - tag):
        dic2[seq2[i:i + tag]] = dic2.get(seq2[i:i + tag], 0) + 1

    k = list(dic.keys())
    for i in range(len(k)):
        dic2[k[i]] = (dic2.get(k[i], 0) - dic[k[i]])
    d = list(dic2.values())
    Sum = 0
    for i in range(len(d)):
        Sum += d[i] ** 2
    distance = Sum ** (0.5)

    textbox = customtkinter.CTkTextbox(tab_7, width=400, height=100)
    textbox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    textbox.insert("0.0", f"The Distance Between two DNA Sequences = {distance}")  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")  # configure textbox to be read-only


# ------------------------------------------
label_2 = customtkinter.CTkLabel(master=tab_7,
                                 text="Calculating distance between two Sequences",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_2.pack(pady=12, padx=10)
label_2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

seq1_entry = customtkinter.CTkEntry(master=tab_7,
                                 placeholder_text="Sequence 1",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
seq1_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

seq2_entry = customtkinter.CTkEntry(master=tab_7,
                                 placeholder_text="Sequence 2",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
seq2_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

table_bt = customtkinter.CTkButton(master=tab_7,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=8,
                                  text="Calculate distance",
                                  command=cal_dist)
table_bt.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
