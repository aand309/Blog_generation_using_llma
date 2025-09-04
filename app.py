import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#funtion to get response from llama 2 model
def getllamaresponse(input_text,no_words,blog_style):  
    #loading the model
    #llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama',config={'max_new_token':256,'temperature':0.01})
    llm = CTransformers(
    model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
    model_type='llama',
    config={'max_new_tokens': 256, 'temperature': 0.01}
)

    #prompt template
    template="""write a blog post about {input_text} in {no_words} words with a {blog_style} style."""
    prompt=PromptTemplate(template=template, input_variables=["input_text","no_words","blog_style"])
    response=llm(prompt.format(input_text=input_text,no_words=no_words,blog_style=blog_style))
    return response

st.set_page_config(page_title="Generate Blogs",layout='centered',initial_sidebar_state='collapsed')
st.header("Generate Blogs")
input_text=st.text_input("Enter the Blog Topic")
#creating 2 more columns for additional 2 fields
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input('NO of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',('Research', 'Technology', 'Lifestyle'),index=0)

submit=st.button("Generate Blog")

#final response
if submit:
    st.write(getllamaresponse(input_text,no_words,blog_style))
