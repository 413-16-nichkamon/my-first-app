import time
import streamlit as st

st.title("🍰 เกมทายคำศัพท์ของหวาน ")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

if "score" not in st.session_state:
    st.session_state.score = 0


# ----------------------------------------------------
# 📌 ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""

    st.session_state.score = 0
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox สรุปผล
# ----------------------------------------------------
@st.dialog(" สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):

    score = 0

    # แปลงคำตอบให้เป็นตัวพิมพ์เล็ก
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    # ------------------------------------------------
    # ตรวจคำตอบข้อ 1
    # ------------------------------------------------
    if u_ans1 == "cake":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ผิด (คุณตอบ '{u_ans1}')")

    # ------------------------------------------------
    # ตรวจคำตอบข้อ 2
    # ------------------------------------------------
    if u_ans2 == "donut":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ผิด (คุณตอบ '{u_ans2}')")

    # ------------------------------------------------
    # ตรวจคำตอบข้อ 3
    # ------------------------------------------------
    if u_ans3 == "pancake":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ผิด (คุณตอบ '{u_ans3}')")

    # ------------------------------------------------
    # ตรวจคำตอบข้อ 4
    # ------------------------------------------------
    if u_ans4 == "cookie":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ผิด (คุณตอบ '{u_ans4}')")

    # ------------------------------------------------
    # ตรวจคำตอบข้อ 5
    # ------------------------------------------------
    if u_ans5 == "waffle":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ผิด (คุณตอบ '{u_ans5}')")

    # บันทึกคะแนนสะสม
    st.session_state.score = score

    # ------------------------------------------------
    # แสดงคะแนน
    # ------------------------------------------------
    st.info(f"🏆 ได้คะแนนรวม: {score} / 5 คะแนน")

    # ------------------------------------------------
    # เกณฑ์ประเมินคะแนนด้วย if-else
    # ------------------------------------------------
    if score == 5:
        st.success(" ระดับเทพ!")
    elif score >= 3:
        st.warning(" พยายามอีกนิด!")
    else:
        st.error(" แพ้!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# 2. แถบแสดงเวลานับถอยหลัง
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    # 120 วินาที = 2 นาที
    time_left = int(120 - (time.time() - st.session_state.start))

    if time_left > 0:
        minutes = time_left // 60
        seconds = time_left % 60

        st.error(
            f"⏳ เหลือเวลา: {minutes}:{seconds:02d} นาที"
        )

    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 3. ช่องรับคำตอบ
# ----------------------------------------------------

ans1 = st.text_input(
    "ข้อ 1: A birthday dessert `c _ k e` 🍰",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: A round dessert with a hole `d _ n _ t` 🍩",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: A soft, flat dessert `p _ n c _ k e` 🥞",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: A small sweet baked dessert `c _ _ k i e` 🍪",
    value=st.session_state.ans4_val
)

ans5 = st.text_input(
    "ข้อ 5: A crispy dessert with a square pattern `w _ f f l e` 🧇",
    value=st.session_state.ans5_val
)


# ----------------------------------------------------
# อัปเดตค่าล่าสุดเข้าตัวแปร
# ----------------------------------------------------

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


# ----------------------------------------------------
# 4. ปุ่มส่งคำตอบ
# ----------------------------------------------------

if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()

    # อัปเดตเวลา
    time.sleep(1)
    st.rerun()


# ----------------------------------------------------
# 5. แสดง Dialog ผลลัพธ์
# ----------------------------------------------------

if st.session_state.get("is_ended", False):

    show_result_dialog(
        ans1,
        ans2,
        ans3,
        ans4,
        ans5
    )


st.divider()
st.write("นางสาวรพีพร อำภา เลขที่2 / นางสาวณภษร ปฐมทิตรเมธา เลขที่9 / นางสาวณิชกมล บัวตรง เลขที่16 / นายภีมพัฒน์ วงศ์ษานันท์ เลขที่22 ")
