from tkinter import *
from tkinter import messagebox
import os.path
import random

if not os.path.isfile("log"):
    test_file = open("log", "x")
    test_file.close()

root = Tk()
root.title("Scale Practice")
root.geometry("640x350")

select_s_frame = LabelFrame(root, text="Select scales", padx=5, pady=11)
select_s_frame.grid(column=0, row=0, rowspan=4, padx=5, pady=5, sticky=NW)
run_frame = LabelFrame(root, text="Results", padx=10, pady=5)
run_frame.grid(column=1, row=0, columnspan=2, padx=5, pady=5, sticky=NE)
select_n_frame = LabelFrame(root, text="No. of scales", padx=10, pady=8)
select_n_frame.grid(column=1, row=1, rowspan=3,  padx=5, pady=5, sticky=NW)
minor_frame = LabelFrame(root, text="Minor options", padx=10)
minor_frame.grid(column=2, row=1, padx=5, pady=5, sticky=NE)

scale_variables = ["c_maj_v", "a_min_v", "g_maj_v", "e_min_v", "d_maj_v", "b_min_v", "a_maj_v", "f_sharp_min_v",
                   "e_maj_v", "c_sharp_min_v", "b_maj_v", "g_sharp_min_v", "f_sharp_maj_v", "d_sharp_min_v",
                   "f_maj_v", "d_min_v", "b_flat_maj_v", "g_min_v", "e_flat_maj_v", "c_min_v", "a_flat_maj_v",
                   "f_min_v", "d_flat_maj_v", "b_flat_min_v"]

for scale_var_global in scale_variables:
    exec(scale_var_global + " = IntVar()")

c_maj = Checkbutton(select_s_frame, text="C-major", variable=c_maj_v)
a_min = Checkbutton(select_s_frame, text="A-minor", variable=a_min_v)
g_maj = Checkbutton(select_s_frame, text="G-major", variable=g_maj_v)
e_min = Checkbutton(select_s_frame, text="E-minor", variable=e_min_v)
d_maj = Checkbutton(select_s_frame, text="D-major", variable=d_maj_v)
b_min = Checkbutton(select_s_frame, text="B-minor", variable=b_min_v)
a_maj = Checkbutton(select_s_frame, text="A-major", variable=a_maj_v)
f_sharp_min = Checkbutton(select_s_frame, text="F♯-minor", variable=f_sharp_min_v)
e_maj = Checkbutton(select_s_frame, text="E-major", variable=e_maj_v)
c_sharp_min = Checkbutton(select_s_frame, text="C♯-minor", variable=c_sharp_min_v)
b_maj = Checkbutton(select_s_frame, text="B-major", variable=b_maj_v)
g_sharp_min = Checkbutton(select_s_frame, text="G♯-minor", variable=g_sharp_min_v)
f_sharp_maj = Checkbutton(select_s_frame, text="F♯/G♭-major", variable=f_sharp_maj_v)
d_sharp_min = Checkbutton(select_s_frame, text="D♯/E♭-minor", variable=d_sharp_min_v)
f_maj = Checkbutton(select_s_frame, text="F-major", variable=f_maj_v)
d_min = Checkbutton(select_s_frame, text="D-minor", variable=d_min_v)
b_flat_maj = Checkbutton(select_s_frame, text="B♭-major", variable=b_flat_maj_v)
g_min = Checkbutton(select_s_frame, text="G-minor", variable=g_min_v)
e_flat_maj = Checkbutton(select_s_frame, text="E♭-major", variable=e_flat_maj_v)
c_min = Checkbutton(select_s_frame, text="C-minor", variable=c_min_v)
a_flat_maj = Checkbutton(select_s_frame, text="A♭-major", variable=a_flat_maj_v)
f_min = Checkbutton(select_s_frame, text="F-minor", variable=f_min_v)
d_flat_maj = Checkbutton(select_s_frame, text="D♭-major", variable=d_flat_maj_v)
b_flat_min = Checkbutton(select_s_frame, text="B♭-minor", variable=b_flat_min_v)

c_maj.grid(row=0, column=7, columnspan=3, sticky=W)
a_min.grid(row=1, column=7, columnspan=3, sticky=W)
g_maj.grid(row=1, column=4, columnspan=3, sticky=W)
e_min.grid(row=2, column=4, columnspan=3, sticky=W)
d_maj.grid(row=3, column=2, columnspan=3, sticky=W)
b_min.grid(row=4, column=2, columnspan=3, sticky=W)
a_maj.grid(row=5, column=1, columnspan=3, sticky=W)
f_sharp_min.grid(row=6, column=1, columnspan=3, sticky=W)
e_maj.grid(row=7, column=2, columnspan=3, sticky=W)
c_sharp_min.grid(row=8, column=2, columnspan=3, sticky=W)
b_maj.grid(row=9, column=4, columnspan=3, sticky=W)
g_sharp_min.grid(row=10, column=4, columnspan=3, sticky=W)
f_sharp_maj.grid(row=10, column=7, columnspan=3, sticky=W)
d_sharp_min.grid(row=11, column=7, columnspan=3, sticky=W)
f_maj.grid(row=1, column=10, columnspan=3, sticky=W)
d_min.grid(row=2, column=10, columnspan=3, sticky=W)
b_flat_maj.grid(row=3, column=12, columnspan=3, sticky=W)
g_min.grid(row=4, column=12, columnspan=3, sticky=W)
e_flat_maj.grid(row=5, column=13, columnspan=3, sticky=W)
c_min.grid(row=6, column=13, columnspan=3, sticky=W)
a_flat_maj.grid(row=7, column=12, columnspan=3, sticky=W)
f_min.grid(row=8, column=12, columnspan=3, sticky=W)
d_flat_maj.grid(row=9, column=10, columnspan=3, sticky=W)
b_flat_min.grid(row=10, column=10, columnspan=3, sticky=W)

