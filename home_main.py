import streamlit as st
st.header("Listen Song")
st.subheader("  ",divider=True)
st.image("https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/07/just-listen-to-the-song.jpg?q=50&fit=crop&w=1140&h=&dpr=1.5")
a=st.file_uploader("Select a music File",type=None)

if a:
    try:
    
       st.audio(a)
       st.info("File Opened")
       
       
    except Exception as E:
        
        st.exception(E)
        st.info("Error Generated")
        

   

