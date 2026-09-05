import streamlit as st
from supabase import create_client

st.set_page_config(page_title="VEYRA", page_icon="🛍️", layout="wide")

# DARK RED THEME
st.markdown("""
<style>
.stApp {background-color: #8B0000;}
div[data-testid="stSidebar"] {background-color: #5C0000;}
h1, h2, h3, h4, h5, h6, p, label {color: white;}
.stButton>button {background-color: white; color: #8B0000; font-weight: bold; border-radius: 8px;}
</style>
""", unsafe_allow_html=True)

# CONNECT TO SUPABASE
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# CART IN SESSION STATE
if "cart" not in st.session_state:
    st.session_state.cart = []

# GET PRODUCTS FROM NEW TABLE
@st.cache_data
def get_products():
    data = supabase.table("veyra_products").select("*").execute()
    return data.data

products = get_products()

# HEADER
st.title("🛍️ VEYRA STORE")
st.write("Welcome to Veyra. Premium products, delivered to you.")

# SHOW PRODUCTS
if not products:
    st.error("No products found. Check if veyra_products table has data and RLS is OFF")
else:
    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i % 3]:
            # FIX: ONLY SHOW IMAGE IF IT EXISTS
            if product["image_url"]:
                st.image(product["image_url"], use_column_width=True)
            else:
                st.write("🖼️ No Image")
                
            st.subheader(product["name"])
            st.write(f"**₦{product['price']:,.0f}**")
            st.write(f"Stock: {product['stock']}")
            st.write(product["description"])
            if st.button(f"Add to Cart", key=product["id"]):
                st.session_state.cart.append(product)
                st.success(f"{product['name']} added to cart!")

# SIDEBAR CART WITH AUTO CALCULATION
with st.sidebar:
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
            st.success("Order placed! We will contact you.")
            st.session_state.cart = []