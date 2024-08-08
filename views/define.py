import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Define")

st.write("## Análise de Viabilidade")

# Análise de Viabilidade
with st.expander("__Análise de Viabilidade__"):

    st.write("Para avaliar se um projeto é mesmo LSS, preencha a tabela abaixo de acordo com o grau de concordância.")
    st.write("Os primeiros 3 critérios são excludentes: se seu projeto não se encaixar nos três, o direcionamento deve ser revisto;")
    st.write("Os outros 4 critérios são decidisivos e deveriam ser atendidos também, mas não impedem o projeto de acontecer. São obstáculos críticos que devem ser superados.")

    tabela_analise_viabilidade = {
        "Item": ["O projeto está alinhado com a estratégia da empresa?",
                 "Está envolvido um ganho de, no mínimo, 200 a 300 mil reais?",
                 "O Champion e as lideranças apoiam o projeto?",
                 "Há probabilidade de sucesso favorável à equipe?",
                 "O time possui a senioridade necessária para executar o projeto?",
                 "Há autoridade e autonomia para a execução das melhorias?",
                 "O projeto pode ser finalizado com 4 a 8 meses de execução?"],
        "Grau de Concordância": [0, 0, 0, 0, 0, 0, 0]
    }

    df_tabela_analise_viabilidade = pd.DataFrame(tabela_analise_viabilidade)
    tabela_editada = st.data_editor(
        df_tabela_analise_viabilidade,
        column_config={
            "Grau de Concordância": st.column_config.SelectboxColumn(
                options=[1, 2, 3, 4, 5]
            )
        },
        hide_index=True,
    )

    # Acessando o valor específico da primeira linha e coluna "Nota"
    grau_concordancia_1 = tabela_editada.at[0, 'Grau de Concordância']
    grau_concordancia_2 = tabela_editada.at[1, 'Grau de Concordância']
    grau_concordancia_3 = tabela_editada.at[2, 'Grau de Concordância']
    grau_concordancia_4 = tabela_editada.at[3, 'Grau de Concordância']
    grau_concordancia_5 = tabela_editada.at[4, 'Grau de Concordância']
    grau_concordancia_6 = tabela_editada.at[5, 'Grau de Concordância']
    grau_concordancia_7 = tabela_editada.at[6, 'Grau de Concordância']

    soma_grau_concordancia = (grau_concordancia_1 + grau_concordancia_2 + grau_concordancia_3 +
                              grau_concordancia_4 + grau_concordancia_5 + grau_concordancia_6 + grau_concordancia_7)

    grau_concordancia_divisor_1 = 0
    if grau_concordancia_1 != 0:
        grau_concordancia_divisor_1 = 1

    grau_concordancia_divisor_2 = 0
    if grau_concordancia_2 != 0:
        grau_concordancia_divisor_2 = 1

    grau_concordancia_divisor_3 = 0
    if grau_concordancia_3 != 0:
        grau_concordancia_divisor_3 = 1

    grau_concordancia_divisor_4 = 0
    if grau_concordancia_4 != 0:
        grau_concordancia_divisor_4 = 1

    grau_concordancia_divisor_5 = 0
    if grau_concordancia_5 != 0:
        grau_concordancia_divisor_5 = 1

    grau_concordancia_divisor_6 = 0
    if grau_concordancia_6 != 0:
        grau_concordancia_divisor_6 = 1

    grau_concordancia_divisor_7 = 0
    if grau_concordancia_7 != 0:
        grau_concordancia_divisor_7 = 1

    soma_grau_concordancia_divisor = (grau_concordancia_divisor_1 + grau_concordancia_divisor_2 + grau_concordancia_divisor_3 +
                                      grau_concordancia_divisor_4 + grau_concordancia_divisor_5 + grau_concordancia_divisor_6 + grau_concordancia_divisor_7)

    if grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0:
        st.write("Informe os valores para realizar a análise de viabilidade.")
    elif grau_concordancia_1 < 5 or grau_concordancia_2 < 5 or grau_concordancia_3 < 5:
        st.error(
            "O projeto pouco se caracteriza como Lean Seis Sigma. O escopo deve ser revisto com o Champion antes do início.")
    elif soma_grau_concordancia/soma_grau_concordancia_divisor < 4:
        st.warning(
            "O projeto pode ser considerado Lean Seis Sigma, mas pode ser ajustado para garantir maior chance de sucesso.")
    else:
        st.success("O projeto atende plenamente aos critérios Lean Seis Sigma.")

