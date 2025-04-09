import streamlit as st
# import pyperclip # Убрано
import json

# Устанавливаем конфигурацию страницы (лучше делать в самом начале)
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Nfinite Prompt Generator")

# --- Новые опции для поверхностей ---
surface_options = {
    "None": "on an appropriate surface", # Дефолт/fallback
    "Light Oak Parquet": "on a light oak parquet floor",
    "Dark Walnut Parquet (Herringbone)": "on a dark walnut herringbone parquet floor",
    "Aged Pine Floorboards": "on aged pine floorboards",
    "Grey Laminate": "on a grey laminate floor",
    "Natural Wood Laminate": "on a natural wood laminate floor",
    "Large Beige Area Rug": "on a large beige area rug covering the floor",
    "Colorful Geometric Rug": "on a colorful geometric area rug",
    "Persian Style Rug": "on an intricate Persian style rug",
    "Neutral Carpet over Wooden Floor": "on a soft, neutral-toned carpet covering the wooden floor",
    "White Marble Tile": "on white marble floor tiles",
    "Black Slate Tile": "on black slate floor tiles",
    "Terracotta Tile": "on terracotta floor tiles",
    "Polished Concrete": "on a polished concrete floor",
    "Matte Concrete": "on a matte concrete floor"
}

# --- Структурированные опции для Окружающих Элементов ---
surrounding_details_structured = {
    "Left Zone": [
        "Large potted plant (left)",
        "Modern floor lamp (left)",
        "Side table (left)",
    ],
    "Wall / Background": [
        "Single picture frame on wall",
        "Set of 2-3 picture frames on wall",
        "Multiple picture frames on wall",
        "Framed floral artwork(s) on wall",
        "Wall mirror with ornate frame",
        "Floating wall shelves with books",
        "Visible window with sheer curtains",
        "Visible window with heavy drapes",
        "Beige curtains framing the scene",
        "Fireplace (inactive)",
    ],
    "Right Zone": [
        "Large potted plant (right)",
        "Modern floor lamp (right)",
        "Side table (right)",
        "Sculpture on a pedestal (right)",
    ],
    "Foreground / General": [
        "Coffee table with vase of flowers (foreground)",
        "Stack of books on the floor",
        "Magazines on a nearby table",
        "Empty coffee cups on a surface",
        "Laptop on a desk nearby",
        "Decorative pillows on seating",
        "Throw blanket draped over furniture",
        "Small decorative objects on shelves/surfaces",
    ]
}
# Создадим плоский список всех опций для проверки при загрузке и для функции генерации
all_surrounding_options = [item for sublist in surrounding_details_structured.values() for item in sublist]


# Промпты для каждого стиля
style_prompts = {
    "None": "",
    "Bohemian": "with eclectic decor, vibrant colors, mixed patterns, and layered textiles, featuring natural materials, global influences, and artistic elements",
    "Casual": "with comfortable furniture, soft textures, and neutral colors, featuring a relaxed atmosphere and practical decor",
    "Classic": "with timeless design, luxurious fabrics, and symmetrical layouts, featuring rich colors and antique furniture",
    "Coastal": "with light colors, beach vibes, and nautical elements, featuring natural light, wicker furniture, and sea-inspired decor",
    "Contemporary": "with bold colors, unique shapes, and mixed materials, featuring artistic decor and open spaces",
    "Cottage": "with floral patterns, pastel colors, and vintage furniture, featuring light-filled spaces and textiles",
    "Countryside": "with natural materials, rustic textures, and earthy tones, featuring wooden furniture, floral decor, and an inviting atmosphere",
    "Craftsman": "with handcrafted furniture, natural wood, and earthy tones, featuring built-in elements and an inviting atmosphere",
    "Farmhouse": "with shabby chic decor, reclaimed wood, and vintage elements, featuring neutral colors, textiles, and a farmhouse sink",
    "French Inspired": "with elegant decor, ornate details, and pastel colors, featuring vintage furniture, chandeliers, and a romantic atmosphere",
    "Industrial": "with exposed brick, metal accents, and raw materials, featuring open layouts, high ceilings, and vintage furniture",
    "Midcentury Modern": "with clean lines, organic shapes, and minimal ornamentation, featuring iconic furniture and a retro vibe",
    "Minimalist": "with simplicity, clean lines, and neutral colors, featuring clutter-free spaces and functional furniture",
    "Modern": "with sleek lines, neutral colors, and minimal decor, featuring open spaces, natural light, and metal accents",
    "Rustic": "with natural materials, rough textures, and earthy tones, featuring wooden beams, stone fireplaces, and cozy textiles",
    "Scandinavian": "with simplicity, functionality, and minimalism, featuring light colors, natural wood, and cozy textiles",
    "Southwestern": "with earthy colors, tribal patterns, and natural materials, featuring terracotta, cacti, and rustic furniture",
    "Spanish": "with warm colors, wrought iron, and textured walls, featuring arched doorways, tiled floors, and rustic furniture",
    "Traditional": "with classic furniture, rich colors, and detailed ornamentation, featuring symmetry, elegant fabrics, and dark wood",
    "Transitional": "with a mix of traditional and modern elements, featuring neutral colors, comfortable furniture, and clean lines",
    "Tropical": "with vibrant colors, exotic plants, and natural materials, featuring rattan furniture, bold patterns, and a relaxed vibe",
    "Vintage": "with antique furniture, retro patterns, and nostalgic decor, featuring classic pieces and a charming atmosphere"
}

