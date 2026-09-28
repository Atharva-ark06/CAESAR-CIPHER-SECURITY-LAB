import streamlit as st

from cipher_engine import CaesarCipher
from cryptanalysis import (
    brute_force_decrypt,
    frequency_analysis,
    verify_round_trip,
)
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


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Caesar Cipher Security Lab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# DATABASE
# ============================================================

initialize_database()


# ============================================================
# HEADER
# ============================================================

st.title("CAESAR // SECURITY LAB")

st.caption(
    "Interactive Cryptography Laboratory • "
    "Python + Streamlit + SQLite"
)


# ============================================================
# SIDEBAR — CONTROL + TECHNIQUE SELECTOR
# ============================================================

with st.sidebar:

    st.header("Control Panel")

    # --------------------------------------------------------
    # CORE OPERATIONS
    # --------------------------------------------------------

    st.subheader("Core Operations")

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

    st.caption(
        f"Normalized key: {normalized_key}"
    )

    st.divider()

    # --------------------------------------------------------
    # SECURITY TECHNIQUES
    # --------------------------------------------------------

    with st.expander("🔬 SECURITY TECHNIQUES", expanded=True):
     technique = st.radio(
        "Select Technique",
        [
            "Cipher Console",
            "Security Analysis",
            "Character Mapping",
            "Cryptographic Model",
            "Brute-Force Attack",
            "Frequency Analysis",
            "Round-Trip Verification",
            "Automated Test Center",
            "Audit History",
            "Security Summary",
        ],
        label_visibility="collapsed",
    )
    st.divider()

    # --------------------------------------------------------
    # SYSTEM STATUS
    # --------------------------------------------------------

    st.subheader("System Status")

    st.success("Cipher Engine: ONLINE")
    st.success("Database: ONLINE")
    st.success("Validation: ACTIVE")
    st.success("Cryptanalysis: ONLINE")


# ============================================================
# RIGHT-SIDE WORKSPACE
# ============================================================

# ============================================================
# CIPHER CONSOLE
# ============================================================

if technique == "Cipher Console":

    st.header("Cipher Console")

    st.write(
        "Encrypt plaintext or decrypt ciphertext "
        "using the selected Caesar Cipher key."
    )

    message = st.text_area(
        "Message",
        placeholder="Enter plaintext or ciphertext...",
        height=180,
    )

    execute = st.button(
        "ENCRYPT MESSAGE"
        if mode == "Encrypt"
        else "DECRYPT MESSAGE",
        type="primary",
        use_container_width=True,
    )

    if execute:

        valid, validation_message = validate_message(
            message
        )

        if not valid:

            st.error(validation_message)

        else:

            cipher = CaesarCipher(
                normalized_key
            )

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

            st.subheader("Result")

            st.code(
                result,
                language="text",
            )

            st.success(
                f"{mode} operation completed successfully."
            )

            st.session_state[
                "last_message"
            ] = message

            st.session_state[
                "last_result"
            ] = result

            st.session_state[
                "last_key"
            ] = normalized_key

            st.session_state[
                "last_mode"
            ] = mode


# ============================================================
# SECURITY ANALYSIS
# ============================================================

elif technique == "Security Analysis":

    st.header("Security Analysis")

    analysis_message = (
        st.session_state.get(
            "last_message",
            "",
        )
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
            "Alphabetic Characters",
            analysis["alphabetic_characters"],
        )

    with col3:

        st.metric(
            "Key Space",
            analysis["key_space"],
        )

    with col4:

        st.metric(
            "Brute Force Attempts",
            analysis["brute_force_attempts"],
        )

    st.warning(
        f"Security Assessment: "
        f"{analysis['security_level']}"
    )

    st.info(
        analysis["reason"]
    )

    st.subheader("Current Analysis Input")

    st.code(
        analysis_message,
        language="text",
    )


# ============================================================
# CHARACTER MAPPING
# ============================================================

