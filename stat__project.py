from tkinter import *
from tkinter import ttk
import statistics
import numpy                         #   <------ Libraries we used
import scipy.stats
from matplotlib import *
import matplotlib.pyplot as plt
from tkinter import filedialog
ent3hidden = True
ent2hidden = True

#Code of the first window appears ---->

def win1():
    try:
        root.destroy()
    except:
        pass

    global root1
    root1 = Tk()
    root1.title("DashBoard")
    root1.geometry("500x500")
    ttk.Label(root1, text='\n').grid(row=0, column=0)
    ttk.Label(root1, text='Choose From Buttons Below the process you want : ').grid(row=0, column=0)
    Button1 = ttk.Button(root1, text=" Graphs ", command=win2)
    Button2 = ttk.Button(root1, text=" Data Measurement ", command=win3)
    Button3 = ttk.Button(root1, text=" Correlations ", command=win4)

    Button1.grid(row=4, column=2)
    ttk.Label(root1, text='\n').grid(row=5, column=0)
    Button2.grid(row=6, column=2)
    ttk.Label(root1, text='\n').grid(row=7, column=0)
    Button3.grid(row=8, column=2)
    ttk.Label(root1, text='\n').grid(row=9, column=0)
    root1.mainloop()



#When Clicking the first button in the first window .. the second window of graphs will appear :

