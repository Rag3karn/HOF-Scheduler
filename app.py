"""
HOF Scheduler - Streamlit Web Application
User-friendly interface for generating match announcements
"""

import streamlit as st # type: ignore
import tempfile
import os
from scheduler import process_schedule_file
import pandas as pd # type: ignore


# Page configuration
st.set_page_config(
    page_title="HOF Scheduler",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF5252;
        transform: scale(1.02);
    }
    .success-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #FFEBEE;
        border-left: 5px solid #F44336;
        margin: 1rem 0;
    }
    .announcement-box {
        background-color: #F5F5F5;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #E0E0E0;
        font-family: monospace;
        white-space: pre-wrap;
        margin: 1rem 0;
        max-height: 500px;
        overflow-y: auto;
    }
    .header-title {
        text-align: center;
        color: #FF6B6B;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .header-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        background-color: #000;
        color: #FFF;
    }
    .stCodeBlock pre {
        background-color: #000;
        color: #FFF;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)


def reset_app():
    """Reset all session state variables"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]


def initialize_session_state():
    """Initialize session state variables"""
    if 'announcement' not in st.session_state:
        st.session_state.announcement = None
    if 'errors' not in st.session_state:
        st.session_state.errors = None
    if 'file_processed' not in st.session_state:
        st.session_state.file_processed = False


def main():
    """Main application function"""
    initialize_session_state()
    
    # Header
    st.markdown('<p class="header-title">⚽ HOF - Scheduler</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="header-subtitle">Generate match announcements effortlessly</p>', 
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # File upload section
    st.subheader("📁 Upload Match Schedule")
    uploaded_file = st.file_uploader(
        "Choose an Excel file (.xlsx)",
        type=['xlsx'],
        help="Upload your match schedule Excel file with the required columns",
        key="file_uploader"
    )
    
    # Action buttons in columns
    col1, col2 = st.columns(2)
    
    with col1:
        generate_button = st.button(
            "🚀 Generate Announcement",
            disabled=uploaded_file is None,
            use_container_width=True
        )
    
    with col2:
        reset_button = st.button(
            "🔄 Reset",
            use_container_width=True,
            type="secondary"
        )
    
    # Handle reset
    if reset_button:
        reset_app()
        st.rerun()
    
    # Process file when generate button is clicked
    if generate_button and uploaded_file is not None:
        with st.spinner("🔄 Processing your schedule..."):
            try:
                # Save uploaded file to temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name
                
                # Process the file
                success, announcement, errors = process_schedule_file(tmp_file_path)
                
                # Clean up temporary file
                os.unlink(tmp_file_path)
                
                # Store results in session state
                st.session_state.file_processed = True
                if success:
                    st.session_state.announcement = announcement
                    st.session_state.errors = None
                else:
                    st.session_state.announcement = None
                    st.session_state.errors = errors
                
            except Exception as e:
                st.session_state.file_processed = True
                st.session_state.announcement = None
                st.session_state.errors = [f"Unexpected error: {str(e)}"]
    
    # Display results
    if st.session_state.file_processed:
        st.markdown("---")
        
        if st.session_state.errors:
            # Display errors
            st.markdown('<div class="error-box">', unsafe_allow_html=True)
            st.error("❌ **Validation Errors Found**")
            for error in st.session_state.errors:
                st.markdown(f"- {error}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("""
                <div class="info-box">
                    <strong>💡 Tips:</strong>
                    <ul style="margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                        <li>Check that all required columns are present and spelled correctly</li>
                        <li>Ensure dates and times are in the correct format</li>
                        <li>Verify that playerCapacity is an even number</li>
                        <li>Make sure all required fields have values</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        elif st.session_state.announcement:
            # Display success and announcement
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.success("✅ **Announcement Generated Successfully!**")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.subheader("📢 Generated Announcement")

            # Copy functionality using streamlit-javascript
            st.info("💡 **Tip:** Expand 'View Raw Text' for easy copying.")
            
            # Alternative: Use st.code for easy copying
            with st.expander("📝 View Raw Text (Click to Expand for Easy Copy)", expanded=True):
                st.code(st.session_state.announcement, language=None)
            
            # Download button as backup
            st.download_button(
                label="📥 Download as Text File",
                data=st.session_state.announcement,
                file_name="hof_announcement.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #999; font-size: 0.9rem;'>"
        "Made with ❤️ for Humans of Football | Version 1.0"
        "</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
