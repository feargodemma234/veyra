import streamlit as st
import json
import os
st.set_page_config(page_title="VEYRA | Shop Like a Millionaire", layout="wide", page_icon="🔷")
css = """<style>.stApp { background-color: #0A0F2C; }#MainMenu {visibility: hidden;}footer {visibility: hidden;}header {visibility: hidden;}.logo-text { font-size: 32px; font-weight: 900; color: white; letter-spacing: 3px; }.stButton>button[kind="secondary"] { background: #FFC107; color: #0A0F2C; padding: 10px 25px; border-radius: 50px; font-weight: 800; border: none; font-size: 16px; }.hero { height: 85vh; background: linear-gradient(rgba(10,15,44,0.85), rgba(10,15,44,0.85)), url('https://images.unsplash.com/photo-1441986300917-64674bd60018?w=1400') center/cover; display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center; margin-bottom: 60px; }.hero-logo-container { margin-bottom: 30px; padding: 20px; background: rgba(18, 25, 53, 0.6); border-radius: 50%; border: 2px solid #FFC107; display: flex; justify-content: center; align-items: center; }.hero h1 { color: white; font-size: 60px; font-weight: 900; margin-bottom: 15px; letter-spacing: 2px; }.hero p { color: #C0C5D0; font-size: 20px; margin-bottom: 30px; }.shop-btn button { background: #FFC107 !important; color: #0A0F2C !important; padding: 18px 60px !important; border-radius: 50px !important; font-size: 20px !important; font-weight: 800 !important; border: none !important; }.section-title { text-align: center; font-size: 42px; color: white; font-weight: 900; margin: 60px 0 40px 0; }.product-card { background: #121935; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #1E2A5E; transition: 0.3s; }.product-card:hover { transform: translateY(-10px); border: 1px solid #FFC107; }.price { color: #FFC107; font-size: 22px; font-weight: 700; }.add-cart button { background: transparent !important; color: #FFC107 !important; border: 1px solid #FFC107 !important; border-radius: 20px !important; width: 100%; }.add-cart button:hover { background: #FFC107 !important; color: #0A0F2C !important; }.buy-btn button { background: #25D366 !important; color: white !important; border-radius: 20px !important; width: 100%; font-weight: 800 !important; }.owner-panel { background: #121935; padding: 30px; border-radius: 15px; border: 1px solid #FFC107; margin: 40px 5%; }.contact-btn { display: flex; gap: 20px; justify-content: center; margin-top: 20px; }.contact-btn a { background: #FFC107; color: #0A0F2C; padding: 12px 30px; border-radius: 50px; text-decoration: none; font-weight: 800; }.footer { text-align: center; color: #777; padding: 40px; border-top: 1px solid #1E2A5E; margin-top: 60px; }</style>"""
st.markdown(css, unsafe_allow_html=True)
PRODUCTS_FILE = "products.json"
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'owner_mode' not in st.session_state:
    st.session_state.owner_mode = False
def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r") as f:
            return json.load(f)
    return [
        {"name": "Signature Jacket", "price": 299000, "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600"},
        {"name": "Luxury Sneakers", "price": 189000, "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600"},
        {"name": "Gold Chrono", "price": 499000, "image": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=600"}
    ]
def save_products(products):
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products, f)
products = load_products()
col1, col2, col3 = st.columns([3,1,1])
with col1:
    st.markdown('<div class="logo-text">VEYRA</div>', unsafe_allow_html=True)
with col2:
    if st.button(f"Cart ({len(st.session_state.cart)})", type="secondary"):
        st.session_state.show_cart = True
with col3:
    if st.button("Owner"):
        st.session_state.owner_mode = not st.session_state.owner_mode
if st.session_state.owner_mode:
    st.markdown('<div class="owner-panel">', unsafe_allow_html=True)
    st.write("### 🔒 Owner Panel - Add New Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price in ₦", min_value=1000)
    img = st.text_input("Image URL")
    if st.button("Add Product"):
        products.append({"name": name, "price": price, "image": img})
        save_products(products)
        st.success("Product Added!")
        st.rerun()
    st.write("### Current Products")
    for p in products:
        st.write(f"- {p['name']} - ₦{p['price']:,}")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="hero-logo-container">', unsafe_allow_html=True)
if os.path.exists("veyra_logo.png"):
    st.image("veyra_logo.png", width=180)
else:
    st.markdown('<h1 style="color:#FFC107;font-size:48px;">V</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<h1>Shop Like a Millionaire</h1>', unsafe_allow_html=True)
st.markdown('<p>Luxury fashion & streetwear for those who lead</p>', unsafe_allow_html=True)
st.markdown('<div class="shop-btn">', unsafe_allow_html=True)
st.button("Shop Now")
st.markdown('</div></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Featured Drops</h2>', unsafe_allow_html=True)
cols = st.columns(3, gap="large")
for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image(product["image"])
        st.write(f"### {product['name']}")
        st.markdown(f'<p class="price">₦{product["price"]:,}</p>', unsafe_allow_html=True)
        st.markdown('<div class="add-cart">', unsafe_allow_html=True)
        if st.button("Add to Cart", key=f"add{idx}"):
            st.session_state.cart.append(product)
            st.toast(f"{product['name']} Added!")
        st.markdown('</div></div>', unsafe_allow_html=True)
if st.session_state.get("show_cart", False):
    st.markdown('<h2 class="section-title">Your Cart</h2>', unsafe_allow_html=True)
    if len(st.session_state.cart) == 0:
        st.write("Cart is empty")
    else:
        total = sum([p["price"] for p in st.session_state.cart])
        for item in st.session_state.cart:
            st.write(f"- {item['name']} - ₦{item['price']:,}")
        st.write(f"### Total: ₦{total:,}")
        order_text = "Hello VEYRA, I want to order:%0A" + "%0A".join([f"- {p['name']} - ₦{p['price']:,}" for p in st.session_state.cart]) + f"%0A%0ATotal: ₦{total:,}"
        whatsapp_link = f"https://wa.me/2348012345678?text={order_text}"
        st.markdown(f'<div class="buy-btn">', unsafe_allow_html=True)
        st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button>Buy on WhatsApp</button></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.write("### Contact Us")
st.markdown('<div class="contact-btn">', unsafe_allow_html=True)
st.markdown('<a href="https://wa.me/2348012345678" target="_blank">WhatsApp</a>', unsafe_allow_html=True)
st.markdown('<a href="mailto:veyraofficial@gmail.com">Email Us</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.write("© 2026 VEYRA. Built for leaders.")
st.markdown('</div>', unsafe_allow_html=True)