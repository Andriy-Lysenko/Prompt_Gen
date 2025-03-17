import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Title of the app
st.title("Furniture Product Shot Generator")

# Sidebar for user inputs
with st.sidebar:
    st.header("Furniture Details")
    furniture_type = st.selectbox(
        "Select Furniture Type",
        ["Sofa", "Armchair", "Table", "Bed", "Dining Chair"]
    )
    material = st.selectbox(
        "Select Material",
        ["Leather", "Wood", "Fabric", "Metal"]
    )
    color = st.selectbox(
        "Select Color",
        ["Beige", "Black", "White", "Gray", "Brown"]
    )

    st.header("Room Settings")
    room_type = st.selectbox(
        "Select Room Type",
        ["Living Room", "Bedroom", "Dining Room", "Office"]
    )
    style = st.selectbox(
        "Select Style",
        ["Scandinavian", "Minimalist", "Industrial", "Bohemian", "Classic"]
    )

# Generate scene description using OpenAI
if st.button("Generate Scene"):
    prompt = f"""
    Create a detailed description of a {room_type} with a {furniture_type} in {color} {material}.
    The room should be styled in a {style} theme. Include details about lighting, decor, and overall ambiance.
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    
    scene_description = response.choices[0].text.strip()
    
    st.subheader("Generated Scene Description")
    st.write(scene_description)
    # Add this after the scene description generation
image_prompt = f"A {room_type} with a {furniture_type} in {color} {material}, styled in a {style} theme."
image_response = openai.Image.create(
    prompt=image_prompt,
    n=1,
    size="1024x1024"
)

image_url = image_response['data'][0]['url']
st.image(image_url, caption="Generated Scene", use_column_width=True)