# Описание контроля освещения
lighting_control = {
    "None": "",
    "Natural Light": "with abundant natural light flooding the space, clear daylight illuminating the scene, highlighting all details",
    "Soft Ambient Light": "with soft ambient light creating a cozy atmosphere",
    "Bright Studio Light": "with bright studio lighting for a clear view",
    "Dramatic Cinematic Light": "with dramatic cinematic lighting, casting deep shadows",
    "Warm Evening Light": "with warm evening light casting a golden glow",
    "Overcast Daylight": "with diffused overcast daylight, providing even illumination",
    "Golden Hour Light": "during the golden hour, with warm, soft, and long shadows",
    "Candlelight": "lit by flickering candlelight, creating an intimate and warm ambiance"
}

# Описание контроля FOV
fov_control = {
    "None": "",
    "Close up": "Close up shot",
    "Zoomed-in partially visible": "Zoomed-in partially visible shot",
    "Midshot": "Midshot",
    "Full interior": "Full interior shot",
    "Wide angle": "Wide angle shot"
}

# Описание контроля камеры
camera_control = {
    "None": "",
    "Front view": "Front view",
    "Side view": "Side view",
    "High-angle view": "High-angle view",
    "Low-angle view": "Low-angle view",
    "Dutch angle view": "Dutch angle view",
    "Top-down view": "Top-down view",
    "3/4 view": "3/4 view"
}

# Описание типов мебели и их подтипов
furniture_options = {
    "None": ["None"],
    "Seating": [
        "None", "Two-seater Sofa", "Three-seater Sofa", "Corner Sofa", "Modular Sofa",
        "Sectional Sofa", "Armchair", "Accent Chair", "Recliner", "Chaise Lounge",
        "Bench", "Stool", "Ottoman",
    ],
    "Tables": [
        "None", "Coffee Table", "Side Table", "Console Table", "Dining Table", "Desk"
    ],
    "Storage": [
        "None", "Bookshelf", "Cabinet", "Chest of Drawers", "Wardrobe", "Sideboard",
        "Entertainment Center"
    ],
    "Beds": [
        "None", "Single Bed", "Double Bed", "Queen Size Bed", "King Size Bed",
        "Platform Bed", "Canopy Bed", "Bunk Bed", "Daybed", "Headboard",
    ],
    "Lighting": [
        "None", "Table Lamp", "Floor Lamp", "Pendant Light", "Chandelier", "Wall Sconce",
        "Ceiling fan"
    ],
    "Rugs": [
        "None", "Large area outdoor rug", "Runner rug", "Round rug", "Horizontal placed rug"
    ]
}

# Описание типов комнат
room_options = [
    "None", "Living Room", "Bedroom", "Dining Room", "Kitchen", "Home Office",
    "Bathroom", "Entryway", "Kids Room", "Outdoor Patio", "Balcony",
    "Studio Apartment", "Hallway", "Outdoor lounge zone"
]

# Токены качества
quality_tokens = "Best quality, photorealistic, high resolution, sharp focus, detailed texture, professional photography"

