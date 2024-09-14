import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from google.oauth2 import service_account
import gspread

def grafico_linha_RS_linha_numero(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax
    
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_1][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
            
    ax2 = ax.twinx()
    
    ax2.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
        
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_2][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax2.set_ylim(top=max(referencia[eixo_y_2]) * 2)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    ax2.legend(loc='lower left', bbox_to_anchor=(1.02, 1))
    st.pyplot(fig)
    plt.close(fig)

def grafico_linha_RS_linha_RS(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax
    
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_1][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
            
    ax2 = ax.twinx()
    
    ax2.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
        
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_2][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax2.set_ylim(top=max(referencia[eixo_y_2]) * 2)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    ax2.legend(loc='lower left', bbox_to_anchor=(1.02, 1))
    st.pyplot(fig)
    plt.close(fig)

def grafico_duas_linhas_percentual(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
    
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_1][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_2][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def grafico_tres_linhas_percentual(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, eixo_y_3, ref_3_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
    ax.plot(referencia[eixo_x], referencia[eixo_y_3], label = ref_3_label, linewidth = 0.5, color = 'black')
    
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_1][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_2][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_3][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_3][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def grafico_quatro_linhas_percentual(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, eixo_y_3, ref_3_label, eixo_y_4, ref_4_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
    ax.plot(referencia[eixo_x], referencia[eixo_y_3], label = ref_3_label, linewidth = 0.5, color = 'black')
    ax.plot(referencia[eixo_x], referencia[eixo_y_4], label = ref_4_label, linewidth = 0.5, color = 'green')
    
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_1][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_2][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_3][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_3][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_4][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_4][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def filtrar_dataframes(df1, df2, df3, df4, coluna, variavel):

    df1 = df1[df1[coluna]==variavel].reset_index(drop=True)

    df2 = df2[df2[coluna]==variavel].reset_index(drop=True)

    df3 = df3[df3[coluna]==variavel].reset_index(drop=True)

    df4 = df4[df4[coluna]==variavel].reset_index(drop=True)

    return df1, df2, df3, df4

def inserir_tm(df1, df2, df3, df4, df5):

    df1['tm'] = round(df1['valor'] / df1['unidade'], 2)

    df2['tm'] = round(df2['valor'] / df2['unidade'], 2)

    df3['tm'] = round(df3['valor'] / df3['unidade'], 2)

    df4['tm'] = round(df4['valor'] / df4['unidade'], 2)

    df5['tm'] = round(df5['valor'] / df5['unidade'], 2)

    return df1, df2, df3, df4, df5

def gerar_valor_vestidos_pp_sm(df):

    if not df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'NOIVA'), 'valor'].empty:

        valor_pp_noiva = df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'NOIVA'), 'valor'].values[0]

    else:

        valor_pp_noiva = 0

    if not df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'FESTA'), 'valor'].empty:

        valor_pp_festa = df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'FESTA'), 'valor'].values[0]

    else:

        valor_pp_festa = 0

    if not df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'NOIVA'), 'valor'].empty:

        valor_sm_noiva = df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'NOIVA'), 'valor'].values[0]

    else:

        valor_sm_noiva = 0

    if not df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'FESTA'), 'valor'].empty:

        valor_sm_festa = df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'FESTA'), 'valor'].values[0]

    else:

        valor_sm_festa = 0

    return valor_pp_noiva, valor_pp_festa, valor_sm_noiva, valor_sm_festa

def gerar_valor_vestidos_jp_sp_on(df):

    if not df.loc[(df['unidade'] == 'JP'), 'valor'].empty:

        valor_jp = df.loc[(df['unidade'] == 'JP'), 'valor'].values[0]

    else:

        valor_jp = 0

    if not df.loc[(df['unidade'] == 'SP'), 'valor'].empty:

        valor_sp = df.loc[(df['unidade'] == 'SP'), 'valor'].values[0]

    else:

        valor_sp = 0

    if not df.loc[(df['unidade'] == 'ON'), 'valor'].empty:

        valor_on = df.loc[(df['unidade'] == 'ON'), 'valor'].values[0]

    else:

        valor_on = 0

    return valor_jp, valor_sp, valor_on

def crar_colunas_valor_e_percentuais(df):

    df['valor_total'] = df['valor_sm_noiva'] + df['valor_pp_noiva'] +  df['valor_sm_festa'] + df['valor_pp_festa']
    
    df['valor_sm_total'] = df['valor_sm_noiva'] + df['valor_sm_festa']

    df['valor_pp_total'] = df['valor_pp_noiva'] + df['valor_pp_festa']

    df['%sm_noiva'] = df['valor_sm_noiva'] / df['valor_total']

    df['%sm_festa'] = df['valor_sm_festa'] / df['valor_total']

    df['%pp_noiva'] = df['valor_pp_noiva'] / df['valor_total']

    df['%pp_festa'] = df['valor_pp_festa'] / df['valor_total']

    df['%sm_total'] = df['valor_sm_total'] / df['valor_total']

    df['%pp_total'] = df['valor_pp_total'] / df['valor_total']

    return df

