<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

fig, ax = plt.subplots()

# Fixing random state for reproducibility
np.random.seed(19680801)


# histogram our data with numpy

data = np.random.randn(1000)
n, bins = np.histogram(data, 50)

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n


# we need a (numrects x numsides x 2) numpy array for the path helper
# function to build a compound path
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

# get the Path object
barpath = path.Path.make_compound_path_from_polys(XY)

# make a patch out of it
patch = patches.PathPatch(barpath)
ax.add_patch(patch)

# update the view limits
ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

plt.title('Histograms using Rectangles and PolyCollections')
=======
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from numpy.random import multivariate_normal

data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[2, 3], [1, 3]], size=1000)
])

gammas = [0.8, 0.5, 0.3, 0.1, 0.05]

fig, axes = plt.subplots(nrows=2, ncols=3)#グラフの数を2*2から2*3に変更

axes[0, 0].set_title('Linear normalization')
H = axes[0, 0].hist2d(data[:, 0], data[:, 1], bins=100)
axes[0, 0].set_xlabel('x')#xラベルを追加
axes[0, 0].set_ylabel('y')#yラベルを追加
fig.colorbar(H[3], ax=axes[0, 0])#ヒストグラムのカラーバーを追加
axes[0, 0].grid()#gridの追加

for ax, gamma in zip(axes.flat[1:], gammas):
    ax.set_title('Power law $(\gamma=%1.2f)$' % gamma)
    ax.hist2d(data[:, 0], data[:, 1],
                  bins=100, norm=mcolors.PowerNorm(gamma))
    ax.set_xlabel('x')#xラベルを追加
    ax.set_ylabel('y')#yラベルを追加
    fig.colorbar(H[3], ax=ax)#ヒストグラムのカラーバーを追加
    ax.grid()#gridの追加

fig.tight_layout()

>>>>>>> cd951456a9bfcb1d5a5e23da9e18aa3af1adea66

plt.show()
