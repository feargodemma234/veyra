import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

# CONNECT TO SUPABASE
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# SESSION STATE
if "user" not in st.session_state: st.session_state.user = None
if "cart" not in st.session_state: st.session_state.cart = []

# AUTH FUNCTIONS
def signup(email, password):
    try: return supabase.auth.sign_up({"email": email, "password": password}).user, None
    except Exception as e: return None, str(e)

def login(email, password):
    try: return supabase.auth.sign_in_with_password({"email": email, "password": password}).user, None
    except Exception as e: return None, str(e)

def logout():
    supabase.auth.sign_out()
    st.session_state.user = None
    st.session_state.cart = []
    st.rerun()

# GET PRODUCTS
@st.cache_data
def get_products():
    data = supabase.table("products").select("*").execute()
    return data.data

# HEADER
st.title("🛍️ VEYRA Store")

# IF NOT LOGGED IN
if st.session_state.user is None:
    tab1, tab2 = st.tabs(["Login", "Create Account"])
    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            user, error = login(email, password)
            if user: st.session_state.user = user; st.rerun()
            else: st.error(f"Login failed: {error}")
    with tab2:
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Sign Up"):
            user, error = signup(email, password)
            if user: st.success("Account created! Login now.")
            else: st.error(f"Signup failed: {error}")

# IF LOGGED IN
else:
    col1, col2 = st.columns([4,1])
    with col1: st.success(f"Welcome, {st.session_state.user.email}")
    with col2: st.button("Logout", on_click=logout)
    
    st.divider()
    
    # SHOW PRODUCTS
    products = get_products()
    st.subheader("Products")
    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i % 3]:
            st.image(product["image_url"] if product["image_url"] else "https://via.placeholder.com/150")
            st.markdown(f"### {product['name']}")
            st.write(f"₦{product['price']:,.2f}")
            st.write(f"Stock: {product['stock']}")
            if st.button("Add to Cart", key=product["id"]):
                st.session_state.cart.append(product)
                st.toast(f"{product['name']} added to cart!")
    
    # SHOW CART
    with st.sidebar:
        st.subheader(f"🛒 Cart: {len(st.session_state.cart)} items")
        total = sum([p["price"] for p in st.session_state.cart])
        for item in st.session_state.cart:
            st.write(f"{item['name']} - ₦{item['price']:,.2f}")
        st.divider()
        st.markdown(f"**Total: ₦{total:,.2f}**")
        if st.button("Checkout", use_container_width=True):
            st.info("Next: We will connect Paystack here for payment + delivery form")