def plotar_graficos_vendas_qtd(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_linha_RS_linha_numero(df1, 'Ano/Mês', 'valor', 'Vendas Vestidos', 'unidade', 'Qtd.', 
                                        'Vendas Vestidos vs Qtd. Vestidos | Mensal')
        
        grafico_linha_RS_linha_numero(df2, 'trimestre', 'valor', 'Vendas Vestidos', 'unidade', 'Qtd.', 
                                        'Vendas Vestidos vs Qtd. Vestidos | Trimestral')
        
    with row1[1]:

        grafico_linha_RS_linha_numero(df3, 'Ano/Mês', 'valor', 'Vendas Vestidos', 'unidade', 'Qtd.', 
                                        'Vendas Vestidos vs Qtd. Vestidos | Mensal')
        
        grafico_linha_RS_linha_numero(df4, 'trimestre', 'valor', 'Vendas Vestidos', 'unidade', 'Qtd.', 
                                        'Vendas Vestidos vs Qtd. Vestidos | Trimestral')
        
    with row2[0]:

        grafico_linha_RS_linha_numero(df5, 'ano', 'valor', 'Vendas Vestidos', 'unidade', 'Qtd.', 
                                        'Vendas Vestidos vs Qtd. Vestidos | Anual')

def plotar_graficos_tm_qtd(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_linha_RS_linha_numero(df1, 'Ano/Mês', 'tm', 'Ticket Médio', 'unidade', 'Qtd.', 
                                        'Ticket Médio vs Qtd. Vestidos | Mensal')
        
        grafico_linha_RS_linha_numero(df2, 'trimestre', 'tm', 'Ticket Médio', 'unidade', 'Qtd.', 
                                        'Ticket Médio vs Qtd. Vestidos | Trimestral')
        
    with row1[1]:

        grafico_linha_RS_linha_numero(df3, 'Ano/Mês', 'tm', 'Ticket Médio', 'unidade', 'Qtd.', 
                                        'Ticket Médio vs Qtd. Vestidos | Mensal')
        
        grafico_linha_RS_linha_numero(df4, 'trimestre', 'tm', 'Ticket Médio', 'unidade', 'Qtd.', 
                                        'Ticket Médio vs Qtd. Vestidos | Trimestral')
        
    with row2[0]:

        grafico_linha_RS_linha_numero(df5, 'ano', 'tm', 'Ticket Médio', 'unidade', 'Qtd.', 
                                        'Ticket Médio vs Qtd. Vestidos | Anual')

def plotar_graficos_vendas_tm(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_linha_RS_linha_RS(df1, 'Ano/Mês', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                    'Vendas vs Ticket Médio Vestidos | Mensal')
        
        grafico_linha_RS_linha_RS(df2, 'trimestre', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                    'Vendas vs Ticket Médio Vestidos | Trimestral')
        
    with row1[1]:

        grafico_linha_RS_linha_RS(df3, 'Ano/Mês', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                    'Vendas vs Ticket Médio Vestidos | Mensal')
        
        grafico_linha_RS_linha_RS(df4, 'trimestre', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                    'Vendas vs Ticket Médio Vestidos | Trimestral')
        
    with row2[0]:

        grafico_linha_RS_linha_RS(df5, 'ano', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                    'Vendas vs Ticket Médio Vestidos | Anual')

def criar_df_mensal_perc_sm_perc_pp(df1):

    df_ref = df1[df1['tipo_de_produto']!='SALE'].groupby(['Ano/Mês', 'tipo_de_produto', 'noiva_festa'])\
        .agg({'valor': 'sum', 'unidade': 'count'}).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['Ano/Mês', 'valor_sm_noiva', 'valor_pp_noiva', 'valor_sm_festa', 'valor_pp_festa'])

    contador = 0

    for ano_mes in df_ref['Ano/Mês'].unique().tolist():

        df_ref_2 = df_ref[df_ref['Ano/Mês']==ano_mes].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_pp_noiva'], df_grafico_mensal_1.at[contador, 'valor_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'valor_sm_noiva'], df_grafico_mensal_1.at[contador, 'valor_sm_festa'] = gerar_valor_vestidos_pp_sm(df_ref_2)

        df_grafico_mensal_1.at[contador, 'Ano/Mês'] = ano_mes

        contador+=1

    df_grafico_mensal_1 = crar_colunas_valor_e_percentuais(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_mensal_trimestral_anual(df1, df2, df3, df4, df5):

    df_grafico_mensal_1 = df1.groupby('Ano/Mês').agg({'valor': 'sum', 'unidade': 'count'}).reset_index()

    df_grafico_mensal_2 = df2.groupby('Ano/Mês').agg({'valor': 'sum', 'unidade': 'count'}).reset_index()

    df_grafico_trimestral_1 = df3.groupby(['ano', 'trimestre']).agg({'valor': 'sum', 'unidade': 'count'})\
        .sort_values(by=['ano', 'trimestre']).reset_index()
    
    df_grafico_trimestral_2 = df4.groupby(['ano', 'trimestre']).agg({'valor': 'sum', 'unidade': 'count'})\
        .sort_values(by=['ano', 'trimestre']).reset_index()
    
    df_grafico_anual = df5.groupby('ano').agg({'valor': 'sum', 'unidade': 'count'}).reset_index()

    df_grafico_mensal_1, df_grafico_mensal_2, df_grafico_trimestral_1, df_grafico_trimestral_2, df_grafico_anual = \
        inserir_tm(df_grafico_mensal_1, df_grafico_mensal_2, df_grafico_trimestral_1, df_grafico_trimestral_2, df_grafico_anual)
    
    return df_grafico_mensal_1, df_grafico_mensal_2, df_grafico_trimestral_1, df_grafico_trimestral_2, df_grafico_anual

def criar_df_trimestral_perc_sm_perc_pp(df1):

    df_ref = df1[df1['tipo_de_produto']!='SALE'].groupby(['ano', 'trimestre', 'tipo_de_produto', 'noiva_festa'])\
        .agg({'valor': 'sum', 'unidade': 'count'}).sort_values(by=['ano', 'trimestre']).reset_index()
    
    df_grafico_trimestral_1 = pd.DataFrame(columns=['trimestre', 'valor_sm_noiva', 'valor_pp_noiva', 'valor_sm_festa', 'valor_pp_festa'])

    contador = 0

    for trimestre in df_ref['trimestre'].unique().tolist():

        df_ref_2 = df_ref[df_ref['trimestre']==trimestre].reset_index(drop=True)

        df_grafico_trimestral_1.at[contador, 'valor_pp_noiva'], df_grafico_trimestral_1.at[contador, 'valor_pp_festa'], \
            df_grafico_trimestral_1.at[contador, 'valor_sm_noiva'], df_grafico_trimestral_1.at[contador, 'valor_sm_festa'] = \
                gerar_valor_vestidos_pp_sm(df_ref_2)

        df_grafico_trimestral_1.at[contador, 'trimestre'] = trimestre

        contador+=1

    df_grafico_trimestral_1 = crar_colunas_valor_e_percentuais(df_grafico_trimestral_1)

    return df_grafico_trimestral_1

def criar_df_anual_perc_sm_perc_pp(df1):

    df_ref = df1[df1['tipo_de_produto']!='SALE'].groupby(['ano', 'tipo_de_produto', 'noiva_festa'])\
        .agg({'valor': 'sum', 'unidade': 'count'}).sort_values(by=['ano']).reset_index()
    
    df_grafico_anual = pd.DataFrame(columns=['ano', 'valor_sm_noiva', 'valor_pp_noiva', 'valor_sm_festa', 'valor_pp_festa'])

    contador = 0

    for ano in df_ref['ano'].unique().tolist():

        df_ref_2 = df_ref[df_ref['ano']==ano].reset_index(drop=True)

        df_grafico_anual.at[contador, 'valor_pp_noiva'], df_grafico_anual.at[contador, 'valor_pp_festa'], \
            df_grafico_anual.at[contador, 'valor_sm_noiva'], df_grafico_anual.at[contador, 'valor_sm_festa'] = \
                gerar_valor_vestidos_pp_sm(df_ref_2)

        df_grafico_anual.at[contador, 'ano'] = ano

        contador+=1

    df_grafico_anual = crar_colunas_valor_e_percentuais(df_grafico_anual)

    return df_grafico_anual

def plotar_graficos_perc_sm_perc_pp(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_duas_linhas_percentual(df1, 'Ano/Mês', '%sm_total', '% Sob Medida', '%pp_total', '% Pret a Porter', 
                                    '%Sob Medida vs %Pret a Porter | Mensal')
        
        grafico_quatro_linhas_percentual(df1, 'Ano/Mês', '%sm_noiva', '% Sob Medida Noiva', '%pp_noiva', '% Pret a Porter Noiva', 
                                        '%sm_festa', '% Sob Medida Festa', '%pp_festa', '% Pret a Porter Festa', 
                                        '%Sob Medida vs %Pret a Porter Detalhado | Mensal')
        
        grafico_duas_linhas_percentual(df2, 'trimestre', '%sm_total', '% Sob Medida', '%pp_total', '% Pret a Porter', 
                                    '%Sob Medida vs %Pret a Porter | Trimestral')
        
        grafico_quatro_linhas_percentual(df2, 'trimestre', '%sm_noiva', '% Sob Medida Noiva', '%pp_noiva', '% Pret a Porter Noiva', 
                                        '%sm_festa', '% Sob Medida Festa', '%pp_festa', '% Pret a Porter Festa', 
                                        '%Sob Medida vs %Pret a Porter Detalhado | Trimestral')
        
    with row1[1]:

        grafico_duas_linhas_percentual(df3, 'Ano/Mês', '%sm_total', '% Sob Medida', '%pp_total', '% Pret a Porter', 
                                    '%Sob Medida vs %Pret a Porter | Mensal')
        
        grafico_quatro_linhas_percentual(df3, 'Ano/Mês', '%sm_noiva', '% Sob Medida Noiva', '%pp_noiva', '% Pret a Porter Noiva', 
                                        '%sm_festa', '% Sob Medida Festa', '%pp_festa', '% Pret a Porter Festa', 
                                        '%Sob Medida vs %Pret a Porter Detalhado | Mensal')
        
        grafico_duas_linhas_percentual(df4, 'trimestre', '%sm_total', '% Sob Medida', '%pp_total', '% Pret a Porter', 
                                    '%Sob Medida vs %Pret a Porter | Trimestral')
        
        grafico_quatro_linhas_percentual(df4, 'trimestre', '%sm_noiva', '% Sob Medida Noiva', '%pp_noiva', '% Pret a Porter Noiva', 
                                        '%sm_festa', '% Sob Medida Festa', '%pp_festa', '% Pret a Porter Festa', 
                                        '%Sob Medida vs %Pret a Porter Detalhado | Trimestral')
        
    with row2[0]:

        grafico_duas_linhas_percentual(df5, 'ano', '%sm_total', '% Sob Medida', '%pp_total', '% Pret a Porter', 
                                    '%Sob Medida vs %Pret a Porter | Anual')
        
        grafico_quatro_linhas_percentual(df5, 'ano', '%sm_noiva', '% Sob Medida Noiva', '%pp_noiva', '% Pret a Porter Noiva', 
                                        '%sm_festa', '% Sob Medida Festa', '%pp_festa', '% Pret a Porter Festa', 
                                        '%Sob Medida vs %Pret a Porter Detalhado | Anual')

def grafico_duas_linhas_RS(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')

    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_1][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_2][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def grafico_tres_linhas_RS(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, eixo_y_3, ref_3_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
    ax.plot(referencia[eixo_x], referencia[eixo_y_3], label = ref_3_label, linewidth = 0.5, color = 'black')

    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_1][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_2][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_3][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_3][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def grafico_quatro_linhas_RS(referencia, eixo_x, eixo_y_1, ref_1_label, eixo_y_2, ref_2_label, eixo_y_3, ref_3_label, eixo_y_4, ref_4_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'red')
    ax.plot(referencia[eixo_x], referencia[eixo_y_2], label = ref_2_label, linewidth = 0.5, color = 'blue')
    ax.plot(referencia[eixo_x], referencia[eixo_y_3], label = ref_3_label, linewidth = 0.5, color = 'black')
    ax.plot(referencia[eixo_x], referencia[eixo_y_4], label = ref_4_label, linewidth = 0.5, color = 'green')

    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_1][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_2][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_2][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_3][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_3][i], texto, ha='center', va='bottom')
    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_4][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_4][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def plotar_graficos_tm(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_quatro_linhas_RS(df1, 'Ano/Mês', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                 'Vendas vs Ticket Médio Vestidos | Mensal')
        
        grafico_quatro_linhas_RS(df2, 'trimestre', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                 'Vendas vs Ticket Médio Vestidos | Trimestral')
        
    with row1[1]:

        grafico_quatro_linhas_RS(df3, 'Ano/Mês', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                 'Vendas vs Ticket Médio Vestidos | Mensal')
        
        grafico_quatro_linhas_RS(df4, 'trimestre', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                 'Vendas vs Ticket Médio Vestidos | Trimestral')
        
    with row2[0]:

        grafico_quatro_linhas_RS(df5, 'ano', 'valor', 'Vendas Vestidos', 'tm', 'Ticket Médio', 
                                 'Vendas vs Ticket Médio Vestidos | Anual')

def gerar_qtd_vestidos_pp_sm(df):

    if not df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'NOIVA'), 'unidade'].empty:

        qtd_pp_noiva = df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'NOIVA'), 'unidade'].values[0]

    else:

        qtd_pp_noiva = 0

    if not df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'FESTA'), 'unidade'].empty:

        qtd_pp_festa = df.loc[(df['tipo_de_produto'] == 'PRET A PORTER') & (df['noiva_festa'] == 'FESTA'), 'unidade'].values[0]

    else:

        qtd_pp_festa = 0

    if not df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'NOIVA'), 'unidade'].empty:

        qtd_sm_noiva = df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'NOIVA'), 'unidade'].values[0]

    else:

        qtd_sm_noiva = 0

    if not df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'FESTA'), 'unidade'].empty:

        qtd_sm_festa = df.loc[(df['tipo_de_produto'] == 'SOB MEDIDA') & (df['noiva_festa'] == 'FESTA'), 'unidade'].values[0]

    else:

        qtd_sm_festa = 0

    return qtd_pp_noiva, qtd_pp_festa, qtd_sm_noiva, qtd_sm_festa