# Project Charter
with st.expander("__Project Charter__"):
    st.write(
        "O Project Charter é o documento que lança o projeto e serve como resumo da iniciativa.")
    st.write("Além de preenchido, deve ser validado pelo Champion em sua totalidade.")
    st.write("Dentre as informações, as mais importantes são: Meta, equipe do projeto, prazos, descrição do problema e escopo.")

    st.write("#### Título do Projeto: ")

    titulo_projeto = st.text_input("_Informe o título do projeto_")

    lider_projeto = st.text_input("_Informe o lider do projeto_")

    sponsor_projeto = st.text_input("_Informe o sponsor do projeto_")

    master_black_belt_projeto = st.text_input(
        "_Informe o Master Black Belt do projeto_")

    champion_projeto = st.text_input("_Informe o championo do projeto_")

    st.write("#### Importância do Processo")

    importancia_do_processo = st.text_area(
        "Ligação com a Estratégia", help="_Objetivo estratégico e meta específica à qual o projeto está ligado._ __Exemplo:__ Objetivo: Aumentar a Receita Operacional Líquida até 2020. Meta: Aumentar 2 pontos percentuais.]")

    st.write("#### Problema do processo")

    problema_do_processo = st.text_area(
        "Descrição do problema / oportunidade:", help="_Detalhamento das análises que levaram à identificação da oportunidade._ __Exemplo:__ Nos anos de 2014, 2015 e 2016 o comportamento da margem de resultado no Néctar em percentual foram, -3,9%, -10,9% e -13,2% e em Alimento a base de soja foram 1,6%, -12,0% e -5%. Em 2016 o orçamento foi de  22.046.482 Milhões de Litros de Bebidas (sendo  12.420.720 em Néctar e 9.625.762 em ABSO) com uma meta de resultado em 0,1% (1,6% no Néctar e -2% no ABSO) , porém foi realizado um faturamento de 16.834.644 Milhões (sendo 9.997.509 em Néctar e 6.837.135 no ABSO)  de litros com um resultado líquido de -9,8% (sendo -13,2% no Néctar e -5% no ABSO)  (R$ -3.962.998), ficando o resultado 98% fora do objetivo. Para o orçamento de 2017 a meta de faturamento é de 19.912.906 litros (11.412.906 em Néctar e 8.500.000 em ABSO), tendo como meta 0,11% (-2,83% no Néctar e 4,27% no ABSO) de resultados nas bebidas, com valor aproximado de resultado sendo R$ 57.783,00. (sendo R$ - 885.935 em Néctar e R$ 943.713 no ABSO)")

    st.write("#### Detalhamento do Projeto")

    meta = st.text_area(
        "Meta:", help="_Meta específica do projeto, em indicador técnico e em dinheiro._ __Exemplo:__ Recuperar a rentabilidade de bebidas de -9,78% para -5% (R$ 5 milhões de retorno)")

    meta = st.text_area(
        "Escopo e fronteiras do processo:", help="_Definir o que é e não é escopo do projeto._ __Exemplo:__ Atuar na negociação do pedido (preço médio), no acompanhamento dos descontos concedidos e no controle da compra de insumos (polpa), mas não na industrialização do produto acabado.")

    st.write("##### Equipe do Projeto")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("Black Belts")
    with col2:
        st.text_input("Green Belts")
    with col3:
        st.text_input("Yellow Belts e Outros")
    with col4:
        st.text_input("Especialistas")

    st.write("##### Cronograma Macro")

    tabela_cronograma_macro = {
        "Etapa": ["Definir",
                  "Medir",
                  "Analisar",
                  "Implementar",
                  "Controlar",
                  "Controle e Captura"],
        "Início Previsto": ["", "", "", "", "", ""],
        "Término Previsto": ["", "", "", "", "", ""],
        "Início Real": ["", "", "", "", "", ""],
        "Término Real": ["", "", "", "", "", ""]
    }

    df_tabela_cronograma_macro = pd.DataFrame(tabela_cronograma_macro)
    tabela_editada_cronograma_macro = st.data_editor(
        df_tabela_cronograma_macro,
        hide_index=True,
        width=1375
    )

    st.write("#### Indicadores do Projeto")

    if 'values' not in st.session_state:
        st.session_state['values'] = []

    # Input de texto para adicionar valores
    new_value = st.text_input("Adicione um valor:")

    # Botão para adicionar o valor à lista
    if st.button("Adicionar Valor"):
        if new_value:
            st.session_state['values'].append(new_value)
            st.success(f"Valor '{new_value}' adicionado!")
        else:
            st.warning("Por favor, insira um valor antes de adicionar.")

    # Exibe a lista de valores adicionados
    st.write("Indicadores cadastrados:")
    if st.session_state['values']:
        for idx, value in enumerate(st.session_state['values']):
            st.write(f"__{value}__")
    else:
        st.write("Nenhum valor adicionado ainda.")

