import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", layout="wide")

# DARK BLUE THEME
st.markdown("""<style>
.stApp {background-color: #0A1128;} 
div[data-testid="stSidebar"] {background-color: #1C2541;}
h1, h2, h3, p {color: white;}
.stButton>button {background-color: #3A86FF; color: white; font-weight: bold; border-radius: 8px;}
</style></style>""", unsafe_allow_html=True)

supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

if "cart" not in st.session_state: st.session_state.cart = []

@st.cache_data
def get_products():
    return supabase.table("veyra_products").select("*").execute().data

products = get_products()
st.title("🛍️ VEYRA STORE")

if products:
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i % 3]:
            img = p["image_url"] or "https://via.placeholder.com/400x400/1C2541/FFFFFF?text=VEYRA"
            st.image(img, use_column_width=True)
            st.subheader(p["name"])
            st.write(f"**₦{p['price']:,.0f}** | Stock: {p['stock']}")
            st.write(p["description"])
            if st.button("Add to Cart", key=p["id"]):
                st.session_state.cart.append(p)

with st.sidebar:
    st.header("🛒 Cart")
    total = sum(item['price'] for item in st.session_state.cart)
    for item in st.session_state.cart: st.write(f"- {item['name']}")
    st.write(f"**Total: ₦{total:,.0f}**")
    if st.button("Checkout"): st.success("Order placed!"); st.session_state.cart = []