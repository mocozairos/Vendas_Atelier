import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from google.oauth2 import service_account
import gspread

def grafico_linha_RS(referencia, eixo_x, eixo_y_1, ref_1_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'black')

    for i in range(len(referencia[eixo_x])):
        texto = 'R$' + str(int(referencia[eixo_y_1][i]))
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')

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

def grafico_linha_percentual(referencia, eixo_x, eixo_y_1, ref_1_label, titulo):
    
    fig, ax = plt.subplots(figsize=(15, 8))
    
    plt.plot(referencia[eixo_x], referencia[eixo_y_1], label = ref_1_label, linewidth = 0.5, color = 'black')
    
    for i in range(len(referencia[eixo_x])):
        texto = str(int(referencia[eixo_y_1][i] * 100)) + "%"
        plt.text(referencia[eixo_x][i], referencia[eixo_y_1][i], texto, ha='center', va='bottom')

    plt.title(titulo, fontsize=30)
    plt.xlabel('Ano/Mês')
    ax.legend(loc='lower right', bbox_to_anchor=(1.2, 1))
    st.pyplot(fig)
    plt.close(fig)

def puxar_bds():

    nome_credencial = st.secrets["CREDENCIAL_SHEETS"]
    credentials = service_account.Credentials.from_service_account_info(nome_credencial)
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = credentials.with_scopes(scope)
    client = gspread.authorize(credentials)

    # Abrir a planilha desejada pelo seu ID
    spreadsheet = client.open_by_key('1P9g1KZKJ2h2SbWliHB1FEzf1KmST7Q-EKr3TLICVJK8')

    lista_abas = ['BD - Despesas', 'BD - DRE', 'BD - DRE Trimestral', 'BD - DRE Anual', 
                  'BD - Metas', 'BD - Metas Trimestral', 'BD - Metas Anual']

    lista_dfs = ['df_despesas_mensal', 'df_dre_mensal', 'df_dre_trimestral', 'df_dre_anual', 'df_metas_mensal', 'df_metas_trimestral', 
                 'df_metas_anual']

    for index in range(len(lista_abas)):
    
        sheet = spreadsheet.worksheet(lista_abas[index])
    
        sheet_data = sheet.get_all_values()
    
        st.session_state[lista_dfs[index]] = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])

if 'df_dre_mensal' not in st.session_state:

    puxar_bds()
    
st.title('DRE')

st.divider()

row1 = st.columns(2)

with row1[0]:

    data_inicial = st.date_input('Data Inicial', value=None ,format='DD/MM/YYYY', key='data_inicial')

    data_final = st.date_input('Data Final', value=None ,format='DD/MM/YYYY', key='data_final')

    container_dados = st.container()

    atualizar_dados = container_dados.button('Carregar Dados da Planilha', use_container_width=True)

if atualizar_dados:

    puxar_bds()

with row1[1]:

    container_analise = st.container(height=200)

    analise = container_analise.radio('Análise', ['Vendas Gerais', 'Margens | Bruta vs Operacional vs Líquida', 'Despesas Gerais', 'Margem Bruta', 'CPV',
                                                  'Margem Operacional', 'Folha', 'Despesas Operacionais', 'Margem Líquida', 'Despesas Financeiras', 
                                                  'Impostos'], index=None)

