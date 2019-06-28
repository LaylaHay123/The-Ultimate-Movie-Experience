def intro(hours, minutes):
    if hours <= "01" or hours <= "1" and minutes == "00" or minutes == "0":
        return "Small Popcorn"
    elif hours >=  "01" or hours >= "1" and minutes > "00" or minutes > "0":
        return "Medium Popcorn"
    elif hours > "02" or hours > "2" and minutes >= "00" or minutes >= "0":
        return "Large Popcorn"
        