import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="Bloom’s Taxonomy QPG",
    page_icon="📘",
    layout="centered"
)

# ✅ ONLY THIS LINE — NOTHING ELSE
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")


# ---------------- UI HEADER ----------------
st.markdown(
    """
    <h1 style='text-align: center;'>📘 Bloom’s Taxonomy Question Generator</h1>
    <p style='text-align: center; color: grey;'>
    Generate outcome-based exam questions using AI
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT CARD ----------------
with st.container():
    st.markdown("### 🔧 Question Configuration")

    subject = st.text_input(
        "📚 Subject",
        placeholder="e.g., DBMS"
    )

    topic = st.text_input(
        "🧠 Topic",
        placeholder="e.g., Normalization"
    )

    bloom_level = st.selectbox(
        "🎯 Bloom’s Taxonomy Level",
        ["Remember", "Understand", "Apply", "Analyze"]
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUTTON ----------------
generate = st.button(
    "🚀 Generate Questions",
    use_container_width=True
)

# ---------------- GENERATION LOGIC ----------------
if generate:
    if subject and topic:
        prompt = f"""
        Generate 5 exam questions on the topic '{topic}'
        from the subject '{subject}'
        at the '{bloom_level}' level of Bloom’s Taxonomy.
        """

        with st.spinner("Generating questions using AI..."):
            response = model.generate_content(prompt)

        st.success("Questions generated successfully!")
        st.markdown("### 📝 Generated Questions")

        for q in response.text.split("\n\n"):
            st.markdown(f"👉 {q}")

    else:
        st.warning("Please enter both subject and topic.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Built with ❤️ using Google Gemini & Streamlit</p>",
    unsafe_allow_html=True
)