def win2():

    def readEntries():
        global d1, d2, d3, d4
        if method.get() == 1 or method.get() == 2 or method.get() == 3 or method.get() == 6:
            d3 = ent1.get().split()
            d4 = ent2.get().split()
            d1 = [float(l) for l in d3]
            d2 = [float(l) for l in d4]
        elif method.get() == 4:
            d2 = ent1.get().split()
            d1 = [float(l) for l in d2]
        elif method.get() == 5:
            d3 = ent1.get().split()
            d4 = ent2.get().split()
            d1 = [float(l) for l in d3]
            d2 = [float(l) for l in d4]
            d4 = ent3.get().split()
            d3 = [float(l) for l in d4]
        print(d1)
        print(d2)


    def scatterplotfun():
        global d1, d2
        plt.scatter(d1, d2)
        plt.show()

    def barchartfun():
        global d1, d2
        plt.bar(d1, d2)
        plt.show()

    def piechartfun():
        global d1, d2
        plt.pie(d2, labels=d1, autopct='%1.1f%%', explode=numpy.random.uniform(0.0, 0.08, len(d1)), shadow=True)
        plt.show()


    def histogramfun():
        global d1, d3
        plt.hist(d1, d3)
        plt.show()

    def boxplotfun():
        global d1, d2
        plt.boxplot(d1)
        plt.show()

    def dotplotfun():
        global d1, d2, d4
        d4 = [[]]*len(d1)
        for i in range(len(d2)):
            d4[i] = range(1, int(d2[i])+1)
            b, k = numpy.meshgrid(d1[i], d4[i])
            plt.scatter(b, k)
        plt.show()

    def displayEntries():
        global ent2hidden, ent3hidden
        if method.get() == 1:
            if ent2hidden:
                lbl2.grid(row=15, column=1)
                ent2.grid(row=15, column=2)
                ent2hidden = False
            if not ent3hidden:
                lbl3.grid_remove()
                ent3.grid_remove()
                ent3hidden = True
        elif method.get() == 2:
            if ent2hidden:
                lbl2.grid(row=15, column=1)
                ent2.grid(row=15, column=2)
                ent2hidden = False
            if not ent3hidden:
                lbl3.grid_remove()
                ent3.grid_remove()
                ent3hidden = True
        elif method.get() == 3:
            if ent2hidden:
                lbl2.grid(row=15, column=1)
                ent2.grid(row=15, column=2)
                ent2hidden = False
            if not ent3hidden:
                lbl3.grid_remove()
                ent3.grid_remove()
                ent3hidden = True
        elif method.get() == 4:
            if not ent2hidden:
                lbl2.grid_remove()
                ent2.grid_remove()
                ent2hidden = True
            if not ent3hidden:
                lbl3.grid_remove()
                ent3.grid_remove()
                ent3hidden = True
        elif method.get() == 5:
            if not ent2hidden:
                lbl2.grid_remove()
                ent2.grid_remove()
                ent2hidden = True
            if ent3hidden:
                lbl3.grid(row=16, column=1)
                ent3.grid(row=16, column=2)
                ent3hidden = False
        elif method.get() == 6:
            if ent2hidden:
                lbl2.grid(row=15, column=1)
                ent2.grid(row=15, column=2)
                ent2hidden = False
            if not ent3hidden:
                lbl3.grid_remove()
                ent3.grid_remove()
                ent3hidden = True


    def graph(event):
        readEntries()
        if method.get() == 1:
            scatterplotfun()
        elif method.get() == 2:
            barchartfun()
        elif method.get() == 3:
            piechartfun()
        elif method.get() == 4:
            boxplotfun()
        elif method.get() == 5:
            histogramfun()
        elif method.get() == 6:
            dotplotfun()

    root1.destroy()
    global root
    root = Tk()
    root.title("DashBoard")
    root.geometry("500x500")

    method = IntVar()

    ttk.Label(root, text="Graphing Method").grid(row=7, column=1, sticky=N)
    scatterplot = ttk.Radiobutton(root, text="Scatter plot", variable=method, value=1, command=displayEntries)
    scatterplot.grid(row=8, column=1, sticky=W)
    barchart = ttk.Radiobutton(root, text="Bar chart", variable=method, value=2, command=displayEntries)
    barchart.grid(row=9, column=1, sticky=W)
    piechart = ttk.Radiobutton(root, text="Pie chart", variable=method, value=3, command=displayEntries)
    piechart.grid(row=10, column=1, sticky=W)
    boxplot = ttk.Radiobutton(root, text="Box plot", variable=method, value=4, command=displayEntries)
    boxplot.grid(row=11, column=1, sticky=W)
    histogram = ttk.Radiobutton(root, text="Histogram", variable=method, value=5, command=displayEntries)
    histogram.grid(row=12, column=1, sticky=W)
    dotplot = ttk.Radiobutton(root, text="Dot plot", variable=method, value=6, command=displayEntries)
    dotplot.grid(row=13, column=1, sticky=W)

    lbl1 = Label(root, text="Data 1 or Categories").grid(row=14, column=1)
    ent1 = ttk.Entry(root, width=50)
    ent1.grid(row=14, column=2)
    lbl2 = Label(root, text="Data 2 or Values or %")
    ent2 = ttk.Entry(root, width=50)
    lbl3 = Label(root, text="Bins")
    ent3 = ttk.Entry(root, width=50)

    graphBtn = ttk.Button(root, text="Graph!")
    graphBtn.grid(row=17, column=1)
    graphBtn.bind('<Button-1>', graph)
    btn0 = ttk.Button(root, text="Back ", command=win1).grid(row=17, column=2, sticky=E)
    root.mainloop()


#When Clicking the second button in the first window .. the third window of Data Measurement will appear :

