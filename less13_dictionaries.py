# Dictionaries - special structure in python which allows us to store information in key-value pairs

"""Building a program which concerts 3 digit name into a full moth name"""

monthConvertions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
"""Different ways of accessing month names"""
print(monthConvertions["Nov"])  # --> November
print(monthConvertions.get("Dec"))  # --> December

"""If the key is not in a dictionary, we can pass a default value to it"""
print(monthConvertions.get("Luv", "Not a valid key"))
