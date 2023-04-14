import pandas as pd
import seaborn as sns


# Fonte: IBGE - https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_anual/2015/Volume_Brasil/Brasil/Brasil_ods.zip

df = pd.read_excel('Tabela 4.10 - 1-1.ods', engine='odf')

index = df.iloc[6:14, 0].str.strip().values
columns = df.iloc[4, 2:8].str.strip().values

df2 = df.iloc[6:14, 2:8]

df2.index = index
df2.columns = columns

df2 = df2.astype(float)
df2 = df2.round()

df2 = df2.reindex(index=df2.index[::-1])

ax = sns.heatmap(df2, robust = True, annot=True, fmt='.0f', cbar=False, cmap='Blues')
plt.show()
