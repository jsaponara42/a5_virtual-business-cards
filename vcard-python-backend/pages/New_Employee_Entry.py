import streamlit as st
from io import StringIO


### STREAMLIT PAGE CONFIG AND HEADERS ###

st.set_page_config(page_title="GPT Transcript Summary", page_icon=":brain:", initial_sidebar_state="expanded")

# a title and subheader for the page
st.markdown("<h1 style='text-align: center; color: black;'>OpenAI Summarize Transcript</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>Upload your transcript and get a summary, and quotes of the most important parts</h3>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: red;'>NOTE: THIS WILL TAKE A FEW MINUTES TO LOAD</h4>", unsafe_allow_html=True)

### END STREAMLIT PAGE CONFIG AND HEADERS ###


st.markdown("<h3 style='text-align: center; color: black;'>✍️ Prompt Builder</h3>", unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)


### DISPLAY PROMPT ###
prompt = st.text_area("Ask the question you would like answered here. Be sure to include how many results you would like (i.e. \"top 5)\"", value = "Summarize this transcript in 5 main points", height = 100)
#prompt = "What are the top 5 things that make a company innovative / what does it mean for a company to be innovative? Pull out 2 quotes to support each reason"
# display the prompt
st.markdown(f'''**Prompt** : `{prompt}` Pull out 2 quotes to support each reason

Format:
1. Point
a. Quote
b. Quote 
''')

### END DISPLAY PROMPT ###


st.markdown("<br> <br> ", unsafe_allow_html=True)


### RUN BUTTON GATE ###

# if run button is clicked, run the code below
if st.button("Run"):
    #this is where an example of the vcard and the newly entered database line will go
    st.success("Done!")


    ### CONVERT ANSWER TO TEXT FILE ###


    str_answer = str(vector_answer)

    if str_answer is not None:
        # download text file from streamlit
        st.download_button("Download your summary", str_answer, file_name = "transcript_summary.txt")


    ### END CONVERT ANSWER TO TEXT FILE ###




