import streamlit as st 
from datetime import date

# Configurações iniciais do Streamlit 
st.set_page_config(page_title="FALCON", layout="centered") 

# Inicializar o estado da aplicação 
if "page" not in st.session_state: 
    st.session_state.page = "login" 
# Função para navegação para trocar de página 
def navigate_to(page): 
    st.session_state.page = page 
    st.experimental_rerun()  # Força a atualização da página após a mudança 

# Conteúdo fixo na tela principal com a barra de cabeçalho personalizada 
st.markdown( 
    ''' 
    <style> 
    /* Forçar o fundo preto profundo */ 
    html, body, [data-testid="stAppViewContainer"] { 
        background-color: #000000 !important; /* Preto profundo */ 
        color: white !important; 
    } 
    /* Personalizar a barra superior */ 
    [data-testid="stHeader"] { 
        background-color: #000000 !important; /* Preto profundo */ 
        color: black !important; 
    } 
    /* Customizar o layout da página */ 
    .main-content { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: flex-start; /* Título no topo */ 
        height: 100vh; 
        padding-top: 50px; /* Espaçamento suave no topo */ 
        text-align: center; 
    } 
    </style> 
    <div class="main-content"> 
        <h1 style="font-size: 4rem; margin: 0;">FALCON</h1> 
        <p style="font-size: 1.5rem; margin: 0;">Eficiência no controle de manutenção de pneus</p> 
    </div> 
    ''', 
    unsafe_allow_html=True 
) 

# Função de navegação para trocar de página 
def navigate_to(page): 
    st.session_state.page = page 
    st.experimental_rerun() 

# Usuários fictícios com nome associado ao email 
USERS = { 
    "Vitor@falcon.com": {"senha": "1234", "nome": "Vitor"}, 
    "Matheus@falcon.com": {"senha": "1234", "nome": "Matheus"}, 
    "Leonardo@falcon.com": {"senha": "1234", "nome": "Leonardo"} 
} 

# Inicializa a página, se não houver página definida 
if "page" not in st.session_state: 
    st.session_state.page = "login" 

# Menu lateral para navegação 
with st.sidebar: 
    if st.session_state.page == "login": 
        st.header("Login")  # Cabeçalho da página de login 

        email = st.text_input("Email") 
        password = st.text_input("Password", type="password") 

        # Manter o estilo do botão, mas ajustando para o mesmo comprimento 
        st.markdown( 
            """ 
            <style> 
            /* Ajustar largura do botão para ser igual aos campos de texto */ 
            .stButton>button { 
                width: 100%;  /* Botão com largura total (igual aos campos de texto) */ 
                padding: 10px; /* Ajuste do padding para manter o alinhamento */ 
                font-size: 1rem; /* Ajuste no tamanho da fonte */ 
            } 
            </style> 
            """, 
            unsafe_allow_html=True) 

        if st.button("Sign in"): 
            # Lógica de login 
             if email in USERS and USERS[email]["senha"] == password: 
                nome_usuario = USERS[email]["nome"]  # Pega o nome do usuário 
                st.session_state.nome_usuario = nome_usuario  # Armazena o nome na sessão 

                # Após o login bem-sucedido, navega diretamente para a tela de inserção de placa 
                st.session_state.page = "insert_plate" 
                st.experimental_rerun()  # Redireciona para a tela de inserção de placa 
             else: 
                st.error("Credenciais inválidas. Tente novamente.") 

    elif st.session_state.page == "insert_plate": 
        # Exibir mensagem de boas-vindas no topo da página de inserção de placa 
        if "nome_usuario" in st.session_state: 
            st.success(f"Seja bem-vindo ao Falcon, {st.session_state.nome_usuario}!") 

# Dados dos caminhões
TRUCKS = {
    "956-VAH": {
        "modelo": "Western Star 49x", 
        "fotos": [
            "https://raw.githubusercontent.com/Vitor-coder-eng/FALCON/main/Falcon/Imagens/Western_Star_49x.png", 
            "https://raw.githubusercontent.com/Vitor-coder-eng/FALCON/main/Falcon/Imagens/49x_from_behind.png"
        ]
    },
    "GDA-357": {
        "modelo": "Western Star 4900", 
        "fotos": [
            "https://raw.githubusercontent.com/Vitor-coder-eng/FALCON/main/Falcon/Imagens/Western_Star_4900.png", 
            "https://raw.githubusercontent.com/Vitor-coder-eng/FALCON/main/Falcon/Imagens/4900_from_the_side.png"
        ]
    },
    "586-GKS": {
        "modelo": "Western Star 4700", 
        "fotos": [
            "https://raw.githubusercontent.com/Vitor-coder-eng/FALCON/main/Falcon/Imagens/Western_Star_4700.png", 
            "https://raw.githubusercontent.com/Vitor-coder-eng/FALCON/main/Falcon/Imagens/4700_on_the_other_side.png"
        ]
    }
}

