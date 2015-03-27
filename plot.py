import matplotlib.pyplot as pyplot

colors  = ["#A00000", "#00A000", "#5060D0", "#F25900"]
markers = ['+', 'o', 'x', 'D'] 

def plotBoth(x, y1, y2):
    fig, (ax1, ax2) = pyplot.subplots(2, sharex=True, sharey=True)

    ax1.plot(x, y1)
    ax1.plot(x, y2)

    ax2.patch.set_facecolor('white')

    ax2.plot(x, y1, label="Example Line", marker='+',    lw=3, ms=15, markeredgewidth=2, color="#A00000",)
    ax2.plot(x, y2, label="Another example", marker='o', lw=3, ms=10, markeredgewidth=2, color="#00A000", fillstyle="none")

    ax2 = fig.gca()

    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(0, 1.0)

    ax2.grid(color="#808080", linestyle="solid")

    ax2.xaxis.set_label_text('x axis label', weight="bold", fontsize="large")
    ax2.xaxis.set_tick_params(width=2, length=10, colors="#808080", labelsize="large")
    
    ax2.yaxis.set_label_text('y axis label', weight="bold", fontsize="large")
    ax2.yaxis.set_tick_params(width=2, length=10, colors="#808080", labelsize="large")

    ax2.legend(loc='lower right', fontsize='large', framealpha=0)

    pyplot.show()

def regularPlot(x, y1, y2):

    fig = pyplot.figure()

    pyplot.plot(x, y1)
    pyplot.plot(x, y2)

    pyplot.show()

def prettyPlot(x, y1, y2):

    fig = pyplot.figure()

    fig.patch.set_facecolor('white')

    pyplot.plot(x, y1, label="Example Line", marker='+',    lw=3, ms=15, markeredgewidth=2, color="#A00000",)
    pyplot.plot(x, y2, label="Another example", marker='o', lw=3, ms=10, markeredgewidth=2, color="#00A000", fillstyle="none")

    ax = fig.gca()

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)

    ax.grid(color="#808080", linestyle="solid")

    ax.xaxis.set_label_text('x axis label', weight="bold", fontsize="large")
    ax.xaxis.set_tick_params(width=2, length=10, colors="#808080", labelsize="large")
    
    ax.yaxis.set_label_text('y axis label', weight="bold", fontsize="large")
    ax.yaxis.set_tick_params(width=2, length=10, colors="#808080", labelsize="large")

    ax.legend(loc='lower right', fontsize='large', framealpha=0)

    pyplot.show()

if __name__ == "__main__":
    
    x  = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
    y1 = [0.80, 0.70, 0.81, 0.89, 0.90, 0.96, 0.90, 0.82, 0.75, 0.60, 0.41] 
    y2 = [0.40, 0.39, 0.30, 0.28, 0.38, 0.20, 0.29, 0.39, 0.41, 0.50, 0.70]

    # regularPlot(x, y1, y2)
    # prettyPlot(x, y1, y2)
    plotBoth(x, y1, y2)

    