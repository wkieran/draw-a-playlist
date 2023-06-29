import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import image_utils
import matplotlib.pyplot as plt

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)

    
bg = Image.open(bg_image) if bg_image else None
# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=bg,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
combined = None
# save save RGBA format to a pillow image object
if canvas_result.image_data is not None:
    if bg is not None:
        combined = np.where(np.any(canvas_result.image_data > 0,axis=-1,keepdims=True),canvas_result.image_data,bg)
    else:
        combined = canvas_result.image_data
    st.image(combined)
    
    
# if canvas_result.json_data is not None:
#     objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
#     for col in objects.select_dtypes(include=['object']).columns:
#         objects[col] = objects[col].astype("str")
#     # st.dataframe(objects)

# if button clicked, download image
filename = st.text_input('image filename')
if st.button('Download image') and combined is not None:
    if filename is not None:
        image = Image.fromarray(combined,mode='RGBA')
        image.save(f'{filename}.png')
    else:
        st.write('enter a filename')
if combined is not None:
    image_array = combined
    mean_R,mean_G,mean_B = image_utils.extract_color_features(image_array)
    texture = image_utils.extract_texture_features(image_array)
    temperature = image_utils.extract_temperature_feature(image_array)
    sharpness = image_utils.extract_sharpness(image_array)
    st.write(f"color features: R: {mean_R}\t G: {mean_G}\t B: {mean_B}\n")
    st.write(f"sharpness: {sharpness}\n")
    st.write(f"temperature: {temperature}\n")
    fig,ax = plt.subplots()
    ax.bar(np.arange(1,len(texture) + 1),texture)
    ax.set_xlabel('Bin')
    ax.set_xticks(np.arange(1,len(texture) + 1))
    ax.set_ylabel('Intensity')
    ax.set_title('Local Binary Pattern histogram')
    st.pyplot(fig)
             
    



