from src.scraper import coronaWorldometersScrapper

output_file = "statsCorona.csv"

#We are calling here the main function, receiving a df with the information and storing it in a csv.

scraper = coronaWorldometersScrapper()
df = scraper.scrap()
scraper.df_to_csv(r'/Users/u598728/Documents/Master/PRAC1/csv/' + output_file,df)