# Негативные токены (если нужны)
negative_prompt_base = "Worst quality, low quality, blurry, unfocused, text, words, letters, signature, watermark, username, artist name, deformed, mutated, ugly, distorted, poorly drawn, bad anatomy, extra limbs, missing limbs"


# ----- Инициализация Session State -----
default_values = {
    "furniture_type": "None", "furniture_subtype": "None", "room_type": "None",
    "style": "None", "lighting": "None", "fov": "None", "camera": "None",
    "surface": "None", "surrounding_elements": [], "main_prompt": "",
    "negative_prompt": negative_prompt_base, "quality_enabled": True,
    "negative_enabled": True, "saved_configs": {}, "model_type": "Fooocus",
    "prompt_logic": "FLUX"
}
for key, default_value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = default_value
for item in all_surrounding_options:
    if item not in st.session_state:
         st.session_state[item] = False


# ----- Функции -----
def update_subtypes():
    selected_type = st.session_state.furniture_type_select
    st.session_state.furniture_type = selected_type
    if selected_type != "None":
        current_subtype = st.session_state.get('furniture_subtype', 'None')
        if selected_type in furniture_options:
             if current_subtype not in furniture_options[selected_type]:
                  st.session_state.furniture_subtype = "None"
        else:
             st.session_state.furniture_type = "None"
             st.session_state.furniture_subtype = "None"
    else:
        st.session_state.furniture_subtype = "None"

def get_furniture_description():
    furniture_type = st.session_state.furniture_type
    subtype = st.session_state.furniture_subtype
    if furniture_type != "None" and subtype != "None":
        return f"A {subtype}"
    elif furniture_type != "None":
        return f"A piece of {furniture_type.lower()} furniture"
    return ""

def get_selected_surrounding_elements():
    """Собирает список описаний для выбранных чекбоксов деталей."""
    selected = []
    for item in all_surrounding_options:
        if st.session_state.get(item, False):
            selected.append(item)
    return selected

