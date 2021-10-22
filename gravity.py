import csv
import pandas as pd
rows = []

df = pd.read_csv("main2.csv")
solar_mass_list = df["Mass"].tolist()
solar_radius_list = df["Radius"].tolist()
solar_mass_list.pop(0)
solar_radius_list.pop(0)
star_solar_mass_si_unit = []
for data in solar_mass_list:
    si_unit = float(data)*1.989e+30
    star_solar_mass_si_unit.append(si_unit)
print(star_solar_mass_si_unit)
star_solar_radius_si_unit = []
for data in solar_radius_list:
    si_unit = float(data)*6.957e+8
    star_solar_radius_si_unit.append(si_unit)
print(star_solar_radius_si_unit)
star_masses = star_solar_mass_si_unit
star_radiuses = star_solar_radius_si_unit
star_names = df["Star_name"].tolist()
star_names.pop(0)
star_gravities = []
for index,data in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000) * 6.674e-11
    star_gravities.append(gravity)
print(star_gravities)

df["Gravity"] = pd.Series(star_gravities)
df.to_csv("Final.csv")