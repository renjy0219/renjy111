import streamlit as st
st.title("Hello, 2024!")
st.header("You need to learn some basic operations")
st.subheader("wow, 河北工业大学!")
st.text("It's so beautiful")

st.markdown("this is an image: \n \
            ![](https://www.hebut.edu.cn/images/2024-05/02cc0bf02ad74cdbaf57cdef810ce211.png)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['Reading',
                'Writing',
                'Coding',
                'Traveling'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    