def gerar_qtd_vestidos_jp_sp_on(df):

    if not df.loc[(df['unidade'] == 'JP'), 'tipo_de_produto'].empty:

        qtd_jp = df.loc[(df['unidade'] == 'JP'), 'tipo_de_produto'].values[0]

    else:

        qtd_jp = 0

    if not df.loc[(df['unidade'] == 'SP'), 'tipo_de_produto'].empty:

        qtd_sp = df.loc[(df['unidade'] == 'SP'), 'tipo_de_produto'].values[0]

    else:

        qtd_sp = 0

    if not df.loc[(df['unidade'] == 'ON'), 'tipo_de_produto'].empty:

        qtd_on = df.loc[(df['unidade'] == 'ON'), 'tipo_de_produto'].values[0]

    else:

        qtd_on = 0

    return qtd_jp, qtd_sp, qtd_on

def criar_colunas_tm_pp_sm(df):

    df['valor_total'] = df['valor_sm_noiva'] + df['valor_pp_noiva'] +  df['valor_sm_festa'] + df['valor_pp_festa']

    df['qtd_total'] = df['qtd_sm_noiva'] + df['qtd_pp_noiva'] +  df['qtd_sm_festa'] + df['qtd_pp_festa']
    
    df['valor_sm_total'] = df['valor_sm_noiva'] + df['valor_sm_festa']

    df['qtd_sm_total'] = df['qtd_sm_noiva'] + df['qtd_sm_festa']

    df['valor_pp_total'] = df['valor_pp_noiva'] + df['valor_pp_festa']

    df['qtd_pp_total'] = df['qtd_pp_noiva'] + df['qtd_pp_festa']

    df['tm_sm_noiva'] = np.where(df['qtd_sm_noiva'] > 0, df['valor_sm_noiva'] / df['qtd_sm_noiva'].replace(0, np.nan), 0)

    df['tm_sm_festa'] = np.where(df['qtd_sm_festa'] > 0, df['valor_sm_festa'] / df['qtd_sm_festa'].replace(0, np.nan), 0)

    df['tm_pp_noiva'] = np.where(df['qtd_pp_noiva'] > 0, df['valor_pp_noiva'] / df['qtd_pp_noiva'].replace(0, np.nan), 0)

    df['tm_pp_festa'] = np.where(df['qtd_pp_festa'] > 0, df['valor_pp_festa'] / df['qtd_pp_festa'].replace(0, np.nan), 0)

    df['tm_sm_total'] = np.where(df['qtd_sm_total'] > 0, df['valor_sm_total'] / df['qtd_sm_total'].replace(0, np.nan), 0)

    df['tm_pp_total'] = np.where(df['qtd_pp_total'] > 0, df['valor_pp_total'] / df['qtd_pp_total'].replace(0, np.nan), 0)

    return df

