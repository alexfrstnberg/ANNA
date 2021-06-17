import matplotlib.pyplot as plt
import numpy as n
from collections import OrderedDict
import matplotlib.cm as cm
import os

def replace_all(str):
    chars = '\\`*_{}[]()>#+-.!$?\' '
    for c in chars:
        str = str.replace(c, '')
    return str

fig = plt.figure()

def letters_graph(text, ax):
    text = text.upper()
    data = {i.upper(): text.count(i) for i in set(replace_all(text))}
    stat = OrderedDict(sorted(data.items(), key=lambda x:x[0]))
    colors = cm.rainbow(n.linspace(0, 1, len(stat)))
    ax.bar(stat.keys(), stat.values(), color=colors)
    plt.savefig(os.path.join('L14', '14.1.png'))
    plt.show()

ax1 = fig.add_subplot()
ax1.set_title('Letters stats')

with open(os.path.join('L14', 'text.txt')) as f:
    data = f.read()
    letters_graph(data, ax1)