def generate_prompt():
    logic = st.session_state.prompt_logic

    f_type = st.session_state.get('furniture_type', 'None')
    f_subtype = st.session_state.get('furniture_subtype', 'None')
    r_type = st.session_state.get('room_type', 'None')
    style_sel = st.session_state.get('style', 'None')
    lighting_sel = st.session_state.get('lighting', 'None')
    fov_sel = st.session_state.get('fov', 'None')
    camera_sel = st.session_state.get('camera', 'None')
    surface_sel = st.session_state.get('surface', 'None')
    elements_sel = get_selected_surrounding_elements()


    if logic == "FLUX":
        if f_type == "None" or f_subtype == "None":
            if f_type != "Rugs":
                 return "Please select a Furniture Type and Subtype to use the FLUX logic (unless type is Rugs)."
            elif f_type == "Rugs" and f_subtype == "None":
                 return "Please select a specific Rug subtype for FLUX logic."

        fov_text = "Photo"
        if fov_sel != "None" and fov_sel in fov_control and fov_control[fov_sel]:
             base_fov_text = fov_control[fov_sel]
             if "partially visible" in base_fov_text.lower():
                 fov_text = base_fov_text
             else:
                 fov_text = base_fov_text.replace(" shot", "").strip()
                 if fov_text:
                     fov_text = fov_text[0].upper() + fov_text[1:]
                     fov_text += " photo"
                 else:
                      fov_text = "Photo"

        camera_angle_desc = "emphasize the sense of space and arrangement, focusing on the subject"
        if camera_sel != "None" and camera_sel in camera_control and camera_control[camera_sel]:
            angle_text = camera_control[camera_sel].replace(" view", "").strip().lower()
            if angle_text:
                 camera_angle_desc = f"adopt a {angle_text} angle to emphasize the sense of space and arrangement"

        surface_desc = surface_options.get(surface_sel, surface_options["None"])

        details_desc = "the entire room, including surrounding furniture, decor elements, and room architecture,"
        if elements_sel:
            elements_string = ", ".join(elements_sel)
            details_desc = f"the entire room, including specific elements like {elements_string}, along with other furniture and room architecture,"

        subject = f_subtype
        subject_desc_start = subject

        placement = "positioned in the center of the composition"
        if f_type == "Rugs":
             placement = "laid out on the floor"
             surface_desc = ""
             if surface_sel != "None" and "rug" in surface_options.get(surface_sel, "").lower():
                  surface_desc = f", {surface_options[surface_sel].replace(' covering the floor','')}"


        style_desc = f"{style_sel} style" if style_sel != "None" and style_sel in style_prompts else "a specified style"
        room_desc = r_type if r_type != "None" and r_type in room_options else "room"
        lighting_condition_desc = "under clear diffuse lighting conditions"
        if lighting_sel != "None":
             if lighting_sel in lighting_control and lighting_control[lighting_sel]:
                 lighting_condition_desc = f"under {lighting_sel.lower()} conditions"
             elif lighting_sel != "None":
                 lighting_condition_desc = f"with {lighting_sel.lower()} lighting"

        atmosphere_desc = f"in {style_desc} {room_desc} with bright airy atmosphere"

        prompt = (
            f"{fov_text} of a {subject_desc_start} {placement}{surface_desc}, {atmosphere_desc}, "
            f"captured with a Nikon Z7 II camera and a 24mm f/1.2L lens. "
            # <<< Фраза "for a wide depth of field" удалена ниже vvv
            f"Set the aperture to f/22, ensuring {details_desc} is in sharp focus. "
            f"The composition should {camera_angle_desc}, with the {subject}. "
            f"Adjust the shutter speed to 1/160 to maintain crisp clarity {lighting_condition_desc}. "
            f"Set the white balance to 6500k to ensure a neutral white color pallete. "
            f"Soft shadows and subtle reflections on mixed materials can be used to add highlight on the artistic decor and unique shapes within the open space."
        )
        prompt = prompt.replace(", ,", ",").replace(" ,", ",").replace("  ", " ")


    else: # SDXL Logic
        furniture_desc = get_furniture_description()

        style_prompt_text = style_prompts.get(style_sel, "")
        if r_type != "None" and style_sel != "None":
             room_desc = f" in a {style_sel} {r_type} with a detailed interior featuring visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity{style_prompt_text}"
        elif r_type != "None":
            room_desc = f" in a {r_type} with a detailed interior featuring visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity"
        else:
            room_desc = " in a detailed indoor setting with visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity"

        lighting_prompt_text = lighting_control.get(lighting_sel, "")
        lighting_desc = f" {lighting_prompt_text}" if lighting_sel != "None" and lighting_prompt_text else " with clear daylight illuminating the scene, highlighting all details"

        fov = fov_sel
        camera = camera_sel
        view_desc = ""

        if fov != "None" and camera != "None":
            fov_text_sdxl = fov_control.get(fov, "")
            camera_text_sdxl = camera_control.get(camera, "")
            if camera_text_sdxl and camera in ["Front view", "Side view"]:
                 view_desc = f"{fov_text_sdxl} {camera_text_sdxl}"
            elif fov_text_sdxl and camera_text_sdxl:
                 view_desc = f"{fov_text_sdxl} from a {camera_text_sdxl}"
            else:
                 view_desc = fov_text_sdxl
        elif fov != "None":
             view_desc = fov_control.get(fov, "")
        elif camera != "None":
             camera_text_sdxl = camera_control.get(camera, "")
             if camera_text_sdxl and "view" not in camera_text_sdxl.lower():
                  view_desc = f"View from a {camera_text_sdxl}"
             else:
                  view_desc = camera_text_sdxl

        if view_desc and furniture_desc:
             if furniture_desc.lower().startswith(("a ", "an ")):
                 article = furniture_desc.split(' ', 1)[0]
                 noun_phrase = furniture_desc.split(' ', 1)[1]
                 prompt_start = f"{view_desc} of {article} {noun_phrase.lower()}"
             else:
                 article = "an" if furniture_desc.lower().startswith(("a", "e", "i", "o", "u")) else "a"
                 prompt_start = f"{view_desc} of {article} {furniture_desc.lower()}"
        elif furniture_desc:
             prompt_start = furniture_desc
        elif view_desc:
             prompt_start = view_desc
        else:
             prompt_start = "A scene"

        centering_desc = f" The {f_subtype} is positioned in the center of the composition." if f_subtype != "None" and furniture_desc else ""

        if prompt_start != "A scene":
            if lighting_desc.strip().startswith("with"):
                lighting_desc = lighting_desc.strip()[4:].strip()
            prompt = f"{prompt_start}{room_desc}, with {lighting_desc}{centering_desc}".replace("..", ".").replace(", ,", ",").replace(" ,", ",").strip()
        else:
            if lighting_desc.strip().startswith("with"):
                 lighting_desc = lighting_desc.strip()[4:].strip()
            if room_desc.strip().startswith("in a"):
                 room_desc = room_desc.strip()[4:].strip()
            prompt = f"{room_desc.capitalize()}, with {lighting_desc}".replace("..", ".").replace(", ,", ",").replace(" ,", ",").strip()

    # Add quality tokens
    if st.session_state.quality_enabled:
        if prompt and not prompt.endswith(" ") and quality_tokens:
            prompt += " "
        prompt += quality_tokens

    return prompt.strip()

