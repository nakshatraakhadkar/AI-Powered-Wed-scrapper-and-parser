import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content)
from parse import parse_with_ollama
from export import export_to_excel, export_to_powerpoint
import traceback

st.set_page_config(page_title="Nax's Web Scraper", layout="wide")
st.title("Nax's Web Scraper")

# Initialize session state
if 'parsed_result' not in st.session_state:
    st.session_state.parsed_result = None

url = st.text_input("Enter a website URL")

if st.button("Scrape it!"):
    try:
        with st.spinner("Scraping the website..."):
            result = scrape_website(url)
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)
            st.session_state.dom_content = cleaned_content
            st.success("Website scraped successfully!")
    except Exception as e:
        st.error(f"Error scraping website: {str(e)}")
        st.code(traceback.format_exc())

# Always display the DOM content if it exists
if "dom_content" in st.session_state:
    with st.expander("View DOM content"):
        st.text_area("DOM content", st.session_state.dom_content, height=300)

    parse_description = st.text_area("What would you like me to extract?")

    if st.button("Parse content"):
        if parse_description:
            try:
                with st.spinner("Parsing content..."):
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    result = parse_with_ollama(dom_chunks, parse_description)
                    st.session_state.parsed_result = result
                    st.success("Content parsed successfully!")
            except Exception as e:
                st.error(f"Error parsing content: {str(e)}")
                st.code(traceback.format_exc())
        else:
            st.warning("Please enter what you'd like to extract from the content.")

# Always display the parsed content if it exists
if "parsed_result" in st.session_state and st.session_state.parsed_result is not None:
    st.write("### Parsed Content")
    st.write(st.session_state.parsed_result)

    # Export section
    st.write("### Export Options")
    col1, col2 = st.columns(2)
    
    with col1:
        export_to_excel(st.session_state.parsed_result)

    with col2:
        export_to_powerpoint(st.session_state.parsed_result)
