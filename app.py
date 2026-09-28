import streamlit as st

from cipher_engine import CaesarCipher
from database import (
    initialize_database,
    log_operation,
    get_history,
    clear_history,
)
from security_analysis import (
    validate_message,
    normalize_key,
    analyze_message,
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Caesar Cipher Security Lab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM UI
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #16213e 0%, transparent 35%),
        radial-gradient(circle at 90% 20%, #102a43 0%, transparent 35%),
        #070b12;
    color: #f5f7fa;
}

.main-title {
    font-size: 4rem;
    font-weight: 900;
    letter-spacing: -3px;
    margin-bottom: 0;
}

.subtitle {
    color: #8b98a9;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    margin-top: 2rem;
}

.security-card {
    padding: 1.2rem;
    border: 1px solid #263449;
    border-radius: 16px;
    background: rgba(15, 23, 42, 0.72);
    margin-bottom: 1rem;
}

.result-box {
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid #334155;
    background: #0d1420;
    font-size: 1.3rem;
    font-family: monospace;
}

.metric-box {
    padding: 1rem;
    border-radius: 14px;
    background: #0d1420;
    border: 1px solid #263449;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

initialize_database()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">CAESAR // SECURITY LAB</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Interactive cryptography laboratory • Python + Streamlit + SQLite'
    '</div>',
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## CONTROL PANEL")

    mode = st.radio(
        "Operation",
        ["Encrypt", "Decrypt"],
    )

    key = st.number_input(
        "Cipher Key",
        min_value=-1000,
        max_value=1000,
        value=3,
        step=1,
    )

    normalized_key = normalize_key(key)

    st.caption(f"Normalized key: {normalized_key}")

    st.divider()

    st.markdown("### System")

    st.success("Cipher Engine: ONLINE")
    st.success("Database: ONLINE")
    st.success("Validation: ACTIVE")


# --------------------------------------------------
# MAIN CIPHER CONSOLE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">01 / CIPHER CONSOLE</div>',
    unsafe_allow_html=True,
)

message = st.text_area(
    "Message",
    placeholder="Enter plaintext or ciphertext...",
    height=180,
)

execute = st.button(
    f"{'ENCRYPT' if mode == 'Encrypt' else 'DECRYPT'} MESSAGE",
    type="primary",
    use_container_width=True,
)


if execute:

    valid, validation_message = validate_message(message)

    if not valid:

        st.error(validation_message)

    else:

        cipher = CaesarCipher(normalized_key)

        if mode == "Encrypt":
            result = cipher.encrypt(message)
        else:
            result = cipher.decrypt(message)

        log_operation(
            mode,
            message,
            normalized_key,
            result,
        )

        st.markdown("### Result")

        st.markdown(
            f"""
            <div class="result-box">
                {result}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.success(
            f"{mode} operation completed successfully."
        )

        st.session_state["last_message"] = message
        st.session_state["last_result"] = result
        st.session_state["last_key"] = normalized_key
        st.session_state["last_mode"] = mode


# --------------------------------------------------
# CIPHER MAPPING
# --------------------------------------------------

st.markdown(
    '<div class="section-title">02 / CHARACTER MAPPING</div>',
    unsafe_allow_html=True,
)

cipher = CaesarCipher(normalized_key)
mapping = cipher.get_mapping()

mapping_text = "   ".join(
    f"{source} → {target}"
    for source, target in mapping.items()
)

st.code(mapping_text)


# --------------------------------------------------
# SECURITY ANALYSIS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">03 / SECURITY ANALYSIS</div>',
    unsafe_allow_html=True,
)

analysis_message = (
    st.session_state.get("last_message", message)
    or "CAESAR CIPHER"
)

analysis = analyze_message(
    analysis_message,
    normalized_key,
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Message Length",
        analysis["message_length"],
    )

with col2:
    st.metric(
        "Letters",
        analysis["alphabetic_characters"],
    )

with col3:
    st.metric(
        "Key Space",
        analysis["key_space"],
    )

with col4:
    st.metric(
        "Brute Force",
        f"{analysis['brute_force_attempts']} attempts",
    )


st.warning(
    f"Security Assessment: {analysis['security_level']}"
)

st.info(analysis["reason"])


# --------------------------------------------------
# FORMULAS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">04 / CRYPTOGRAPHIC MODEL</div>',
    unsafe_allow_html=True,
)

formula_col1, formula_col2 = st.columns(2)

with formula_col1:

    st.markdown("### Encryption")

    st.latex(
        r"C = (P + K) \mod 26"
    )

    st.caption(
        "Plaintext + Key → Ciphertext"
    )


with formula_col2:

    st.markdown("### Decryption")

    st.latex(
        r"P = (C - K) \mod 26"
    )

    st.caption(
        "Ciphertext − Key → Plaintext"
    )


# --------------------------------------------------
# AUDIT HISTORY
# --------------------------------------------------

st.markdown(
    '<div class="section-title">05 / AUDIT HISTORY</div>',
    unsafe_allow_html=True,
)

history_col1, history_col2 = st.columns(
    [5, 1]
)

with history_col1:

    st.caption(
        "Operations stored locally using SQLite."
    )

with history_col2:

    if st.button("CLEAR LOG"):

        clear_history()

        st.success("Audit history cleared.")

        st.rerun()


history = get_history()

if history:

    for timestamp, operation, key_value, msg, result in history:

        with st.expander(
            f"{timestamp}  |  {operation}  |  Key {key_value}"
        ):

            st.write("Input:")
            st.code(msg)

            st.write("Output:")
            st.code(result)

else:

    st.info(
        "No operations recorded yet."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "CAESAR CIPHER SECURITY LAB • "
    "Educational Cryptography Project • "
    "Python / Streamlit / SQLite"
)