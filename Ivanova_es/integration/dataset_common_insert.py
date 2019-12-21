import Ivanova_es.integration.dataset_structure_common as d
import Ivanova_es.validator.lib as i
import sydorovos.validator.lib as s

def add_data(dataset: dict, latin_name: str, zip_city: str, st_assem: str, cen_year: str, horz_blck: str, whire_htap: str, horz_plant: str):
    latin_name1 = i.latin_name_validator(latin_name)
    zip_city1 = s.zip_city_validator(zip_city)
    st_assem1 = s.st_assem_validator(st_assem)
    cen_year1 = i.cen_year_validator(cen_year)
    horz_blck1 = s.horz_blck_validator(horz_blck)
    whire_htap1 = i.whire_htap_validator(whire_htap)
    horz_plant1 = i.horz_plant_validator(horz_plant)
    if latin_name1 == True and zip_city1 == True and st_assem1 == True and cen_year1 == True and horz_blck1 == True and whire_htap1 == True and horz_plant1 == True:
        dataset[latin_name] = {
            'zip_city': zip_city
            ,'st_assem': st_assem
            ,'cen_year': cen_year
            ,'horz_blck': horz_blck
            ,'whire_htap': whire_htap
            ,'horz_plant': horz_plant
            }
    else:
        print("Incorrect input")
add_data(d.dataset, 'FRAXINUS PENNSYLVANICA', 'Bronx', '0', '2006', 'No', 'No', 'No')
print(d.dataset)