def criar_colunas_tm_jp_sp_on(df):

    df['tm_jp'] = np.where(df['qtd_jp'] > 0, df['valor_jp'] / df['qtd_jp'].replace(0, np.nan), 0)

    df['tm_sp'] = np.where(df['qtd_sp'] > 0, df['valor_sp'] / df['qtd_sp'].replace(0, np.nan), 0)

    df['tm_on'] = np.where(df['qtd_on'] > 0, df['valor_on'] / df['qtd_on'].replace(0, np.nan), 0)

    return df

def criar_colunas_perc_jp_sp_on(df):

    df['valor_total'] = df['valor_jp'] + df['valor_sp'] +  df['valor_on']

    df['%jp'] = round(df['valor_jp'] / df['valor_total'], 2)

    df['%sp'] = round(df['valor_sp'] / df['valor_total'], 2)

    df['%on'] = round(df['valor_on'] / df['valor_total'], 2)

    return df

def plotar_graficos_tm(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_duas_linhas_RS(df1, 'Ano/Mês', 'tm_sm_total', 'T.M. Sob Medida', 'tm_pp_total', 'T.M. Pret a Porter', 
                                    'T.M. Sob Medida vs T.M. Pret a Porter | Mensal')
        
        grafico_quatro_linhas_RS(df1, 'Ano/Mês', 'tm_sm_noiva', 'T.M. Sob Medida Noiva', 'tm_pp_noiva', 'T.M. Pret a Porter Noiva', 
                                        'tm_sm_festa', 'T.M. Sob Medida Festa', 'tm_pp_festa', 'T.M. Pret a Porter Festa', 
                                        'T.M. Sob Medida vs T.M. Pret a Porter Detalhado | Mensal')
        
        grafico_duas_linhas_RS(df2, 'trimestre', 'tm_sm_total', 'T.M. Sob Medida', 'tm_pp_total', 'T.M. Pret a Porter', 
                                    'T.M. Sob Medida vs T.M. Pret a Porter | Trimestral')
        
        grafico_quatro_linhas_RS(df2, 'trimestre', 'tm_sm_noiva', 'T.M. Sob Medida Noiva', 'tm_pp_noiva', 'T.M. Pret a Porter Noiva', 
                                        'tm_sm_festa', 'T.M. Sob Medida Festa', 'tm_pp_festa', 'T.M. Pret a Porter Festa', 
                                        'T.M. Sob Medida vs T.M. Pret a Porter Detalhado | Trimestral')
        
    with row1[1]:

        grafico_duas_linhas_RS(df3, 'Ano/Mês', 'tm_sm_total', 'T.M. Sob Medida', 'tm_pp_total', 'T.M. Pret a Porter', 
                                    'T.M. Sob Medida vs T.M. Pret a Porter | Mensal')
        
        grafico_quatro_linhas_RS(df3, 'Ano/Mês', 'tm_sm_noiva', 'T.M. Sob Medida Noiva', 'tm_pp_noiva', 'T.M. Pret a Porter Noiva', 
                                        'tm_sm_festa', 'T.M. Sob Medida Festa', 'tm_pp_festa', 'T.M. Pret a Porter Festa', 
                                        'T.M. Sob Medida vs T.M. Pret a Porter Detalhado | Mensal')
        
        grafico_duas_linhas_RS(df4, 'trimestre', 'tm_sm_total', 'T.M. Sob Medida', 'tm_pp_total', 'T.M. Pret a Porter', 
                                    'T.M. Sob Medida vs T.M. Pret a Porter | Trimestral')
        
        grafico_quatro_linhas_RS(df4, 'trimestre', 'tm_sm_noiva', 'T.M. Sob Medida Noiva', 'tm_pp_noiva', 'T.M. Pret a Porter Noiva', 
                                        'tm_sm_festa', 'T.M. Sob Medida Festa', 'tm_pp_festa', 'T.M. Pret a Porter Festa', 
                                        'T.M. Sob Medida vs T.M. Pret a Porter Detalhado | Trimestral')
        
    with row2[0]:

        grafico_duas_linhas_RS(df5, 'ano', 'tm_sm_total', 'T.M. Sob Medida', 'tm_pp_total', 'T.M. Pret a Porter', 
                                    'T.M. Sob Medida vs T.M. Pret a Porter | Anual')
        
        grafico_quatro_linhas_RS(df5, 'ano', 'tm_sm_noiva', 'T.M. Sob Medida Noiva', 'tm_pp_noiva', 'T.M. Pret a Porter Noiva', 
                                        'tm_sm_festa', 'T.M. Sob Medida Festa', 'tm_pp_festa', 'T.M. Pret a Porter Festa', 
                                        'T.M. Sob Medida vs T.M. Pret a Porter Detalhado | Anual')

def criar_df_mensal_tm(df1):

    df_ref = df1.groupby(['Ano/Mês', 'tipo_de_produto', 'noiva_festa']).agg({'valor': 'sum', 'unidade': 'count'}).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['Ano/Mês', 'valor_sm_noiva', 'valor_pp_noiva', 'valor_sm_festa', 'valor_pp_festa', 
                                                'qtd_sm_noiva', 'qtd_pp_noiva', 'qtd_sm_festa', 'qtd_pp_festa',
                                                'tm_sm_noiva', 'tm_pp_noiva', 'tm_sm_festa', 'tm_pp_festa'])

    contador = 0

    for ano_mes in df_ref['Ano/Mês'].unique().tolist():

        df_ref_2 = df_ref[df_ref['Ano/Mês']==ano_mes].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_pp_noiva'], df_grafico_mensal_1.at[contador, 'valor_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'valor_sm_noiva'], df_grafico_mensal_1.at[contador, 'valor_sm_festa'] = gerar_valor_vestidos_pp_sm(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_pp_noiva'], df_grafico_mensal_1.at[contador, 'qtd_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'qtd_sm_noiva'], df_grafico_mensal_1.at[contador, 'qtd_sm_festa'] = gerar_qtd_vestidos_pp_sm(df_ref_2)

        df_grafico_mensal_1.at[contador, 'Ano/Mês'] = ano_mes

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_pp_sm(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_trimestral_tm(df1):

    df_ref = df1.groupby(['ano', 'trimestre', 'tipo_de_produto', 'noiva_festa']).agg({'valor': 'sum', 'unidade': 'count'}).sort_values(by=['ano', 'trimestre'])\
        .reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'trimestre', 'valor_sm_noiva', 'valor_pp_noiva', 'valor_sm_festa', 'valor_pp_festa', 
                                                'qtd_sm_noiva', 'qtd_pp_noiva', 'qtd_sm_festa', 'qtd_pp_festa',
                                                'tm_sm_noiva', 'tm_pp_noiva', 'tm_sm_festa', 'tm_pp_festa'])

    contador = 0

    for trimestre in df_ref['trimestre'].unique().tolist():

        df_ref_2 = df_ref[df_ref['trimestre']==trimestre].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_pp_noiva'], df_grafico_mensal_1.at[contador, 'valor_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'valor_sm_noiva'], df_grafico_mensal_1.at[contador, 'valor_sm_festa'] = gerar_valor_vestidos_pp_sm(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_pp_noiva'], df_grafico_mensal_1.at[contador, 'qtd_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'qtd_sm_noiva'], df_grafico_mensal_1.at[contador, 'qtd_sm_festa'] = gerar_qtd_vestidos_pp_sm(df_ref_2)

        df_grafico_mensal_1.at[contador, 'trimestre'] = trimestre

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_pp_sm(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_anual_tm(df1):

    df_ref = df1.groupby(['ano', 'tipo_de_produto', 'noiva_festa']).agg({'valor': 'sum', 'unidade': 'count'}).sort_values(by=['ano'])\
        .reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'valor_sm_noiva', 'valor_pp_noiva', 'valor_sm_festa', 'valor_pp_festa', 
                                                'qtd_sm_noiva', 'qtd_pp_noiva', 'qtd_sm_festa', 'qtd_pp_festa',
                                                'tm_sm_noiva', 'tm_pp_noiva', 'tm_sm_festa', 'tm_pp_festa'])

    contador = 0

    for ano in df_ref['ano'].unique().tolist():

        df_ref_2 = df_ref[df_ref['ano']==ano].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_pp_noiva'], df_grafico_mensal_1.at[contador, 'valor_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'valor_sm_noiva'], df_grafico_mensal_1.at[contador, 'valor_sm_festa'] = gerar_valor_vestidos_pp_sm(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_pp_noiva'], df_grafico_mensal_1.at[contador, 'qtd_pp_festa'], \
            df_grafico_mensal_1.at[contador, 'qtd_sm_noiva'], df_grafico_mensal_1.at[contador, 'qtd_sm_festa'] = gerar_qtd_vestidos_pp_sm(df_ref_2)

        df_grafico_mensal_1.at[contador, 'ano'] = ano

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_pp_sm(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_mensal_jp_sp_on(df):

    df_ref = df.groupby(['Ano/Mês', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['Ano/Mês', 'valor_jp', 'valor_sp', 'valor_on', 'valor_total', '%jp', '%sp', '%on'])

    contador = 0

    for ano_mes in df_ref['Ano/Mês'].unique().tolist():

        df_ref_2 = df_ref[df_ref['Ano/Mês']==ano_mes].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], df_grafico_mensal_1.at[contador, 'valor_on'] = \
            gerar_valor_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'Ano/Mês'] = ano_mes

        contador+=1

    df_grafico_mensal_1 = criar_colunas_perc_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_trimestral_jp_sp_on(df):

    df_ref = df.groupby(['ano', 'trimestre', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).sort_values(by=['ano', 'trimestre'])\
        .reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'trimestre', 'valor_jp', 'valor_sp', 'valor_on', 'valor_total', '%jp', '%sp', '%on'])

    contador = 0

    for trimestre in df_ref['trimestre'].unique().tolist():

        df_ref_2 = df_ref[df_ref['trimestre']==trimestre].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], df_grafico_mensal_1.at[contador, 'valor_on'] = \
            gerar_valor_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'trimestre'] = trimestre

        contador+=1

    df_grafico_mensal_1 = criar_colunas_perc_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_anual_jp_sp_on(df):

    df_ref = df.groupby(['ano', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).sort_values(by=['ano'])\
        .reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'valor_jp', 'valor_sp', 'valor_on', 'valor_total', '%jp', '%sp', '%on'])

    contador = 0

    for ano in df_ref['ano'].unique().tolist():

        df_ref_2 = df_ref[df_ref['ano']==ano].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], df_grafico_mensal_1.at[contador, 'valor_on'] = \
            gerar_valor_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'ano'] = ano

        contador+=1

    df_grafico_mensal_1 = criar_colunas_perc_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def plotar_graficos_perc_jp_sp_on(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_tres_linhas_percentual(df1, 'Ano/Mês', '%jp', '% JP', '%sp', '% SP', '%on', '% ON',
                                    '%JP vs %SP vs %ON | Mensal')
        
        grafico_tres_linhas_percentual(df2, 'trimestre', '%jp', '% JP', '%sp', '% SP', '%on', '% ON',
                                    '%JP vs %SP vs %ON | Trimestral')
        
    with row1[1]:

        grafico_tres_linhas_percentual(df3, 'Ano/Mês', '%jp', '% JP', '%sp', '% SP', '%on', '% ON',
                                    '%JP vs %SP vs %ON | Mensal')
        
        grafico_tres_linhas_percentual(df4, 'trimestre', '%jp', '% JP', '%sp', '% SP', '%on', '% ON',
                                    '%JP vs %SP vs %ON | Trimestral')
        
    with row2[0]:

        grafico_tres_linhas_percentual(df5, 'ano', '%jp', '% JP', '%sp', '% SP', '%on', '% ON',
                                    '%JP vs %SP vs %ON | Anual')

def criar_df_mensal_tm_unidade(df):

    df_ref = df.groupby(['Ano/Mês', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['Ano/Mês', 'valor_jp', 'valor_sp', 'valor_on', 'qtd_jp', 'qtd_sp', 'qtd_on',
                                                'tm_jp', 'tm_sp', 'tm_on'])

    contador = 0

    for ano_mes in df_ref['Ano/Mês'].unique().tolist():

        df_ref_2 = df_ref[df_ref['Ano/Mês']==ano_mes].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], \
            df_grafico_mensal_1.at[contador, 'valor_on'] = gerar_valor_vestidos_jp_sp_on(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_jp'], df_grafico_mensal_1.at[contador, 'qtd_sp'], \
            df_grafico_mensal_1.at[contador, 'qtd_on'] = gerar_qtd_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'Ano/Mês'] = ano_mes

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_trimestral_tm_unidade(df):

    df_ref = df.groupby(['ano', 'trimestre', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).sort_values(by=['ano', 'trimestre'])\
        .reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'trimestre', 'valor_jp', 'valor_sp', 'valor_on', 'qtd_jp', 'qtd_sp', 'qtd_on',
                                                'tm_jp', 'tm_sp', 'tm_on'])

    contador = 0

    for trimestre in df_ref['trimestre'].unique().tolist():

        df_ref_2 = df_ref[df_ref['trimestre']==trimestre].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], \
            df_grafico_mensal_1.at[contador, 'valor_on'] = gerar_valor_vestidos_jp_sp_on(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_jp'], df_grafico_mensal_1.at[contador, 'qtd_sp'], \
            df_grafico_mensal_1.at[contador, 'qtd_on'] = gerar_qtd_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'trimestre'] = trimestre

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_anual_tm_unidade(df):

    df_ref = df.groupby(['ano', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).sort_values(by=['ano'])\
        .reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'valor_jp', 'valor_sp', 'valor_on', 'qtd_jp', 'qtd_sp', 'qtd_on',
                                                'tm_jp', 'tm_sp', 'tm_on'])

    contador = 0

    for ano in df_ref['ano'].unique().tolist():

        df_ref_2 = df_ref[df_ref['ano']==ano].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], \
            df_grafico_mensal_1.at[contador, 'valor_on'] = gerar_valor_vestidos_jp_sp_on(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_jp'], df_grafico_mensal_1.at[contador, 'qtd_sp'], \
            df_grafico_mensal_1.at[contador, 'qtd_on'] = gerar_qtd_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'ano'] = ano

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def plotar_graficos_tm_unidade(df1, df2, df3, df4, df5, row1, row2):

    with row1[0]:

        grafico_tres_linhas_RS(df1, 'Ano/Mês', 'tm_jp', 'T.M. JP', 'tm_sp', 'T.M. SP', 'tm_on', 'T.M. ON', 'T.M. JP vs SP vs ON | Mensal')

        grafico_tres_linhas_RS(df2, 'trimestre', 'tm_jp', 'T.M. JP', 'tm_sp', 'T.M. SP', 'tm_on', 'T.M. ON', 
                                'T.M. JP vs SP vs ON | Trimestral')
    
    with row1[1]:

        grafico_tres_linhas_RS(df3, 'Ano/Mês', 'tm_jp', 'T.M. JP', 'tm_sp', 'T.M. SP', 'tm_on', 'T.M. ON', 'T.M. JP vs SP vs ON | Mensal')

        grafico_tres_linhas_RS(df4, 'trimestre', 'tm_jp', 'T.M. JP', 'tm_sp', 'T.M. SP', 'tm_on', 'T.M. ON', 
                                'T.M. JP vs SP vs ON | Trimestral')
        
    with row2[0]:

        grafico_tres_linhas_RS(df5, 'ano', 'tm_jp', 'T.M. JP', 'tm_sp', 'T.M. SP', 'tm_on', 'T.M. ON', 'T.M. JP vs SP vs ON | Anual')

def criar_df_mensal_tm_unidade_detalhado(df):

    df_ref = df[(df['tipo_de_produto']==tipo_produto) & (df['noiva_festa']==noiva_festa)]\
        .groupby(['Ano/Mês', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['Ano/Mês', 'valor_jp', 'valor_sp', 'valor_on', 'qtd_jp', 'qtd_sp', 'qtd_on',
                                                'tm_jp', 'tm_sp', 'tm_on'])

    contador = 0

    for ano_mes in df_ref['Ano/Mês'].unique().tolist():

        df_ref_2 = df_ref[df_ref['Ano/Mês']==ano_mes].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], \
            df_grafico_mensal_1.at[contador, 'valor_on'] = gerar_valor_vestidos_jp_sp_on(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_jp'], df_grafico_mensal_1.at[contador, 'qtd_sp'], \
            df_grafico_mensal_1.at[contador, 'qtd_on'] = gerar_qtd_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'Ano/Mês'] = ano_mes

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_trimestral_tm_unidade_detalhado(df):

    df_ref = df[(df['tipo_de_produto']==tipo_produto) & (df['noiva_festa']==noiva_festa)]\
        .groupby(['ano', 'trimestre', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).sort_values(by=['ano', 'trimestre']).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'trimestre', 'valor_jp', 'valor_sp', 'valor_on', 'qtd_jp', 'qtd_sp', 'qtd_on',
                                                'tm_jp', 'tm_sp', 'tm_on'])

    contador = 0

    for trimestre in df_ref['trimestre'].unique().tolist():

        df_ref_2 = df_ref[df_ref['trimestre']==trimestre].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], \
            df_grafico_mensal_1.at[contador, 'valor_on'] = gerar_valor_vestidos_jp_sp_on(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_jp'], df_grafico_mensal_1.at[contador, 'qtd_sp'], \
            df_grafico_mensal_1.at[contador, 'qtd_on'] = gerar_qtd_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'trimestre'] = trimestre

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def criar_df_anual_tm_unidade_detalhado(df):

    df_ref = df[(df['tipo_de_produto']==tipo_produto) & (df['noiva_festa']==noiva_festa)]\
        .groupby(['ano', 'unidade']).agg({'valor': 'sum', 'tipo_de_produto': 'count'}).sort_values(by=['ano']).reset_index()

    df_grafico_mensal_1 = pd.DataFrame(columns=['ano', 'valor_jp', 'valor_sp', 'valor_on', 'qtd_jp', 'qtd_sp', 'qtd_on',
                                                'tm_jp', 'tm_sp', 'tm_on'])

    contador = 0

    for ano in df_ref['ano'].unique().tolist():

        df_ref_2 = df_ref[df_ref['ano']==ano].reset_index(drop=True)

        df_grafico_mensal_1.at[contador, 'valor_jp'], df_grafico_mensal_1.at[contador, 'valor_sp'], \
            df_grafico_mensal_1.at[contador, 'valor_on'] = gerar_valor_vestidos_jp_sp_on(df_ref_2)
        
        df_grafico_mensal_1.at[contador, 'qtd_jp'], df_grafico_mensal_1.at[contador, 'qtd_sp'], \
            df_grafico_mensal_1.at[contador, 'qtd_on'] = gerar_qtd_vestidos_jp_sp_on(df_ref_2)

        df_grafico_mensal_1.at[contador, 'ano'] = ano

        contador+=1

    df_grafico_mensal_1 = criar_colunas_tm_jp_sp_on(df_grafico_mensal_1)

    return df_grafico_mensal_1

def puxar_bd_receitas():

    nome_credencial = st.secrets["CREDENCIAL_SHEETS"]
    credentials = service_account.Credentials.from_service_account_info(nome_credencial)
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = credentials.with_scopes(scope)
    client = gspread.authorize(credentials)

    # Abrir a planilha desejada pelo seu ID
    spreadsheet = client.open_by_key('10eeoCrCFauVPcus6MCV7DWHOpzljb334EA4V-mZZ8CI')
    
    sheet = spreadsheet.worksheet('BD - Receitas')

    sheet_data = sheet.get_all_values()

    st.session_state.df_receitas = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])

    st.session_state.df_receitas = st.session_state.df_receitas[st.session_state.df_receitas['produto']=='VESTIDO']\
        .reset_index(drop=True)

    st.session_state.df_receitas['ano'] = st.session_state.df_receitas['ano'].astype(int)

    st.session_state.df_receitas['mes'] = st.session_state.df_receitas['mes'].astype(int)

    st.session_state.df_receitas['Ano/Mês'] = st.session_state.df_receitas['mes'].astype(str) + '/' + \
        st.session_state.df_receitas['ano'].astype(str).str[-2:]

