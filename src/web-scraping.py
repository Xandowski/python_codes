from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd


PATH = "C:/Program Files (x86)/msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://globoesporte.globo.com/futebol/brasileirao-serie-a/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='classificacao__wrapper']/article"))
    )
    element_table_points = driver.find_element_by_xpath(
        "//*[@id='classificacao__wrapper']/article/section[1]/div/table[2]")

    html_content_points = element_table_points.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content_points, 'html.parser')
    table_points = soup.find(name='table')

    df_fullp = pd.read_html(str(table_points))[0].head(10)
    dfp = df_fullp[['P', 'J', 'V', 'E', 'D']]
    dfp.columns = ['partidas', 'jogos', 'vitorias', 'empates', 'derrotas']

    element_table_teams = driver.find_element_by_xpath(
        "//*[@id='classificacao__wrapper']/article/section[1]/div/table[1]")
    html_content_teams = element_table_teams.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content_teams, 'html.parser')
    table_teams = soup.find(name='table')

    df_fullt = pd.read_html(str(table_teams))[0].head(10)
    dft = df_fullt[['Classificação', 'Classificação.1']]
    dft.columns = ['Posição', 'Times']
    dft['Times'] = dft['Times'].str[:-3]
    result = pd.concat([dft, dfp], axis=1)
    print(result)
    cla_csv = dft.to_csv()

    print(cla_csv)
    f = open("C:/Users/xandy/Documents/txtFiles/tabelabr.txt", "a")
    f.writelines(cla_csv)
    f.close()
    df = pd.read_csv(
        "C:/Users/xandy/Documents/txtFiles/tabelabr.txt", sep=",", header=None, encoding='ISO-8859-1')
    df.to_excel("C:/Users/xandy/Documents/txtFiles/newF.xlsx", "sheet1")

except Exception as erro:
    print(erro)

driver.quit()
