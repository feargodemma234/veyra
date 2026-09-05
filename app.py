import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

# DARK BLUE THEME
st.markdown("""
<style>
.stApp {background-color: #0A1128;} /* Deep Navy */
div[data-testid="stSidebar"] {background-color: #1C2541;} /* Royal Navy */
h1, h2, h3, h4, h5, h6, p, label {color: white;}
.stButton>button {background-color: #3A86FF; color: white; font-weight: bold; border-radius: 8px; border: none;}
.stTextInput>div>div>input {color: white; background-color: #1C2541;}
</style>
""", unsafe_allow_html=True)

# CONNECT TO SUPABASE
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# SESSION STATE
if "cart" not in st.session_state:
    st.session_state.cart = []
if "user" not in st.session_state:
    st.session_state.user = None

# AUTH FUNCTIONS
def login(email, password):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user = res.user
        st.success("Logged in!")
        st.rerun()
    except Exception as e:
        st.error(f"Login failed: {e}")

def signup(email, password):
    try:
        res = supabase.auth.sign_up({"email": email, "password": password})
        st.session_state.user = res.user
        st.success("Account created! Check email to confirm.")
        st.rerun()
    except Exception as e:
        st.error(f"Signup failed: {e}")

def logout():
    supabase.auth.sign_out()
    st.session_state.user = None
    st.session_state.cart = []
    st.rerun()

# GET PRODUCTS
@st.cache_data
def get_products():
    data = supabase.table("veyra_products").select("*").execute()
    return data.data

products = get_products()

# HEADER + AUTH IN SIDEBAR
with st.sidebar:
    st.title("VEYRA")
    if st.session_state.user:
        st.write(f"Welcome, {st.session_state.user.email}")
        if st.button("Logout"):
            logout()
    else:
        auth_tab = st.tabs(["Login", "Sign Up"])
        with auth_tab[0]:
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_pass")
            if st.button("Login"):
                login(email, password)
        with auth_tab[1]:
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_pass")
            if st.button("Sign Up"):
                signup(email, password)
    
    st.divider()
    # CART
    st.header("🛒 Your Cart")
    if len(st.session_state.cart) == 0:
        st.write("Cart is empty")
    else:
        total = 0
        for item in st.session_state.cart:
            st.write(f"- {item['name']} : ₦{item['price']:,.0f}")
            total += item['price']
        
        st.divider()
        st.subheader(f"Total: ₦{total:,.0f}")
        
        if st.button("Checkout"):
            if st.session_state.user:
                st.success("Order placed! We will contact you.")
                st.session_state.cart = []
            else:
                st.warning("Please login to checkout")

# MAIN PAGE
st.title("🛍️ VEYRA STORE")
st.write("Welcome to Veyra. Premium products, delivered to you.")

# SHOW PRODUCTS
if not products:
    st.error("No products found. Check if veyra_products table has data and RLS is OFF")
else:
    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i % 3]:
            if product["image_url"]:
                st.image(product["image_url"], use_column_width=True)
            st.subheader(product["name"])
            st.write(f"**₦{product['price']:,.0f}**")
            st.write(f"Stock: {product['stock']}")
            st.write(product["description"])
            if st.button(f"Add to Cart", key=product["id"]):
                st.session_state.cart.append(product)
                st.success(f"{product['name']} added to cart!")