def generate_negative_prompt():
    if st.session_state.negative_enabled:
        return negative_prompt_base
    return ""

# --- Обновленная функция предпросмотра (полностью) ---
def generate_composition_preview():
    """Генерирует текстовое описание композиции на английском языке."""
    # <<< ЗАГОЛОВОК И МЕТКИ ПЕРЕВЕДЕНЫ НА АНГЛИЙСКИЙ >>>
    preview = ["--- Scene Composition (Textual Preview) ---"]

    # 1. Обзор (FOV, Camera)
    fov_desc = st.session_state.get('fov', 'None')
    cam_desc = st.session_state.get('camera', 'None')
    view_parts = []
    if fov_desc != 'None': view_parts.append(f"FOV: {fov_desc}")
    if cam_desc != 'None': view_parts.append(f"Angle: {cam_desc}")
    preview.append(f"View: {', '.join(view_parts) if view_parts else 'Default'}") # Переведено

    # 2. Основной объект и поверхность
    f_type = st.session_state.get('furniture_type', 'None')
    f_subtype = st.session_state.get('furniture_subtype', 'None')
    surface_sel = st.session_state.get('surface', 'None')
    surface_text = surface_options.get(surface_sel, '')

    if f_subtype != 'None':
        obj_line = f"Center: {f_subtype}" # Переведено
        if f_type == "Rugs":
             placement = " (on floor)" # Переведено
             if surface_sel != 'None' and 'rug' in surface_text.lower():
                  placement += f" ({surface_text.strip()})"
             obj_line += placement
        elif surface_sel != 'None' and surface_text and surface_text != surface_options["None"]:
             # Убираем начальное "on a " или "on an " для краткости в скобках
             surface_short = surface_text.replace("on a ", "").replace("on an ", "").strip()
             obj_line += f" ({surface_short})"
        preview.append(obj_line)
    else:
         preview.append("Center: (No main object selected)") # Переведено

    # 3. Окружающие элементы
    preview.append("\nSurroundings:") # Переведено
    elements_left = [item for item in surrounding_details_structured["Left Zone"] if st.session_state.get(item, False)]
    elements_wall = [item for item in surrounding_details_structured["Wall / Background"] if st.session_state.get(item, False)]
    elements_right = [item for item in surrounding_details_structured["Right Zone"] if st.session_state.get(item, False)]
    elements_general = [item for item in surrounding_details_structured["Foreground / General"] if st.session_state.get(item, False)]

    has_elements = False
    if elements_left:
        preview.append(f"  - Left Side: {', '.join(elements_left)}") # Переведено
        has_elements = True
    if elements_wall:
        preview.append(f"  - Wall/Background: {', '.join(elements_wall)}") # Переведено
        has_elements = True
    if elements_right:
        preview.append(f"  - Right Side: {', '.join(elements_right)}") # Переведено
        has_elements = True
    if elements_general:
        preview.append(f"  - Foreground/General: {', '.join(elements_general)}") # Переведено
        has_elements = True

    if not has_elements:
         preview.append("  (No extra details selected)") # Переведено


    preview.append("\n--- End Preview ---") # Переведено
    return "\n".join(preview)


