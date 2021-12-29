def date_format(date_list):
    for date in date_list:
        yy, mm, dd = date.split("-")

        yy = int(yy)
        mm = int(mm)
        dd = int(dd)

        if dd <= 0 or dd > 31:
            return False
        if mm <= 0 or mm > 12:
            return False
        if yy < 0:
            return False

    return True

def year_interval(date_list, min_year=1930, max_year=2022):
    for date in date_list:
        yy,_,_ = date.split("-")
        yy = int(yy)

        if yy < min_year or yy > max_year:
            return False
    
    return True