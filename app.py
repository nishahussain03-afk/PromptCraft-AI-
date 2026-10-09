import streamlit as st
from llm import generate_response


st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 PromptCraft AI")
st.subheader("Prompt Engineering Playground")

st.write(
    "Experiment with prompts and control the creativity "
    "and response length of the AI."
)


prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: Explain Artificial Intelligence in simple English",
    height=150
)


st.markdown("### ⚙️ Generation Settings")


temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1,
    format="%.2f"
)

max_tokens = st.slider(
    "Maximum Tokens",
    min_value=50,
    max_value=1000,
    value=300,
    step=50
)

st.write(f"Temperature: `{temperature:.2f}`")
st.write(f"Maximum Tokens: `{max_tokens}`")

if st.button("✨ Generate Response", use_container_width=True):

    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:

        with st.spinner("Generating response..."):

            try:

                response = generate_response(
                    prompt,
                    temperature,
                    max_tokens
                )

                st.success("Response generated successfully!")

                st.markdown("### 🤖 AI Response")

                st.write(response)

            except Exception as e:

                st.error(f"Error: {e}")