def calculate_age_on_planet(age_in_seconds):
    earth_seconds = 31557600
    planet_ratios = {
        'Earth': 1,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    earth_years = age_in_seconds / earth_seconds
    age_on_planets = {planet: earth_years / ratio for planet, ratio in planet_ratios.items()}

    return age_on_planets

age_in_seconds = 1000000000
age_on_planets = calculate_age_on_planet(age_in_seconds)

for planet, age in age_on_planets.items():
    print(f"Age on {planet}: {age:.2f} Earth-years")
