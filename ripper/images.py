import numpy
import skimage.io
import matplotlib.pyplot

matplotlib.pyplot.rcParams["image.cmap"] = 'viridis'
# matplotlib.pyplot.rcParams["image.cmap"] = 'gray'

def open_rgb(filepath):
    return skimage.io.imread(fname=filepath)

def convert_rgb_to_lab(img):
    return skimage.color.rgb2lab(img)

def split_by_channels(img):
    n = len(img[0, 0, :])
    return [ img[:, :, i] for i in range(n) ]

def show_one(img, vmin=None, vmax=None):
    if vmin is None and vmax is None:
        matplotlib.pyplot.imshow(img)
    else:
        matplotlib.pyplot.imshow(img, vmin=vmin, vmax=vmax)
    matplotlib.pyplot.show()

def show_in_grid(images, rows, cols, width, height, vmin=None, vmax=None):
    fig, axs = matplotlib.pyplot.subplots(
        nrows=rows, ncols=cols,
        figsize=(width, height),
        subplot_kw={'xticks': [], 'yticks': []}
    )
    for ax, img in zip(axs.flat, images):
        if vmin is None and vmax is None:
            ax.imshow(img)
        else:
             ax.imshow(img, vmin=vmin, vmax=vmax)
    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.show()

def show_two_by_one(images, width, height, vmin=None, vmax=None):
    show_in_grid(images, 1, 2, width, height, vmin=vmin, vmax=vmax)

# skimage.color.rgb2lab goes values:
#    0 - 100 for L
#    sometimes >50 or <-50 for A (using 200 to ensure 0..1)
#    sometimes >50 or <-50 for B (using 200 to ensure 0..1)
def lab_to_rgb_without_conversion(img):
    rows, cols, channels = img.shape
    rgb = numpy.zeros((rows, cols, channels))
    rgb[:, :, 0] = img[:, :, 0] / 100.0
    rgb[:, :, 1] = img[:, :, 1] / 200.0 + 0.5
    rgb[:, :, 2] = img[:, :, 2] / 200.0 + 0.5
    return rgb