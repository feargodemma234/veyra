import streamlit as st
st.set_page_config(page_title="VEYRA | Shop Like a Millionaire", layout="wide", page_icon="🔷")
css = """
<style>
.stApp { background-color: #0A0F2C; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.navbar { display: flex; justify-content: space-between; align-items: center; padding: 20px 5%; background: #0A0F2C; position: sticky; top: 0; z-index: 99; border-bottom: 1px solid #1E2A5E; }
.logo-text { font-size: 32px; font-weight: 900; color: white; letter-spacing: 3px; }
.stButton>button[kind="secondary"] { background: #FFC107; color: #0A0F2C; padding: 10px 25px; border-radius: 50px; font-weight: 800; border: none; font-size: 16px; }
.hero { height: 85vh; background: linear-gradient(rgba(10,15,44,0.85), rgba(10,15,44,0.85)), url('https://images.unsplash.com/photo-1441986300917-64674bd60018?w=1400') center/cover; display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center; margin-bottom: 60px; }
.hero-logo-container { margin-bottom: 30px; padding: 20px; background: rgba(18, 25, 53, 0.6); border-radius: 50%; border: 2px solid #FFC107; display: flex; justify-content: center; align-items: center; }
.hero h1 { color: white; font-size: 60px; font-weight: 900; margin-bottom: 15px; letter-spacing: 2px; }
.hero p { color: #C0C5D0; font-size: 20px; margin-bottom: 30px; }
.shop-btn button { background: #FFC107 !important; color: #0A0F2C !important; padding: 18px 60px !important; border-radius: 50px !important; font-size: 20px !important; font-weight: 800 !important; border: none !important; }
.shop-btn button:hover { background: white !important; transform: scale(1.05); }
.section-title { text-align: center; font-size: 42px; color: white; font-weight: 900; margin: 60px 0 40px 0; }
.product-card { background: #121935; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #1E2A5E; transition: 0.3s; }
.product-card:hover { transform: translateY(-10px); border: 1px solid #FFC107; }
.price { color: #FFC107; font-size: 22px; font-weight: 700; }
.add-cart button { background: transparent !important; color: #FFC107 !important; border: 1px solid #FFC107 !important; border-radius: 20px !important; width: 100%; }
.add-cart button:hover { background: #FFC107 !important; color: #0A0F2C !important; }
.footer { text-align: center; color: #777; padding: 40px; border-top: 1px solid #1E2A5E; margin-top: 60px; }
</style>
"""
st.markdown(css, unsafe_allow_html=True)
if 'cart' not in st.session_state:
    st.session_state.cart = 0
col1, col2 = st.columns([4,1])
with col1:
    st.markdown('<div class="logo-text">VEYRA</div>', unsafe_allow_html=True)
with col2:
    if st.button(f"Cart ({st.session_state.cart})", type="secondary"):
        st.toast("Cart feature coming soon!")
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="hero-logo-container">', unsafe_allow_html=True)
st.image("veyra_logo.png", width=180)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<h1>Shop Like a Millionaire</h1>', unsafe_allow_html=True)
st.markdown('<p>Luxury fashion & streetwear for those who lead</p>', unsafe_allow_html=True)
st.markdown('<div class="shop-btn">', unsafe_allow_html=True)
if st.button("Shop Now"):
    st.session_state.scroll = True
st.markdown('</div></div>', unsafe_allow_html=True)
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
st.markdown('<div class="footer">© 2026 VEYRA. Built for leaders.</div>', unsafe_allow_html=True)