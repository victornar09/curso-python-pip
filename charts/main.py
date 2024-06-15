import charts
import read_data as rd
import utils

def run():

    data = rd.read_csv('world_pop.csv')
    datos_pais, pais = utils.get_country_info(data)
    pobl, anos = utils.get_population_info(datos_pais)
    demografia = utils.dict_population(anos, pobl)
    utils.plot_bar(demografia, pais)


if __name__ == '__main__':
    run()