elif technique == "Character Mapping":

    st.header("Character Mapping")

    st.write(
        f"Alphabet transformation using key "
        f"**{normalized_key}**."
    )

    cipher = CaesarCipher(
        normalized_key
    )

    mapping = cipher.get_mapping()

    mapping_text = "   ".join(
        f"{source} → {target}"
        for source, target in mapping.items()
    )

    st.code(
        mapping_text
    )

    st.subheader("Mapping Table")

    mapping_rows = [
        {
            "Plaintext": source,
            "Ciphertext": target,
        }
        for source, target in mapping.items()
    ]

    st.dataframe(
        mapping_rows,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# CRYPTOGRAPHIC MODEL
# ============================================================

elif technique == "Cryptographic Model":

    st.header("Cryptographic Model")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Encryption")

        st.latex(
            r"C = (P + K) \mod 26"
        )

        st.write(
            "Plaintext + Key → Ciphertext"
        )

    with col2:

        st.subheader("Decryption")

        st.latex(
            r"P = (C - K) \mod 26"
        )

        st.write(
            "Ciphertext − Key → Plaintext"
        )

    st.divider()

    st.subheader("Current Key")

    st.metric(
        "Normalized Key",
        normalized_key,
    )

    st.write(
        "The Caesar Cipher shifts each alphabetic "
        "character by the selected key value."
    )


# ============================================================
# BRUTE-FORCE ATTACK
# ============================================================

elif technique == "Brute-Force Attack":

    st.header("Brute-Force Attack Lab")

    st.write(
        "Simulate an attack by testing all "
        "26 possible Caesar Cipher keys."
    )

    brute_ciphertext = st.text_area(
        "Ciphertext for Attack",
        placeholder="Example: KHOOR",
    )

    run_bruteforce = st.button(
        "RUN 26-KEY BRUTE FORCE",
        type="primary",
        use_container_width=True,
    )

    if run_bruteforce:

        valid, validation_message = validate_message(
            brute_ciphertext
        )

        if not valid:

            st.error(validation_message)

        else:

            candidates = brute_force_decrypt(
                brute_ciphertext
            )

            log_operation(
                "Brute Force",
                brute_ciphertext,
                -1,
                f"{len(candidates)} candidates generated",
            )

            st.success(
                f"Attack completed — "
                f"{len(candidates)} keys tested."
            )

            st.dataframe(
                candidates,
                use_container_width=True,
                hide_index=True,
            )

            st.warning(
                "Security observation: Caesar Cipher "
                "has only 26 possible shifts, making "
                "brute-force attacks practical."
            )


# ============================================================
# FREQUENCY ANALYSIS
# ============================================================

elif technique == "Frequency Analysis":

    st.header("Frequency Analysis")

    st.write(
        "Analyze character frequency to demonstrate "
        "the weakness of simple substitution ciphers."
    )

    frequency_text = st.text_area(
        "Text for Frequency Analysis",
        placeholder="Enter ciphertext or sample text...",
    )

    run_frequency = st.button(
        "ANALYZE FREQUENCY",
        type="primary",
        use_container_width=True,
    )

    if run_frequency:

        valid, validation_message = validate_message(
            frequency_text
        )

        if not valid:

            st.error(validation_message)

        else:

            frequency_result = frequency_analysis(
                frequency_text
            )

            st.success(
                "Frequency analysis completed."
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Total Letters",
                    frequency_result[
                        "total_letters"
                    ],
                )

            with col2:

                st.metric(
                    "Unique Letters",
                    frequency_result[
                        "unique_letters"
                    ],
                )

            if frequency_result[
                "frequencies"
            ]:

                chart_data = {
                    letter: data["count"]
                    for letter, data
                    in frequency_result[
                        "frequencies"
                    ].items()
                }

                st.subheader(
                    "Character Frequency"
                )

                st.bar_chart(
                    chart_data
                )

                st.subheader(
                    "Frequency Details"
                )

                for (
                    letter,
                    data,
                ) in frequency_result[
                    "frequencies"
                ].items():

                    st.write(
                        f"**{letter}** — "
                        f"{data['count']} occurrences "
                        f"({data['percentage']}%)"
                    )

                most_frequent = (
                    frequency_result[
                        "most_frequent"
                    ]
                )

                st.info(
                    f"Most frequent character: "
                    f"{most_frequent['letter']} "
                    f"({most_frequent['percentage']}%)"
                )


# ============================================================
# ROUND-TRIP VERIFICATION
# ============================================================

elif technique == "Round-Trip Verification":

    st.header("Round-Trip Verification")

    st.write(
        "Encrypt a message and decrypt the resulting "
        "ciphertext to verify that the original "
        "plaintext is recovered."
    )

    roundtrip_text = st.text_input(
        "Plaintext",
        value="HELLO WORLD",
    )

    roundtrip_key = st.number_input(
        "Verification Key",
        min_value=-1000,
        max_value=1000,
        value=3,
        step=1,
        key="roundtrip_key",
    )

    run_roundtrip = st.button(
        "RUN ROUND-TRIP TEST",
        type="primary",
        use_container_width=True,
    )

    if run_roundtrip:

        valid, validation_message = validate_message(
            roundtrip_text
        )

        if not valid:

            st.error(validation_message)

        else:

            verification = verify_round_trip(
                roundtrip_text,
                roundtrip_key,
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("Original Plaintext")

                st.code(
                    verification[
                        "plaintext"
                    ]
                )

                st.write("Encrypted Ciphertext")

                st.code(
                    verification[
                        "ciphertext"
                    ]
                )

            with col2:

                st.write("Key")

                st.code(
                    str(
                        verification["key"]
                    )
                )

                st.write("Decrypted Plaintext")

                st.code(
                    verification[
                        "decrypted"
                    ]
                )

            if verification["passed"]:

                st.success(
                    "PASS — Original plaintext "
                    "successfully recovered."
                )

            else:

                st.error(
                    "FAIL — Decrypted text does "
                    "not match the original."
                )


# ============================================================
# AUTOMATED TEST CENTER
# ============================================================

elif technique == "Automated Test Center":

    st.header("Automated Test Center")

    st.write(
        "Run predefined positive and negative "
        "test cases against the cipher implementation."
    )

    run_tests = st.button(
        "RUN ALL TEST CASES",
        type="primary",
        use_container_width=True,
    )

    if run_tests:

        test_results = []

        # ----------------------------------------------------
        # TEST 1
        # ----------------------------------------------------

        cipher = CaesarCipher(3)

        actual = cipher.encrypt(
            "HELLO"
        )

        test_results.append({
            "Test": "Encryption",
            "Input": "HELLO",
            "Expected": "KHOOR",
            "Actual": actual,
            "Status": (
                "PASS"
                if actual == "KHOOR"
                else "FAIL"
            ),
        })

        # ----------------------------------------------------
        # TEST 2
        # ----------------------------------------------------

        actual = cipher.decrypt(
            "KHOOR"
        )

        test_results.append({
            "Test": "Decryption",
            "Input": "KHOOR",
            "Expected": "HELLO",
            "Actual": actual,
            "Status": (
                "PASS"
                if actual == "HELLO"
                else "FAIL"
            ),
        })

        # ----------------------------------------------------
        # TEST 3
        # ----------------------------------------------------

        verification = verify_round_trip(
            "HELLO WORLD",
            3,
        )

        test_results.append({
            "Test": "Round Trip",
            "Input": "HELLO WORLD",
            "Expected": "HELLO WORLD",
            "Actual": verification[
                "decrypted"
            ],
            "Status": (
                "PASS"
                if verification["passed"]
                else "FAIL"
            ),
        })

        # ----------------------------------------------------
        # TEST 4 — NEGATIVE CASE
        # ----------------------------------------------------

        wrong_key_result = (
            CaesarCipher(4)
            .decrypt("KHOOR")
        )

        test_results.append({
            "Test": "Negative / Wrong Key",
            "Input": "KHOOR + Key 4",
            "Expected": "Not HELLO",
            "Actual": wrong_key_result,
            "Status": (
                "PASS"
                if wrong_key_result != "HELLO"
                else "FAIL"
            ),
        })

        # ----------------------------------------------------
        # TEST 5 — EMPTY INPUT
        # ----------------------------------------------------

        valid, _ = validate_message("")

        test_results.append({
            "Test": "Empty Input Validation",
            "Input": "Empty",
            "Expected": "Rejected",
            "Actual": (
                "Accepted"
                if valid
                else "Rejected"
            ),
            "Status": (
                "FAIL"
                if valid
                else "PASS"
            ),
        })

        st.dataframe(
            test_results,
            use_container_width=True,
            hide_index=True,
        )

        passed = sum(
            1
            for test in test_results
            if test["Status"] == "PASS"
        )

        total = len(test_results)

        if passed == total:

            st.success(
                f"ALL TESTS PASSED — "
                f"{passed}/{total}"
            )

        else:

            st.error(
                f"{passed}/{total} tests passed."
            )


# ============================================================
# AUDIT HISTORY
# ============================================================

elif technique == "Audit History":

    st.header("Audit History")

    st.write(
        "Local record of operations performed "
        "inside the security laboratory."
    )

    col1, col2 = st.columns([5, 1])

    with col1:

        st.caption(
            "Records are stored locally using SQLite."
        )

    with col2:

        if st.button(
            "CLEAR LOG",
            key="clear_history",
        ):

            clear_history()

            st.success(
                "Audit history cleared."
            )

            st.rerun()

    history = get_history()

    if history:

        for (
            timestamp,
            operation,
            key_value,
            msg,
            result,
        ) in history:

            with st.expander(
                f"{timestamp} | "
                f"{operation} | "
                f"Key {key_value}"
            ):

                st.write("Input")

                st.code(msg)

                st.write("Output")

                st.code(result)

    else:

        st.info(
            "No operations recorded yet."
        )


# ============================================================
# SECURITY SUMMARY
# ============================================================

elif technique == "Security Summary":

    st.header("Security Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Key Space",
            "26",
        )

        st.caption(
            "Only 26 possible Caesar shifts."
        )

    with col2:

        st.metric(
            "Attack Method",
            "Brute Force",
        )

        st.caption(
            "All possible keys can be tested."
        )

    with col3:

        st.metric(
            "Cipher Strength",
            "Weak",
        )

        st.caption(
            "Suitable for education, "
            "not sensitive data."
        )

    st.divider()

    st.subheader(
        "Security Limitations"
    )

    st.write(
        "• Small key space"
    )

    st.write(
        "• Vulnerable to brute-force attacks"
    )

    st.write(
        "• Vulnerable to frequency analysis"
    )

    st.write(
        "• Simple substitution mechanism"
    )

    st.write(
        "• Not suitable for protecting "
        "real confidential information"
    )

    st.warning(
        "Caesar Cipher is intended for "
        "educational cryptography demonstrations."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "CAESAR CIPHER SECURITY LAB • "
    "Educational Cryptography Project • "
    "Python / Streamlit / SQLite"
)