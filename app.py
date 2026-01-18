import streamlit as st
from src.pipeline import orchestrator
from dotenv import load_dotenv
import tempfile
import os

load_dotenv()

#--------------------HOME PAGE---------------------
#--------------------------------------------------

st.set_page_config(
    page_title="Verify ai",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <h1 style="text-align: center;">🔍 VERIFY AI ✅</h1>
    <br><br/>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <h3 style="text-align: center;" >Welcome to Verify AI, <br/> Where facts get verified and claims get challenged !</h3>
    <br><br/>
    """,
    unsafe_allow_html=True
)


st.write("")




#--------------------UPLOAD FILE---------------------
#----------------------------------------------------


upload_file = st.file_uploader("Upload a PDF file", type=["pdf"])

st.write("")


if upload_file:
    if st.button("Verify Claims"):

        with st.spinner("Verifying..."):
            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(delete = False, suffix = '.pdf') as tmp:
                tmp.write(upload_file.read())
                temp_path = tmp.name

            results = orchestrator(temp_path)

            os.remove(temp_path)



        st.write("")

        st.success("Done!")


# -------------------- DISPLAY RESULTS --------------------
#----------------------------------------------------------


        for item in results:
            st.markdown("--------")


            # -------- Claim --------

            st.markdown("### 📌 Claim: ")
            st.markdown(f"##### **{item.get('claim', 'N/A')}**")

            st.write("")

            # -------- Verdict --------

            st.markdown("### ⚖️ Verdict: ")

            verdict = item.get("verdict", "N/A")

            if verdict == "Verified":
                st.success("✅ Verified")

            elif verdict == "Inaccurate":
                st.warning("⚠️ Inaccurate")

            elif verdict == "False":
                st.error("❌ False")

            else:
                st.info(verdict)


            st.write("")


 # --------------- SOURCES -----------------
  # ----------------------------------------


            with st.expander("📚 Sources"):

                source_data = item.get("source", {})
                source_results = source_data.get("results", [])

                if not source_results:
                    st.write("No sources found.")

                else:
                    for i, src in enumerate(source_results, 1):
                        st.markdown(f"### {i}. {src.get('title', 'No title')}")
                        st.write(src.get("content", ""))
                        st.write(src.get("url", ""))
                        st.markdown("---")

            