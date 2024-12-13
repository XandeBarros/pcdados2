# Análise da Pecuária nas Cidades do Maranhão

## Sobre o Projeto

Este projeto foi desenvolvido no âmbito da disciplina *Práticas em Ciência de Dados II*. Ele analisa dados da pecuária no estado do Maranhão, com foco na produção de leite e gado de corte, abordando aspectos como:

- Perfil de produção e distribuição geográfica.
- Relação entre a agricultura familiar e a produção agropecuária.
- Fluxos de insumos, produção e destino da produção.
- Correlações geoespaciais.

Os dados foram tratados e analisados usando métodos estatísticos e técnicas de clusterização, com o objetivo de identificar padrões e dinâmicas regionais.

## Fontes de Dados

### 1. *Censo Agropecuário 2017 (IBGE)*

- *Tabela 6911*: Estabelecimentos agropecuários com bovinos.
- *Tabela 6912*: Estabelecimentos agropecuários que produziram leite de vaca.
- Tratamento dos dados:
  - Substituição de valores "-" por 0 (ausência de dados).
  - Estimação de valores faltantes (“X”) com base em médias ponderadas.

### 2. *Regiões de Influência das Cidades (REGIC 2018)*

- Fluxos agropecuários de leite e gado de corte.
- Identificação de padrões de deslocamento e destino da produção.

### 3. *MapBiomas Brasil*

- Uso e cobertura do solo nas cidades maranhenses.
- Identificação de áreas urbanas, pastagens e biomas.

## Metodologia

### Produção de Leite

- *Análise por categoria de estabelecimentos*:
  - Tipos de produtores (pequenos, médios, grandes).
  - Distância euclidiana entre perfis de produção e agricultura familiar.
- *Clusterização*:
  - Variáveis: número de vacas, quantidade de leite produzido, valor da produção e vendas.
  - Identificação de regiões com alta produtividade e comercialização.

### Produção de Gado de Corte

- *Perfil dos estabelecimentos*:
  - Separados por tamanho de rebanho (<50 e >50 bovinos).
  - Correlação com a proporção de agricultura familiar.
- *Clusterização*:
  - Variáveis: tamanho do rebanho, valor e tipo de vendas.

### Correlações Geoespaciais

- *Índice de Moran*:
  - Mede autocorrelação espacial da produção.
  - Moran Global: Correlação positiva moderada
  - Moran Local: Identifica hotspots e coldspots.

## Principais Resultados

- *Produção de leite*:
  - Regiões com alta produtividade estão associadas à agricultura não familiar.
  - Diversidade maior em áreas com produção intermediária.
- *Produção de corte*:
  - Agricultura familiar perde relevância em rebanhos maiores.
  - Clusterização identifica concentração de rebanhos no eixo rodoviário principal.
- Fluxos e Logística
  - BR-010, BR-222 e BR-226 destacam-se como eixos logísticos.

## Ferramentas e Tecnologias

- *Linguagens*: Python (Pandas, Scikit-learn, Matplotlib).
- *Bibliotecas adicionais*: GeoPandas, PySAL (análises geoespaciais).
- *Plataformas*: Jupyter Notebook.

## Limitações

- Dados com lacunas preenchidas por estimativas.
- Foco em destinos imediatos, excluindo etapas subsequentes da cadeia produtiva.

## Contribuição

Projeto realizado por:

- `*Arthur Pompeu dos Santos Rocha*`
- `*Alexandre Barros de Araújo*`
