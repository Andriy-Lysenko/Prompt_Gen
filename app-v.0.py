import streamlit as st

# Промпты для каждого стиля (отсортированные по алфавиту)
style_prompts = {
    "Boho": "A boho-style room with eclectic decor, vibrant colors, and layered textiles. The space features natural materials and global influences.",
    "Bohemia": "A bohemian room with eclectic decor, vibrant colors, and mixed patterns. The space features artistic elements, global influences, and cozy textiles.",
    "Casual": "A casual room with comfortable furniture, soft textures, and neutral colors. The space has a relaxed atmosphere and practical decor.",
    "Classic": "A classic room with timeless design, luxurious fabrics, and symmetrical layouts. The space features rich colors and antique furniture.",
    "Coastal": "A coastal-themed room with light colors, beach vibes, and nautical elements. The space is filled with natural light, wicker furniture, and sea-inspired decor.",
    "Contemporary": "A contemporary room with bold colors, unique shapes, and mixed materials. The space features artistic decor and open spaces.",
    "Cottage": "A cottage-style room with floral patterns, pastel colors, and vintage furniture. The space is light-filled and features cozy textiles.",
    "Countryside": "A countryside-style room with natural materials, rustic textures, and earthy tones. The space features wooden furniture, floral decor, and a cozy atmosphere.",
    "Craftsman": "A craftsman-style room with handcrafted furniture, natural wood, and earthy tones. The space features built-in elements and a cozy atmosphere.",
    "Farmhouse": "A farmhouse-style room with shabby chic decor, reclaimed wood, and vintage elements. The space features neutral colors, cozy textiles, and a farmhouse sink.",
    "French Inspired": "A French-inspired room with elegant decor, ornate details, and pastel colors. The space features vintage furniture, chandeliers, and a romantic atmosphere.",
    "Haussmannian": "A Haussmannian-style room with elegant architecture, high ceilings, and ornate moldings. The space features large windows, classic furniture, and luxurious decor.",
    "Japandi": "A Japandi-inspired room combining Scandinavian simplicity with Japanese minimalism. The space features natural materials, muted colors, wooden textures, and a zen atmosphere.",
    "Mid-century Modern": "A mid-century modern room with retro vibes, organic shapes, and bold colors. The space features wooden furniture, vintage decor, and clean lines.",
    "Minimalist": "A minimalist room with clean lines, neutral colors, and functional furniture. The space is open, simple, and free of clutter.",
    "Modern": "A modern living space with clean lines, minimalistic design, and a neutral color palette. The room features sleek furniture, geometric shapes, and metallic accents.",
    "Modern Traditional": "A modern traditional room blending classic furniture with modern accents. The design features symmetry, rich colors, and elegant decor for a timeless look.",
    "Rustic": "A rustic room with natural materials, rough textures, and earthy tones. The space features wooden beams, stone elements, and a cozy atmosphere.",
    "Traditional": "A traditional room with ornate details, rich fabrics, and dark wood furniture. The space features classic patterns, antique decor, and warm colors.",
    "Vintage": "A vintage room with retro furniture, antique decor, and muted colors. The space features nostalgic elements and classic patterns."
}

# Контроль над камерой
camera_control = {
    "Close-up": "Close-up view focusing on the details of the furniture.",
    "Mid-range": "Mid-range shot capturing the furniture and its immediate surroundings.",
    "Wide-angle": "Wide-angle view showing the entire room with the furniture as the focal point.",
    "20% angle": "Slightly angled view to add depth and perspective to the scene.",
    "Full interior": "Full interior shot showcasing the entire room layout.",
    "A little above view": "A slightly elevated view to provide a better sense of space and arrangement."
}

# Контроль над освещением
lighting_control = {
    "Soft natural daylight": "Soft natural daylight streaming through large windows, creating a warm and inviting atmosphere.",
    "Evening mood lighting": "Evening mood lighting with soft, warm tones to create a cozy ambiance.",
    "Studio lighting": "Studio lighting with balanced brightness to highlight the furniture details.",
    "Golden hour": "Golden hour lighting with warm, golden tones to enhance the textures and colors.",
    "Overcast lighting": "Overcast lighting with diffused natural light for a calm and serene atmosphere."
}

# Контроль над позицией продукта
position_control = {
    "Center": "The furniture is positioned in the center of the frame, drawing immediate attention.",
    "Left side": "The furniture is placed on the left side of the frame, creating a balanced composition.",
    "Right side": "The furniture is placed on the right side of the frame, adding visual interest.",
    "Foreground": "The furniture is in the foreground, with the rest of the room in the background.",
    "Background": "The furniture is in the background, with other elements in the foreground to create depth."
}

# Токены для качества
quality_tokens = "Hyperrealistic 3D rendering, ultra-detailed, 8K resolution, photorealistic, cinematic quality, sharp focus, lifelike lighting, realistic shadows, intricate details, crystal-clear image quality."

