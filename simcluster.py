"""Utilities for generating simulated astronomical images."""

import numpy as np
from scipy.ndimage.filters import gaussian_filter


CLUSTER_DEFAULTS = {
    'stars': 10000,
    'dimensions': (512, 512)
}


def simulated_cluster(n_stars=CLUSTER_DEFAULTS['stars'],
                      dimensions=CLUSTER_DEFAULTS['dimensions']):
    """
    Generates an image simulating a cluster of stars, including
    a Gaussian filter and background noise.

    Parameters
    ----------
    n_stars : `int`
        A positive integer giving the number of visible stars in the image
        (default: 10000).

    dimensions : `tuple`
        A two-tuple of positive integers specifying the dimensions (in pixels)
        of the output image (default: 512x512).

    Returns
    -------
    array : `~numpy.ndarray`
        A 2D Numpy array containing the pixels of the generated image.
    """

    nx, ny = dimensions

    # Create empty image
    image = np.zeros((ny, nx))

    # Generate random positions
    r = np.random.random(n_stars) * nx
    theta = np.random.uniform(0., 2. * np.pi, n_stars)

    # Generate random fluxes
    fluxes = np.random.random(n_stars) ** 2

    # Compute position
    x = nx / 2 + r * np.cos(theta)
    y = ny / 2 + r * np.sin(theta)

    # Add stars to image
    # ==> First for loop and if statement <==
    for idx in range(n_stars):
        if x[idx] >= 0 and x[idx] < nx and y[idx] >= 0 and y[idx] < ny:
            image[y[idx], x[idx]] += fluxes[idx]

    # Convolve with a gaussian
    image = gaussian_filter(image, sigma=1)

    # Add noise
    image += np.random.normal(1., 0.001, image.shape)

    return image