# ----- UI Definition -----
with st.sidebar:
    st.title("Settings")

    st.header("Generation Logic")
    prompt_logic_options = ["SDXL", "FLUX"]
    current_logic = st.session_state.prompt_logic
    if current_logic not in prompt_logic_options:
        st.session_state.prompt_logic = "FLUX"
        current_logic = "FLUX"
    st.selectbox(
        "Select Prompt Logic", prompt_logic_options,
        index=prompt_logic_options.index(current_logic),
        key="prompt_logic",
        help="Choose the generation logic: SDXL (current flexible logic) or FLUX (specific structured logic)."
    )

    st.header("Furniture / Main Subject")
    furniture_type_keys = list(furniture_options.keys())
    current_f_type_ui = st.session_state.furniture_type
    if current_f_type_ui not in furniture_type_keys:
        st.session_state.furniture_type = "None"
        current_f_type_ui = "None"
    st.selectbox(
        "Select Type", furniture_type_keys,
        index=furniture_type_keys.index(current_f_type_ui),
        key="furniture_type_select", on_change=update_subtypes
    )

    current_f_type = st.session_state.furniture_type
    if current_f_type != "None":
        subtype_options = furniture_options.get(current_f_type, ["None"])
        current_subtype = st.session_state.get('furniture_subtype', 'None')
        try:
            current_subtype_index = subtype_options.index(current_subtype) if current_subtype in subtype_options else 0
        except ValueError: current_subtype_index = 0
        st.selectbox(
            f"Select {current_f_type} Subtype", subtype_options,
            index=current_subtype_index, key="furniture_subtype"
        )
    else:
         st.selectbox("Select Subtype", ["None"], index=0, key="furniture_subtype", disabled=True)

    st.header("Placement Surface")
    surface_type_keys = list(surface_options.keys())
    current_surface = st.session_state.surface
    if current_surface not in surface_type_keys:
        st.session_state.surface = "None"
        current_surface = "None"
    st.selectbox(
        "Surface Type", surface_type_keys,
        index=surface_type_keys.index(current_surface),
        key="surface", help="Select the type of surface the main object is placed on/near."
    )

    st.header("Environment")
    room_options_actual = room_options
    current_room = st.session_state.room_type
    if current_room not in room_options_actual:
        st.session_state.room_type = "None"
        current_room = "None"
    st.selectbox("Room Type", room_options_actual, index=room_options_actual.index(current_room), key="room_type")

    style_keys = list(style_prompts.keys())
    current_style = st.session_state.style
    if current_style not in style_keys:
        st.session_state.style = "None"
        current_style = "None"
    st.selectbox("Style", style_keys, index=style_keys.index(current_style), key="style")

    st.header("Visuals")
    lighting_keys = list(lighting_control.keys())
    current_lighting = st.session_state.lighting
    if current_lighting not in lighting_keys:
        st.session_state.lighting = "None"
        current_lighting = "None"
    st.selectbox("Lighting", lighting_keys, index=lighting_keys.index(current_lighting), key="lighting")

    fov_keys = list(fov_control.keys())
    current_fov = st.session_state.fov
    if current_fov not in fov_keys:
        st.session_state.fov = "None"
        current_fov = "None"
    st.selectbox("Field of View (FOV)", fov_keys, index=fov_keys.index(current_fov), key="fov")

    camera_keys = list(camera_control.keys())
    current_camera = st.session_state.camera
    if current_camera not in camera_keys:
        st.session_state.camera = "None"
        current_camera = "None"
    st.selectbox("Camera Angle/View", camera_keys, index=camera_keys.index(current_camera), key="camera")

    # Убрали Surrounding Details из сайдбара

    st.header("Prompt Settings")
    st.checkbox("Add Quality Tokens", value=st.session_state.quality_enabled, key="quality_enabled")
    st.checkbox("Enable Negative Prompt", value=st.session_state.negative_enabled, key="negative_enabled")

# ----- Main App Area -----