# Mapa SIPOC
with st.expander("__Mapa SIPOC__"):
    st.write(
        "O SIPOC é o mapeamento macro do processo, que garante que a equipe se ambiente ao trabalho que envolve o resultado a melhorar. É importante, por exemplo, para quando os belts do projeto não são da área de escopo.")

    col1_sipoc, col2_sipoc = st.columns(2)

    with col1_sipoc:
        st.text_input("__Início__")

    with col2_sipoc:
        st.text_input("__Fim__")

    tabela_sipoc = {
        "Fornecedores": [" ", " ", " ", " ", " ", " ",],
        "Entradas": [" ", " ", " ", " ", " ", " ",],
        "Processos": [" ", " ", " ", " ", " ", " ",],
        "Saídas": [" ", " ", " ", " ", " ", " ",],
        "Clientes": [" ", " ", " ", " ", " ", " "]
    }

    df_tabela_sipoc = pd.DataFrame(tabela_sipoc)
    tabela_editada_sipoc = st.data_editor(
        df_tabela_sipoc,
        hide_index=True,
        width=1375
    )

# VOC/VOB
with st.expander("__VOC/VOB__"):
    st.write("A voz do cliente é utilizada para capturar o que seu cliente espera de um determinado processo, ou seja, o que ele considera bom.")
    st.write("Já a VOB é o que o seu processo consegue produzir. Ambos, VOC e VOB andam sempre juntos em um programa de melhoria como o Six Sigma.")
    st.write("Entender a voz dos diferentes clientes e garantir a sua satisfação é essencial para qualquer empresa.")

    st.write("#### Controle da Qualidade Total")

    col1_vocvob, col2_vocvob, col3_vocvob = st.columns(3)

    # Inicializar listas separadas no session_state, se ainda não existirem
    if 'values_col1' not in st.session_state:
        st.session_state['values_col1'] = []

    if 'values_col2' not in st.session_state:
        st.session_state['values_col2'] = []

    if 'values_col3' not in st.session_state:
        st.session_state['values_col3'] = []

    with col1_vocvob:
        new_value_col1_vocvob = st.text_input("__Qualidade (CTQ)__")
        if st.button("Adicionar Valor para Qualidade (CTQ)"):
            if new_value_col1_vocvob:
                st.session_state['values_col1'].append(new_value_col1_vocvob)
                st.success(f"Valor '{new_value_col1_vocvob}' adicionado!")
            else:
                st.warning("Por favor, insira um valor antes de adicionar.")

        # Exibe a lista de valores adicionados
        st.write("Valores cadastrados para Qualidade (CTQ):")
        if st.session_state['values_col1']:
            for idx, value in enumerate(st.session_state['values_col1']):
                st.write(f"__{value}__")
        else:
            st.write("Nenhum valor adicionado ainda.")

    with col2_vocvob:
        new_value_col2_vocvob = st.text_input("__Custo (CTC)__")
        if st.button("Adicionar Valor para Custo (CTC)"):
            if new_value_col2_vocvob:
                st.session_state['values_col2'].append(new_value_col2_vocvob)
                st.success(f"Valor '{new_value_col2_vocvob}' adicionado!")
            else:
                st.warning("Por favor, insira um valor antes de adicionar.")

        # Exibe a lista de valores adicionados
        st.write("Valores cadastrados para Custo (CTC):")
        if st.session_state['values_col2']:
            for idx, value in enumerate(st.session_state['values_col2']):
                st.write(f"__{value}__")
        else:
            st.write("Nenhum valor adicionado ainda.")

    with col3_vocvob:

        new_value_col3_vocvob = st.text_input("__Entrega (CTD)__")
        if st.button("Adicionar Valor para Entrega (CTD)"):
            if new_value_col3_vocvob:
                st.session_state['values_col3'].append(new_value_col3_vocvob)
                st.success(f"Valor '{new_value_col3_vocvob}' adicionado!")
            else:
                st.warning("Por favor, insira um valor antes de adicionar.")

        # Exibe a lista de valores adicionados
        st.write("Valores cadastrados para Entrega (CTD):")
        if st.session_state['values_col3']:
            for idx, value in enumerate(st.session_state['values_col3']):
                st.write(f"__{value}__")
        else:
            st.write("Nenhum valor adicionado ainda.")

