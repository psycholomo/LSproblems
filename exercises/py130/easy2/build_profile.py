def build_profile(first_name, last_name, **kwargs):
    return f"{first_name} {last_name}, {kwargs}"


print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}