st.set_page_config(layout='wide')

base_excel = 'BD - RN Atelier.xlsm'

if 'df_receitas' not in st.session_state:

    puxar_bd_receitas()

st.title('Análise de Vendas', help='É preciso preencher todos os campos: Período, Unidade, Tipo de Produto e Noiva | Festa')

st.divider()

row1 = st.columns(5)

with row1[0]:

    data_inicial = st.date_input('Data Inicial', value=None, format='DD/MM/YYYY', key='data_inicial')

    data_final = st.date_input('Data Final', value=None, format='DD/MM/YYYY', key='data_final')

    container_dados = st.container()

    atualizar_dados = container_dados.button('Carregar Dados da Planilha', use_container_width=True)

if atualizar_dados:

    puxar_bd_receitas()

st.divider()

if data_inicial and data_final:

    ano_inicial = data_inicial.year

    mes_inicial = data_inicial.month

    ano_final = data_final.year

    mes_final = data_final.month

    df_trimestre_atual = st.session_state.df_receitas.loc[(st.session_state.df_receitas['ano'] == ano_final) & 
                                                          (st.session_state.df_receitas['mes'] == mes_final), ['trimestre']]

    trimestre_atual = df_trimestre_atual['trimestre'].iloc[0]

    tri_atual = trimestre_atual[:2]

    df_receitas_filtro = st.session_state.df_receitas[((st.session_state.df_receitas['ano']>=ano_inicial) & 
                                                       (st.session_state.df_receitas['mes']>=mes_inicial)) & 
                                                      ((st.session_state.df_receitas['ano']<=ano_final) & 
                                                       (st.session_state.df_receitas['mes']<=mes_final))].reset_index(drop=True)
    
    df_receitas_mesmo_mes = st.session_state.df_receitas[st.session_state.df_receitas['mes']==mes_final].reset_index(drop=True)

    df_receitas_trimestral = st.session_state.df_receitas[st.session_state.df_receitas['ano']<=ano_final].reset_index(drop=True)

    df_receitas_mesmo_trimestre = st.session_state.df_receitas[(st.session_state.df_receitas['ano']<=ano_final) & 
                                                               (st.session_state.df_receitas['tri']==tri_atual)].reset_index(drop=True)

    df_trimestre_atual

    trimestre_atual

    tri_atual
    df_receitas_filtro
    df_receitas_mesmo_mes
    df_receitas_trimestral
    df_receitas_mesmo_trimestre
    
    
