import cianparser

parser = cianparser.CianParser(location="Пересвет")

data = parser.get_flats(deal_type="sale", rooms=(1), additional_settings={"start_page": 1, "end_page": 30}, with_extra_data=True, with_saving_csv=True)