minor_natural_v = IntVar()
minor_natural_v.set(1)
minor_harmonic_v = IntVar()
minor_melodic_v = IntVar()
minor_natural = Checkbutton(minor_frame, text="Natural", variable=minor_natural_v, onvalue=1)
minor_natural.grid(sticky=W)
minor_harmonic = Checkbutton(minor_frame, text="Harmonic", variable=minor_harmonic_v, onvalue=1)
minor_harmonic.grid(sticky=W)
minor_melodic = Checkbutton(minor_frame, text="Melodic", variable=minor_melodic_v, onvalue=1)
minor_melodic.grid(sticky=W)

number_results = IntVar()
number_results.set(3)
Radiobutton(select_n_frame, text=1, variable=number_results, value=1).grid()
Radiobutton(select_n_frame, text=2, variable=number_results, value=2).grid()
Radiobutton(select_n_frame, text=3, variable=number_results, value=3).grid()
Radiobutton(select_n_frame, text=4, variable=number_results, value=4).grid()
Radiobutton(select_n_frame, text=5, variable=number_results, value=5).grid()


def count_scales():
    number = c_maj_v.get() + a_min_v.get() + g_maj_v.get() + e_min_v.get() + d_maj_v.get() + b_min_v.get() +\
             a_maj_v.get() + f_sharp_min_v.get() + e_maj_v.get() + c_sharp_min_v.get() + b_maj_v.get() +\
             g_sharp_min_v.get() + f_sharp_maj_v.get() + d_sharp_min_v.get() + f_maj_v.get() + d_min_v.get() +\
             b_flat_maj_v.get() + g_min_v.get() + e_flat_maj_v.get() + c_min_v.get() + a_flat_maj_v.get() +\
             f_min_v.get() + d_flat_maj_v.get() + b_flat_min_v.get()
    return number


def select_all():
    for scale_var in scale_variables:
        exec(scale_var + ".set(1)")


def clear_all():
    for scale_var in scale_variables:
        exec(scale_var + ".set(0)")


def clear_log():
    open("log", "w").close()


button_select_all = Button(select_s_frame, text="Select all", command=select_all)
button_select_all.grid(row=11, column=1, rowspan=2, columnspan=2, padx=5, sticky=SE)
button_clear_all = Button(select_s_frame, text="Clear all", command=clear_all)
button_clear_all.grid(row=11, column=14, rowspan=2, columnspan=2, padx=5, sticky=SE)