st.markdown(
    """
    <div class="title-container">
        <h1 style="color: white; margin: 0;">
            <img src="https://res.cloudinary.com/dts5q0ryk/image/upload/v1742992900/Logo_white_a3f4t1.png" width="60" height="60" style="vertical-align: middle; margin-right: 10px;">
            Nfinite Prompt Generator
        </h1>
    </div>
    <style>
        .title-container img {
            vertical-align: middle;
            margin-right: 10px; /* Отступ справа от лого */
        }
        .stApp > header {
             background-color: transparent; /* Попробовать убрать фон заголовка Streamlit по умолчанию */
        }
       /* Стилизация для темной темы */
       body:not([data-theme="light"]) .title-container h1 {
           color: var(--text-color, white) !important;
       }
       /* Стилизация для светлой темы */
       body[data-theme="light"] .title-container h1 {
          color: var(--text-color, black) !important;
       }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- НОВЫЙ UI ДЛЯ ВЫБОРА ОКРУЖАЮЩИХ ДЕТАЛЕЙ -----
st.divider()
with st.expander("Configure Surrounding Details (Optional)", expanded=False):
    current_selected_elements = get_selected_surrounding_elements()
    # Обновляем глобальный state для использования при сохранении/загрузке
    st.session_state.surrounding_elements = current_selected_elements

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Left Zone")
        for item in surrounding_details_structured["Left Zone"]:
            st.checkbox(item, key=item, value=(item in current_selected_elements))
    with col2:
        st.subheader("Wall / Background")
        for item in surrounding_details_structured["Wall / Background"]:
            st.checkbox(item, key=item, value=(item in current_selected_elements))
    with col3:
        st.subheader("Right Zone")
        for item in surrounding_details_structured["Right Zone"]:
            st.checkbox(item, key=item, value=(item in current_selected_elements))

    st.subheader("Foreground / General")
    cols_general = st.columns(3)
    general_items = surrounding_details_structured["Foreground / General"]
    items_per_col = (len(general_items) + 2) // 3
    for i, item in enumerate(general_items):
         with cols_general[i % 3]:
              st.checkbox(item, key=item, value=(item in current_selected_elements))

st.divider()
# ----- КОНЕЦ НОВОГО UI -----


# ----- Генерация промптов и предпросмотра -----
main_prompt_generated = generate_prompt()
negative_prompt_generated = generate_negative_prompt()
composition_preview_text = generate_composition_preview()

st.subheader("Main Prompt")
main_prompt_input = st.text_area("Edit or use the generated prompt:", value=main_prompt_generated, height=150, key="main_prompt_area")
st.session_state.main_prompt = main_prompt_input

# --- Отображение текстового предпросмотра ---
st.subheader("Composition Preview (Textual)") # Заголовок переведен
st.code(composition_preview_text, language=None) # Вывод текста предпросмотра
# --- Конец отображения ---


if st.session_state.negative_enabled:
    st.subheader("Negative Prompt")
    negative_prompt_input = st.text_area("Edit or use the generated negative prompt:", value=negative_prompt_generated, height=100, key="negative_prompt_area")
    st.session_state.negative_prompt = negative_prompt_input
else:
     negative_prompt_input = ""
     st.session_state.negative_prompt = ""

# ----- Configuration Management -----
st.divider()
st.header("Configuration Management")

config_name = st.text_input("Configuration Name", key="config_name_input")

if st.button("Save Configuration", key="save_config_btn"):
    if config_name:
        elements_to_save = get_selected_surrounding_elements()
        current_f_type_save = st.session_state.furniture_type
        current_f_subtype_save = st.session_state.furniture_subtype

        config = {
            "furniture_type": current_f_type_save if current_f_type_save in furniture_options else "None",
            "furniture_subtype": current_f_subtype_save if current_f_type_save != "None" and current_f_subtype_save in furniture_options.get(current_f_type_save, ["None"]) else "None",
            "room_type": st.session_state.room_type if st.session_state.room_type in room_options else "None",
            "style": st.session_state.style if st.session_state.style in style_prompts else "None",
            "lighting": st.session_state.lighting if st.session_state.lighting in lighting_control else "None",
            "fov": st.session_state.fov if st.session_state.fov in fov_control else "None",
            "camera": st.session_state.camera if st.session_state.camera in camera_control else "None",
            "surface": st.session_state.surface if st.session_state.surface in surface_options else "None",
            "surrounding_elements": elements_to_save,
            "quality_enabled": st.session_state.quality_enabled,
            "negative_enabled": st.session_state.negative_enabled,
            "prompt_logic": st.session_state.prompt_logic if st.session_state.prompt_logic in ["SDXL", "FLUX"] else "FLUX",
            "model_type": st.session_state.model_type,
            "main_prompt": main_prompt_input,
            "negative_prompt": negative_prompt_input if st.session_state.negative_enabled else ""
        }
        st.session_state.saved_configs[config_name] = config
        st.success(f"Configuration '{config_name}' saved!")
        st.rerun()
    else:
        st.warning("Please enter a name for the configuration.")

if st.session_state.saved_configs:
    config_options = [""] + list(st.session_state.saved_configs.keys())
    current_selection_index = 0
    if "config_select" in st.session_state and st.session_state.config_select in config_options:
        try: current_selection_index = config_options.index(st.session_state.config_select)
        except ValueError: current_selection_index = 0

    config_to_load = st.selectbox(
        "Load Configuration", options=config_options,
        index=current_selection_index, key="config_select"
    )
    if config_to_load:
        col1_load, col2_delete = st.columns(2)
        with col1_load:
            if st.button("Load Selected Configuration", key="load_config_btn"):
                config = st.session_state.saved_configs[config_to_load]
                # Load with validation against current options
                st.session_state.furniture_type = config.get("furniture_type", "None") if config.get("furniture_type", "None") in furniture_options else "None"
                st.session_state.furniture_subtype = config.get("furniture_subtype", "None") if st.session_state.furniture_type != "None" and config.get("furniture_subtype", "None") in furniture_options.get(st.session_state.furniture_type, ["None"]) else "None"
                st.session_state.room_type = config.get("room_type", "None") if config.get("room_type", "None") in room_options else "None"
                st.session_state.style = config.get("style", "None") if config.get("style", "None") in style_prompts else "None"
                st.session_state.lighting = config.get("lighting", "None") if config.get("lighting", "None") in lighting_control else "None"
                st.session_state.fov = config.get("fov", "None") if config.get("fov", "None") in fov_control else "None"
                st.session_state.camera = config.get("camera", "None") if config.get("camera", "None") in camera_control else "None"
                st.session_state.surface = config.get("surface", "None") if config.get("surface", "None") in surface_options else "None"

                loaded_elements = config.get("surrounding_elements", [])
                st.session_state.surrounding_elements = [el for el in loaded_elements if el in all_surrounding_options]
                # Устанавливаем состояние чекбоксов в соответствии с загруженным списком
                for item in all_surrounding_options:
                    st.session_state[item] = (item in st.session_state.surrounding_elements)

                st.session_state.quality_enabled = config.get("quality_enabled", True)
                st.session_state.negative_enabled = config.get("negative_enabled", True)
                st.session_state.prompt_logic = config.get("prompt_logic", "FLUX") if config.get("prompt_logic", "FLUX") in ["SDXL", "FLUX"] else "FLUX"
                st.session_state.model_type = config.get("model_type", "Fooocus")
                st.session_state.main_prompt = config.get("main_prompt", "")
                st.session_state.negative_prompt = config.get("negative_prompt", negative_prompt_base if st.session_state.negative_enabled else "")

                st.session_state.config_select = ""
                st.rerun()
        with col2_delete:
            if st.button("Delete Selected Configuration", key="delete_config_btn", type="secondary"):
                 if config_to_load in st.session_state.saved_configs:
                     del st.session_state.saved_configs[config_to_load]
                     st.success(f"Configuration '{config_to_load}' deleted!")
                     st.session_state.config_select = ""
                     st.rerun()
                 else: st.warning("Please select a valid configuration to delete.")

# ----- Export -----
st.divider()
st.header("Export")
export_col1, export_col2 = st.columns(2)
current_main_prompt_for_export = main_prompt_input
current_neg_prompt_for_export = negative_prompt_input if st.session_state.negative_enabled else ""
with export_col1:
    json_str_export = json.dumps({
        "main_prompt": current_main_prompt_for_export,
        "negative_prompt": current_neg_prompt_for_export
    }, indent=4)
    st.download_button(
        label="Export Current Prompts to JSON", data=json_str_export,
        file_name="current_prompts.json", mime="application/json", key="export_json_dl_btn"
    )
with export_col2:
    txt_content_export = f"Main Prompt:\n{current_main_prompt_for_export}\n\n"
    if st.session_state.negative_enabled and current_neg_prompt_for_export:
        txt_content_export += f"Negative Prompt:\n{current_neg_prompt_for_export}"
    else: txt_content_export += "Negative Prompt: (disabled or empty)"
    st.download_button(
        label="Export Current Prompts to TXT", data=txt_content_export.encode('utf-8'),
        file_name="current_prompts.txt", mime="text/plain", key="export_txt_dl_btn"
    )