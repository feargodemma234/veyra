import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

# DARK BLUE THEME
st.markdown("""
<style>
.stApp {background-color: #0A1128;} 
div[data-testid="stSidebar"] {background-color: #1C2541;}
h1, h2, h3, h4, h5, h6, p, label {color: white;}
.stButton>button {background-color: #3A86FF; color: white; font-weight: bold; border-radius: 8px; border: none;}
</style>
""", unsafe_allow_html=True)

supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

if "cart" not in st.session_state: st.session_state.cart = []
if "user" not in st.session_state: st.session_state.user = None

def login(email, password):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user = res.user; st.rerun()
    except Exception as e: st.error(f"Login failed: {e}")

def signup(email, password):
    try:
        res = supabase.auth.sign_up({"email": email, "password": password})
        st.session_state.user = res.user; st.rerun()
    except Exception as e: st.error(f"Signup failed: {e}")

def logout():
    supabase.auth.sign_out(); st.session_state.user = None; st.session_state.cart = []; st.rerun()

@st.cache_data
def get_products():
    return supabase.table("veyra_products").select("*").execute().data

products = get_products()

with st.sidebar:
    st.title("VEYRA")
    if st.session_state.user:
        st.write(f"Welcome, {st.session_state.user.email}")
        st.button("Logout", on_click=logout)
    else:
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        with tab1:
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_pass")
            st.button("Login", on_click=login, args=(email, password))
        with tab2:
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_pass")
            st.button("Sign Up", on_click=signup, args=(email, password))
    
    st.divider()
    st.header("🛒 Your Cart")
    if len(st.session_state.cart) == 0: st.write("Cart is empty")
    else:
        total = sum(item['price'] for item in st.session_state.cart)
        for item in st.session_state.cart: st.write(f"- {item['name']} : ₦{item['price']:,.0f}")
        st.subheader(f"Total: ₦{total:,.0f}")
        if st.button("Checkout"):
            if st.session_state.user: st.success("Order placed!"); st.session_state.cart = []
            else: st.warning("Please login to checkout")

st.title("🛍️ VEYRA STORE")
st.write("Welcome to Veyra. Premium products, delivered to you.")

if not products:
    st.error("No products found. Check if veyra_products table has data and RLS is OFF")
else:
    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i % 3]:
            # THE FIX: Check if image_url exists, else use placeholder
            img_url = product["image_url"] if product["image_url"] else "https://via.placeholder.com/400x400/1C2541/FFFFFF?text=No+Image"
            st.image(img_url, use_column_width=True)
                
            st.subheader(product["name"])
            st.write(f"**₦{product['price']:,.0f}**")
            st.write(f"Stock: {product['stock']}")
            st.write(product["description"])
            if st.button(f"Add to Cart", key=product["id"]):
                st.session_state.cart.append(product); st.success(f"{product['name']} added!")