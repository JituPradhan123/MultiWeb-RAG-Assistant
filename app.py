import streamlit as st
from multiweb_assistant.pipeline import ask, build_multiweb_assistant

try:
    st.set_page_config(
        page_title="Your Web Assistant",
        page_icon="🤖"
    )
    st.title("🤖 Web Assistant")
    @st.cache_resource(
        show_spinner="Setting up the assistant (only happens once)..."
    )
    def get_agent():
        try:
            return build_multiweb_assistant()
        except Exception as e:
            print(f"Error building assistant: {e}")
            return None
    try:
        agent = get_agent()
        if agent is None:
            st.error("Unable to initialize the assistant.")
            st.stop()
    except Exception as e:
        st.error(f"Error initializing assistant: {e}")
        st.stop()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Show the page conversation
    try:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    except Exception as e:
        st.error(f"Error displaying conversation: {e}")
    question = st.chat_input(
        "Ask a question about your web..."
    )
    if question:
        try:
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )
            with st.chat_message("user"):
                st.markdown(question)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer = ask(
                        agent,
                        question
                    )
                st.markdown(answer)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )
        except Exception as e:
            st.error(
                f"Error processing your question: {e}"
            )
except Exception as e:
    st.error(
        f"An unexpected application error occurred: {e}"
    )