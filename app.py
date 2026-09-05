import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

# DARK THEME LIKE THE VIDEO
st.markdown("""
<style>
.stApp {background-color: #0A1128;} /* Deep Navy */
div[data-testid="stSidebar"] {background-color: #1C2541;}
h1, h2, h3, h4, p, label {color: white;}

/* Product Card */
.product-card {
    background-color: #1C2541;
    padding: 12px;
    border-radius: 16px;
    margin-bottom: 15px;
}

/* Banner */
.banner {
    background: linear-gradient(90deg, #1C2541 0%, #3A86FF 100%);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
}

.stButton>button {
    background-color: #FF3131; /* Red accent like cart icon */
    color: white; 
    font-weight: bold; 
    border-radius: 12px; 
    border: none;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# CONNECT
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# SESSION STATE
if "cart" not in st.session_state: st.session_state.cart = []
if "user" not in st.session_state: st.session_state.user = None
if "search" not in st.session_state: st.session_state.search = ""
if "category" not in st.session_state: st.session_state.category = "All"

# AUTH
def login(email, password):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user = res.user; st.rerun()
    except: st.error("Login failed")

def signup(email, password):
    try:
        supabase.auth.sign_up({"email": email, "password": password})
        st.success("Account created! Check email")
    except: st.error("Signup failed")

def logout():
    supabase.auth.sign_out(); st.session_state.user = None; st.session_state.cart = []; st.rerun()

# GET PRODUCTS
@st.cache_data
def get_products():
    return supabase.table("veyra_products").select("*").execute().data

products = get_products()

# HEADER WITH CART ICON
col1, col2 = st.columns([6,1])
with col1:
    st.title("VEYRA")
with col2:
    st.write(f"🛒 {len(st.session_state.cart)}")

# BANNER LIKE 40% OFF
st.markdown("""
<div class="banner">
    <h2>40% OFF NEW ARRIVALS</h2>
    <p>Premium products. Limited time.</p>
</div>
""", unsafe_allow_html=True)

# SEARCH BAR
st.session_state.search = st.text_input("Search products...", placeholder="Search Shoes", label_visibility="collapsed")

# BRAND FILTER ROW
st.write("**Popular Brands**")
brands = ["All", "Nike", "Adidas", "ZARA", "Puma", "LV"]
st.session_state.category = st.selectbox("Filter", brands, label_visibility="collapsed")

# CATEGORY TABS
tab1, tab2, tab3 = st.tabs(["All", "Men's", "Women's"])

def show_products(product_list):
    cols = st.columns(2) # 2 per row like the video
    for i, p in enumerate(product_list):
        with cols[i % 2]:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            img = p["image_url"] or "https://via.placeholder.com/400x400/1C2541/FFFFFF?text=VEYRA"
            st.image(img, use_column_width=True)
            st.subheader(p["name"])
            st.write(f"**₦{p['price']:,.0f}**")
            st.write(f"⭐ 4.5 | Stock: {p['stock']}")
            if st.button("Add to Cart", key=p["id"]):
                st.session_state.cart.append(p)
                st.toast(f"{p['name']} added!")
            st.markdown('</div>', unsafe_allow_html=True)

with tab1:
    filtered = [p for p in products if st.session_state.search.lower() in p["name"].lower()]
    show_products(filtered)
with tab2:
    filtered = [p for p in products if "men" in p["name"].lower() and st.session_state.search.lower() in p["name"].lower()]
    show_products(filtered)
with tab3:
    filtered = [p for p in products if "women" in p["name"].lower() and st.session_state.search.lower() in p["name"].lower()]
    show_products(filtered)


# SIDEBAR = CART + LOGIN
with st.sidebar:
    st.title("Account")
    if st.session_state.user:
        st.write(f"Hi, {st.session_state.user.email}")
        st.button("Logout", on_click=logout)
    else:
        t1, t2 = st.tabs(["Login", "Sign Up"])
        with t1:
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_pass")
            st.button("Login", on_click=login, args=(email, password))
        with t2:
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_pass")
            st.button("Sign Up", on_click=signup, args=(email, password))
    
    st.divider()
    st.header("🛒 Your Cart")
    if len(st.session_state.cart) == 0: 
        st.write("Cart is empty")
    else:
        total = sum(item['price'] for item in st.session_state.cart)
        for item in st.session_state.cart: 
            st.write(f"- {item['name']}")
        st.subheader(f"Total: ₦{total:,.0f}")
        if st.button("Checkout"):
            if st.session_state.user: 
                st.success("Order placed!"); st.session_state.cart = []
            else: 
                st.warning("Please login to checkout")