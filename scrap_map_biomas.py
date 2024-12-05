# scrap_map_biomas

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import os
import shutil
#  
municipios = [
    "Olho d`Água das Cunhãs", "Olinda Nova do Maranhão", "Paço do Lumiar", "Palmeirândia", 
    "Paraibano", "Parnarama", "Passagem Franca", "Pastos Bons", "Paulino Neves", "Paulo Ramos", 
    "Pedreiras", "Pedro do Rosário", "Penalva", "Peri Mirim", "Peritoró", "Pindaré-Mirim", "Pinheiro", 
    "Pio XII", "Pirapemas", "Poção de Pedras", "Porto Franco", "Porto Rico do Maranhão", 
    "Presidente Dutra", "Presidente Juscelino", "Presidente Médici", "Presidente Sarney", 
    "Presidente Vargas", "Primeira Cruz", "Raposa", "Riachão", "Ribamar Fiquene", "Rosário", "Sambaíba", 
    "Santa Filomena do Maranhão", "Santa Helena", "Santa Inês", "Santa Luzia", "Santa Luzia do Paruá", 
    "Santa Quitéria do Maranhão", "Santa Rita", "Santana do Maranhão", "Santo Amaro do Maranhão", 
    "Santo Antônio dos Lopes", "São Benedito do Rio Preto", "São Bento", "São Bernardo", 
    "São Domingos do Azeitão", "São Domingos do Maranhão", "São Félix de Balsas", "São Francisco do Brejão", 
    "São Francisco do Maranhão", "São João Batista", "São João do Carú", "São João do Paraíso", 
    "São João do Soter", "São João dos Patos", "São José de Ribamar", "São José dos Basílios", 
    "São Luís", "São Luís Gonzaga do Maranhão", "São Mateus do Maranhão", "São Pedro da Água Branca", 
    "São Pedro dos Crentes", "São Raimundo das Mangabeiras", "São Raimundo do Doca Bezerra", 
    "São Roberto", "São Vicente Ferrer", "Satubinha", "Senador Alexandre Costa", "Senador La Rocque", 
    "Serrano do Maranhão", "Sítio Novo", "Sucupira do Norte", "Sucupira do Riachão", "Tasso Fragoso", 
    "Timbiras", "Timon", "Trizidela do Vale", "Tufilândia", "Tuntum", "Turiaçu", "Turilândia", "Tutóia", 
    "Urbano Santos", "Vargem Grande", "Viana", "Vila Nova dos Martírios", "Vitória do Mearim", 
    "Vitorino Freire", "Zé Doca"
]


codigos_array = [
  '2107407', '2107456', '2107506', '2107605', '2107704', '2107803', '2107902', '2108009', 
  '2108058', '2108108', '2108207', '2108256', '2108306', '2108405', '2108454', '2108504', '2108603', 
  '2108702', '2108801', '2108900', '2109007', '2109056', '2109106', '2109205', '2109239', '2109270', 
  '2109304', '2109403', '2109452', '2109502', '2109551', '2109601', '2109700', '2109759', '2109809', 
  '2109908', '2110005', '2110039', '2110104', '2110203', '2110237', '2110278', '2110302', '2110401', 
  '2110500', '2110609', '2110658', '2110708', '2110807', '2110856', '2110906', '2111003', '2111029', 
  '2111052', '2111078', '2111102', '2111201', '2111250', '2111300', '2111409', '2111508', '2111532', 
  '2111573', '2111607', '2111631', '2111672', '2111706', '2111722', '2111748', '2111763', '2111789', 
  '2111805', '2111904', '2111953', '2112001', '2112100', '2112209', '2112233', '2112274', '2112308', 
  '2112407', '2112456', '2112506', '2112605', '2112704', '2112803', '2112852', '2112902', '2113009', 
  '2114007'
]

result = [f"{municipio} (MA) ({codigo})" for municipio, codigo in zip(municipios, codigos_array)]


def load_page(id_ibge, city):
  url = "https://plataforma.brasil.mapbiomas.org/cobertura?activeBaseMap=9&layersOpacity=100&activeModule=coverage&activeModuleContent=coverage%3Acoverage_main&activeYear=2023&mapPosition=-15.072124%2C-51.459961%2C4&timelineLimitsRange=1985%2C2023&baseParams[territoryType]=1&baseParams[territories]=10001%3BBrasil%3B1%3BPa%C3%ADs%3B0%3B0%3B0%3B0&baseParams[activeClassTreeOptionValue]=default&baseParams[activeClassTreeNodeIds]=1%2C7%2C8%2C9%2C10%2C11%2C2%2C12%2C13%2C14%2C15%2C16%2C3%2C18%2C19%2C28%2C30%2C31%2C32%2C33%2C34%2C29%2C35%2C36%2C37%2C38%2C20%2C21%2C4%2C22%2C23%2C24%2C25%2C5%2C26%2C27%2C6&baseParams[activeSubmodule]=coverage_main&baseParams[yearRange]=1985-2023"

  driver = uc.Chrome()
  driver.get(url)

  time.sleep(5)
  # /html/body/div[7]/div[3]/div/div/div/div[2]/button/span
  Button = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div/div[2]/button/span")
  Button.click()

  time.sleep(5)
  
  print("Click Município")
  Select_Area_Municipio = driver.find_element(By.CSS_SELECTOR, "input[value='País']")
  Select_Area_Municipio.click()
  Select_Area_Municipio = driver.find_element(By.XPATH, "//*[text()='Município']")
  Select_Area_Municipio.click()
  print("era pra ter clicado kkkk")


  time.sleep(5)
  Input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[2]/div[2]/div/div[1]/div[2]/div/div/div/input")
  Input.send_keys(id_ibge)
  time.sleep(5)
  # 
  Input = driver.find_element(By.XPATH, f'//*[text()="{city}"]')
  time.sleep(5)
  Input.click()

  time.sleep(5)
  Type_Area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[2]/div[2]/div/div[2]/div[1]/div/button[2]")
  Type_Area.click()

  time.sleep(5)
  View_Data = driver.find_element(By.XPATH, '//*[text()="visualizar dados"]')
  View_Data.click()

  time.sleep(5)
  Download_Data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[12]/div/div[2]/div[1]/a")
  Download_Data.click()

  time.sleep(5)
  # Definindo o diretório de download e o diretório de destino
  origem = r"C:\Users\Zilda\Downloads\MapBiomas - Tabela de Dados.csv"
  destino_pasta = r"C:\Users\Zilda\Biomas"

  # Verifique se a pasta de destino existe, se não, crie-a
  if not os.path.exists(destino_pasta):
      os.makedirs(destino_pasta)


  # Iterar pelos códigos e mover o arquivo, renomeando com o código

  novo_nome_arquivo = f"{id_ibge}.csv"
  
  # Definir o caminho completo para o novo arquivo
  destino_arquivo = os.path.join(destino_pasta, novo_nome_arquivo)
  
  # Copiar o arquivo para o novo local com o novo nome
  shutil.move(origem, destino_arquivo)
  
  print(f"Arquivo movido para {destino_arquivo}")

  driver.quit()
  
for index, codigo in enumerate(codigos_array):
  load_page(codigo, result[index])
