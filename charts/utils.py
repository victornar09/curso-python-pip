from matplotlib import pyplot as plt

# Funcion para seleccionar un pais de interos
def get_country_info(datos):
    country = input('What country are you interested in? Write your answer: ')
    filtrado = list(filter(lambda item: item['Country/Territory'] == country, datos))
    return filtrado[0], country

# Funcion para obtener la informacion relacionada con la población de un país

def get_population_info(country):
    years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']
    population = [int(country[poblacion]) for poblacion in years]
    year_labels = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]
    population.reverse()
    year_labels.reverse()
    return population, year_labels

# Funcion para obtener un diccionario de poblacion

def dict_population(years, population):
    result = {ano: pobl for (ano, pobl) in zip(years, population)}
    return result

# Funcion para graficar

def plot_bar(info, country):
    fig, ax = plt.subplots()
    ax.bar(info.keys(), info.values())
    plt.savefig(f'./img/{country}.png')
    plt.close()