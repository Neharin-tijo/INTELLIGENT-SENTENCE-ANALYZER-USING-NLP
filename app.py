
import streamlit as st
import spacy
import pandas as pd
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer, SnowballStemmer

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Intelligent Sentence Analyzer Using NLP",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# Load NLP model and stemmers
# --------------------------------------------------

@st.cache_resource
def load_nlp_model():
    return spacy.load("en_core_web_sm")


@st.cache_resource
def load_stemmers():
    return PorterStemmer(), SnowballStemmer("english")


# --------------------------------------------------
# Dependency tree visualization
# --------------------------------------------------

def display_dependency_tree(doc):
    """
    Draw a hierarchical dependency tree.
    Root is at the top; dependency labels appear on branches.
    """

    st.subheader("Dependency Parse Tree")

    roots = [token for token in doc if token.dep_ == "ROOT"]

    if not roots:
        st.warning("Could not identify the root of the sentence.")
        return

    root = roots[0]

    # Sort children according to their position in the sentence.
    def get_children(token):
        return sorted(list(token.children), key=lambda child: child.i)

    # Store horizontal position and depth for each token.
    positions = {}
    leaf_counter = [0]

    def assign_positions(token, depth=0):
        children = get_children(token)

        if not children:
            x = leaf_counter[0]
            leaf_counter[0] += 1
        else:
            child_positions = [
                assign_positions(child, depth + 1)
                for child in children
            ]
            x = sum(child_positions) / len(child_positions)

        positions[token.i] = (x, depth)
        return x

    assign_positions(root)

    # Find all tokens, including punctuation and any extra branches.
    # Normally all tokens belong to the root's dependency tree.
    for token in doc:
        if token.i not in positions:
            positions[token.i] = (leaf_counter[0], 1)
            leaf_counter[0] += 1

    # Draw the tree.
    max_depth = max(depth for _, depth in positions.values())
    min_x = min(x for x, _ in positions.values())
    max_x = max(x for x, _ in positions.values())

    fig_width = max(7, (max_x - min_x + 1) * 1.65)
    fig_height = max(3.5, (max_depth + 1) * 1.15)

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Draw dependency edges and labels.
    for token in doc:
        if token.dep_ == "ROOT":
            continue

        child_x, child_depth = positions[token.i]
        head_x, head_depth = positions[token.head.i]

        # Edges connect the parent to its child.
        ax.plot(
            [head_x, child_x],
            [-head_depth - 0.15, -child_depth + 0.15],
            color="black",
            linewidth=1.2,
            zorder=1
        )

        # Dependency label is placed near the middle of the branch.
        label_x = (head_x + child_x) / 2
        label_y = (
            -head_depth - 0.15 - child_depth + 0.15
        ) / 2

        ax.text(
            label_x,
            label_y,
            token.dep_,
            ha="center",
            va="center",
            fontsize=10,
            bbox={
                "facecolor": "white",
                "edgecolor": "none",
                "pad": 1.5
            },
            zorder=2
        )

    # Draw token names.
    for token in doc:
        x, depth = positions[token.i]

        ax.text(
            x,
            -depth,
            token.text,
            ha="center",
            va="center",
            fontsize=11,
            bbox={
                "boxstyle": "round,pad=0.3",
                "facecolor": "#F0F0F0",
                "edgecolor": "none"
            },
            zorder=3
        )

    ax.set_xlim(min_x - 0.7, max_x + 0.7)
    ax.set_ylim(-max_depth - 0.6, 0.6)
    ax.axis("off")

    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.caption(
        "The root is shown at the top. Each branch connects a dependent "
        "word to its syntactic head, with the dependency label displayed "
        "along the branch."
    )


# --------------------------------------------------
# Token analysis
# --------------------------------------------------

def analyze_sentence(doc, porter_stemmer, snowball_stemmer):
    rows = []

    for token in doc:
        rows.append({
            "Token": token.text,
            "Lemma": token.lemma_,
            "Porter Stem": porter_stemmer.stem(token.text),
            "Snowball Stem": snowball_stemmer.stem(token.text),
            "POS": token.pos_,
            "Detailed POS": token.tag_,
            "Dependency": token.dep_,
            "Head": token.head.text,
            "Head Index": token.head.i,
            "Morphology": str(token.morph),
            "Is Stopword": token.is_stop,
            "Is Punctuation": token.is_punct,
            "Is Alphabetic": token.is_alpha
        })

    return pd.DataFrame(rows)


# --------------------------------------------------
# Main application
# --------------------------------------------------

