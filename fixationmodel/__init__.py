from numbers import Number

# Semantic versioning
version = '0.1.0'

def variance(it, mean):
    # Biased sample variance
    s = 0.0
    for x in it:
        d = x - mean
        s += d * d
    return s / len(it)

def fit(pointlist):
    '''
    Parameters
        pointlist
            [[x0,y0], [x1,y1], [x2,y2], ...]
            Points [None, None] are allowed but ignored.
    '''

    # Separate x and y and clear Nones
    is_num = lambda x: isinstance(x, Number)
    pick_x = lambda x: x[0]
    pick_y = lambda x: x[1]
    xs = list(filter(is_num, map(pick_x, pointlist)))
    ys = list(filter(is_num, map(pick_y, pointlist)))

    # Note biased mean and variance
    mean_x = sum(xs) / float(len(xs))
    mean_y = sum(xs) / float(len(xs))
    var_x = variance(xs, mean_x)
    var_y = variance(ys, mean_y)

    # Combine variances:
    #     variance_x = (dx0^2 + dx1^2 + ...) / n
    #   Therefore
    #     variance_xy = ((dx0^2 + dy0^2) + (dx1^2 + dy1^2) + ...) / n
    #                 = variance_x + variance_y
    var_xy = var_x + var_y

    return {
        'centroid': [mean_x, mean_y],
        'mean_squared_error': var_xy
    }