lista_unidade = ['TODAS']

lista_unidade.extend(st.session_state.df_receitas.unidade.unique().tolist())

with row1[1]:

    unidade = st.radio('Unidade', lista_unidade, index=None)

if unidade and data_inicial and data_final:

    if unidade!='TODAS':

        df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre = \
            filtrar_dataframes(df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre, 
                               'unidade', unidade)

lista_tipo_produtos = ['TODOS']

lista_tipo_produtos.extend(st.session_state.df_receitas.tipo_de_produto.unique().tolist())

with row1[2]:

    tipo_produto = st.radio('Tipo de Produto', lista_tipo_produtos, index=None)

if tipo_produto and data_inicial and data_final:

    if tipo_produto!='TODOS':

        df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre = \
            filtrar_dataframes(df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre, 'tipo_de_produto', tipo_produto)

lista_noiva_festa = ['TODOS']

lista_noiva_festa.extend(st.session_state.df_receitas['noiva_festa'].unique().tolist())

with row1[3]:

    noiva_festa = st.radio('Noiva | Festa', lista_noiva_festa, index=None)

if noiva_festa and data_inicial and data_final:

    if noiva_festa!='TODOS':

        df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre = \
            filtrar_dataframes(df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre, 'noiva_festa', noiva_festa)

if data_inicial and data_final and unidade and tipo_produto and noiva_festa:
                        
    # if tipo_produto=='TODOS' and noiva_festa=='TODOS':

    #     if unidade!='TODAS':

    #         lista_analises = ['Vendas vs Qtd.', 'Ticket Médio vs Qtd.', 'Vendas vs Ticket Médio', '%Sob Medida vs %Pret a Porter', 
    #                           'Ticket Médio vs Tipo de Produto']

    #         with row1[4]:

    #             analise = st.radio('Análises Gráficas', lista_analises, index=None)

    #     elif unidade=='TODAS':

    #         lista_analises = ['Vendas vs Qtd.', 'Ticket Médio vs Qtd.', 'Vendas vs Ticket Médio', '%Sob Medida vs %Pret a Porter', 
    #                           'Ticket Médio vs Tipo de Produto', 'Ticket Médio vs Unidade', '%SP vs %JP vs %ON']

    #         with row1[4]:

    #             analise = st.radio('Análises Gráficas', lista_analises, index=None)

    # elif unidade=='TODAS' and tipo_produto!='TODOS' and noiva_festa!='TODOS':

    #     lista_analises = ['Vendas vs Qtd.', 'Ticket Médio vs Qtd.', 'Vendas vs Ticket Médio', 'Ticket Médio vs Unidade']

    #     with row1[4]:

    #         analise = st.radio('Análises Gráficas', lista_analises, index=None)

    # else:

    #     lista_analises = ['Vendas vs Qtd.', 'Ticket Médio vs Qtd.', 'Vendas vs Ticket Médio']

    #     with row1[4]:

    #         analise = st.radio('Análises Gráficas', lista_analises, index=None)

    lista_analises = ['Vendas vs Qtd.', 'Ticket Médio vs Qtd.', 'Vendas vs Ticket Médio', '%Sob Medida vs %Pret a Porter', 
                        'Ticket Médio vs Tipo de Produto', 'Ticket Médio vs Unidade', '%SP vs %JP vs %ON']

    with row1[4]:

        analise = st.radio('Análises Gráficas', lista_analises, index=None)

    row2 = st.columns(2)

    row3 = st.columns(1)

    if analise=='Vendas vs Qtd.' or analise=='Ticket Médio vs Qtd.' or analise=='Vendas vs Ticket Médio':

        df_grafico_mensal_1, df_grafico_mensal_2, df_grafico_trimestral_1, df_grafico_trimestral_2, df_grafico_anual = \
            criar_df_mensal_trimestral_anual(df_receitas_filtro, df_receitas_mesmo_mes, df_receitas_trimestral, df_receitas_mesmo_trimestre, 
                                             st.session_state.df_receitas)

    elif analise=='%Sob Medida vs %Pret a Porter' and tipo_produto=='TODOS' and noiva_festa=='TODOS':

        df_grafico_mensal_1 = criar_df_mensal_perc_sm_perc_pp(df_receitas_filtro)

        df_grafico_mensal_2 = criar_df_mensal_perc_sm_perc_pp(df_receitas_mesmo_mes)

        df_grafico_trimestral_1 = criar_df_trimestral_perc_sm_perc_pp(df_receitas_trimestral)

        df_grafico_trimestral_2 = criar_df_trimestral_perc_sm_perc_pp(df_receitas_mesmo_trimestre)

        df_grafico_anual = criar_df_anual_perc_sm_perc_pp(st.session_state.df_receitas)

    elif analise=='Ticket Médio vs Tipo de Produto' and tipo_produto=='TODOS' and noiva_festa=='TODOS':

        df_grafico_mensal_1 = criar_df_mensal_tm(df_receitas_filtro)

        df_grafico_mensal_2 = criar_df_mensal_tm(df_receitas_mesmo_mes)

        df_grafico_trimestral_1 = criar_df_trimestral_tm(df_receitas_trimestral)

        df_grafico_trimestral_2 = criar_df_trimestral_tm(df_receitas_mesmo_trimestre)

        df_grafico_anual = criar_df_anual_tm(st.session_state.df_receitas)

    elif (analise=='%Sob Medida vs %Pret a Porter' or analise=='Ticket Médio vs Tipo de Produto') and \
        (tipo_produto!='TODOS' or noiva_festa!='TODOS'):

        st.warning("Para visualizar a análise solicitada, 'Tipo de Produto' e 'Noiva | Festa' precisam ser 'TODOS'")

        st.stop()

    elif analise=='%SP vs %JP vs %ON' and tipo_produto=='TODOS' and noiva_festa=='TODOS' and unidade=='TODAS':

        df_grafico_mensal_1 = criar_df_mensal_jp_sp_on(df_receitas_filtro)

        df_grafico_mensal_2 = criar_df_mensal_jp_sp_on(df_receitas_mesmo_mes)

        df_grafico_trimestral_1 = criar_df_trimestral_jp_sp_on(df_receitas_trimestral)

        df_grafico_trimestral_2 = criar_df_trimestral_jp_sp_on(df_receitas_mesmo_trimestre)

        df_grafico_anual = criar_df_anual_jp_sp_on(st.session_state.df_receitas)

    elif analise=='%SP vs %JP vs %ON' and (tipo_produto!='TODOS' or noiva_festa!='TODOS' or unidade!='TODAS'):

        st.warning("Para visualizar a análise solicitada, 'Tipo de Produto', 'Noiva | Festa' e 'Unidade' precisam ser 'TODOS'")

        st.stop()

    elif analise=='Ticket Médio vs Unidade' and tipo_produto=='TODOS' and noiva_festa=='TODOS' and unidade=='TODAS':    

        df_grafico_mensal_1 = criar_df_mensal_tm_unidade(df_receitas_filtro)

        df_grafico_mensal_2 = criar_df_mensal_tm_unidade(df_receitas_mesmo_mes)

        df_grafico_trimestral_1 = criar_df_trimestral_tm_unidade(df_receitas_trimestral)

        df_grafico_trimestral_2 = criar_df_trimestral_tm_unidade(df_receitas_mesmo_trimestre)

        df_grafico_anual = criar_df_anual_tm_unidade(st.session_state.df_receitas)

    elif analise=='Ticket Médio vs Unidade' and tipo_produto!='TODOS' and noiva_festa!='TODOS' and unidade=='TODAS':
        
        df_grafico_mensal_1 = criar_df_mensal_tm_unidade_detalhado(df_receitas_filtro)

        df_grafico_mensal_2 = criar_df_mensal_tm_unidade_detalhado(df_receitas_mesmo_mes)

        df_grafico_trimestral_1 = criar_df_trimestral_tm_unidade_detalhado(df_receitas_trimestral)

        df_grafico_trimestral_2 = criar_df_trimestral_tm_unidade_detalhado(df_receitas_mesmo_trimestre)

        df_grafico_anual = criar_df_anual_tm_unidade_detalhado(st.session_state.df_receitas)

    elif analise=='Ticket Médio vs Unidade' and unidade!='TODAS':

        st.warning("Para visualizar a análise solicitada, 'Unidade' precisa ser 'TODAS'")

        st.stop()

    elif analise=='Ticket Médio vs Unidade' and ((tipo_produto!='TODOS' and noiva_festa=='TODOS') or 
                                                 (tipo_produto=='TODOS' and noiva_festa!='TODOS')):

        st.warning("Para visualizar a análise solicitada, 'Unidade' precisa ser 'TODAS' e: 'Tipo de Produto' e 'Noiva | Festa' igual a 'TODOS' ou 'Tipo de Produto' e 'Noiva | Festa' diferente de 'TODOS'")

        st.stop()

    if analise=='Vendas vs Qtd.':

        plotar_graficos_vendas_qtd(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)
            
    elif analise=='Ticket Médio vs Qtd.':

        plotar_graficos_tm_qtd(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)
            
    elif analise=='Vendas vs Ticket Médio':

        plotar_graficos_vendas_tm(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)
            
    elif analise=='%Sob Medida vs %Pret a Porter':

        plotar_graficos_perc_sm_perc_pp(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)

    elif analise=='Ticket Médio vs Tipo de Produto':

        plotar_graficos_tm(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)
        
    elif analise=='%SP vs %JP vs %ON':
        
        plotar_graficos_perc_jp_sp_on(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)

    elif analise=='Ticket Médio vs Unidade':

        plotar_graficos_tm_unidade(df_grafico_mensal_1, df_grafico_trimestral_1, df_grafico_mensal_2, df_grafico_trimestral_2, df_grafico_anual, row2, row3)