def main():
    st.title("🧠 Intelligent Sentence Analyzer Using NLP")

    st.write(
        "An NLP application for analyzing sentence structure, "
        "grammatical relationships, and linguistic features."
    )

    st.divider()

    # Load resources.
    try:
        nlp = load_nlp_model()
        porter_stemmer, snowball_stemmer = load_stemmers()

    except OSError:
        st.error(
            "The spaCy English model is not installed. "
            "Run the following commands in your terminal."
        )
        st.code(
            "pip install -r requirements.txt\n"
            "python -m spacy download en_core_web_sm"
        )
        st.stop()

    # --------------------------------------------------
    # Input
    # --------------------------------------------------

    st.subheader("Enter Text")

    examples = {
        "Simple sentence": "The boy eats an apple.",
        "Compound sentence": (
            "The boy eats an apple, and his sister drinks milk."
        ),
        "Complex sentence": (
            "Although it was raining, the students continued playing."
        ),
        "Named entities": (
            "Dr. A. P. J. Abdul Kalam was born in India in 1931."
        )
    }

    selected_example = st.selectbox(
        "Select an example",
        ["Custom input"] + list(examples.keys())
    )

    initial_text = (
        examples[selected_example]
        if selected_example != "Custom input"
        else "The boy eats an apple."
    )

    text_input = st.text_area(
        "Sentence or paragraph",
        value=initial_text,
        height=120,
        max_chars=10000
    )

    analyze_button = st.button(
        "Analyze Text",
        type="primary",
        use_container_width=True
    )

    if not analyze_button:
        st.info("Enter your text and click Analyze Text.")
        st.markdown(
            """
            **Features**
            - Tokenization and sentence segmentation
            - Stemming and lemmatization
            - Part-of-speech tagging
            - Hierarchical dependency parse tree
            - Named entity recognition
            - Stopword and punctuation identification
            - Downloadable CSV analysis
            """
        )
        return

    if not text_input.strip():
        st.warning("Please enter a sentence or paragraph.")
        return

    # --------------------------------------------------
    # Process input
    # --------------------------------------------------

    try:
        doc = nlp(text_input)
        if not list(doc):
            st.warning("No tokens were found.")
            return

        token_df = analyze_sentence(
            doc,
            porter_stemmer,
            snowball_stemmer
        )

    except Exception as error:
        st.error(f"An error occurred during analysis: {error}")
        return

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    st.divider()
    st.subheader("Analysis Summary")

    sentences = list(doc.sents)
    entities = list(doc.ents)
    tokens = [token for token in doc if not token.is_space]
    alphabetic_tokens = [token for token in doc if token.is_alpha]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Tokens", len(tokens))
    col2.metric("Sentences", len(sentences))
    col3.metric("Alphabetic Tokens", len(alphabetic_tokens))
    col4.metric("Named Entities", len(entities))

    # --------------------------------------------------
    # Sentence segmentation
    # --------------------------------------------------

    st.divider()
    st.subheader("1. Sentence Segmentation")

    for index, sent in enumerate(sentences, start=1):
        st.write(f"**Sentence {index}:** {sent.text}")

    # --------------------------------------------------
    # Tokenization
    # --------------------------------------------------

    st.divider()
    st.subheader("2. Tokenization")

    st.write(" → ".join(token.text for token in tokens))

    # --------------------------------------------------
    # POS tagging
    # --------------------------------------------------

    st.divider()
    st.subheader("3. Part-of-Speech Tagging")

    st.dataframe(
        token_df[["Token", "POS", "Detailed POS"]],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # Lemmatization and stemming
    # --------------------------------------------------

    st.divider()
    st.subheader("4. Lemmatization and Stemming")

    st.dataframe(
        token_df[
            ["Token", "Lemma", "Porter Stem", "Snowball Stem"]
        ],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # Dependency parsing
    # --------------------------------------------------

    st.divider()
    st.subheader("5. Syntactic Analysis")

    st.write(
        "The dependency tree displays the syntactic head and its "
        "dependent words. Labels such as nsubj, obj, and det describe "
        "grammatical relationships."
    )

    display_dependency_tree(doc)

    st.subheader("Dependency Details")

    st.dataframe(
        token_df[["Token", "Dependency", "Head", "Head Index"]],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # Named entity recognition
    # --------------------------------------------------

    st.divider()
    st.subheader("6. Named Entity Recognition")

    if entities:
        entity_df = pd.DataFrame([
            {
                "Entity": entity.text,
                "Entity Type": entity.label_,
                "Description": (
                    spacy.explain(entity.label_) or entity.label_
                )
            }
            for entity in entities
        ])

        st.dataframe(
            entity_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No named entities were detected.")

    # --------------------------------------------------
    # Stopwords and punctuation
    # --------------------------------------------------

    st.divider()
    st.subheader("7. Stopword and Punctuation Analysis")

    stopwords = [
        token.text for token in doc
        if token.is_stop and not token.is_punct
    ]

    punctuation = [
        token.text for token in doc
        if token.is_punct
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Stopwords**")
        st.write(", ".join(stopwords) if stopwords else "None")

    with col2:
        st.markdown("**Punctuation**")
        st.write(", ".join(punctuation) if punctuation else "None")

    # --------------------------------------------------
    # Export CSV
    # --------------------------------------------------

    st.divider()
    st.subheader("8. Export Results")

    csv_data = token_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Analysis as CSV",
        data=csv_data,
        file_name="sentence_analysis.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.success("Analysis completed successfully.")

    st.caption(
        "The results depend on the installed spaCy language model. "
        "Review the predicted grammatical relationships before using "
        "them as ground-truth annotations."
    )


if __name__ == "__main__":
    main()