def print_results():

    scales_used = []
    minor_option = []

    if minor_natural_v.get() != 0:
        minor_option.append(" natural")
    if minor_harmonic_v.get() != 0:
        minor_option.append(" harmonic")
    if minor_melodic_v.get() != 0:
        minor_option.append(" melodic")

    if len(minor_option) == 0:
        messagebox.showerror("Error", "Select at least one option for minor scales")
        return

    old_scales = []
    with open("log", "r") as scale_log:

        for line in scale_log:
            line = line.strip()
            old_scales.append(line)

    if count_scales() - number_results.get() <= 1:
        old_scales = []
    else:
        old_scales = old_scales[(int(-(count_scales() - number_results.get() - 1))):]

    scale_code = []

    if c_maj_v.get() != 0 and "001" not in old_scales:
        scales_used.append("C-Major")
        scale_code.append("001")
    if a_min_v.get() != 0 and "101" not in old_scales:
        scales_used.append("A-Minor" + random.choice(minor_option))
        scale_code.append("101")
    if g_maj_v.get() != 0 and "002" not in old_scales:
        scales_used.append("G-Major" + " (1♯)")
        scale_code.append("002")
    if e_min_v.get() != 0 and "102" not in old_scales:
        scales_used.append("E-Minor" + random.choice(minor_option) + " (1♯)")
        scale_code.append("102")
    if d_maj_v.get() != 0 and "003" not in old_scales:
        scales_used.append("D-Major" + " (2♯)")
        scale_code.append("003")
    if b_min_v.get() != 0 and "103" not in old_scales:
        scales_used.append("B-Minor" + random.choice(minor_option) + " (2♯)")
        scale_code.append("103")
    if a_maj_v.get() != 0 and "004" not in old_scales:
        scales_used.append("A-Major" + " (3♯)")
        scale_code.append("004")
    if f_sharp_min_v.get() != 0 and "104" not in old_scales:
        scales_used.append("F♯-Minor" + random.choice(minor_option) + " (3♯)")
        scale_code.append("104")
    if e_maj_v.get() != 0 and "005" not in old_scales:
        scales_used.append("E-Major" + " (4♯)")
        scale_code.append("005")
    if c_sharp_min_v.get() != 0 and "105" not in old_scales:
        scales_used.append("C♯-Minor" + random.choice(minor_option) + " (4♯)")
        scale_code.append("105")
    if b_maj_v.get() != 0 and "006" not in old_scales:
        scales_used.append("B-Major" + " (5♯)")
        scale_code.append("006")
    if g_sharp_min_v.get() != 0 and "106" not in old_scales:
        scales_used.append("G♯-Minor" + random.choice(minor_option) + " (5♯)")
        scale_code.append("106")
    if f_sharp_maj_v.get() != 0 and "007" not in old_scales:
        scales_used.append("F♯/G♭-Major" + " (6♯ or ♭)")
        scale_code.append("007")
    if d_sharp_min_v.get() != 0 and "107" not in old_scales:
        scales_used.append("D♯/E♭-Minor" + random.choice(minor_option) + " (6♯ or ♭)")
        scale_code.append("107")
    if f_maj_v.get() != 0 and "008" not in old_scales:
        scales_used.append("F-Major" + " (1♭)")
        scale_code.append("008")
    if d_min_v.get() != 0 and "108" not in old_scales:
        scales_used.append("D-Minor" + random.choice(minor_option) + " (1♭)")
        scale_code.append("108")
    if b_flat_maj_v.get() != 0 and "009" not in old_scales:
        scales_used.append("B♭-Major" + " (2♭)")
        scale_code.append("009")
    if g_min_v.get() != 0 and "109" not in old_scales:
        scales_used.append("G-Minor" + random.choice(minor_option) + " (2♭)")
        scale_code.append("109")
    if e_flat_maj_v.get() != 0 and "010" not in old_scales:
        scales_used.append("E♭-Major" + " (3♭)")
        scale_code.append("010")
    if c_min_v.get() != 0 and "110" not in old_scales:
        scales_used.append("C-Minor" + random.choice(minor_option) + " (3♭)")
        scale_code.append("110")
    if a_flat_maj_v.get() != 0 and "011" not in old_scales:
        scales_used.append("A♭-Major" + " (4♭)")
        scale_code.append("011")
    if f_min_v.get() != 0 and "111" not in old_scales:
        scales_used.append("F-Minor" + random.choice(minor_option) + " (4♭)")
        scale_code.append("111")
    if d_flat_maj_v.get() != 0 and "012" not in old_scales:
        scales_used.append("D♭-Major" + " (5♭)")
        scale_code.append("012")
    if b_flat_min_v.get() != 0 and "112" not in old_scales:
        scales_used.append("B♭-Minor" + random.choice(minor_option) + " (5♭)")
        scale_code.append("120")

    if len(scales_used) >= number_results.get():
        mediator = list(range(0, len(scales_used)))
        mediator_results = random.sample(mediator, k=number_results.get())
        result1.delete(0, END)
        result2.delete(0, END)
        result3.delete(0, END)
        result4.delete(0, END)
        result5.delete(0, END)

        with open("log", "a+") as scale_log:
            result1.insert(0, scales_used[mediator_results[0]])
            scale_log.write(scale_code[mediator_results[0]] + "\n")
            if number_results.get() >= 2:
                result2.insert(0, scales_used[mediator_results[1]])
                scale_log.write(scale_code[mediator_results[1]] + "\n")

            if number_results.get() >= 3:
                result3.insert(0, scales_used[mediator_results[2]])
                scale_log.write(scale_code[mediator_results[2]] + "\n")

            if number_results.get() >= 4:
                result4.insert(0, scales_used[mediator_results[3]])
                scale_log.write(scale_code[mediator_results[3]] + "\n")

            if number_results.get() >= 5:
                result5.insert(0, scales_used[mediator_results[4]])
                scale_log.write(scale_code[mediator_results[4]] + "\n")

            scale_log.seek(0, 0)
            old_log = scale_log.read()

        if len(old_log) > 96:

            with open("log", "w") as scale_log:
                scale_log.write(old_log[number_results.get() * 4:])

    else:
        messagebox.showerror("Error", "Select more scales")


result1 = Entry(run_frame,  width=28)
result1.grid(row=0, column=1)
result2 = Entry(run_frame, width=28)
result2.grid(row=1, column=1)
result3 = Entry(run_frame, width=28)
result3.grid(row=2, column=1)
result4 = Entry(run_frame, width=28)
result4.grid(row=3, column=1)
result5 = Entry(run_frame, width=28)
result5.grid(row=4, column=1)

button_exit = Button(root, text="Exit", command=root.quit, padx=39).grid(row=3, column=2, padx=5, pady=5, sticky=SE)
button_clear_log = Button(root, text="Clear log", command=clear_log, padx=25).grid(row=2, column=2, padx=5, sticky=NE)
button_run = Button(run_frame, text="Run", command=print_results, padx=25)
button_run.grid(row=5, column=1, pady=10)

root.mainloop()
