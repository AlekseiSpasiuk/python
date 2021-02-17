#!python3

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def contact_to_string(name,soname, year, city, email, tel):
    c = f"{name} {soname} {year} {city} {email} {tel}"
    return c
name = input("Name = ")
soname = input("Soname = ")
year = input("Year = ")
city = input("City = ")
email = input("Email = ")
tel = input("tel = ")
print(contact_to_string(soname=soname,name=name,year=year,city=city,email=email,tel=tel))

