import streamlit as st
from supabase import create_client
import time
from datetime import datetime

# PUT YOUR KEYS HERE
SUPABASE_URL = "https://your-project.supabase.co" 
SUPABASE_KEY = "your-anon-key"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="VEYRA", layout="wide", page_icon="🔷")
css = """<style>.stApp { background-color: #0A0F2C; } .chat-box { background: #121935; padding: 20px; border-radius: 15px; border: 1px solid #25D366; height: 400px; overflow-y: auto; } .customer { background: #1E2A5E; color: white; padding: 10px; border-radius: 10px; margin: 5px 0; } .owner { background: #FFC107; color: #0A0F2C; padding: 10px; border-radius: 10px; margin: 5px 0; margin-left: 50px; }</style>"""
st.markdown(css, unsafe_allow_html=True)

# LOGIN
if 'user' not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.markdown("<h1 style='text-align:center; color:#FFC107'>VEYRA LOGIN</h1>", unsafe_allow_html=True)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up"):
            res = supabase.auth.sign_up({"email": email, "password": password})
            st.success("Check your email to confirm")
    with col2:
        if st.button("Login"):
            res = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if res.user:
                st.session_state.user = res.user
                st.rerun()
    st.stop()

user = st.session_state.user
st.write(f"Welcome {user.email}")
if st.button("Logout"):
    supabase.auth.sign_out()
    st.session_state.user = None
    st.rerun()

# LOAD PRODUCTS FROM DB
products = supabase.table('products').select('*').execute().data

st.markdown("<h1 style='color:white'>Shop Like a Millionaire</h1>", unsafe_allow_html=True)
cols = st.columns(3)
for i, p in enumerate(products):
    with cols[i%3]:
        st.image(p['image'])
        st.write(f"### {p['name']}")
        st.write(f"₦{p['price']:,}")

# LIVE CHAT FROM DB
st.markdown("<h2 style='color:white'>Chat with Support</h2>", unsafe_allow_html=True)
chat_data = supabase.table('chats').select('*').eq('user_id', user.id).order('created_at').execute().data

st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for msg in chat_data:
    cls = "owner" if msg['sender'] == 'Owner' else 'customer'
    st.markdown(f"<div class='{cls}'><b>{msg['sender']}</b>: {msg['message']}</div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

new_msg = st.text_input("Type message")
if st.button("Send"):
    supabase.table('chats').insert({
        "user_id": user.id, 
        "user_email": user.email,
        "sender": user.email, 
        "message": new_msg
    }).execute()
    st.rerun()

# OWNER PANEL
if user.email == "veyraofficial@gmail.com": # CHANGE TO YOUR EMAIL
    st.write("### Owner Panel")
    all_chats = supabase.table('chats').select('*').order('created_at').execute().data
    for c in all_chats:
        st.write(f"{c['user_email']}: {c['message']}")

# AUTO REFRESH
time.sleep(3)
st.rerun()