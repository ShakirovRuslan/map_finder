def get_scale_params(object):
    corners = object["boundedBy"]["Envelope"]
    lower_corner = list(map(float, corners["lowerCorner"].split()))
    upper_corner = list(map(float, corners["upperCorner"].split()))
    width = upper_corner[0] - lower_corner[0]
    height = upper_corner[1] - lower_corner[1]
    return [width, height]