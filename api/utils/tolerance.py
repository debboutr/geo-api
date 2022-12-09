def find_tolerance(area):
    if area > 1_000_000:
        return "0.005"
    elif area > 10_000:
        return "0.002"
    elif area > 1_000:
        return "0.001"
    else:
        None
