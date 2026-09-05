import streamlit as st

st.set_page_config(page_title="VEYRA", layout="wide", page_icon="🔷")

# CUSTOM CSS FOR LUXURY LOOK
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    .navbar { display: flex; justify-content: space-between; padding: 20px 5%; background: #000; position: sticky; top: 0; z-index: 99; }
    .logo { font-size: 32px; font-weight: 900; color: white; letter-spacing: 3px; }
    .cart-btn { background: #FFC107; color: #000; padding: 10px 25px; border-radius: 50px; font-weight: 700; border: none; }
    .hero { 
        height: 60vh; 
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
        url('https://images.unsplash.com/photo-1441986300917-64674bd60018?w=1200') center/cover;
        display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center;
    }
    .hero h1 { color: white; font-size: 60px; }
    .shop-btn { background: white; color: black; padding: 18px 60px; border-radius: 50px; font-size: 20px; font-weight: 800; border: none; }
    .product-card { background: #111; padding: 20px; border-radius: 15px; text-align: center; }
    .price { color: #FFC107; font-size: 22px; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# SESSION STATE FOR CART
if 'cart' not in st.session_state:
    st.session_state.cart = 0

# NAVBAR
col1, col2 = st.columns([4,1])
with col1:
    st.markdown('<div class="logo">VEYRA</div>', unsafe_allow_html=True)
with col2:
    if st.button(f"Cart ({st.session_state.cart})"):
        st.toast("Cart opened!")

# HERO SECTION
st.markdown('<div class="hero">', unsafe_allow_html=True)
if st.button("Shop Now"):
    st.session_state.scroll = True
st.markdown('</div>', unsafe_allow_html=True)

# FEATURED DROPS
st.markdown("<h2 style='text-align: center; font-size: 42px; color: white;'>Featured Drops</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500")
    st.write("### Signature Jacket")
    st.markdown('<p class="price">₦299,000</p>', unsafe_allow_html=True)
    if st.button("Add to Cart", key="1"):
        st.session_state.cart += 1
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500")
    st.write("### Luxury Sneakers")
    st.markdown('<p class="price">₦189,000</p>', unsafe_allow_html=True)
    if st.button("Add to Cart", key="2"):
        st.session_state.cart += 1
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=500")
    st.write("### Gold Chrono")
    st.markdown('<p class="price">₦499,000</p>', unsafe_allow_html=True)
    if st.button("Add to Cart", key="3"):
        st.session_state.cart += 1
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #777; padding: 40px;'>© 2026 VEYRA. Built for leaders.</p>", unsafe_allow_html=True)