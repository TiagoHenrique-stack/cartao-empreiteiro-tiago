import streamlit as st
import base64
import os

st.set_page_config(layout="centered", page_title="João Silva - Pedreiro")

def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

img_base64 = get_image_base64("foto_pedreiro.jpg")
qr_base64 = get_image_base64("qr_code.png")

st.markdown("""
<style>
header, #MainMenu, footer {visibility: hidden !important;}

/* ZERA TUDO DO STREAMLIT */
.stApp {
    background: linear-gradient(135deg, #064e3b 0%, #0f766e 30%, #1f2937 100%) !important;
    min-height: 100vh !important;
    padding: 0 !important;
    margin: 0 !important;
}

.block-container {
    padding: 0 !important;
    margin: 0 auto !important;
    max-width: 440px !important;
}

.float-card {
    background: rgba(255, 255, 255, 0.96) !important;
    backdrop-filter: blur(24px) !important;
    border-radius: 40px !important;
    padding: 0 32px 36px 32px !important; /* Padding 0 no topo */
    box-shadow: 0 40px 80px rgba(0,0,0,0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.4) !important;
    position: relative !important;
    margin: 120px auto 0 auto !important; /* Espaço pra foto de 170px não cortar */
    text-align: center !important;
}

/* WRAPPER DA FOTO - NÃO USA POSITION ABSOLUTE */
.avatar-wrapper {
    position: relative !important;
    width: 100% !important;
    height: 0 !important; /* Altura 0 pra não empurrar o conteúdo */
}

.avatar-float {
    position: absolute !important;
    top: -85px !important; /* Metade da altura da foto */
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 10 !important;
}

.avatar-ring {
    padding: 8px !important;
    background: white !important;
    border-radius: 50% !important;
    display: inline-block !important;
    box-shadow: 0 25px 70px rgba(0,0,0,0.3) !important;
}

.avatar-img {
    width: 170px !important;
    height: 170px !important;
    border-radius: 50% !important;
    border: 7px solid white !important;
    object-fit: cover !important;
    display: block !important;
    margin: 0 auto !important;
}

/* CONTEÚDO COM PADDING SUPERIOR GARANTIDO */
.content-start {
    padding-top: 120px !important; /* 170px foto - 85px + 35px de respiro */
}

.name {
    text-align: center !important;
    color: #0f172a !important;
    font-weight: 800 !important;
    font-size: 36px !important;
    margin: 0 0 12px 0 !important; /* Margem 0 no topo */
    letter-spacing: -1.5px !important;
}

.tag {
    text-align: center !important;
    color: #64748b !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    margin: 0 0 40px 0 !important;
}

/* STATS SEM DIVISOR */
.stats-container {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 48px !important;
    margin: 0 0 44px 0 !important;
    padding: 0 !important;
    border: none !important;
}

.stat-box {
    text-align: center !important;
}

.stat-number { 
    font-size: 32px !important;
    font-weight: 800 !important; 
    color: #0f172a !important; 
    line-height: 1 !important; 
    margin-bottom: 8px !important;
    background: linear-gradient(135deg, #10b981, #14b8a6) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

.stat-label { 
    font-size: 12px !important;
    color: #64748b !important; 
    font-weight: 600 !important; 
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important; 
}

/* BOTÕES PREMIUM */
.btn-premium-stack {
    display: flex !important;
    flex-direction: column !important;
    gap: 14px !important;
    margin-bottom: 36px !important;
}

.btn-premium {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
    height: 64px !important;
    padding: 0 24px !important;
    border-radius: 22px !important;
    background: rgba(6, 78, 59, 0.92) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    backdrop-filter: blur(12px) !important;
    text-decoration: none !important;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer !important;
}

.btn-premium:hover {
    background: rgba(0, 0, 0, 0.95) !important;
    transform: translateY(-6px) !important;
    box-shadow: 0 25px 50px rgba(16, 185, 129, 0.45) !important;
    border-color: rgba(16, 185, 129, 0.4) !important;
}

.btn-premium-content {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
}

.btn-premium-icon {
    font-size: 22px !important;
    line-height: 1 !important;
}

.btn-premium-text {
    color: white !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px !important;
}

.btn-premium-arrow {
    color: rgba(255, 255, 255, 0.6) !important;
    font-size: 18px !important;
    transition: all 0.3s ease !important;
}

.btn-premium:hover .btn-premium-arrow {
    color: #10b981 !important;
    transform: translateX(4px) !important;
}

/* QR SECTION TRANSPARENTE */
.qr-section {
    background: transparent !important;
    border-radius: 0 !important;
    padding: 0 !important;
    border: none !important;
    backdrop-filter: none !important;
    margin-top: 8px !important;
}

.qr-label-container {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
    margin-bottom: 20px !important;
}

.qr-label-badge {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    background: rgba(255, 255, 255, 0.25) !important;
    border: 1px solid rgba(255, 255, 255, 0.35) !important;
    border-radius: 50px !important;
    padding: 10px 22px !important;
    backdrop-filter: blur(12px) !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08) !important;
}

.qr-label-icon {
    font-size: 16px !important;
    line-height: 1 !important;
}

.qr-label-text {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 12px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.25) !important;
}

.qr-wrapper {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
}

.qr-wrapper img {
    display: block !important;
    margin: 0 auto !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15) !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="float-card">', unsafe_allow_html=True)

# WRAPPER DA FOTO COM ALTURA 0
st.markdown('<div class="avatar-wrapper">', unsafe_allow_html=True)
if img_base64:
    st.markdown(f'''
    <div class="avatar-float">
        <div class="avatar-ring">
            <img src="data:image/jpeg;base64,{img_base64}" class="avatar-img">
        </div>
    </div>
    ''', unsafe_allow_html=True)
else:
    st.markdown('<div class="avatar-float"><div style="width:170px;height:170px;background:#e2e8f0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#64748b;font-size:14px;font-weight:600;">Sem foto</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# CONTEÚDO COM PADDING SUPERIOR FIXO
st.markdown('<div class="content-start">', unsafe_allow_html=True)

st.markdown('<h1 class="name">João Silva</h1>', unsafe_allow_html=True)
st.markdown('<p class="tag">Pedreiro • Construtor • Reforma</p>', unsafe_allow_html=True)

# Stats sem divisor
st.markdown('''
<div class="stats-container">
    <div class="stat-box">
        <div class="stat-number">12</div>
        <div class="stat-label">Anos</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">200+</div>
        <div class="stat-label">Obras</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">98%</div>
        <div class="stat-label">Satisfação</div>
    </div>
</div>
''', unsafe_allow_html=True)

# Botões premium
st.markdown('<div class="btn-premium-stack">', unsafe_allow_html=True)

st.markdown('''
<a href="https://wa.me/47999999?text=Olá%20João,%20vi%20seu%20cartão%20digital%20e%20quero%20um%20orçamento" target="_blank" class="btn-premium">
    <div class="btn-premium-content">
        <span class="btn-premium-icon">💬</span>
        <span class="btn-premium-text">Falar no WhatsApp</span>
    </div>
    <span class="btn-premium-arrow">→</span>
</a>
''', unsafe_allow_html=True)

st.markdown('''
<a href="https://seusite.com.br/obras" target="_blank" class="btn-premium">
    <div class="btn-premium-content">
        <span class="btn-premium-icon">🏗️</span>
        <span class="btn-premium-text">Ver Portfólio de Obras</span>
    </div>
    <span class="btn-premium-arrow">→</span>
</a>
''', unsafe_allow_html=True)

st.markdown('''
<a href="tel:47999999" target="_blank" class="btn-premium">
    <div class="btn-premium-content">
        <span class="btn-premium-icon">📞</span>
        <span class="btn-premium-text">Ligar Agora</span>
    </div>
    <span class="btn-premium-arrow">→</span>
</a>
''', unsafe_allow_html=True)

st.markdown('''
<a href="https://maps.google.com/?q=Picarras+SC" target="_blank" class="btn-premium">
    <div class="btn-premium-content">
        <span class="btn-premium-icon">📍</span>
        <span class="btn-premium-text">Como Chegar</span>
    </div>
    <span class="btn-premium-arrow">→</span>
</a>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# QR CODE TRANSPARENTE
st.markdown('<div class="qr-section">', unsafe_allow_html=True)

st.markdown('''
<div class="qr-label-container">
    <div class="qr-label-badge">
        <span class="qr-label-icon">📱</span>
        <span class="qr-label-text">Escaneie para salvar contato</span>
    </div>
</div>
''', unsafe_allow_html=True)

if qr_base64:
    st.markdown(f'''
    <div class="qr-wrapper">
        <img src="data:image/png;base64,{qr_base64}" width="140">
    </div>
    ''', unsafe_allow_html=True)
else:
    st.markdown('<div class="qr-wrapper"><div style="width:140px;height:140px;background:rgba(255,255,255,0.25);border-radius:16px;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:12px;font-weight:600;border:1px solid rgba(255,255,255,0.35);backdrop-filter:blur(12px);">QR Code</div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