# Токены для негативного промпта
negative_tokens = "busy patterns, dark lighting, cluttered, artificial colors, cartoon style, low resolution, blurry, noisy, grainy, distorted proportions, unrealistic textures, harsh shadows, oversaturated colors, highly decorated, chaotic composition, rough surfaces, childish design, unrefined edges, gaudy colors, overly complex, heavy appearance, dirty, worn, antique, steampunk elements, depth of field, (yellow walls:1.5), (warm walls:1.5), nude, NSFW."

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
        sorted(style_prompts.keys())  # Сортировка стилей по алфавиту
    )

    st.header("Camera Control")
    camera = st.selectbox(
        "Select Camera Angle/View",
        sorted(camera_control.keys())  # Сортировка по алфавиту
    )

    st.header("Lighting Control")
    lighting = st.selectbox(
        "Select Lighting",
        sorted(lighting_control.keys())  # Сортировка по алфавиту
    )

    st.header("Product Position")
    position = st.selectbox(
        "Select Product Position",
        sorted(position_control.keys())  # Сортировка по алфавиту
    )

    st.header("Quality and Negative Prompts")
    if st.button("Enable Quality Prompt", type="primary"):  # Зеленая кнопка
        st.session_state.quality_enabled = True
    if st.button("Enable Negative Prompt", type="secondary"):  # Красная кнопка
        st.session_state.negative_enabled = True

# Основная область
st.header("Selected Parameters")
st.write(f"**Furniture Type:** {furniture_type}")
st.write(f"**Material:** {material}")
st.write(f"**Color:** {color}")
st.write(f"**Room Type:** {room_type}")
st.write(f"**Style:** {style}")
st.write(f"**Camera Angle/View:** {camera}")
st.write(f"**Lighting:** {lighting}")
st.write(f"**Product Position:** {position}")

# Главный промпт
main_prompt = (
    f"A {room_type} with a {furniture_type} in {color} {material}, styled in a {style} theme. "
    f"{style_prompts[style]} {camera_control[camera]} {lighting_control[lighting]} "
    f"{position_control[position]}"
)

# Добавляем токены качества, если кнопка была нажата
if getattr(st.session_state, "quality_enabled", False):
    main_prompt += " " + quality_tokens

# Окно для негативного промпта
negative_prompt = ""
if getattr(st.session_state, "negative_enabled", False):
    negative_prompt = negative_tokens

# Главный промпт с кнопкой копирования
st.header("Generated Prompt")
st.code(main_prompt, language="text")
if st.button("Copy Main Prompt to Clipboard"):
    st.code(main_prompt, language="text")  # Показываем текст для копирования
    st.markdown(f'<textarea id="main-prompt" style="opacity:0;">{main_prompt}</textarea>', unsafe_allow_html=True)
    st.markdown('<button onclick="copyMainPrompt()">Copy Main Prompt</button>', unsafe_allow_html=True)
    st.markdown(
        """
        <script>
        function copyMainPrompt() {
            var copyText = document.getElementById("main-prompt");
            copyText.select();
            document.execCommand("copy");
            alert("Main prompt copied to clipboard!");
        }
        </script>
        """,
        unsafe_allow_html=True
    )

# Негативный промпт с кнопкой копирования
st.header("Negative Prompt")
st.code(negative_prompt, language="text")
if st.button("Copy Negative Prompt to Clipboard"):
    st.code(negative_prompt, language="text")  # Показываем текст для копирования
    st.markdown(f'<textarea id="negative-prompt" style="opacity:0;">{negative_prompt}</textarea>', unsafe_allow_html=True)
    st.markdown('<button onclick="copyNegativePrompt()">Copy Negative Prompt</button>', unsafe_allow_html=True)
    st.markdown(
        """
        <script>
        function copyNegativePrompt() {
            var copyText = document.getElementById("negative-prompt");
            copyText.select();
            document.execCommand("copy");
            alert("Negative prompt copied to clipboard!");
        }
        </script>
        """,
        unsafe_allow_html=True
    )

# Кнопка для сохранения настроек
if st.button("Save Configuration"):
    config = {
        "furniture_type": furniture_type,
        "material": material,
        "color": color,
        "room_type": room_type,
        "style": style,
        "camera": camera,
        "lighting": lighting,
        "position": position,
        "quality_enabled": getattr(st.session_state, "quality_enabled", False),
        "negative_enabled": getattr(st.session_state, "negative_enabled", False),
        "main_prompt": main_prompt,
        "negative_prompt": negative_prompt
    }
    st.session_state.config = config  # Сохраняем настройки в session_state
    st.success("Configuration saved!")

# Показ сохраненных настроек
if "config" in st.session_state:
    st.header("Saved Configuration")
    st.write(st.session_state.config)