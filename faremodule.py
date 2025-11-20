def cal_fare(distance, coach):
    if coach == "AC":
        return distance * 3        # AC = ₹3 per km
    else:
        return distance * 1.5      # Sleeper = ₹1.5 per km