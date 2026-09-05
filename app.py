import streamlit as st

st.set_page_config(page_title="VEYRA | Shop Like a Millionaire", layout="wide", page_icon="🔷")

# ===== CUSTOM CSS - DARK NAVY THEME =====
st.markdown("""
<style>
    .stApp { background-color: #0A0F2C; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .navbar { 
        display: flex; justify-content: space-between; align-items: center;
        padding: 20px 5%; background: #0A0F2C; position: sticky; top: 0; z-index: 99;
        border-bottom: 1px solid #1E2A5E;
    }
    .logo-text { font-size: 32px; font-weight: 900; color: white; letter-spacing: 3px; }
    
    .stButton>button[kind="secondary"] { 
        background: #FFC107; color: #0A0F2C; padding: 10px 25px; border-radius: 50px; 
        font-weight: 800; border: none; font-size: 16px;
    }
    
    /* HERO SECTION WITH LOGO */
    .hero { 
        height: 85vh; 
        background: linear-gradient(rgba(10,15,44,0.85), rgba(10,15,44,0.85)), 
        url('https://images.unsplash.com/photo-1441986300917-64674bd60018?w=1400') center/cover;
        display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center;
        margin-bottom: 60px;
    }
    .hero-logo-container {
        margin-bottom: 30px;
        padding: 20px;
        background: rgba(18, 25, 53, 0.6);
        border-radius: 50%;
        border: 2px solid #FFC107;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .hero h1 { color: white; font-size: 60px; font-weight: 900; margin-bottom: 15px; letter-spacing: 2px; }
    .hero p { color: #C0C5D0; font-size: 20px; margin-bottom: 30px; }
    
    .shop-btn button { 
        background: #FFC107 !important; color: #0A0F2C !important; 
        padding: 18px 60px !important; border-radius: 50px !important; 
        font-size: 20px !important; font-weight: 800 !important; border: none !important;
    }
    .shop-btn button:hover