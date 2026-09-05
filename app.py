import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

if "user" not in st.session_state: st.session_state.user = None
if "cart" not in st.session_state: st.session_state.cart = []

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

@st.cache_data
def get_products():
    return supabase.table("products").select("*").execute().data

st.title("🛍️ VEYRA Store")

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
else:
    top1, top2 = st.columns([5,1])
    with top1: st.write(f"Welcome, **{st.session_state.user.email}**")
    with top2: st.button("Logout", on_click=logout)
    
    products = get_products()
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
                if st.button("Add to Cart", key=p["id"], use_container_width=True):
                    st.session_state.cart.append(p)
                    st.toast(f"Added {p['name']}")
    
    with st.sidebar:
        st.header(f"🛒 Your Cart ({len(st.session_state.cart)})")
        total = sum([p["price"] for p in st.session_state.cart])
        for item in st.session_state.cart:
            st.write(f"- {item['name']}")
        st.divider()
        st.subheader(f"Total: ₦{total:,.0f}")
        if st.button("Proceed to Checkout", use_container_width=True, type="primary"):
            st.info("Next step: Add delivery details + Paystack payment")