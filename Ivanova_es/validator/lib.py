import re

def latin_name_validator(input: str):
    return bool(re.fullmatch(r"([A-Z]+\s*)+", input))

def cen_year_validator(input: str):
    return bool(re.fullmatch(r"(19[0-9]{2}|20([0-1][0-9]))", input))

def whire_htap_validator(input: str):
    return bool(re.fullmatch(r"Yes|No|yes|no", input))

def horz_plant_validator(input: str):
    return bool(re.fullmatch(r"Yes|No|yes|no", input))