# Mapa de Indicadores
with st.expander("__Mapa de Indicadores__"):
    st.write("A Árvore de Indicadores é utilizada para priorizar o escopo, partindo a partir da meta e desdobrando is itens conforme faça sentido para encontrar problemas menores mas que, quando resulvidos, solucionem um problema maior.")

    imagem_mapa_indicadores = st.file_uploader(
        "Carregue sua imagem do Mapa de Indicadores")

    if imagem_mapa_indicadores:
        st.image(imagem_mapa_indicadores)

# Baseline e Meta
with st.expander("__Baseline e Meta__"):
    st.write("O ganho pode ser projetado tanto no indicador do tipo técnico quanto no próprio volume financeiro. É importante projetar o ganho do projeto para entender se o esforço trará a recompensa conforme o esperado.")

    st.write("#### Cálculo de Ganho - Indicador Técnico (Y)")

    col1_baseline_meta, col2_baseline_meta = st.columns(2)

    with col2_baseline_meta:
        st.write("__Dados__")

        # Tópicos iniciais
        topics = ["Baseline", "Benchmarking", "Lacuna", "Ganho", "Meta"]

        # Cria uma tabela inicial com valores 0
        data = pd.DataFrame({"Tópico": topics, "Valor": [0] * len(topics)})

        # Exibe a tabela e permite que o usuário edite os valores
        st.write("Preencha a tabela abaixo:")
        edited_data = st.data_editor(data, hide_index=True)

    with col1_baseline_meta:
        st.write("__Ganho Projetado__")
        # Cria um gráfico de barras responsivo aos valores da tabela
        fig = px.bar(edited_data, x="Tópico", y="Valor")
        st.plotly_chart(fig)


