import streamlit as st
from supabase import create_client

# PAGE SETUP
st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="centered")

# CONNECT TO SUPABASE
try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except:
    st.error("Supabase keys not found. Add them in Streamlit Settings > Secrets")
    st.stop()


# SESSION STATE
if "user" not in st.session_state:
    st.session_state.user = None


# AUTH FUNCTIONS
def signup(email, password):
    try:
        res = supabase.auth.sign_up({"email": email, "password": password})
        return res.user, None
    except Exception as e:
        return None, str(e)

def login(email, password):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return res.user, None
    except Exception as e:
        return None, str(e)

def logout():
    supabase.auth.sign_out()
    st.session_state.user = None
    st.rerun()


# HEADER
st.title("🛍️ VEYRA")
st.caption("Your online store")


# IF USER IS NOT LOGGED IN
if st.session_state.user is None:
    tab1, tab2 = st.tabs(["Login", "Create Account"])
    
    with tab1:
        st.subheader("Login")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login", use_container_width=True):
            if email and password:
                user, error = login(email, password)
                if user:
                    st.session_state.user = user
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error(f"Login failed: {error}")
            else:
                st.warning("Please enter email and password")

    with tab2:
        st.subheader("Create Account")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Sign Up", use_container_width=True):
            if email and password:
                if len(password) < 6:
                    st.warning("Password must be at least 6 characters")
                else:
                    user, error = signup(email, password)
                    if user:
                        st.success("Account created! You can login now.")
                    else:
                        st.error(f"Signup failed: {error}")
            else:
                st.warning("Please enter email and password")


# IF USER IS LOGGED IN
else:
    st.success(f"Welcome, {st.session_state.user.email} 👋")
    if st.button("Logout"):
        logout()
    
    st.divider()
    st.subheader("VEYRA Store Coming Soon...")
    st.write("Next we will add products, cart, and checkout here.")