import numpy as np
import matplotlib.pyplot as plt

def plot_1D_data(x, y, xlabel="x", ylabel="y", title="My First Plot",
                 line_color="red", line_style="dotted"):
    plt.plot(x, y, color=line_color, linestyle=line_style)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

x = np.genfromtxt("../../data/x.csv")
y = np.genfromtxt("../../data/y.csv")

plot_1D_data(x, y)
plt.show()
plt.savefig("../../figures/3_exercise1_default_params.png")

plot_1D_data(x, y, xlabel="data", ylabel="predictions",
             title="Plot with custom parameters", line_color="blue",
             line_style="dashed")
plt.show()
plt.savefig("../../figures/3_exercise1_custom_params.png")

