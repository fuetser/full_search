def get_spn(envelope):
    bottom_long, bottom_lat = map(float, envelope['lowerCorner'].split())
    top_long, top_lat = map(float, envelope['upperCorner'].split())
    return f"{abs(bottom_long - top_long)},{abs(bottom_lat - top_lat)}"