def win3():
    def get_data():
        data = ent.get()
        data = data.strip()
        data_list = data.split(" ")
        new_data = [float(i) for i in data_list]
        return new_data

    def Mean(values):
        # li = get_data()
        mean_result = statistics.mean(values)
        return mean_result

    def Mode(values):
        # li = get_data()
        '''
        mode_result = statistics.mode(values)
        return mode_result
        '''
        list_table = statistics._counts(values)
        len_table = len(list_table)
        if len_table == 1:
            mode_result = statistics.mode(values)
        else:
            new_list = []
            for i in range(len_table):
                new_list.append(list_table[i][0])
            mode_result = max(new_list)
        return mode_result

    def Median(values):
        # li = get_data()
        median_result = statistics.median(values)
        return median_result

    def Range(values):
        values.sort()
        first = values[0]
        last = values[-1]
        range_result = last - first
        return range_result

    def Varience(values):
        variance_result = statistics.variance(values)
        return variance_result

    def Standard_Devition(values):
        st_dev = statistics.stdev(values)
        return st_dev

    def IQR(values):
        def median(a, l, r):
            n = r - l + 1
            n = (n + 1) // 2 - 1
            return n + l

            # Function to calculate IQR

        def IQR_2(a, n):
            a.sort()

            # Index of median of entire data
            mid_index = median(a, 0, n)

            # Median of first half
            Q1 = a[median(a, 0, mid_index)]

            # Median of second half
            Q3 = a[median(a, mid_index + 1, n)]

            # IQR calculation
            return (Q3 - Q1)

        x = IQR_2(values, len(values))
        return x

    def show_data():
        data = get_data()
        mean_result = int(Mean(data))
        a.set(mean_result)
        mode_result = int(Mode(data))
        b.set(mode_result)
        median_result = int(Median(data))
        c.set(median_result)
        range_result = int(Range(data))
        d.set(range_result)
        varience_result = Varience(data)
        e.set(varience_result)
        st = Standard_Devition(data)
        f.set(st)
        iqr = IQR(data)
        g.set(iqr)

    root1.destroy()
    global root
    root = Tk()
    root.title('Data Measurement')
    root.geometry("800x400")
    ttk.Label(root, text='\n\t Enter The Series of Data You Want To Measure :\t').grid(row=0, column=1)
    style = ttk.Style()
    '''
    ent = Entry(root, width=50).grid(row=0, column=3)#ent = Entry(root, width=250).grid(row=0, column=3)
    #ent = Entry.config(command=get_data)
    '''
    style.configure('TEntry', pady="10", padding="5")

    ent = Entry(root, width=50)
    ent.grid(row=0, column=3)
    btn0 = Button(root, text="Back ", command=win1).grid(row=12, column=3)

    btn = Button(root, text="show result", command=show_data).grid(row=0, column=5)

    ttk.Label(root, text='\n').grid(row=1, column=0)

    ttk.Label(root, text='Mean :').grid(row=2, column=1)
    a = StringVar()
    r1 = ttk.Label(root, textvariable=a).grid(row=2, column=2)

    ttk.Label(root, text='\n').grid(row=3, column=0)

    ttk.Label(root, text='Mode :').grid(row=4, column=1)
    b = StringVar()
    r2 = ttk.Label(root, textvariable=b).grid(row=4, column=2)

    ttk.Label(root, text='\n').grid(row=5, column=0)

    c = StringVar()
    ttk.Label(root, text='Median :').grid(row=6, column=1)
    r3 = ttk.Label(root, textvariable=c).grid(row=6, column=2)

    ttk.Label(root, text='\n').grid(row=7, column=0)

    d = StringVar()
    ttk.Label(root, text='Range :').grid(row=8, column=1)
    r4 = ttk.Label(root, textvariable=d).grid(row=8, column=2)

    ttk.Label(root, text='\n').grid(row=9, column=0)

    e = StringVar()
    ttk.Label(root, text='Variance :').grid(row=10, column=1)
    r5 = ttk.Label(root, textvariable=e).grid(row=10, column=2)

    ttk.Label(root, text='\n').grid(row=11, column=0)

    f = StringVar()
    ttk.Label(root, text='Standard Deviation :').grid(row=2, column=3)
    r6 = ttk.Label(root, textvariable=f).grid(row=2, column=4)

    g = StringVar()
    ttk.Label(root, text='IQR :').grid(row=4, column=3)
    r7 = ttk.Label(root, textvariable=g).grid(row=4, column=4)


    root.mainloop()


