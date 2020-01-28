import numpy
import pandas
import sklearn.cluster

def split_by_data(org, channels, weights, keys, n_clusters):
    print("Running split_by_data (%d channels w %d clusters)" % (len(channels), n_clusters))

    print("    ... checks and config")
    for c in channels[1:]:
        if c.shape != channels[0].shape:
            for i, c in enumerate(channels):
                print("Channel", i, "shape is ", c.shape)
            raise ValueError("All channels must have the same shape (see listed shapes above)")

    rows, cols = channels[0].shape
    dims = len(channels)

    print("    ... building data frame")
    df = pandas.DataFrame()
    for channel, weight, key in zip(channels, weights, keys):
        df[key] = channel.flatten() * weight

    print("    ... running kmeans")
    kmeans = sklearn.cluster.KMeans(n_clusters=n_clusters, verbose=0)
    clusters = kmeans.fit_predict(df)

    print("    ... grabbing brushes")
    brushes = []
    for cluster_ix in range(max(clusters) + 1):
        brush = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append([255, 255, 255] if clusters[i * cols + j] != cluster_ix else org[i][j])
            brush.append(row)
        brush = numpy.array(brush)
        brushes.append(brush)

    print("done")
    return brushes