# Função para navegação
def navigate_to(page):
    st.session_state.page = page

# Inicialização do estado
if "page" not in st.session_state:
    st.session_state.page = "insert_plate"
if "plate" not in st.session_state:
    st.session_state.plate = None
if "model" not in st.session_state:
    st.session_state.model = None

# Página de inserção de placa
if st.session_state.page == "insert_plate":
    with st.sidebar:
        st.header("Consultar Veículo")
        plate = st.text_input("Digite a placa do caminhão para manutenção")

        # Estilo para botão
        st.markdown(
            """
            <style>
            .stButton>button {
                width: 100%;
                padding: 10px;
                font-size: 1rem;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Buscar"):
            if plate.strip() in TRUCKS:
                st.session_state.plate = plate.strip()
                st.session_state.model = TRUCKS[plate.strip()]["modelo"]
                navigate_to("maintenance_report")
            else:
                st.error("Caminhão não encontrado. Tente novamente.")

# Página de relatório de manutenção
if st.session_state.page == "maintenance_report":
    st.markdown(
        """
        <style>
        .css-1aumxhk {display: none;}  /* Esconde o menu lateral */
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Relatório de Manutenção")
    st.header(f"Modelo do Caminhão: {st.session_state.model}")
    st.write(f"Placa: {st.session_state.plate}")

    # Exibir as imagens do caminhão (antes dos campos de texto)
if st.session_state.plate in TRUCKS and "fotos" in TRUCKS[st.session_state.plate]:
    for foto in TRUCKS[st.session_state.plate]["fotos"]:
        st.image(foto, caption=f"Caminhão {st.session_state.model}", width=600)

    # Criar campos para o relatório de manutenção
    st.text_area("Condições dos Pneus:", height=100, key="pneu")
    st.text_area("Serviços Realizados:", height=100, key="servicos")
    st.text_area("Nota Final:", height=100, key="nota")

 # Botão para salvar e ir para o relatório final
    if st.button("Salvar e Avançar"):
        # Armazenando os dados inseridos no session_state
        st.session_state.maintenance_data = {
            "pneu": st.session_state.pneu,
            "servicos": st.session_state.servicos,
            "nota": st.session_state.nota
        }
        
        # Mudar a página para o relatório final
        st.session_state.page = "final_report"  # Avança para a próxima página

# Página do relatório final (para exibir as informações armazenadas)
if st.session_state.page == "final_report":
    st.title("Resumo da Manutenção")

    # Mostrar as informações do relatório
    st.subheader("Informações do Caminhão")
    st.write(f"**Modelo:** {st.session_state.model}")
    st.write(f"**Placa:** {st.session_state.plate}")

    st.subheader("Detalhes do Relatório")
    st.write(f"**Condições dos Pneus:** {st.session_state.maintenance_data.get('pneu', '')}")
    st.write(f"**Serviços Realizados:** {st.session_state.maintenance_data.get('servicos', '')}")
    st.write(f"**Nota Final:** {st.session_state.maintenance_data.get('nota', '')}")

    # Campos adicionais no relatório final
    st.subheader("Informações Adicionais")
    date_input = st.date_input("Data", value=date.today())
    borracheiro = st.text_input("Nome do Borracheiro")

# Página de Relatório Final
if st.session_state.page == "final_report":
    # Criar três colunas de igual tamanho para os botões
    col1, col2, col3 = st.columns(3)

    # Botão "Finalizar Relatório"
    with col1:
        if st.button("   Finalizar Relatório   "):
            # Salvar as informações do relatório final
            st.session_state.maintenance_data["data"] = date_input
            st.session_state.maintenance_data["borracheiro"] = borracheiro
            st.success("Relatório finalizado. Os dados já estão disponíveis no sistema da empresa.")
            st.session_state.page = "home"  # Muda para a tela "home"

    # Botão "Voltar"
    with col2:
        if st.button("   Voltar   "):
            st.session_state.page = "maintenance_report"  # Volta para a página de manutenção

    # Botão "Home"
    with col3:
        if st.button("   Home   "):
            st.session_state.page = "home"  # Define a página inicial como "home"
            st.experimental_rerun()  # Garante que a tela seja atualizada para o topo

# Página inicial (tela preta com o título "FALCON")
if st.session_state.page == "home":
    # Página simples com fundo preto e o título "FALCON"
    st.markdown(
        """
        <style>
        .stApp { background-color: black; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; }
        </style>
        """,
        unsafe_allow_html=True,
    )
