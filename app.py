import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

# DARK RED BACKGROUND
st.markdown("""
    <style>
    .stApp {
        background-color: #8B0000;
    }
    div[data-testid="stSidebar"] {
        background-color: #5C0000;
    }
    </style>
""", unsafe_allow_html=True)

# CONNECT TO SUPABASE
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# SESSION STATE
if "user" not in st.session_state: st.session_state.user = None
if "cart" not in st.session_state: st.session_state.cart = []

# AUTH
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

# GET PRODUCTS - with error handling
@st.cache_data(ttl=60)
def get_products():
    try:
        data = supabase.table("products").select("*").execute()
        return data.data
    except Exception as e:
        st.error(f"Can't load products: {e}")
        return []

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
            else: st.error(error)
    with tab2:
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Sign Up"):
            user, error = signup(email, password)
            if user: st.success("Account created! Login now.")
            else: st.error(error)

# IF LOGGED IN
else:
    top1, top2 = st.columns([5,1])
    with top1: st.write(f"Welcome, **{st.session_state.user.email}**")
    with top2: st.button("Logout", on_click=logout)
    
    products = get_products()
    
    if not products:
        st.warning("No products found. Did you add them to Supabase and turn off RLS?")
    else:
        st.subheader("New Arrivals")
        cols = st.columns(3)
        for i, p in enumerate(products):
            with cols[i % 3]:
                with st.container(border=True):
                    st.image(p["image_url"], use_container_width=True)
                    st.markdown(f"**{p['name']}**")
                    st.caption(p["description"])
                    st.markdown(f"### ₦{p['price']:,.0f}")
                    st.write(f"In Stock: {p['stock']}")
                    qty = st.number_input("Qty", min_value=1, max_value=p["stock"], value=1, key=f"qty{p['id']}")
                    if st.button("Add to Cart", key=p["id"], use_container_width=True):
                        st.session_state.cart.append({"item": p, "qty": qty})
                        st.toast(f"Added {qty} x {p['name']}")
    
    # AUTO CALCULATING CART
    with st.sidebar:
        st.header(f"🛒 Your Cart")
        subtotal = 0
        if st.session_state.cart:
            for cart_item in st.session_state.cart:
                p = cart_item["item"]
                qty = cart_item["qty"]
                line_total = p["price"] * qty
                subtotal += line_total
                st.write(f"{p['name']} x{qty} = ₦{line_total:,.0f}")
        else:
            st.write("Cart is empty")
        
        delivery = 2500
        total = subtotal + delivery
        
        st.divider()
        st.write(f"Subtotal: ₦{subtotal:,.0f}")
        st.write(f"Delivery: ₦{delivery:,.0f}")
        st.subheader(f"Total: ₦{total:,.0f}")
        if st.button("Proceed to Checkout", use_container_width=True, type="primary"):
            st.info("Next: Delivery form + Paystack")