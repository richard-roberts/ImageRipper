import numpy

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