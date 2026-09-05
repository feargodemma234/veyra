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
    .st.image("https://placehold.co/200x200/121935/FFC107?text=VEYRA", width=200)
    
    .stButton>button[kind="secondary"] { 
        background: #FFC107; color: #0A0F2C; padding: 10px 25px; border-radius: 50px; 
        font-weight: 800; border: none; font-size: 16px;
    }
    
    /* HERO SECTION WITH LOGO */
    .hero { 
        height: 80vh; 
        background: linear-gradient(rgba(10,15,44,0.85), rgba(10,15,44,0.85)), 
        url('https://images.unsplash.com/photo-1441986300917-64674bd60018?w=1400') center/cover;
        display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center;
        margin-bottom: 60px;
    }
    .hero-logo {
        width: 200px;
        height: 200px;
        margin-bottom: 30px;
        border-radius: 50%;
        border: 3px solid #FFC107;
        object-fit: cover;
        background: #121935;
    }
    .hero h1 { color: white; font-size: 60px; font-weight: 900; margin-bottom: 15px; }
    .hero p { color: #C0C5D0; font-size: 20px; margin-bottom: 30px; }
    
    .shop-btn button { 
        background: #FFC107 !important; color: #0A0F2C !important; 
        padding: 18px 60px !important; border-radius: 50px !important; 
        font-size: 20px !important; font-weight: 800 !important; border: none !important;
    }
    
    .section-title { text-align: center; font-size: 42px; color: white; font-weight: 900; margin: 60px 0 40px 0; }
    .product-card { 
        background: #121935; padding: 20px; border-radius: 15px; text-align: center; 
        border: 1px solid #1E2A5E; transition: 0.3s;
    }
    .product-card:hover { transform: translateY(-10px); border: 1px solid #FFC107; }
    .price { color: #FFC107; font-size: 22px; font-weight: 700; }
    
    .add-cart button { 
        background: transparent !important; color: #FFC107 !important; 
        border: 1px solid #FFC107 !important; border-radius: 20px !important;
        width: 100%;
    }
    .add-cart button:hover { background: #FFC107 !important; color: #0A0F2C !important; }
    .footer { text-align: center; color: #777; padding: 40px; border-top: 1px solid #1E2A5E; margin-top: 60px; }
</style>
""", unsafe_allow_html=True)


# ===== SESSION STATE =====
if 'cart' not in st.session_state:
    st.session_state.cart = 0


# ===== NAVBAR =====
col1, col2 = st.columns([4,1])
with col1:
    st.markdown('<div class="logo-text">VEYRA</div>', unsafe_allow_html=True)
with col2:
    if st.button(f"Cart ({st.session_state.cart})", type="secondary"):
        st.toast("Cart feature coming soon!")


# ===== HERO SECTION WITH LOGO =====
st.markdown('<div class="hero">', unsafe_allow_html=True)

# LOGO GOES HERE - Replace the URL with your logo link
st.image("https://placehold.co/200x200/121935/FFC107?text=VEYRA", use_container_width=False, width=200)

st.markdown('<h1>Shop Like a Millionaire</h1>', unsafe_allow_html=True)
st.markdown('<p>Luxury fashion & streetwear for those who lead</p>', unsafe_allow_html=True)

st.markdown('<div class="shop-btn">', unsafe_allow_html=True)
if st.button("Shop Now"):
    st.session_state.scroll = True
st.markdown('</div></div>', unsafe_allow_html=True)


# ===== FEATURED DROPS =====
st.markdown('<h2 class="section-title">Featured Drops</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600")
    st.write("### Signature Jacket")
    st.markdown('<p class="price">₦299,000</p>', unsafe_allow_html=True)
    st.markdown('<div class="add-cart">', unsafe_allow_html=True)
    if st.button("Add to Cart", key="1"):
        st.session_state.cart += 1
        st.toast("Added to Cart!")
    st.markdown('</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600")
    st.write("### Luxury Sneakers")
    st.markdown('<p class="price">₦189,000</p>', unsafe_allow_html=True)
    st.markdown('<div class="add-cart">', unsafe_allow_html=True)
    if st.button("Add to Cart", key="2"):
        st.session_state.cart += 1
        st.toast("Added to Cart!")
    st.markdown('</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=600")
    st.write("### Gold Chrono")
    st.markdown('<p class="price">₦499,000</p>', unsafe_allow_html=True)
    st.markdown('<div class="add-cart">', unsafe_allow_html=True)
    if st.button("Add to Cart", key="3"):
        st.session_state.cart += 1
        st.toast("Added to Cart!")
    st.markdown('</div></div>', unsafe_allow_html=True)


# ===== FOOTER =====
st.markdown('<div class="footer">© 2026 VEYRA. Built for leaders.</div>', unsafe_allow_html=True)