if data_inicial and data_final:

    ano_inicial = data_inicial.year

    mes_inicial = data_inicial.month

    ano_final = data_final.year

    mes_final = data_final.month

    df_trimestre_atual = st.session_state.df_dre_mensal.loc[(st.session_state.df_dre_mensal['ano'] == ano_final) & 
                                                            (st.session_state.df_dre_mensal['mes'] == mes_final), ['trimestre']]

    trimestre_atual = df_trimestre_atual['trimestre'].iloc[0]

    tri_atual = trimestre_atual[:2]

    df_dre_mensal = st.session_state.df_dre_mensal[((st.session_state.df_dre_mensal['ano']>=ano_inicial) & 
                                                    (st.session_state.df_dre_mensal['mes']>=mes_inicial)) & 
                                                    ((st.session_state.df_dre_mensal['ano']<=ano_final) & 
                                                     (st.session_state.df_dre_mensal['mes']<=mes_final))].reset_index(drop=True)
    
    df_dre_mesmo_mes = st.session_state.df_dre_mensal[st.session_state.df_dre_mensal['mes']==mes_final].reset_index(drop=True)

    df_dre_trimestral = st.session_state.df_dre_trimestral[st.session_state.df_dre_trimestral['ano']<=ano_final].reset_index(drop=True)

    df_dre_mesmo_trimestre = st.session_state.df_dre_trimestral[(st.session_state.df_dre_trimestral['ano']<=ano_final) & 
                                                                (st.session_state.df_dre_trimestral['tri']==tri_atual)].reset_index(drop=True)

    st.divider()

    row2 = st.columns(2)

    row3 = st.columns(1)

    if analise=='Vendas Gerais':

        with row2[0]:

            grafico_linha_RS(df_dre_mensal, 'Ano/Mês', 'vendas', 'Vendas', 'Vendas Gerais | Mensal')

            grafico_linha_RS(df_dre_trimestral, 'trimestre', 'vendas', 'Vendas', 'Vendas Gerais | Trimestral')

        with row2[1]:

            grafico_linha_RS(df_dre_mesmo_mes, 'Ano/Mês', 'vendas', 'Vendas', 'Vendas Gerais | Mensal')

            grafico_linha_RS(df_dre_mesmo_trimestre, 'trimestre', 'vendas', 'Vendas', 'Vendas Gerais | Trimestral')

        with row3[0]:

            grafico_linha_RS(st.session_state.df_dre_anual, 'ano', 'vendas', 'Vendas', 'Vendas Gerais | Anual')

    elif analise=='Margens | Bruta vs Operacional vs Líquida':

        with row2[0]:

            grafico_tres_linhas_percentual(df_dre_mensal, 'Ano/Mês', 'margem_bruta', 'Margem Bruta', 'margem_operacional', 'Margem Operacional', 
                                        'margem_liquida', 'Margem Líquida', 'Margens | Mensal')

            grafico_tres_linhas_percentual(df_dre_trimestral, 'trimestre', 'margem_bruta', 'Margem Bruta', 'margem_operacional', 'Margem Operacional', 
                                        'margem_liquida', 'Margem Líquida', 'Margens | Trimestral')

        with row2[1]:

            grafico_tres_linhas_percentual(df_dre_mesmo_mes, 'Ano/Mês', 'margem_bruta', 'Margem Bruta', 'margem_operacional', 'Margem Operacional', 
                                        'margem_liquida', 'Margem Líquida', 'Margens | Mensal')

            grafico_tres_linhas_percentual(df_dre_mesmo_trimestre, 'trimestre', 'margem_bruta', 'Margem Bruta', 'margem_operacional', 'Margem Operacional', 
                                        'margem_liquida', 'Margem Líquida', 'Margens | Trimestral')

        with row3[0]:

            grafico_tres_linhas_percentual(st.session_state.df_dre_anual, 'ano', 'margem_bruta', 'Margem Bruta', 'margem_operacional', 'Margem Operacional', 
                                        'margem_liquida', 'Margem Líquida', 'Margens | Anual')
            
    elif analise=='Despesas Gerais':

        with row2[0]:

            grafico_quatro_linhas_RS(df_dre_mensal, 'Ano/Mês', 'cpv', 'CPV', 'despesas_operacionais', 'Despesas Operacionais', 
                                        'despesas_financeiras', 'Despesas Financeiras', 'impostos', 'Impostos', 'Despesas Gerais | Mensal')

            grafico_quatro_linhas_RS(df_dre_trimestral, 'trimestre', 'cpv', 'CPV', 'despesas_operacionais', 'Despesas Operacionais', 
                                        'despesas_financeiras', 'Despesas Financeiras', 'impostos', 'Impostos', 'Despesas Gerais | Trimestral')

        with row2[1]:

            grafico_quatro_linhas_RS(df_dre_mesmo_mes, 'Ano/Mês', 'cpv', 'CPV', 'despesas_operacionais', 'Despesas Operacionais', 
                                        'despesas_financeiras', 'Despesas Financeiras', 'impostos', 'Impostos', 'Despesas Gerais | Mensal')

            grafico_quatro_linhas_RS(df_dre_mesmo_trimestre, 'trimestre', 'cpv', 'CPV', 'despesas_operacionais', 'Despesas Operacionais', 
                                        'despesas_financeiras', 'Despesas Financeiras', 'impostos', 'Impostos', 'Despesas Gerais | Trimestral')

        with row3[0]:

            grafico_quatro_linhas_RS(st.session_state.df_dre_anual, 'ano', 'cpv', 'CPV', 'despesas_operacionais', 'Despesas Operacionais', 
                                        'despesas_financeiras', 'Despesas Financeiras', 'impostos', 'Impostos', 'Despesas Gerais | Anual')
            
    elif analise=='Margem Bruta':

        with row2[0]:

            grafico_duas_linhas_percentual(df_dre_mensal, 'Ano/Mês', 'margem_bruta', 'Margem Bruta', 'meta_margem_bruta', 'Meta Margem Bruta', 
                                        'Margem Bruta | Mensal')

            grafico_duas_linhas_percentual(df_dre_trimestral, 'trimestre', 'margem_bruta', 'Margem Bruta', 'meta_margem_bruta', 'Meta Margem Bruta', 
                                        'Margem Bruta | Trimestral')

        with row2[1]:

            grafico_duas_linhas_percentual(df_dre_mesmo_mes, 'Ano/Mês', 'margem_bruta', 'Margem Bruta', 'meta_margem_bruta', 'Meta Margem Bruta', 
                                        'Margem Bruta | Mensal')

            grafico_duas_linhas_percentual(df_dre_mesmo_trimestre, 'trimestre', 'margem_bruta', 'Margem Bruta', 'meta_margem_bruta', 'Meta Margem Bruta', 
                                        'Margem Bruta | Trimestral')

        with row3[0]:

            grafico_duas_linhas_percentual(st.session_state.df_dre_anual, 'ano', 'margem_bruta', 'Margem Bruta', 'meta_margem_bruta', 'Meta Margem Bruta', 
                                        'Margem Bruta | Anual')
            
    elif analise=='Margem Operacional':

        with row2[0]:

            grafico_duas_linhas_percentual(df_dre_mensal, 'Ano/Mês', 'margem_operacional', 'Margem Operacional', 'meta_margem_operacional', 'Meta Margem Operacional', 
                                        'Margem Operacional | Mensal')

            grafico_duas_linhas_percentual(df_dre_trimestral, 'trimestre', 'margem_operacional', 'Margem Operacional', 'meta_margem_operacional', 
                                        'Meta Margem Operacional', 'Margem Operacional | Trimestral')

        with row2[1]:

            grafico_duas_linhas_percentual(df_dre_mesmo_mes, 'Ano/Mês', 'margem_operacional', 'Margem Operacional', 'meta_margem_operacional', 
                                        'Meta Margem Operacional', 'Margem Operacional | Mensal')

            grafico_duas_linhas_percentual(df_dre_mesmo_trimestre, 'trimestre', 'margem_operacional', 'Margem Operacional', 'meta_margem_operacional', 
                                        'Meta Margem Operacional', 'Margem Operacional | Trimestral')

        with row3[0]:

            grafico_duas_linhas_percentual(st.session_state.df_dre_anual, 'ano', 'margem_operacional', 'Margem Operacional', 'meta_margem_operacional', 
                                        'Meta Margem Operacional', 'Margem Operacional | Anual')
            
    elif analise=='Margem Líquida':

        with row2[0]:

            grafico_duas_linhas_percentual(df_dre_mensal, 'Ano/Mês', 'margem_liquida', 'Margem Líquida', 'meta_margem_liquida', 'Meta Margem Líquida', 
                                        'Margem Líquida | Mensal')

            grafico_duas_linhas_percentual(df_dre_trimestral, 'trimestre', 'margem_liquida', 'Margem Líquida', 'meta_margem_liquida', 'Meta Margem Líquida', 
                                        'Margem Líquida | Trimestral')

        with row2[1]:

            grafico_duas_linhas_percentual(df_dre_mesmo_mes, 'Ano/Mês', 'margem_liquida', 'Margem Líquida', 'meta_margem_liquida', 'Meta Margem Líquida', 
                                        'Margem Líquida | Mensal')

            grafico_duas_linhas_percentual(df_dre_mesmo_trimestre, 'trimestre', 'margem_liquida', 'Margem Líquida', 'meta_margem_liquida', 'Meta Margem Líquida', 
                                        'Margem Líquida | Trimestral')

        with row3[0]:

            grafico_duas_linhas_percentual(st.session_state.df_dre_anual, 'ano', 'margem_liquida', 'Margem Líquida', 'meta_margem_liquida', 'Meta Margem Líquida', 
                                        'Margem Líquida | Anual')

    elif analise=='CPV' or analise=='Despesas Operacionais' or analise=='Despesas Financeiras':

        if analise=='Despesas Operacionais':

            analise='OPERACIONAIS'

        elif analise=='Despesas Financeiras':

            analise='FINANCEIRAS'

        row2=st.columns(2)

        df_ref_mensal = st.session_state.df_despesas_mensal[((st.session_state.df_despesas_mensal['ano']>=ano_inicial) & 
                                                            (st.session_state.df_despesas_mensal['mes']>=mes_inicial)) & 
                                                            ((st.session_state.df_despesas_mensal['ano']<=ano_final) & 
                                                            (st.session_state.df_despesas_mensal['mes']<=mes_final)) & 
                                                            (st.session_state.df_despesas_mensal['categoria_1']==analise.upper())].reset_index(drop=True)
        
        df_ref_trimestral = st.session_state.df_despesas_mensal[st.session_state.df_despesas_mensal['ano']<=ano_final]\
            .groupby(['ano', 'trimestre', 'categoria_1', 'categoria_2', 'categoria_3']).agg({'valor_total': 'sum'})\
                .sort_values(by=['ano', 'trimestre']).reset_index()

        with row2[0]:

            container_categoria_2 = st.container(height=200)

            categoria_2 = container_categoria_2.radio(f'Categoria 1 | {analise.upper()}', sorted(df_ref_mensal['categoria_2'].unique().tolist()), index=None)

        if categoria_2:

            df_ref_mensal_2 = df_ref_mensal[df_ref_mensal['categoria_2']==categoria_2].reset_index(drop=True)

            with row2[1]:

                container_categoria_3 = st.container(height=200)

                lista_categoria_3 = ['TODAS']

                lista_categoria_3.extend(sorted(df_ref_mensal_2['categoria_3'].unique().tolist()))

                categoria_3 = container_categoria_3.radio(f'Categoria 2 | {categoria_2.upper()}', lista_categoria_3, index=None)

            if categoria_3=='TODAS':

                titulo_geral_categoria = f'{analise.upper()} {categoria_2.upper()}'

                row3 = st.columns(2)

                row4 = st.columns(1)

                df_grafico_mensal = df_ref_mensal_2.groupby(['Ano/Mês', 'categoria_2']).agg({'valor_total': 'sum'}).reset_index()

                df_grafico_trimestral = df_ref_trimestral[df_ref_trimestral['categoria_2']==categoria_2].groupby(['ano', 'trimestre', 'categoria_2'])\
                    .agg({'valor_total': 'sum'}).sort_values(by=['ano', 'trimestre']).reset_index()
                
                df_grafico_anual = st.session_state.df_despesas_mensal[st.session_state.df_despesas_mensal['categoria_2']==categoria_2]\
                    .groupby(['ano', 'categoria_2']).agg({'valor_total': 'sum'}).sort_values(by=['ano']).reset_index()
                
                if not titulo_geral_categoria in st.session_state.df_metas_mensal.columns.tolist():
                
                    with row3[0]:

                        grafico_linha_RS(df_grafico_mensal, 'Ano/Mês', 'valor_total', f'{categoria_2.upper()}', f'{categoria_2.upper()}')

                    with row3[1]:

                        grafico_linha_RS(df_grafico_trimestral, 'trimestre', 'valor_total', f'{categoria_2.upper()}', f'{categoria_2.upper()}')

                    with row4[0]:

                        grafico_linha_RS(df_grafico_anual, 'ano', 'valor_total', f'{categoria_2.upper()}', f'{categoria_2.upper()}')

                else:

                    df_grafico_mensal = pd.merge(df_grafico_mensal, st.session_state.df_metas_mensal[['Ano/Mês', titulo_geral_categoria]], on='Ano/Mês', how='left')

                    df_grafico_trimestral = pd.merge(df_grafico_trimestral, st.session_state.df_metas_trimestral[['trimestre', titulo_geral_categoria]], 
                                                    on='trimestre', how='left')
                    
                    df_grafico_anual = pd.merge(df_grafico_anual, st.session_state.df_metas_anual[['ano', titulo_geral_categoria]], 
                                                    on='ano', how='left')

                    with row3[0]:

                        grafico_duas_linhas_RS(df_grafico_mensal, 'Ano/Mês', 'valor_total', f'{categoria_2.upper()}', titulo_geral_categoria, 
                                            f'Meta {categoria_2.upper()}', f'{categoria_2.upper()} | Mensal')
                        
                    with row3[1]:

                        grafico_duas_linhas_RS(df_grafico_trimestral, 'trimestre', 'valor_total', f'{categoria_2.upper()}', titulo_geral_categoria, 
                                            f'Meta {categoria_2.upper()}', f'{categoria_2.upper()} | Trimestral')
                        
                    with row4[0]:

                        grafico_duas_linhas_RS(df_grafico_anual, 'ano', 'valor_total', f'{categoria_2.upper()}', titulo_geral_categoria, 
                                            f'Meta {categoria_2.upper()}', f'{categoria_2.upper()} | Anual')
                        
            elif categoria_3:

                titulo_geral_categoria = f'{analise.upper()} {categoria_2.upper()} {categoria_3.upper()}'

                row3 = st.columns(2)

                row4 = st.columns(1)

                df_ref_mensal_3 = df_ref_mensal_2[df_ref_mensal_2['categoria_3']==categoria_3].reset_index(drop=True)

                df_grafico_mensal = df_ref_mensal_3.groupby(['Ano/Mês', 'categoria_2', 'categoria_3']).agg({'valor_total': 'sum'}).reset_index()

                df_grafico_trimestral = df_ref_trimestral[(df_ref_trimestral['categoria_2']==categoria_2) & 
                                                        (df_ref_trimestral['categoria_3']==categoria_3)].groupby(['ano', 'trimestre', 'categoria_2', 'categoria_3'])\
                    .agg({'valor_total': 'sum'}).sort_values(by=['ano', 'trimestre']).reset_index()
                
                df_grafico_anual = st.session_state.df_despesas_mensal[(st.session_state.df_despesas_mensal['categoria_2']==categoria_2) & 
                                                                    (st.session_state.df_despesas_mensal['categoria_3']==categoria_3)]\
                    .groupby(['ano', 'categoria_2']).agg({'valor_total': 'sum'}).sort_values(by=['ano']).reset_index()

                if not titulo_geral_categoria in st.session_state.df_metas_mensal.columns.tolist():
                
                    with row3[0]:

                        grafico_linha_RS(df_grafico_mensal, 'Ano/Mês', 'valor_total', f'{categoria_3.upper()}', f'{categoria_3.upper()}')

                    with row3[1]:

                        grafico_linha_RS(df_grafico_trimestral, 'trimestre', 'valor_total', f'{categoria_3.upper()}', f'{categoria_3.upper()}')

                    with row4[0]:

                        grafico_linha_RS(df_grafico_anual, 'ano', 'valor_total', f'{categoria_3.upper()}', f'{categoria_3.upper()}')

                else:

                    df_grafico_mensal = pd.merge(df_grafico_mensal, st.session_state.df_metas_mensal[['Ano/Mês', titulo_geral_categoria]], on='Ano/Mês', how='left')

                    df_grafico_trimestral = pd.merge(df_grafico_trimestral, st.session_state.df_metas_trimestral[['trimestre', titulo_geral_categoria]], 
                                                    on='trimestre', how='left')
                    
                    df_grafico_anual = pd.merge(df_grafico_anual, st.session_state.df_metas_anual[['ano', titulo_geral_categoria]], 
                                                    on='ano', how='left')
                    
                    with row3[0]:

                        grafico_duas_linhas_RS(df_grafico_mensal, 'Ano/Mês', 'valor_total', f'{categoria_3.upper()}', titulo_geral_categoria, 
                                            f'Meta {categoria_3.upper()}', f'{categoria_3.upper()} | Mensal')
                        
                    with row3[1]:

                        grafico_duas_linhas_RS(df_grafico_trimestral, 'trimestre', 'valor_total', f'{categoria_3.upper()}', titulo_geral_categoria, 
                                            f'Meta {categoria_3.upper()}', f'{categoria_3.upper()} | Trimestral')
                        
                    with row4[0]:

                        grafico_duas_linhas_RS(df_grafico_anual, 'ano', 'valor_total', f'{categoria_3.upper()}', titulo_geral_categoria, 
                                            f'Meta {categoria_3.upper()}', f'{categoria_3.upper()} | Anual')

    elif analise=='Folha':

        with row2[0]:

            grafico_duas_linhas_percentual(df_dre_mensal, 'Ano/Mês', '%_folha', '% Folha', 'meta_%_folha', 'Meta % Folha', 
                                        '% Folha | Mensal')

            grafico_duas_linhas_percentual(df_dre_trimestral, 'trimestre', '%_folha', '% Folha', 'meta_%_folha', 'Meta % Folha', 
                                        '% Folha | Trimestral')

        with row2[1]:

            grafico_duas_linhas_percentual(df_dre_mesmo_mes, 'Ano/Mês', '%_folha', '% Folha', 'meta_%_folha', 'Meta % Folha', 
                                        '% Folha | Mensal')

            grafico_duas_linhas_percentual(df_dre_mesmo_trimestre, 'trimestre', '%_folha', '% Folha', 'meta_%_folha', 'Meta % Folha', 
                                        '% Folha | Trimestral')

        with row3[0]:

            grafico_duas_linhas_percentual(st.session_state.df_dre_anual, 'ano', '%_folha', '% Folha', 'meta_%_folha', 'Meta % Folha', 
                                        '% Folha | Anual')

    elif analise=='Impostos':

        with row2[0]:

            grafico_linha_percentual(df_dre_mensal, 'Ano/Mês', '%_impostos', '% Impostos', '% Impostos | Mensal')

            grafico_linha_percentual(df_dre_trimestral, 'trimestre', '%_impostos', '% Impostos', '% Impostos | Trimestral')

        with row2[1]:

            grafico_linha_percentual(df_dre_mesmo_mes, 'Ano/Mês', '%_impostos', '% Impostos', '% Impostos | Mensal')

            grafico_linha_percentual(df_dre_mesmo_trimestre, 'trimestre', '%_impostos', '% Impostos', '% Impostos | Trimestral')

        with row3[0]:

            grafico_linha_percentual(st.session_state.df_dre_anual, 'ano', '%_impostos', '% Impostos', '% Impostos | Anual')

