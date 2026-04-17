def search_country(country_name):
    countries = ["nepal", "usa", "canada", "russia", "turkey"]  
    try:
        index = countries.index(country_name)
        return index 
    except ValueError:
        return "Country not found"


print("Enter your Country name")
a = input("> ")
result = search_country(a)  
print(result) 