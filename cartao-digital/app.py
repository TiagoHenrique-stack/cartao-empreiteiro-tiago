import streamlit as st

st.set_page_config(
    page_title="João Silva - Pedreiro Profissional", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS completo com fundo e sem barra branca
st.markdown("""
<style>
/* Fundo do app - gradiente verde/azul */
.stApp {
    background: linear-gradient(135deg, #0f7a4d 0%, #1e3a8a 100%) !important;
}
.main {
    background: transparent !important;
}

/* Esconde barra branca do Streamlit */
header, #MainMenu, footer {visibility: hidden !important;}
.stApp > div {
    padding-top: 0 !important;
}

/* Card principal flutuante */
.float-card {
    background: rgba(255,255,255,0.98);
    backdrop-filter: blur(10px);
    border-radius: 18px;
    padding: 30px;
    margin-top: 35px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.12);
    max-width: 480px;
    margin-left: auto;
    margin-right: auto;
}

/* Foto circular flutuante */
.avatar-wrap {
    display: flex;
    justify-content: center;
    margin-top: -60px;
    margin-bottom: 10px;
}
.avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #fff;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

/* Textos */
.name {
    text-align: center;
    font-size: 26px;
    font-weight: 700;
    color: #1e293b;
    margin: 10px 0 5px 0;
}
.role {
    text-align: center;
    color: #64748b;
    font-size: 14px;
    margin-bottom: 25px;
}
.section-title {
    font-size: 16px;
    font-weight: 600;
    color: #1e293b;
    margin: 20px 0 10px 0;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 5px;
}
.info-line {
    font-size: 15px;
    color: #334155;
    margin: 8px 0;
}
.qr-wrap {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
.qr {
    width: 140px;
    height: 140px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Botões */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-weight: 600;
    border: none;
    transition: 0.2s;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Card flutuante
st.markdown('<div class="float-card">', unsafe_allow_html=True)

# Foto flutuante
st.markdown('<div class="avatar-wrap">', unsafe_allow_html=True)
st.image("pedreiro.jpg", use_container_width=False, width=120, output_format="JPEG")
st.markdown('</div>', unsafe_allow_html=True)

# Nome e cargo
st.markdown('<div class="name">João Silva</div>', unsafe_allow_html=True)
st.markdown('<div class="role">Pedreiro Profissional • 15 anos de experiência</div>', unsafe_allow_html=True)

# Contato
st.markdown('<div class="section-title">Contato</div>', unsafe_allow_html=True)
st.markdown('<div class="info-line">📱 WhatsApp: (11) 99999-9999</div>', unsafe_allow_html=True)
st.markdown('<div class="info-line">📞 Telefone: (11) 3333-4444</div>', unsafe_allow_html=True)
st.markdown('<div class="info-line">📧 Email: joao.silva@email.com</div>', unsafe_allow_html=True)

# Botões de ação
col1, col2 = st.columns(2)
with col1:
    if st.button("💬 WhatsApp", use_container_width=True):
        st.link_button("Abrir WhatsApp", "https://wa.me/5511999999")
with col2:
    if st.button("📞 Ligar", use_container_width=True):
        st.link_button("Ligar agora", "tel:+551133334444")

# Serviços
st.markdown('<div class="section-title">Serviços</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-line">• Construção e reforma residencial</div>
<div class="info-line">• Alvenaria e acabamento</div>
<div class="info-line">• Assentamento de pisos e azulejos</div>
<div class="info-line">• Pequenos reparos e manutenção</div>
""", unsafe_allow_html=True)

# Localização
st.markdown('<div class="section-title">Localização</div>', unsafe_allow_html=True)
st.markdown('<div class="info-line">📍 São Paulo - SP</div>', unsafe_allow_html=True)
if st.button("📍 Ver no Google Maps", use_container_width=True):
    st.link_button("Abrir mapa", "https://maps.google.com/?q=Sao+Paulo+SP")

# QR Code
st.markdown('<div class="section-title">Compartilhar</div>', unsafe_allow_html=True)
st.markdown('<div class="qr-wrap">', unsafe_allow_html=True)
st.image("qr_code.png", width=140)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-size:12px; color:#64748b; margin-top:8px;">Escaneie para salvar o contato</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
