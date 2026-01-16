import streamlit as st
import requests
import random
from user_agent import generate_user_agent
from time import sleep

# --- إعدادات الصفحة والتصميم ---
st.set_page_config(page_title="علــش | @GX1GX1", page_icon="⚔️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    
    @keyframes pulse-gold {
        0% { transform: scale(1); box-shadow: 0 0 5px #FFD700; }
        50% { transform: scale(1.05); box-shadow: 0 0 20px #FFD700; }
        100% { transform: scale(1); box-shadow: 0 0 5px #FFD700; }
    }
    .user-avatar {
        display: block; margin: auto; border: 4px solid #FFD700;
        border-radius: 50%; animation: pulse-gold 2s infinite;
        margin-bottom: 20px;
    }

    .stButton>button {
        width: 100%; border-radius: 12px; 
        background: linear-gradient(45deg, #FFD700, #DAA520);
        color: black; font-weight: bold; border: none; height: 3.5em;
        transition: 0.3s; margin-top: 10px;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 5px 15px rgba(255,215,0,0.4); }

    .stSelectbox div[data-baseweb="select"] { background-color: #1a1a1a; border: 1px solid #DAA520; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #FFD700; border: 1px solid #DAA520; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- عرض الصورة الشخصية ---
st.markdown(f'<img src="https://i.ibb.co/cXgRkRTf/6e37bd54624a0d987f097ff5bb04a58e.jpg" class="user-avatar" width="160">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #FFD700;'>علـــش | GX1GX1</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'> رشق الخدمات الاجتماعية المتكاملة</p>", unsafe_allow_html=True)
st.write("---")

# --- دالة لتوليد IP عشوائي ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# --- دالات الرشق الأصلية ---
def send_request(url, link, quantity=None):
    random_ip = generate_random_ip()
    headers = {
        "User-Agent": generate_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://leofame.com",
        "referer": url.split('?')[0],
        "cookie": "token=FAKETOKEN; cf_clearance=FAKECOOKIE",
        "X-Forwarded-For": random_ip,
        "Client-IP": random_ip
    }
    data = {
        "token": "FAKETOKEN",
        "timezone_offset": "Asia/Baghdad",
        "free_link": link
    }
    if quantity: data["quantity"] = quantity
    
    try:
        # إضافة تأخير عشوائي بين 3 إلى 7 ثوانٍ
        wait_time = random.randint(3, 7)
        st.info(f"⏳ جاري الانتظار {wait_time} ثوانٍ لتجنب الحظر...")
        sleep(wait_time)
        
        r = requests.post(url, headers=headers, data=data)
        if "Please wait" in r.text or '"error":' in r.text:
            st.error("⚠️ الموقع يطلب الانتظار. جرب لاحقاً أو غير الرابط.")
        else:
            st.success(f"✅ تم الإرسال بنجاح بـ IP وهمي: {random_ip}")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")

# --- واجهة الاختيار ---
option = st.selectbox(
    "اختر الخدمة المطلوبة:",
    ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ منشور إنستغرام", "مشاهدات تيك توك"]
)

video_url = st.text_input("ضع الرابط هنا 👇", placeholder="https://...")

if st.button("بدأ"):
    if video_url:
        with st.spinner('جاري معالجة الطلب...'):
            if option == "إعجابات يوتيوب":
                send_request("https://leofame.com/free-youtube-likes?api=1", video_url)
            elif option == "إعجابات تيك توك":
                send_request("https://leofame.com/free-tiktok-likes?api=1", video_url)
            elif option == "حفظ منشور إنستغرام":
                send_request("https://leofame.com/free-instagram-saves?api=1", video_url, "30")
            elif option == "مشاهدات تيك توك":
                send_request("https://leofame.com/ar/free-tiktok-views?api=1", video_url, "200")
    else:
        st.warning("يرجى إدخال الرابط أولاً!")

st.write("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #555;'>تم التطوير بواسطة علش @GX1GX1</p>", unsafe_allow_html=True)