#When Clicking the third button in the first window .. the fourth window of Data Measurement will appear :
def win4():
    root1.destroy()
    global root
    root = Tk()
    global x, y,r,p
    x = []
    y = []

    # Correlate Function. It's bound to Button's event handler. It internally calls 3 correlation methods built-in functions
    # depending on which Radio Button is currently active

    def correlate(event):
        r = -2  # Initial value for r, in case the user didn't check any Radio button
        p = -2  # Initial value for p, in case the user didn't check any Radio button
        if val.get() == 1:
            r, p = scipy.stats.pearsonr(x, y)
        elif val.get() == 2:
            r, p = scipy.stats.spearmanr(x, y)
        elif val.get() == 3:
            r, p = scipy.stats.kendalltau(x, y)
        rt.set(r)
        pt.set(p)

    # A function to open a file, read it and populate the X and Y arrays with the values with in
    def openFile(event):
        
        filename = filedialog.askopenfilename()
        file_handler = open(filename)
        for line in file_handler:
            elements = line.split()
            x.append(float(elements[0]))
            y.append(float(elements[1]))



    def regress(event):
        pl = numpy.polyfit(x,y,1)
        f = numpy.poly1d(pl)
        x_line = numpy.linspace(min(x), max(x), 50)
        y_line = f(x_line)
        plt.figure(clear=True)
        plt.title("Data Points")
        plt.plot(x, y, 'o')
        plt.plot(x_line, y_line)
        plt.legend(['Actual Data Points', 'Linear Regression'])
        plt.show()


    #fig = plt.figure(1)

    # Beginning of the GUI
    #root = Tk()
    rt = StringVar()  # Label that displays r value has text dependent on this value
    pt = StringVar()  # Label that displays p value has text dependent on this value
    val = IntVar()
    root.title("Regression & Correlation")
    # root.geometry("800x450")
    # myplt = Canvas(root, width=400, height=225)
    # myplt.grid(row=1, column=5)
    root.title("Regression & Correlation")
    root.geometry("500x500")
    btn0 = Button(root, text="Back ", command=win1).grid(row=12, column=3)

    # Correlation Method Label and 3 Radio Buttons to indicate choice
    Label(root, text="Correlation Method").grid(row=7, column=1, sticky=N)
    pearson = Radiobutton(root, text="Pearson's Method", variable=val, value=1)
    pearson.grid(row=8, column=1, sticky=W)
    spearman = Radiobutton(root, text="Spearman's Method", variable=val, value=2)
    spearman.grid(row=9, column=1, sticky=W)
    kendall = Radiobutton(root, text="Kendall's Method", variable=val, value=3)
    kendall.grid(row=10, column=1, sticky=W)

    # Button with its event handler calling the correlate function
    corr = Button(root, text="Calculate correlation!")
    corr.grid(row=11, column=1, sticky=S)
    corr.bind('<Button-1>', correlate)

    # Group of Labels on which the result of the correlate function and its internally called methods is displayed.
    # Needs some work for the aesthetics. Sorry :)))))
    Label(root, text="Correlation Results").grid(row=7, column=10, sticky=N)
    Label(root, text="Correlation Coefficient").grid(row=8, column=10, sticky=W)
    Label(root, textvariable=rt).grid(row=8, column=11, sticky=W)
    Label(root, text="Statistical Significance").grid(row=9, column=10, sticky=W)
    Label(root, textvariable=pt).grid(row=9, column=11, sticky=W)

    # Button used to open an open file dialog box
    openBtn = Button(root, text="Open File")
    openBtn.grid(row=10, column=10, sticky=S)
    openBtn.bind('<Button-1>', openFile)

    # Button to start Graphing and calculate Linear Regression
    regressBtn = Button(root, text="Graph and Calculate Linear Regression")
    regressBtn.grid(row=11, column=10, sticky=S)
    regressBtn.bind('<Button-1>', regress)
    root.mainloop()


win1()
