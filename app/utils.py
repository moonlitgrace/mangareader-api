
# Check if string is float or not
def isfloat(str: str) -> bool:
    try:
        float(str)
        return True
    except ValueError: return False