# Gantt
with st.expander("__Gantt__"):
    st.write("O diagrama de Gantt é um gráfico usado para ilustrar o avanço das diferentes etapas de um projeto. Os intervalos de tempo representando o início e fim de cada fase aparecem como barras coloridas sobre o eixo horizontal do gráfico.")

    # Definindo os dados da tabela
    tasks = [
        "Elaborar o Project Charter", "Definir a equipe e a dedicação", "Estabelecer a meta preliminar",
        "Validar com o Champion", "Desenhar o Mapa SIPOC", "Preencher e analisar VOC/VOB",
        "Desenhar a Árvore de Indicadores", "Priorizar os principais Ys", "Validar com o Champion",
        "Estabelecer a meta dos Ys", "Calcular meta no indicador", "Calcular ganho previsto",
        "Validar cálculos com o financeiro", "Preencher o cronograma", "Desenhar Mapa Mental",
        "Aplicar Análise GRIP: Definir", "Validar etapa com Champion", "Mapear o processo",
        "Listar Ganhos Rápidos", "Validar com o Champion", "Levantar causas (X): Ishikawa",
        "Priorizar causas: Matriz Causa-Efeito", "Analisar o Sistema de Medição", "Coletar dados do processo",
        "Calcular a Capacidade", "Desenhar Mapa Mental", "Aplicar Análise GRIP: Medir",
        "Validar etapa com Champion", "Levantar causas-raíz", "Elaborar o FMEA", "Preencher Modos de Falha, Efeitos, Causas e Controles",
        "Atribuir notas e priorizar", "Fazer 5 Porquês com as causas do FMEA", "Testar Hipóteses levantadas",
        "Testar influência dos X nos Y: Regressão", "Listar causas-raíz comprovadas", "Desenhar Mapa Futuro",
        "Listar Ganhos Rápidos", "Desenhar Mapa Mental", "Aplicar Análise GRIP: Analisar", "Validar etapa com Champion",
        "Gerar soluções: brainstorm", "Listar soluções", "Priorizar soluções", "Aplicar Análise GRIP: Implementar",
        "Validar com o Champion", "Criar o Plano de Ação", "Desenhar Mapa Mental", "Monitorar o Y e tratar desvios",
        "Remover causas especiais", "Calcular ganho real e previsto", "Padronizar o Processo",
        "Criar CEPs, OCAP, PTPs e POPs", "Treinar a operação", "Calcular a nova Capacidade",
        "Aplicar Análise GRIP: Controlar", "Validar etapa com Champion"
    ]

    # Cria um DataFrame com os dados
    df = pd.DataFrame({
        "Tarefa": tasks,
        "Etapa DMAIC": ["" for _ in tasks],
        "Responsável": ["" for _ in tasks],
        "Data início Previsto": ["" for _ in tasks],
        "Data término Previsto": ["" for _ in tasks],
        "Data início Realizado": ["" for _ in tasks],
        "Data término Realizado": ["" for _ in tasks],
        "Status": ["" for _ in tasks]
    })

    # Exibe a tabela para que o usuário possa preencher os dados
    st.write("Preencha a tabela abaixo:")
    edited_df = st.data_editor(df)

    # Cria um gráfico de Gantt com base nos dados preenchidos
    # (Assumindo que o usuário irá preencher as datas e status)
    if not edited_df["Data início Previsto"].isnull().all() and not edited_df["Data término Previsto"].isnull().all():
        fig = px.timeline(
            edited_df,
            x_start="Data início Previsto",
            x_end="Data término Previsto",
            y="Tarefa",
            color="Status",
            title="Gantt Chart"
        )
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig)
    else:
        st.write("Preencha as datas para visualizar o gráfico de Gantt.")

# Mapa Mental
with st.expander("__Mapa Mental__"):
    st.write("O Mapa Mental é utilizado para organizar as ideias e as pendências que surgem ao longo de cada etapa do projeto. Pode ser construído como a equipe quiser, desde que feito em grupo e que represente as informações de forma lógica.")

    imagem_mapa_mental = st.file_uploader(
        "Carregue sua imagem do Mapa Mental")

    if imagem_mapa_mental:
        st.image(imagem_mapa_mental)
