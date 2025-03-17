import streamlit as st
import replicate

# Установите API-ключ Replicate
replicate_api_key = "r8_2WN4pibm60lyInGSnRSH6Ibq7W7lgI31BtXMB"
replicate_client = replicate.Client(api_token=replicate_api_key)

# Заголовок приложения
st.title("Furniture Product Shot Generator")

# Боковая панель для ввода данных
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

# Генерация изображения с использованием Stable Diffusion
if st.button("Generate Scene"):
    # Создаем описание сцены
    prompt = f"A {room_type} with a {furniture_type} in {color} {material}, styled in a {style} theme."
    
    # Генерация изображения через Replicate
    st.write("Generating image... Please wait.")
    output = replicate_client.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 1024,
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "num_inference_steps": 50
        }
    )
    
    # Показываем изображение
    st.subheader("Generated Scene")
    st.image(output[0], caption=prompt, use_column_width=True)