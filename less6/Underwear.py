underwear = {
    "XXS": {"Ukraine": 42, "Germany": 36, "USA": 8, "France": 38, "UK": 24},
    "XS": {"Ukraine": 44, "Germany": 38, "USA": 10, "France": 40, "UK": 26},
    "S": {"Ukraine": 46, "Germany": 40, "USA": 12, "France": 42, "UK": 28},
    "M": {"Ukraine": 48, "Germany": 42, "USA": 14, "France": 44, "UK": 30},
    "L": {"Ukraine": 50, "Germany": 44, "USA": 16, "France": 46, "UK": 32},
    "XL": {"Ukraine": 52, "Germany": 46, "USA": 18, "France": 48, "UK": 34},
    "XXL": {"Ukraine": 54, "Germany": 48, "USA": 20, "France": 50, "UK": 36},
    "XXXL": {"Ukraine": 56, "Germany": 50, "USA": 22, "France": 52, "UK": 38}
}


def size(a, b):
    return f"your size in {b} : {(underwear.get(a)).get(b)}"


print(size(input("Choose international size: "), input("Select your country: ")))
