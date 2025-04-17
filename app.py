import streamlit as st
import json
import random

# Устанавливаем конфигурацию страницы
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Nfinite Prompt Generator")

# --- Опции для поверхностей ---
surface_options = {
    "None": "on an appropriate surface",
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

# --- Структурированные опции для окружающих элементов ---
surrounding_details_structured = {
    "Left Zone": [
        "Large floor-to-ceiling window",
        "Visible window with a sheer curtain",
        "Visible window with a heavy drapes",
        "Small vase with flowers",
        "Potted plant",
        "Hanging plant",
        "Floor lamp",
        "Side table",
        "Bedside table",
        "Coffee table",
        "Stack of books",
        "Wardrobe",
        "Sideboard",
        "Decor set",
        "Magazines on nearby table",
        "Laptop on desk nearby",
        "Decorative pillows on a seat",
        "Throw blanket draped over furniture"
    ],
    "Right Zone": [
        "Large floor-to-ceiling window",
        "Visible window with a sheer curtain",
        "Visible window with a heavy drapes",
        "Small vase with flowers",
        "Potted plant",
        "Hanging plant",
        "Floor lamp",
        "Side table",
        "Bedside table",
        "Coffee table",
        "Stack of books",
        "Wardrobe",
        "Sideboard",
        "Decor set",
        "Magazines on nearby table",
        "Laptop on desk nearby",
        "Decorative pillows on a seat",
        "Throw blanket draped over furniture"
    ],
    "Wall / Background": [
        "Framed neutral floral artwork on a wall",
        "Framed neutral abstract artwork on a wall",
        "Set of 2-3 Framed neutral floral artwork on a wall",
        "Set of 2-3 Framed neutral abstract artwork on a wall",
        "Multiple pictures on a wall",
        "Large floor-to-ceiling window",
        "Visible window with a sheer curtain",
        "Visible window with a heavy drapes",
        "Wall mirror on a wall"
    ],
    "Foreground / General": [
        "Coffee table with vase of flowers (foreground)",
        "Throw blanket draped over furniture",
        "Beige curtains framing a scene",
        "Fireplace",
        "Modern Electric Fireplace",
        "Bookshelves",
        "Wall shelves with decor",
        "Stack of books on a floor",
        "Decorative pillows on a floor"
    ]
}

# Создаём список всех элементов с уникальными ключами (секция_элемент)
all_surrounding_options = []
for section, items in surrounding_details_structured.items():
    for item in items:
        unique_key = f"{section}_{item}"
        all_surrounding_options.append((unique_key, item))

# --- Промпты для стилей ---
style_prompts = {
    "None": "",
    "Bohemian": "bohemian style with eclectic decor, vibrant colors, mixed patterns",
    "Casual": "casual style with comfortable furniture, soft textures, neutral colors",
    "Classic": "classic style with luxurious fabrics, symmetrical layouts, rich colors",
    "Coastal": "coastal style with light colors, nautical elements, wicker furniture",
    "Contemporary": "contemporary style with bold colors, unique shapes, mixed materials",
    "Cottage": "cottage style with floral patterns, pastel colors, vintage furniture",
    "Countryside": "countryside style with rustic textures, earthy tones, wooden furniture",
    "Craftsman": "craftsman style with handcrafted furniture, natural wood, earthy tones",
    "Farmhouse": "farmhouse style with reclaimed wood, vintage elements, neutral colors",
    "French Inspired": "French-inspired style with ornate details, pastel colors, vintage furniture",
    "Industrial": "industrial style with exposed brick, metal accents, raw materials",
    "Midcentury Modern": "midcentury modern style with clean lines, organic shapes, retro vibe",
    "Minimalist": "minimalist style with clean lines, neutral colors, clutter-free spaces",
    "Modern": "modern style with sleek lines, neutral colors, metal accents",
    "Rustic": "rustic style with rough textures, earthy tones, wooden beams",
    "Scandinavian": "Scandinavian style with light colors, natural wood, cozy textiles",
    "Southwestern": "southwestern style with earthy colors, tribal patterns, terracotta",
    "Spanish": "Spanish style with warm colors, wrought iron, textured walls",
    "Traditional": "traditional style with classic furniture, rich colors, elegant fabrics",
    "Transitional": "transitional style with neutral colors, comfortable furniture, clean lines",
    "Tropical": "tropical style with vibrant colors, exotic plants, rattan furniture",
    "Vintage": "vintage style with antique furniture, retro patterns, nostalgic decor"
}

# --- Ключевые слова для стилей ---
style_keywords = {
    "None": [],
    "Bohemian": ["eclectic", "vibrant", "patterned", "textured", "layered", "global"],
    "Casual": ["cozy", "relaxed", "soft", "neutral", "inviting", "lived-in"],
    "Classic": ["elegant", "ornate", "timeless", "luxurious", "symmetrical", "refined"],
    "Coastal": ["airy", "nautical", "breezy", "light", "blue-toned", "natural"],
    "Contemporary": ["bold", "sleek", "innovative", "minimalist", "artistic", "urban"],
    "Cottage": ["charming", "floral", "vintage", "cozy", "pastel", "rustic"],
    "Countryside": ["earthy", "rustic", "warm", "wooden", "pastoral", "sturdy"],
    "Craftsman": ["handcrafted", "natural", "warm", "functional", "earthy", "detailed"],
    "Farmhouse": ["rustic", "reclaimed", "neutral", "cozy", "vintage", "simple"],
    "French Inspired": ["ornate", "delicate", "pastel", "romantic", "vintage", "gilded"],
    "Industrial": ["raw", "exposed", "metallic", "urban", "rugged", "minimalist"],
    "Midcentury Modern": ["retro", "organic", "clean", "geometric", "vibrant", "functional"],
    "Minimalist": ["sleek", "simple", "neutral", "uncluttered", "modern", "airy"],
    "Modern": ["polished", "sleek", "neutral", "streamlined", "metallic", "bold"],
    "Rustic": ["rugged", "natural", "earthy", "textured", "warm", "weathered"],
    "Scandinavian": ["light", "cozy", "functional", "neutral", "wooden", "minimalist"],
    "Southwestern": ["earthy", "tribal", "warm", "textured", "terracotta", "bold"],
    "Spanish": ["warm", "textured", "ornate", "earthy", "tiled", "vibrant"],
    "Traditional": ["classic", "rich", "elegant", "detailed", "formal", "warm"],
    "Transitional": ["balanced", "neutral", "clean", "comfortable", "modern", "timeless"],
    "Tropical": ["lush", "vibrant", "exotic", "green", "airy", "natural"],
    "Vintage": ["nostalgic", "antique", "retro", "ornate", "textured", "classic"]
}

# --- Цветовые палитры ---
color_palettes = {
    "None": "",
    "Pastel color tones": "Pastel color tones including light pink, baby blue, mint green, lavender, and pale yellow",
    "Neutral Palette": "Neutral Palette including tones like beige, gray, taupe, and cream, creating a timeless and elegant look",
    "Analogous Palette": "Analogous Palette combining colors next to each other on the color wheel like blue, turquoise, green, for a smooth transition",
    "Cool Palette": "Cool Palette centered on blues, greens, and purples for calmness and relaxation",
    "Earthy Palette": "Earthy Palette inspired by natural tones like terracotta, olive green, and sandy browns",
    "Muted Palette": "Muted Palette with subdued tones that maintain color depth without being overpowering, such as dusty pink, sage green, slate blue"
}

# Описания цветовых палитр для UI
color_palette_descriptions = {
    "None": "No specific color palette applied.",
    "Pastel color tones": "Soft and light colors including light pink, baby blue, mint green, lavender, and pale yellow, creating a gentle and calming atmosphere.",
    "Neutral Palette": "Timeless and elegant tones such as beige, gray, taupe, and cream, perfect for a sophisticated and understated look.",
    "Analogous Palette": "Harmonious colors that are adjacent on the color wheel, such as blue, turquoise, and green, ensuring a smooth and cohesive transition.",
    "Cool Palette": "Calming and relaxing hues centered on blues, greens, and purples, ideal for creating a serene environment.",
    "Earthy Palette": "Natural tones inspired by the earth, including terracotta, olive green, and sandy browns, for a warm and grounded feel.",
    "Muted Palette": "Subdued tones with depth but not overpowering, such as dusty pink, sage green, and slate blue, for a soft and balanced aesthetic."
}

# --- Освещение ---
lighting_control = {
    "None": "",
    "Natural Light": "natural light",
    "Soft Ambient Light": "soft ambient light",
    "Bright Studio Light": "bright studio light",
    "Dramatic Cinematic Light": "dramatic cinematic light",
    "Warm Evening Light": "warm evening light",
    "Overcast Daylight": "overcast daylight",
    "Golden Hour Light": "golden hour light",
    "Candlelight": "candlelight"
}

# --- FOV ---
fov_control = {
    "None": "",
    "Close up": "Close up",
    "Zoomed-in partially visible": "Zoomed-in partially visible",
    "Midshot": "Midshot",
    "Full interior": "Full interior",
    "Wide angle": "Wide angle"
}

# --- Камера ---
camera_control = {
    "None": "",
    "Front view": "front view",
    "Side view": "side view",
    "High-angle view": "high-angle view",
    "Low-angle view": "low-angle view",
    "Dutch angle view": "Dutch angle view",
    "Top-down view": "top-down view",
    "45 degree angle left side": "oblique view of 45 degree angle left side",
    "45 degree angle right side": "oblique view of 45 degree angle right side"
}

# --- Типы мебели ---
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

# --- Типы комнат ---
room_options = [
    "None", "Living Room", "Bedroom", "Dining Room", "Kitchen", "Home Office",
    "Bathroom", "Entryway", "Kids Room", "Outdoor Patio", "Balcony",
    "Studio Apartment", "Hallway", "Outdoor lounge zone"
]

# --- Токены качества ---
quality_tokens = "Best quality, photorealistic, high resolution, sharp focus, detailed texture, professional photography"

# --- Негативные токены ---
negative_prompt_base = "Worst quality, low quality, blurry, unfocused, text, words, letters, signature, watermark, username, artist name, deformed, mutated, ugly, distorted, poorly drawn, bad anatomy, extra limbs, missing limbs"

# --- Инициализация Session State ---
default_values = {
    "furniture_type": "None", "furniture_subtype": "None", "room_type": "None",
    "style": "None", "lighting": "None", "fov": "None", "camera": "None",
    "surface": "None", "surrounding_elements": [], "main_prompt": "",
    "negative_prompt": negative_prompt_base, "quality_enabled": True,
    "negative_enabled": True, "saved_configs": {}, "model_type": "Fooocus",
    "prompt_logic": "Nfinite", "color_palette": "None"
}
for key, default_value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = default_value

# Инициализация уникальных ключей для всех элементов окружения
for unique_key, _ in all_surrounding_options:
    if unique_key not in st.session_state:
        st.session_state[unique_key] = False

# --- Функции ---
def get_hidden_keyword(fov):
    """Выбирает скрытое ключевое слово на основе FOV."""
    if fov in ["Close up", "Zoomed-in partially visible"]:
        return "TETHERED_LR_6723"
    return "DSC_3921.NEF"

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
        return f"a {subtype.lower()}"
    elif furniture_type != "None":
        return f"a piece of {furniture_type.lower()} furniture"
    return ""

def get_selected_surrounding_elements():
    """Собирает список описаний для выбранных чекбоксов деталей."""
    selected = []
    for unique_key, item in all_surrounding_options:
        if st.session_state.get(unique_key, False):
            selected.append(item)
    return selected

def add_random_surrounding_element():
    """Добавляет случайный элемент окружения, избегая дублирования и несбалансированной композиции."""
    current_elements = get_selected_surrounding_elements()
    available_sections = list(surrounding_details_structured.keys())
    available_items = []

    # Собираем доступные элементы, исключая уже выбранные
    for section in available_sections:
        section_items = [item for item in surrounding_details_structured[section] if item not in current_elements]
        if section_items:
            available_items.extend([(section, item) for item in section_items])

    if not available_items:
        st.warning("All possible surrounding elements have been selected!")
        return

    # Исключаем дублирование между Left Zone и Right Zone
    left_items = [item for section, item in available_items if section == "Left Zone"]
    right_items = [item for section, item in available_items if section == "Right Zone"]
    common_items = set(left_items) & set(right_items)
    for item in common_items:
        if item in left_items and item in right_items:
            available_items = [(s, i) for s, i in available_items if not (i == item and s in ["Left Zone", "Right Zone"])]

    if not available_items:
        st.warning("No unique surrounding elements available to add!")
        return

    # Выбираем случайный элемент
    selected_section, selected_item = random.choice(available_items)
    unique_key = f"{selected_section}_{selected_item}"
    st.session_state[unique_key] = True
    st.session_state.surrounding_elements = get_selected_surrounding_elements()
    # Удаляем вызов st.rerun(), так как Streamlit автоматически перерендерит UI при изменении session_state

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
    color_palette_sel = st.session_state.get('color_palette', 'None')
    elements_sel = get_selected_surrounding_elements()

    if logic == "Nfinite":
        # Проверка на выбор мебели
        if f_type == "None" or f_subtype == "None":
            if f_type != "Rugs":
                return "Please select a Furniture Type and Subtype to use the Nfinite logic (unless type is Rugs)."
            elif f_type == "Rugs" and f_subtype == "None":
                return "Please select a specific Rug subtype for Nfinite logic."

        # Получение скрытого ключевого слова
        hidden_keyword = get_hidden_keyword(fov_sel)

        # FOV
        fov_text = "Photo" if fov_sel == "None" else fov_control[fov_sel]
        if "shot" in fov_text.lower():
            fov_text = fov_text.replace(" shot", "").strip()

        # Описание мебели
        furniture_desc = get_furniture_description()
        if not furniture_desc:
            furniture_desc = "a scene"

        # Центрирование
        placement = "positioned in the center of composition centrally"
        if f_type == "Rugs":
            placement = "laid out on the floor"

        # Поверхность
        surface_desc = surface_options.get(surface_sel, "")
        if f_type == "Rugs" and surface_sel != "None" and "rug" in surface_desc.lower():
            surface_desc = f", {surface_desc.replace(' covering the floor', '')}"
        elif surface_desc and surface_desc != surface_options["None"]:
            surface_desc = f" {surface_desc}"
        else:
            surface_desc = ""

        # Стиль комнаты
        style_desc = style_prompts.get(style_sel, "")
        keywords = style_keywords.get(style_sel, [])
        room_desc = r_type.lower() if r_type != "None" else "room"
        if style_desc and keywords:
            room_desc = f"{style_desc} {room_desc}, {', '.join(keywords)}"
        elif style_desc:
            room_desc = f"{style_desc} {room_desc}"
        else:
            room_desc = f"{room_desc}"

        # Добавление цветовой палитры
        color_palette_desc = color_palettes.get(color_palette_sel, "")
        if color_palette_desc:
            room_desc = f"{room_desc}, {color_palette_desc}"

        # Освещение
        lighting_desc = lighting_control.get(lighting_sel, "natural light")

        # Камера
        camera_desc = camera_control.get(camera_sel, "")
        if camera_desc:
            camera_desc = f"{camera_desc}"

        # Окружающие элементы
        elements_desc = ""
        if elements_sel:
            elements_string = ", ".join(elements_sel)
            elements_desc = f" with {elements_string}"

            # Добавление отражения в зеркале
            if "Wall mirror on a wall" in elements_sel:
                if "Potted plant" in elements_sel:
                    elements_desc += ", wall mirror reflecting a potted plant"
                else:
                    elements_desc += ", wall mirror reflecting a garden view in window"

        # Формирование промпта
        prompt = (
            f"{hidden_keyword}, {camera_desc}, {fov_text} of {furniture_desc} {placement}{surface_desc}, "
            f"{room_desc}, {lighting_desc}{elements_desc}, f/22, 1/160s"
        )

        # Добавление токенов качества
        if st.session_state.quality_enabled:
            prompt += f", {quality_tokens}"

        # Очистка лишних пробелов и запятых
        prompt = prompt.replace(", ,", ",").replace(" ,", ",").replace("  ", " ").strip()

        # Удаление лишней запятой перед качеством, если нет элементов
        if prompt.endswith(","):
            prompt = prompt[:-1]

        return prompt

    elif logic == "FLUX":
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
            angle_text = camera_control[camera_sel].replace("oblique view of ", "").strip().lower()
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
        color_palette_desc = color_palettes.get(color_palette_sel, "")
        if color_palette_desc:
            color_palette_desc = f" using {color_palette_desc.lower()}"
        atmosphere_desc = f"in {style_desc} {room_desc} with bright airy atmosphere{color_palette_desc}"

        lighting_condition_desc = "under clear diffuse lighting conditions"
        if lighting_sel != "None":
            if lighting_sel in lighting_control and lighting_control[lighting_sel]:
                lighting_condition_desc = f"under {lighting_sel.lower()} conditions"
            elif lighting_sel != "None":
                lighting_condition_desc = f"with {lighting_sel.lower()} lighting"

        prompt = (
            f"{fov_text} of a {subject_desc_start} {placement}{surface_desc}, {atmosphere_desc}, "
            f"captured with a Nikon Z7 II camera and a 24mm f/1.2L lens. "
            f"Set the aperture to f/22, ensuring {details_desc} is in sharp focus. "
            f"The composition should {camera_angle_desc}, with the {subject}. "
            f"Adjust the shutter speed to 1/160 to maintain crisp clarity {lighting_condition_desc}. "
            f"Set the white balance to 6500k to ensure a neutral white color pallete. "
            f"Soft shadows and subtle reflections on mixed materials can be used to add highlight on the artistic decor and unique shapes within the open space."
        )
        prompt = prompt.replace(", ,", ",").replace(" ,", ",").replace("  ", " ")

        if st.session_state.quality_enabled:
            if prompt and not prompt.endswith(" ") and quality_tokens:
                prompt += " "
            prompt += quality_tokens

        return prompt.strip()

    else:  # SDXL Logic
        furniture_desc = get_furniture_description()

        style_prompt_text = style_prompts.get(style_sel, "")
        color_palette_desc = color_palettes.get(color_palette_sel, "")
        if color_palette_desc:
            color_palette_desc = f" using {color_palette_desc.lower()}"
        if r_type != "None" and style_sel != "None":
            room_desc = f" in a {style_sel} {r_type} with a detailed interior featuring visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity{style_prompt_text}{color_palette_desc}"
        elif r_type != "None":
            room_desc = f" in a {r_type} with a detailed interior featuring visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity{color_palette_desc}"
        else:
            room_desc = f" in a detailed indoor setting with visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity{color_palette_desc}"

        lighting_prompt_text = lighting_control.get(lighting_sel, "")
        lighting_desc = f" {lighting_prompt_text}" if lighting_sel != "None" and lighting_prompt_text else " with clear daylight illuminating the scene, highlighting all details"

        fov = fov_sel
        camera = camera_sel
        view_desc = ""

        if fov != "None" and camera != "None":
            fov_text_sdxl = fov_control.get(fov, "")
            camera_text_sdxl = camera_control.get(camera, "")
            if camera_text_sdxl:
                camera_text_sdxl = camera_text_sdxl.replace("oblique view of ", "")
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
            if camera_text_sdxl:
                camera_text_sdxl = camera_text_sdxl.replace("oblique view of ", "")
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

        if st.session_state.quality_enabled:
            if prompt and not prompt.endswith(" ") and quality_tokens:
                prompt += " "
            prompt += quality_tokens

        return prompt.strip()

def generate_negative_prompt():
    if st.session_state.negative_enabled:
        return negative_prompt_base
    return ""

def generate_composition_preview():
    preview = ["--- Scene Composition (Textual Preview) ---"]
    fov_desc = st.session_state.get('fov', 'None')
    cam_desc = st.session_state.get('camera', 'None')
    view_parts = []
    if fov_desc != 'None': view_parts.append(f"FOV: {fov_desc}")
    if cam_desc != 'None': view_parts.append(f"Angle: {cam_desc}")
    preview.append(f"View: {', '.join(view_parts) if view_parts else 'Default'}")

    f_type = st.session_state.get('furniture_type', 'None')
    f_subtype = st.session_state.get('furniture_subtype', 'None')
    surface_sel = st.session_state.get('surface', 'None')
    surface_text = surface_options.get(surface_sel, '')

    if f_subtype != 'None':
        obj_line = f"Center: {f_subtype}"
        if f_type == "Rugs":
            placement = " (on floor)"
            if surface_sel != 'None' and 'rug' in surface_text.lower():
                placement += f" ({surface_text.strip()})"
            obj_line += placement
        elif surface_sel != 'None' and surface_text and surface_text != surface_options["None"]:
            surface_short = surface_text.replace("on a ", "").replace("on an ", "").strip()
            obj_line += f" ({surface_short})"
        preview.append(obj_line)
    else:
        preview.append("Center: (No main object selected)")

    preview.append("\nSurroundings:")
    elements_left = [item for unique_key, item in all_surrounding_options if unique_key.startswith("Left Zone_") and st.session_state.get(unique_key, False)]
    elements_wall = [item for unique_key, item in all_surrounding_options if unique_key.startswith("Wall / Background_") and st.session_state.get(unique_key, False)]
    elements_right = [item for unique_key, item in all_surrounding_options if unique_key.startswith("Right Zone_") and st.session_state.get(unique_key, False)]
    elements_general = [item for unique_key, item in all_surrounding_options if unique_key.startswith("Foreground / General_") and st.session_state.get(unique_key, False)]

    has_elements = False
    if elements_left:
        preview.append(f"  - Left Side: {', '.join(elements_left)}")
        has_elements = True
    if elements_wall:
        preview.append(f"  - Wall/Background: {', '.join(elements_wall)}")
        has_elements = True
    if elements_right:
        preview.append(f"  - Right Side: {', '.join(elements_right)}")
        has_elements = True
    if elements_general:
        preview.append(f"  - Foreground/General: {', '.join(elements_general)}")
        has_elements = True

    if not has_elements:
        preview.append("  (No extra details selected)")

    preview.append("\n--- End Preview ---")
    return "\n".join(preview)

# --- UI ---
with st.sidebar:
    st.title("Settings")

    st.header("Generation Logic")
    prompt_logic_options = ["SDXL", "FLUX", "Nfinite"]
    current_logic = st.session_state.prompt_logic
    if current_logic not in prompt_logic_options:
        st.session_state.prompt_logic = "Nfinite"
        current_logic = "Nfinite"
    st.selectbox(
        "Select Prompt Logic", prompt_logic_options,
        index=prompt_logic_options.index(current_logic),
        key="prompt_logic",
        help="Choose the generation logic: SDXL (flexible), FLUX (structured), Nfinite (optimized for furniture and interiors)."
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

    st.header("Color Palette")
    color_palette_keys = list(color_palettes.keys())
    current_color_palette = st.session_state.color_palette
    if current_color_palette not in color_palette_keys:
        st.session_state.color_palette = "None"
        current_color_palette = "None"
    st.selectbox(
        "Select Color Palette",
        color_palette_keys,
        index=color_palette_keys.index(current_color_palette),
        key="color_palette",
        help=color_palette_descriptions.get(current_color_palette, "Select a color palette to define the scene's color scheme.")
    )

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

    st.header("Prompt Settings")
    st.checkbox("Add Quality Tokens", value=st.session_state.quality_enabled, key="quality_enabled")
    st.checkbox("Enable Negative Prompt", value=st.session_state.negative_enabled, key="negative_enabled")

# --- Основная область приложения ---
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
            margin-right: 10px;
        }
        .stApp > header {
            background-color: transparent;
        }
        body:not([data-theme="light"]) .title-container h1 {
            color: var(--text-color, white) !important;
        }
        body[data-theme="light"] .title-container h1 {
            color: var(--text-color, black) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.divider()
with st.expander("Configure Surrounding Details (Optional)", expanded=False):
    current_selected_elements = get_selected_surrounding_elements()
    st.session_state.surrounding_elements = current_selected_elements

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Left Zone")
        for item in surrounding_details_structured["Left Zone"]:
            unique_key = f"Left Zone_{item}"
            st.checkbox(item, key=unique_key, value=(item in current_selected_elements))
    with col2:
        st.subheader("Wall / Background")
        for item in surrounding_details_structured["Wall / Background"]:
            unique_key = f"Wall / Background_{item}"
            st.checkbox(item, key=unique_key, value=(item in current_selected_elements))
    with col3:
        st.subheader("Right Zone")
        for item in surrounding_details_structured["Right Zone"]:
            unique_key = f"Right Zone_{item}"
            st.checkbox(item, key=unique_key, value=(item in current_selected_elements))

    st.subheader("Foreground / General")
    cols_general = st.columns(3)
    general_items = surrounding_details_structured["Foreground / General"]
    items_per_col = (len(general_items) + 2) // 3
    for i, item in enumerate(general_items):
        with cols_general[i % 3]:
            unique_key = f"Foreground / General_{item}"
            st.checkbox(item, key=unique_key, value=(item in current_selected_elements))

    st.button("Add Random Surrounding Element", on_click=add_random_surrounding_element)

st.divider()

main_prompt_generated = generate_prompt()
negative_prompt_generated = generate_negative_prompt()
composition_preview_text = generate_composition_preview()

st.subheader("Main Prompt")
main_prompt_input = st.text_area("Edit or use the generated prompt:", value=main_prompt_generated, height=150, key="main_prompt_area")
st.session_state.main_prompt = main_prompt_input

st.subheader("Composition Preview (Textual)")
st.code(composition_preview_text, language=None)

if st.session_state.negative_enabled:
    st.subheader("Negative Prompt")
    negative_prompt_input = st.text_area("Edit or use the generated negative prompt:", value=negative_prompt_generated, height=100, key="negative_prompt_area")
    st.session_state.negative_prompt = negative_prompt_input
else:
    negative_prompt_input = ""
    st.session_state.negative_prompt = ""

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
            "color_palette": st.session_state.color_palette if st.session_state.color_palette in color_palettes else "None",
            "surrounding_elements": elements_to_save,
            "quality_enabled": st.session_state.quality_enabled,
            "negative_enabled": st.session_state.negative_enabled,
            "prompt_logic": st.session_state.prompt_logic if st.session_state.prompt_logic in ["SDXL", "FLUX", "Nfinite"] else "Nfinite",
            "model_type": st.session_state.model_type,
            "main_prompt": main_prompt_input,
            "negative_prompt": negative_prompt_input if st.session_state.negative_enabled else ""
        }
        st.session_state.saved_configs[config_name] = config
        st.success(f"Configuration '{config_name}' saved!")
        # st.rerun()  # Удаляем, так как не требуется
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
                st.session_state.furniture_type = config.get("furniture_type", "None") if config.get("furniture_type", "None") in furniture_options else "None"
                st.session_state.furniture_subtype = config.get("furniture_subtype", "None") if st.session_state.furniture_type != "None" and config.get("furniture_subtype", "None") in furniture_options.get(st.session_state.furniture_type, ["None"]) else "None"
                st.session_state.room_type = config.get("room_type", "None") if config.get("room_type", "None") in room_options else "None"
                st.session_state.style = config.get("style", "None") if config.get("style", "None") in style_prompts else "None"
                st.session_state.lighting = config.get("lighting", "None") if config.get("lighting", "None") in lighting_control else "None"
                st.session_state.fov = config.get("fov", "None") if config.get("fov", "None") in fov_control else "None"
                st.session_state.camera = config.get("camera", "None") if config.get("camera", "None") in camera_control else "None"
                st.session_state.surface = config.get("surface", "None") if config.get("surface", "None") in surface_options else "None"
                st.session_state.color_palette = config.get("color_palette", "None") if config.get("color_palette", "None") in color_palettes else "None"

                loaded_elements = config.get("surrounding_elements", [])
                st.session_state.surrounding_elements = [el for el in loaded_elements if any(el == item for _, item in all_surrounding_options)]
                for unique_key, item in all_surrounding_options:
                    st.session_state[unique_key] = (item in st.session_state.surrounding_elements)

                st.session_state.quality_enabled = config.get("quality_enabled", True)
                st.session_state.negative_enabled = config.get("negative_enabled", True)
                st.session_state.prompt_logic = config.get("prompt_logic", "Nfinite") if config.get("prompt_logic", "Nfinite") in ["SDXL", "FLUX", "Nfinite"] else "Nfinite"
                st.session_state.model_type = config.get("model_type", "Fooocus")
                st.session_state.main_prompt = config.get("main_prompt", "")
                st.session_state.negative_prompt = config.get("negative_prompt", negative_prompt_base if st.session_state.negative_enabled else "")

                st.session_state.config_select = ""
                # st.rerun()  # Удаляем, так как не требуется
        with col2_delete:
            if st.button("Delete Selected Configuration", key="delete_config_btn", type="secondary"):
                if config_to_load in st.session_state.saved_configs:
                    del st.session_state.saved_configs[config_to_load]
                    st.success(f"Configuration '{config_to_load}' deleted!")
                    st.session_state.config_select = ""
                    # st.rerun()  # Удаляем, так как не требуется
                else: st.warning("Please select a valid configuration to delete.")

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