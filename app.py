# -*- coding: utf-8 -*-
import streamlit as st
import json
import random

# --- Базовые настройки и данные ---
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Nfinite Prompt Generator V2.4")

# --- Логотип и Заголовок ---
st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <img src="https://res.cloudinary.com/dts5q0ryk/image/upload/v1742992900/Logo_white_a3f4t1.png" width="60" height="60" style="vertical-align: middle; margin-right: 10px;">
        <h1 style="margin: 0;">Nfinite Prompt Generator V2.4</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --- Словари Опций ---
surface_options_indoor = { "None": "on an appropriate surface", "Light Oak Parquet": "on a light oak parquet floor", "Dark Walnut Parquet (Herringbone)": "on a dark walnut herringbone parquet floor", "Aged Pine Floorboards": "on aged pine floorboards", "Grey Laminate": "on a grey laminate floor", "Natural Wood Laminate": "on a natural wood laminate floor", "Neutral Carpet over Wooden Floor": "on a soft, neutral-toned carpet covering the wooden floor", "White Marble Tile": "on white marble floor tiles", "Black Slate Tile": "on black slate floor tiles", "Terracotta Tile": "on terracotta floor tiles", "Polished Concrete": "on a polished concrete floor", "Matte Concrete": "on a matte concrete floor", "Large Area Wooden Floor": "on a large area wooden floor", "Large Area Stone Floor": "on a large area stone floor", "Large Area Tiled Floor": "on a large area tiled floor" }
surface_options_outdoor = { "None": "on an appropriate surface", "Grass Lawn": "on a green grass lawn", "Wooden Deck": "on a wooden deck", "Stone Patio": "on a stone patio", "Gravel Path": "on a gravel path", "Concrete Slab": "on a concrete slab", "Sandy Ground": "on sandy ground", "Artificial Turf": "on artificial turf" }
surface_options_tabletop = { "None": "on an appropriate surface", "Linen Tablecloth": "on a linen tablecloth", "Cotton Table Runner": "on a cotton table runner", "Textured Woven Placemats": "on textured woven placemats", "Velvet Table Cover": "on a velvet table cover", "Embroidered Napkins": "on a surface with embroidered napkins", "Pastel Cotton Tablecloth": "on a pastel-colored cotton tablecloth", "Gauzy Linen Fabric": "on gauzy linen fabric", "Patterned Textile Placemat": "on a patterned textile placemat", "Rustic Burlap Runner": "on a rustic burlap runner", "Sheer Organza Overlay": "on a sheer organza overlay" }
tabletop_surface_categories = ["Dishes", "Food", "Vase"]
placement_options_indoor = { "None": "", "Coffee Table": "on a coffee table", "Side Table": "on a side table", "Console Table": "on a console table", "Dining Table": "on a dining table", "Kitchen Counter": "on a kitchen counter", "Shelf": "on a shelf", "Bed": "on the bed", "Sofa": "on the sofa", "Floor": "on the floor", "Mantelpiece": "on the mantelpiece", "Bookshelf": "on a bookshelf", "Desk": "on a desk", "Nightstand": "on a nightstand", "Windowsill": "on the windowsill" }
surrounding_details_structured = { "Left Zone": { "Tall Houseplant": "a tall houseplant in a pot to the left", "Floor Lamp (Left)": "a floor lamp illuminating the area to the left", "Armchair (Left)": "an armchair positioned to the left", "Side Table (Left)": "a small side table to the left", "Window (Left)": "a window with flowing curtains on the left wall", "Bookshelf (Left)": "a bookshelf filled with books on the left" }, "Right Zone": { "Large Potted Palm": "a large potted palm tree to the right", "Floor Lamp (Right)": "a standing lamp providing light to the right", "Occasional Chair (Right)": "an occasional chair placed on the right", "Sideboard (Right)": "a sideboard cabinet along the right wall", "Window (Right)": "sunlight streaming through a window on the right wall", "Artwork (Right)": "a piece of abstract artwork hanging on the right wall" }, "Back Wall / Background": { "Large Window with View": "a large window in the background showing a garden view", "Brick Wall": "an exposed brick wall in the background", "Painted Wall (Neutral)": "a neutrally painted wall in the background", "Painted Wall (Accent Color)": "an accent color painted wall in the background", "Fireplace": "a cozy fireplace in the background", "Bookshelves Wall": "a wall lined with bookshelves in the background", "Empty Wall": "a plain empty wall in the background", "Doorway": "an open doorway leading to another room in the background", "Large Mirror": "a large decorative mirror hanging on the back wall", "Floral Wallpaper (Modern Classic)": "modern classic floral wallpaper (Schumacher/Scalamandré style) on the wall", "Damask Wallpaper (Modern Classic)": "modern classic damask wallpaper on the wall", "Geometric Wallpaper (Bold)": "bold geometric pattern wallpaper on the wall", "Painted Wood Paneling (Bright Color)": "brightly colored painted wood paneling on the wall" }, "Foreground / Floor Area": { "Coffee Table Clutter": "a coffee table in the foreground with magazines and a cup", "Small Rug": "a small patterned rug on the floor in the foreground", "Ottoman": "an ottoman or footstool in the foreground", "Pet Bed": "a pet bed lying on the floor", "Scattered Cushions": "scattered cushions on the floor", "Empty Floor Space": "clear empty floor space in the foreground" }, "Ceiling / Upper Area": { "Chandelier": "an elegant chandelier hanging from the ceiling", "Pendant Lights": "modern pendant lights suspended from the ceiling", "Ceiling Fan": "a ceiling fan mounted overhead", "Exposed Beams": "wooden exposed beams on the ceiling", "Simple Ceiling": "a plain ceiling" }, "Other / Ambient": { "Scattered Books": "books scattered artfully", "Decorative Vases": "decorative vases placed around the room", "Candles": "lit candles creating a warm atmosphere", "Picture Frames": "picture frames on surfaces", "Soft Throw Blanket": "a soft throw blanket draped over furniture", "Indoor Plants": "various indoor plants adding greenery", "Cozy Reading Nook": "a cozy reading nook integrated into the space", "Characterful Mouldings": "decorative characterful mouldings on walls and ceiling", "Built-in Elements": "subtle built-in furniture elements integrated into the walls" } }
style_prompts = { "None": "", "Minimalist": "minimalist style, clean lines, uncluttered space, simple forms", "Scandinavian": "scandinavian style, hygge, cozy textiles, light wood, functional", "Modern": "modern style, sleek lines, neutral colors, metallic accents, open space", "Industrial": "industrial style, exposed brick, metal pipes, raw materials, warehouse look", "Bohemian": "bohemian style, eclectic mix, vibrant colors, layered textures, plants", "Coastal": "coastal style, light and airy, blue and white palette, natural textures, beach vibe", "Mid-Century Modern": "mid-century modern style, organic shapes, tapered legs, wood furniture, retro feel", "Farmhouse": "farmhouse style, rustic charm, weathered wood, vintage elements, cozy", "Traditional": "traditional style, classic furniture, rich colors, ornate details, symmetry", "Art Deco": "art deco style, geometric patterns, luxurious materials, bold colors, glamorous", "Japandi": "japandi style, minimalist japanese and scandinavian fusion, natural materials, neutral palette, tranquility", "Maximalist": "maximalist style, more is more, layered patterns, bold colors, eclectic collections", "Bold Traditional Revisited": "traditional interior revisited with boldness, mix of classic shapes and modern elements, featuring built-in furniture and characterful architectural details, warm and lively space" }
style_keywords = { "Clean lines": "clean lines", "Uncluttered": "uncluttered", "Cozy textiles": "cozy textiles", "Light wood": "light wood", "Metallic accents": "metallic accents", "Exposed brick": "exposed brick", "Raw materials": "raw materials", "Eclectic mix": "eclectic mix", "Layered textures": "layered textures", "Natural textures": "natural textures", "Organic shapes": "organic shapes", "Rustic charm": "rustic charm", "Weathered wood": "weathered wood", "Classic furniture": "classic furniture", "Geometric patterns": "geometric patterns", "Luxurious materials": "luxurious materials", "Natural materials": "natural materials", "Layered patterns": "layered patterns", "Floral wallpaper": "floral wallpaper", "Damask wallpaper": "damask wallpaper", "Geometric wallpaper": "geometric wallpaper", "Scalamandre wallpaper style": "Scalamandre style wallpaper", "Built-in furniture": "built-in furniture", "Painted wood paneling": "painted wood paneling", "Characterful details": "characterful details", }
color_palettes = { "None": "", "Neutral Tones (Beige, Grey, White)": "neutral color palette with beige, grey, and white tones", "Warm Neutrals (Cream, Taupe, Brown)": "warm neutral color palette with cream, taupe, and brown", "Cool Neutrals (Grey, Blue-Grey, White)": "cool neutral color palette with grey, blue-grey, and white", "Monochromatic (Shades of One Color)": "monochromatic color scheme", "Earthy Tones (Green, Brown, Terracotta)": "earthy color palette with greens, browns, and terracotta", "Pastel Colors (Light Pink, Baby Blue, Mint)": "soft pastel color tones including light pink, baby blue, mint green, lavender, and pale yellow", "Bold & Contrasting Colors": "bold and contrasting color palette", "Jewel Tones (Emerald, Sapphire, Ruby)": "rich jewel tones like emerald green, sapphire blue, and ruby red", "Black and White": "black and white color scheme", "Bold & Cheerful Mix": "bold and cheerful color palette with contrasting brights and lively hues", "Vibrant Jewel Tones & Warm Woods": "vibrant jewel tones accented by warm wood finishes", }
lighting_control = { "None": "", "Soft Ambient Light": "soft ambient light", "Bright Natural Light": "bright natural light flooding the room", "Warm Evening Light": "warm evening light from lamps", "Dramatic Spotlight": "dramatic spotlight focusing on the main subject", "Overcast Daylight": "soft, diffused light from an overcast day", "Golden Hour Light": "warm, golden hour sunlight", "Studio Lighting": "professional studio lighting setup" }
fov_control = { "None": "", "Standard View (35mm)": "standard field of view, 35mm equivalent", "Wide Angle View (24mm)": "wide angle view, 24mm equivalent", "Ultra-Wide Angle View (16mm)": "ultra wide angle view, 16mm equivalent", "Telephoto View (85mm Portrait)": "narrow field of view, telephoto lens, 85mm equivalent", "Fisheye Lens View": "fisheye lens perspective" }
camera_control = { "None": "", "Eye-level view": "eye-level view", "Low-angle view": "low-angle view", "High angle view": "high angle view", "Top view": "top view", "Close-up": "close-up shot", "Medium shot": "medium shot", "Full shot": "full shot", "Wide shot": "wide shot", "45 Degree Angle Left": "45 degree angle view from the left side", "45 Degree Angle Right": "45 degree angle view from the right side", "Slight-angled Front View": "slight-angled front view" }
lens_model_options = { "None": "", "DSC_3921.NEF": "DSC_3921.NEF", "TETHERED_LR_6723": "TETHERED_LR_6723", "IMG_2985.HEIC": "IMG_2985.HEIC", "IMG_9854.CR2": "IMG_9854.CR2", "RAW_D850_4721": "RAW_D850_4721", "PROFOTO_A1X_392": "PROFOTO_A1X_392" }
lens_model_descriptions = { "None": "Default model behavior, no specific lens/camera simulation.", "DSC_3921.NEF": "Hint: Standard high-quality DSLR look (Nikon RAW). Ideal for balanced, professional interior shots. Default if no other model is selected.", "TETHERED_LR_6723": "Hint: Simulates professional studio workflow (tethered shooting). Optimized for close-ups, sharp details, vibrant textures.", "IMG_2985.HEIC": "Hint: Simulates realistic photos from an iPhone (HEIC format) with natural light and vivid colors. Good for a 'true-to-life' feel.", "IMG_9854.CR2": "Hint: Simulates photorealistic images from professional Canon cameras (CR2 RAW format). Excellent for high-level, studio-like results.", "RAW_D850_4721": "Hint: Simulates ultra-detailed images from a high-res Nikon D850 (RAW format) with wide dynamic range. Good for high-resolution outputs (e.g., print).", "PROFOTO_A1X_392": "Hint: Simulates professional studio lighting (Profoto A1X flash), emphasizing dramatic light with soft shadows. Ideal for cinematic/artistic compositions." }
room_options = { "None": "", "Living Room": "living room", "Bedroom": "bedroom", "Kitchen": "kitchen", "Dining Room": "dining room", "Bathroom": "bathroom", "Home Office": "home office", "Hallway": "hallway", "Entryway": "entryway", "Attic": "attic space", "Basement": "basement area", "Sunroom": "sunroom", "Library": "library room", "Walk-in Closet": "walk-in closet", "Kids Room": "kids room", "Studio Apartment": "studio apartment" }
environment_options_outdoor = { "None": "", "Outdoor Patio": "in an outdoor patio setting", "Outdoor Lounge Zone": "in an outdoor lounge zone", "Garden Terrace": "on a garden terrace", "Backyard Retreat": "in a backyard retreat", "Balcony Terrace": "on a balcony terrace", "Poolside Lounge": "in a poolside lounge area", "Courtyard Oasis": "in a courtyard oasis", "Rooftop Garden": "in a rooftop garden", "Garden Bistro": "in a garden bistro setting", "Orchard Patio": "on an orchard patio", "Sunlit Courtyard": "in a sunlit courtyard", "Mediterranean Veranda": "on a Mediterranean veranda", "Garden Veranda": "on a garden veranda" }
main_subject_options = { "Indoor Furniture": { "Seating": { "Two-seater Sofa": "two-seater sofa", "Three-seater Sofa": "three-seater sofa", "Four-seater Sofa": "four-seater sofa", "Armchair": "armchair", "Loveseat": "loveseat", "Sectional Sofa": "sectional sofa", "Chaise Lounge": "chaise lounge", "Accent Chair": "accent chair", "Bench": "bench", "Stool": "stool", "Ottoman": "ottoman", "Dining Chair": "dining chair", "Office Chair": "office chair", "Window Seat": "window seat", "Dining Banquette": "dining banquette seating" }, "Tables": { "Coffee Table": "coffee table", "Side Table": "side table", "Console Table": "console table", "Dining Table": "dining table", "Desk": "desk", "Nightstand": "nightstand" }, "Storage": { "Bookshelf": "bookshelf", "Cabinet": "cabinet", "Sideboard": "sideboard", "Dresser": "dresser", "Wardrobe": "wardrobe", "Chest of Drawers": "chest of drawers", "TV Stand": "TV stand", "Built-in Bookcase": "built-in bookcase", "Built-in Storage Unit": "built-in storage unit" }, "Beds": { "Double Bed": "double bed", "Single Bed": "single bed", "Bunk Bed": "bunk bed", "Canopy Bed": "canopy bed", "Daybed": "daybed" }, "Lighting": { "Floor Lamp": "floor lamp", "Table Lamp": "table lamp", "Suspensions-pendant-lights": "suspension lamp", "Chandelier": "chandelier", "Wall Sconce": "wall sconce" }, "Rugs & Decor": { "Area Rug": "area rug", "Mirror": "decorative mirror", "Wall Clock": "wall clock" } }, "Outdoor Furniture": { "Seating": { "Patio Chair": "patio chair", "Outdoor Sofa": "outdoor sofa", "Lounge Chair": "lounge chair", "Adirondack Chair": "Adirondack chair", "Hammock": "hammock", "Swing Chair": "swing chair", "Picnic Bench": "picnic bench" }, "Tables": { "Outdoor Dining Table": "outdoor dining table", "Patio Coffee Table": "patio coffee table", "Bistro Table": "bistro table" }, "Other": { "Umbrella": "patio umbrella", "Sun Lounger": "sun lounger", "Planter Box": "large planter box", "Fire Pit": "fire pit" } }, "Dishes": { 'Plate': 'plate', 'Bowl': 'bowl', 'Cup': 'cup', 'Mug': 'mug', 'Set of Dishes': 'set of dishes', 'Serving Tray': 'serving tray' }, "Food": { 'Fruit Bowl': 'bowl of fruit', 'Cake': 'cake', 'Pastries': 'assortment of pastries', 'Breakfast Set': 'breakfast set on a tray', 'Cheese Platter': 'cheese platter', 'Pizza': 'pizza', 'Salad Bowl': 'salad bowl' }, "Wall art": { 'Painting (Abstract)': 'abstract painting', 'Painting (Landscape)': 'landscape painting', 'Painting (Portrait)': 'portrait painting', 'Framed Print': 'framed print', 'Photograph (B&W)': 'black and white photograph', 'Photograph (Color)': 'color photograph', 'Poster': 'poster', 'Wall Sculpture': 'wall sculpture', 'Tapestry': 'wall tapestry' }, "Pillow": { 'Decorative Pillow': 'decorative pillow', 'Cushion': 'cushion', 'Floor Pillow': 'floor pillow', 'Set of Pillows': 'set of pillows' }, "Vase": { 'Ceramic Vase': 'ceramic vase', 'Glass Vase': 'glass vase', 'Vase with Flowers': 'vase with flowers', 'Vase with Branches': 'vase with dry branches', 'Empty Vase': 'empty vase', 'Set of Vases': 'set of vases' } }
requires_placement_subtypes = [ "Table Lamp", "Suspensions-pendant-lights", "Stool", "Ottoman", "Mirror", "Wall Clock", "Plate", "Bowl", "Cup", "Mug", "Set of Dishes", "Serving Tray", "Fruit Bowl", "Cake", "Pastries", "Breakfast Set", "Cheese Platter", "Pizza", "Salad Bowl", "Decorative Pillow", "Cushion", "Floor Pillow", "Set of Pillows", "Ceramic Vase", "Glass Vase", "Vase with Flowers", "Vase with Branches", "Empty Vase", "Set of Vases" ]
quality_tokens = "Best quality, photorealistic, high resolution, sharp focus, detailed texture, professional photography"

# --- Новый словарь Presets ---
preset_options = {
    "Outdoor": {
        "Outdoor Patio Set": "classic garden sofas and armchairs with waterproof cushions, a coffee table, umbrellas or pergolas for shade, stylish lamps or hanging lanterns",
        "Outdoor Lounge Zone Set": "modular sofas with soft seating, hanging chairs, poufs, low tables with decorative elements, fire pits for coziness",
        "Garden Terrace Set": "wooden or rattan furniture, elegant dining tables with chairs, cocoon swings, decorative lanterns",
        "Backyard Retreat Set": "a hammock or hanging chairs, compact folding loungers, tables with natural materials, a mini-bar for parties",
        "Poolside Lounge Set": "loungers with headrests, rattan side tables, sun umbrellas, bar counters, hanging swings near the pool",
        "Rooftop Garden Set": "minimalist armchairs and small coffee tables, stylish concrete or metal benches, hanging lamps for evening lighting",
        "Courtyard Oasis Set": "elegant deep-seated sofas, natural stone coffee tables, water features (fountain or mini-pool), garden lights"
    },
    "Indoor": {
        # TODO: Добавить пресеты для Indoor позже
        "Cozy Living Room Preset": "a plush velvet sofa, two matching armchairs, a wooden coffee table with books, a soft area rug, a floor lamp, and decorative cushions",
        "Modern Minimalist Bedroom Preset": "a low-profile platform bed with neutral bedding, sleek floating nightstands, a minimalist dresser, abstract wall art, and recessed lighting"
    }
}

# --- Функции ---
def update_dependent_options():
    category = st.session_state.selected_category; scene = st.session_state.scene_type
    category_data = main_subject_options.get(category, {}); st.session_state.category_data = category_data
    first_value = next(iter(category_data.values()), None); has_nested_types = isinstance(first_value, dict)
    st.session_state.has_nested_types = has_nested_types
    if has_nested_types:
        type_options = ["None"] + list(category_data.keys()); st.session_state.type_options = type_options
        if st.session_state.selected_type not in type_options: st.session_state.selected_type = "None"
        update_subtype_options_only(reset_subtype=True)
    else:
        subtype_options = ["None"] + list(category_data.keys()); st.session_state.subtype_options = subtype_options
        st.session_state.selected_type = "None"; st.session_state.type_options = ["None"]
        if st.session_state.selected_subtype not in subtype_options: st.session_state.selected_subtype = "None"
    current_surface_dict = get_current_surface_dict()
    if st.session_state.surface not in current_surface_dict: st.session_state.surface = "None"
    if scene == "Indoor":
        if st.session_state.get("outdoor_environment") != "None": st.session_state.outdoor_environment = "None"
    else:
        if st.session_state.get("room") != "None": st.session_state.room = "None"
    # Сброс пресета при смене сцены
    st.session_state.selected_preset = "None"
    reset_placement_surface_if_needed()

def update_subtype_options_only(reset_subtype=False):
    category = st.session_state.selected_category; type_key = st.session_state.selected_type
    category_data = st.session_state.get('category_data', {})
    if type_key != "None" and category_data and isinstance(category_data.get(type_key), dict):
        subtypes = category_data.get(type_key, {}); subtype_options = ["None"] + list(subtypes.keys())
        st.session_state.subtype_options = subtype_options
        if reset_subtype or st.session_state.selected_subtype not in subtype_options: st.session_state.selected_subtype = "None"
    else:
        st.session_state.subtype_options = ["None"]; st.session_state.selected_subtype = "None"
    reset_placement_surface_if_needed()

def reset_placement_surface_if_needed():
    category = st.session_state.selected_category; subtype = st.session_state.selected_subtype
    if category == "Wall art": st.session_state.placement = "None"; st.session_state.surface = "None"
    elif subtype not in requires_placement_subtypes: st.session_state.placement = "None"

def get_current_surface_dict():
    scene = st.session_state.scene_type; category = st.session_state.selected_category
    if scene == "Indoor" and category in tabletop_surface_categories: return surface_options_tabletop
    elif scene == "Indoor": return surface_options_indoor
    else: return surface_options_outdoor

def get_furniture_description(category_key, type_key, subtype_key):
    if not category_key or category_key == "None": return ""
    main_cat_data = main_subject_options.get(category_key);
    if not main_cat_data: return ""
    base_desc = None; has_nested_types = st.session_state.get('has_nested_types', False)
    if has_nested_types:
        if not type_key or type_key == "None" or not subtype_key or subtype_key == "None": return ""
        type_data = main_cat_data.get(type_key)
        if not type_data or not isinstance(type_data, dict): return ""
        base_desc = type_data.get(subtype_key)
    else:
        if not subtype_key or subtype_key == "None": return ""
        base_desc = main_cat_data.get(subtype_key)
    if base_desc is None: return ""
    base_desc_str = str(base_desc).strip();
    if not base_desc_str: return ""
    is_wall_art = (category_key == "Wall art"); hanging_text = " hanging on the wall" if is_wall_art else ""
    if not base_desc_str.lower().startswith(("a ", "an ")):
        article = "an" if base_desc_str.lower().startswith(tuple("aeiou")) else "a"
        return f"{article} {base_desc_str}{hanging_text}"
    else: return f"{base_desc_str}{hanging_text}"

def get_selected_surrounding_elements():
    selected_elements = [];
    for detail_key, is_selected in st.session_state.surrounding_details_state.items():
        if is_selected:
            for zone, details in surrounding_details_structured.items():
                if detail_key in details: selected_elements.append(details[detail_key]); break
    return selected_elements

def add_random_surrounding_element():
    available_elements = []; current_selection_keys = [key for key, selected in st.session_state.surrounding_details_state.items() if selected]
    all_keys_in_structure = set(k for details in surrounding_details_structured.values() for k in details)
    for key in all_keys_in_structure:
            if not st.session_state.surrounding_details_state.get(key, False):
                 conflicts = False; base_key = key.split(" (")[0]
                 if "Left" in key and any(f"{base_key} (Right)" == sel_key for sel_key in current_selection_keys): conflicts = True
                 elif "Right" in key and any(f"{base_key} (Left)" == sel_key for sel_key in current_selection_keys): conflicts = True
                 if not conflicts: available_elements.append(key)
    if available_elements:
        random_key = random.choice(available_elements)
        if random_key in st.session_state.surrounding_details_state: st.session_state.surrounding_details_state[random_key] = True


# --- Инициализация состояния ---
if "prompt_logic" not in st.session_state: st.session_state.prompt_logic = "Nfinite"
if "scene_type" not in st.session_state: st.session_state.scene_type = "Indoor"
if "selected_category" not in st.session_state: st.session_state.selected_category = "Indoor Furniture"
if "selected_type" not in st.session_state: st.session_state.selected_type = "None"
if "selected_subtype" not in st.session_state: st.session_state.selected_subtype = "None"
if "room" not in st.session_state: st.session_state.room = "None"
if "outdoor_environment" not in st.session_state: st.session_state.outdoor_environment = "None"
if "selected_preset" not in st.session_state: st.session_state.selected_preset = "None" # Инициализация пресета
if "style" not in st.session_state: st.session_state.style = "None"
if "color_palette" not in st.session_state: st.session_state.color_palette = "None"
if "lighting" not in st.session_state: st.session_state.lighting = "None"
if "fov" not in st.session_state: st.session_state.fov = "None"
if "camera" not in st.session_state: st.session_state.camera = "None"
if "surface" not in st.session_state: st.session_state.surface = "None"
if "placement" not in st.session_state: st.session_state.placement = "None"
if "surrounding_details_state" not in st.session_state:
    st.session_state.surrounding_details_state = {}
    for _, details in surrounding_details_structured.items():
        for detail_key in details.keys(): st.session_state.surrounding_details_state[detail_key] = False
if "style_keywords_state" not in st.session_state:
    st.session_state.style_keywords_state = {key: False for key in style_keywords}
if "quality_enabled" not in st.session_state: st.session_state.quality_enabled = True
if "selected_lens_model" not in st.session_state: st.session_state.selected_lens_model = "None"
if "main_prompt_area" not in st.session_state: st.session_state.main_prompt_area = ""
if "saved_configs" not in st.session_state: st.session_state.saved_configs = {}
# Инициализация производных состояний, если их нет (исправление бага)
if 'category_data' not in st.session_state or \
   'has_nested_types' not in st.session_state or \
   'type_options' not in st.session_state or \
   'subtype_options' not in st.session_state:
    update_dependent_options()


# --- Обновленная функция генерации промпта ---
def generate_prompt(prompt_logic):
    scene = st.session_state.scene_type; category = st.session_state.selected_category
    type_sel = st.session_state.selected_type; subtype = st.session_state.selected_subtype
    room_or_env_key = st.session_state.room if scene == "Indoor" else st.session_state.outdoor_environment
    room_or_env_options = room_options if scene == "Indoor" else environment_options_outdoor
    room_or_env_text = room_or_env_options.get(room_or_env_key, "") if room_or_env_key != "None" else ""
    style = st.session_state.style
    color_palette = st.session_state.color_palette; lighting = st.session_state.lighting
    fov = st.session_state.fov; camera = st.session_state.camera
    current_surface_dict = get_current_surface_dict()
    surface = st.session_state.surface if st.session_state.surface in current_surface_dict else "None"
    placement = st.session_state.placement if scene == "Indoor" and subtype in requires_placement_subtypes and category != "Wall art" else "None"
    quality_enabled = st.session_state.quality_enabled
    selected_lens_model_key = st.session_state.selected_lens_model
    selected_lens_model_text = lens_model_options.get(selected_lens_model_key, "")
    selected_preset_key = st.session_state.selected_preset # Получаем ключ пресета
    # Получаем текст пресета из нужного словаря (Indoor/Outdoor)
    current_preset_options = preset_options.get(scene, {})
    preset_text = current_preset_options.get(selected_preset_key, "") if selected_preset_key != "None" else ""

    prompt_parts = []
    if selected_lens_model_text: prompt_parts.append(selected_lens_model_text)

    furniture_desc = get_furniture_description(category, type_sel, subtype)
    placement_text = placement_options_indoor.get(placement, "") if scene == "Indoor" else ""
    surface_text = current_surface_dict.get(surface, "")
    combined_placement_surface = ""
    if category != "Wall art" and subtype in requires_placement_subtypes and placement != "None" and surface != "None" and placement_text and surface_text and surface_text != surface_options_tabletop.get("None",""):
        surface_text_modified = surface_text.strip();
        if surface_text_modified.startswith(("on a ","on an ","on ")): surface_text_modified = surface_text_modified.split(" ", 2)[-1]
        combined_placement_surface = f"{placement_text} staying on {surface_text_modified}"
    elif category != "Wall art" and placement != "None" and subtype in requires_placement_subtypes and placement_text:
         combined_placement_surface = placement_text
    elif category != "Wall art" and surface != "None" and surface_text and surface_text != surface_options_tabletop.get("None",""):
         top_level_category_data = main_subject_options.get(category, {}); first_val = next(iter(top_level_category_data.values()), None)
         is_furniture_category = isinstance(first_val, dict)
         if is_furniture_category or subtype not in requires_placement_subtypes: combined_placement_surface = surface_text
    object_full_desc = furniture_desc
    if combined_placement_surface and category != "Wall art": object_full_desc += f" {combined_placement_surface}"

    surrounding_elements = get_selected_surrounding_elements(); surrounding_desc = ", ".join(surrounding_elements) if surrounding_elements else ""
    selected_style_keywords_texts = [ style_keywords[key] for key, selected in st.session_state.style_keywords_state.items() if selected and key in style_keywords ]
    style_keywords_desc = ", ".join(filter(None, selected_style_keywords_texts))
    centering_phrase = "positioned centrally in the composition"

    # --- Сборка промпта ---
    if prompt_logic == "Nfinite":
        prompt_parts.append("Photo shot")
        if object_full_desc: prompt_parts.append(f"{centering_phrase} {object_full_desc}")
        elif room_or_env_text: prompt_parts.append(f"A scene {room_or_env_text} {centering_phrase}")
        elif scene == "Indoor": prompt_parts.append(f"A scene inside a room {centering_phrase}")
        else: prompt_parts.append(f"An outdoor scene {centering_phrase}")
        style_env_parts = [];
        if style != "None": style_env_parts.append(style_prompts.get(style,""))
        if style_keywords_desc: style_env_parts.append(style_keywords_desc)
        if room_or_env_text: style_env_parts.append(room_or_env_text)
        if style_env_parts: prompt_parts.append(", ".join(filter(None, style_env_parts)))
        if color_palette != "None": prompt_parts.append(color_palettes.get(color_palette,""))
        if lighting != "None": prompt_parts.append(lighting_control.get(lighting,""))
        if fov != "None": prompt_parts.append(fov_control.get(fov,""))
        if camera != "None": prompt_parts.append(camera_control.get(camera,""))
        if surrounding_desc: prompt_parts.append(surrounding_desc)
        if preset_text: prompt_parts.append(preset_text) # Добавляем текст пресета
        prompt_parts.append("f/22, 1/160s");
        if quality_enabled: prompt_parts.append(quality_tokens)

    elif prompt_logic == "FLUX":
        if object_full_desc: prompt_parts.append(f"A scene featuring {object_full_desc} {centering_phrase}.")
        else: prompt_parts.append(f"A scene {centering_phrase}.")
        scene_parts = [];
        if style != "None": scene_parts.append(style_prompts.get(style,""))
        if style_keywords_desc: scene_parts.append(style_keywords_desc)
        if room_or_env_text: scene_parts.append(room_or_env_text)
        if scene_parts: prompt_parts.append(f"Scene details: {', '.join(filter(None, scene_parts))}.")
        if color_palette != "None": prompt_parts.append(f"Colors: {color_palettes.get(color_palette,'')}.")
        atmosphere_parts = []
        if lighting != "None": atmosphere_parts.append(lighting_control.get(lighting,""))
        if surrounding_desc: atmosphere_parts.append(surrounding_desc)
        if preset_text: atmosphere_parts.append(preset_text) # Добавляем текст пресета
        if atmosphere_parts: prompt_parts.append(f"Atmosphere: {', '.join(filter(None, atmosphere_parts))}.")
        camera_parts = []
        if camera != "None": camera_parts.append(camera_control.get(camera,""))
        if fov != "None": camera_parts.append(fov_control.get(fov,""))
        camera_parts.append("Nikon Z7 II, 24mm f/1.2L lens"); camera_parts.append("aperture f/5.6, shutter speed 1/125s, ISO 100, white balance 5500K")
        prompt_parts.append(f"Camera setup: {', '.join(filter(None, camera_parts))}.")
        if quality_enabled: prompt_parts.append(quality_tokens)

    elif prompt_logic == "SDXL":
        view_desc_parts = [];
        if camera != "None": view_desc_parts.append(camera_control.get(camera,""))
        if fov != "None": view_desc_parts.append(fov_control.get(fov,""))
        view_desc = " ".join(filter(None, view_desc_parts)); view_desc = view_desc if view_desc else "A photograph"
        env_style_parts = []
        if style != "None": env_style_parts.append(style_prompts.get(style,""))
        if room_or_env_text: env_style_parts.append(room_or_env_text)
        env_style_desc = " ".join(filter(None, env_style_parts));
        if not env_style_desc: env_style_desc = "setting"
        if object_full_desc: prompt_parts.append(f"{view_desc} of a {env_style_desc} featuring {object_full_desc} {centering_phrase}.")
        else: prompt_parts.append(f"{view_desc} of a {env_style_desc}, {centering_phrase}.")
        cp_text = color_palettes.get(color_palette, ""); lt_text = lighting_control.get(lighting, "")
        if cp_text: prompt_parts.append(f"{cp_text.capitalize()}.")
        if lt_text: prompt_parts.append(f"{lt_text.capitalize()}.")
        if surrounding_desc: prompt_parts.append(surrounding_desc.capitalize() + ".")
        if preset_text: prompt_parts.append(preset_text.capitalize() + ".") # Добавляем текст пресета
        if style_keywords_desc: prompt_parts.append(style_keywords_desc.capitalize() + ".")
        if quality_enabled: prompt_parts.append(quality_tokens)

    # Финальная очистка
    final_prompt = ", ".join(filter(lambda x: x is not None and x.strip() != "", prompt_parts))
    centering_phrase_dot = centering_phrase + ".";
    while f"{centering_phrase}, {centering_phrase}" in final_prompt: final_prompt = final_prompt.replace(f"{centering_phrase}, {centering_phrase}", centering_phrase)
    while f"{centering_phrase_dot} {centering_phrase}" in final_prompt: final_prompt = final_prompt.replace(f"{centering_phrase_dot} {centering_phrase}", centering_phrase_dot)
    final_prompt = final_prompt.replace(" ,", ",").replace(",,", ",").replace(" .", ".").replace("..", ".").strip(", ").strip()
    final_prompt = ". ".join(part.strip() for part in final_prompt.split('.') if part.strip())
    if not final_prompt.endswith(".") and final_prompt: final_prompt += "."
    final_prompt = final_prompt.replace(". , ", ", ").replace(f"{centering_phrase}.", centering_phrase + ".").replace(f". {centering_phrase}.", f" {centering_phrase}.")
    return final_prompt

# --- Обновленная функция предпросмотра ---
def generate_composition_preview():
    parts = [];
    if st.session_state.camera != "None": parts.append(f"View: {st.session_state.camera}")
    if st.session_state.fov != "None": parts.append(f"FOV: {st.session_state.fov}")
    scene = st.session_state.scene_type
    if scene == "Indoor" and st.session_state.room != "None": parts.append(f"Location: {st.session_state.room}")
    elif scene == "Outdoor" and st.session_state.outdoor_environment != "None": parts.append(f"Environment: {st.session_state.outdoor_environment}")
    obj_desc = get_furniture_description(st.session_state.selected_category, st.session_state.selected_type, st.session_state.selected_subtype)
    if obj_desc:
         obj_desc_preview = obj_desc.replace(" hanging on the wall", "")
         if obj_desc_preview.lower().startswith(("a ", "an ")): obj_desc_preview = obj_desc_preview.split(" ", 1)[-1]
         parts.append(f"Main: {obj_desc_preview.capitalize()} (Centered)")
         placement_text = placement_options_indoor.get(st.session_state.placement, "")
         current_surface_dict = get_current_surface_dict(); surface_text = current_surface_dict.get(st.session_state.surface, "")
         if st.session_state.selected_category == "Wall art": parts.append("Placement: Hanging on wall")
         elif placement_text and surface_text and st.session_state.surface != "None": parts.append(f"Placement: {placement_text} staying on {surface_text.replace('on a ', '').replace('on an ', '').replace('on ', '')}")
         elif placement_text: parts.append(f"Placement: {placement_text}")
         elif surface_text and st.session_state.surface != "None": parts.append(f"Surface: {surface_text}")
    # Добавляем выбранный пресет в превью
    if st.session_state.selected_preset != "None":
         parts.append(f"Preset Items: {st.session_state.selected_preset}")
    surroundings = get_selected_surrounding_elements()
    if surroundings:
        parts.append("Surroundings:")
        for item in surroundings:
             preview_item = item.replace("a ", "").replace("an ", "").replace(" to the left", " (Left)").replace(" to the right", " (Right)").replace(" in the background", " (Back)").replace(" on the floor in the foreground", " (Front Floor)").replace(" on the wall", " (Wall)").replace(" from the ceiling", " (Ceiling)").replace(" overhead", " (Ceiling)")
             parts.append(f"- {preview_item.capitalize()}")
    selected_style_kws = [key for key, selected in st.session_state.style_keywords_state.items() if selected]
    if selected_style_kws:
         parts.append("Style Keywords:")
         for kw in selected_style_kws: parts.append(f"- {kw}")
    return "\n".join(parts)

# --- UI ---
with st.sidebar:
    # (Разделы Configuration, Scene Type, Main Subject, Placement & Surface без изменений)
    st.header("⚙️ Configuration")
    st.selectbox("Prompt Logic:", options=["Nfinite", "FLUX", "SDXL"], key="prompt_logic", help="Select generation logic.")
    st.selectbox("Scene Type:", options=["Indoor", "Outdoor"], key="scene_type", on_change=update_dependent_options)

    st.subheader("🎯 Main Subject")
    main_categories = list(main_subject_options.keys()); filtered_categories = []
    is_indoor = st.session_state.scene_type == "Indoor"
    for cat in main_categories:
        if cat == "Indoor Furniture" and is_indoor: filtered_categories.append(cat)
        elif cat == "Outdoor Furniture" and not is_indoor: filtered_categories.append(cat)
        elif cat not in ["Indoor Furniture", "Outdoor Furniture"]: filtered_categories.append(cat)
    if st.session_state.selected_category not in filtered_categories:
        st.session_state.selected_category = filtered_categories[0] if filtered_categories else "None"; update_dependent_options()
    st.selectbox("Select Category:", options=filtered_categories, key="selected_category", index=filtered_categories.index(st.session_state.selected_category) if st.session_state.selected_category in filtered_categories else 0, on_change=update_dependent_options, help="Select main category.")
    has_nested_types = st.session_state.get('has_nested_types', False); type_options = st.session_state.get('type_options', ["None"])
    if has_nested_types:
         st.selectbox("Select Type:", options=type_options, key="selected_type", index=type_options.index(st.session_state.selected_type) if st.session_state.selected_type in type_options else 0, on_change=update_subtype_options_only, help="Select type within category.")
    subtype_options = st.session_state.get('subtype_options', ["None"])
    st.selectbox("Select Subtype:", options=subtype_options, key="selected_subtype", index=subtype_options.index(st.session_state.selected_subtype) if st.session_state.selected_subtype in subtype_options else 0, format_func=lambda x: x, on_change=reset_placement_surface_if_needed, help="Select specific subtype.")

    show_placement = st.session_state.scene_type == "Indoor" and st.session_state.selected_category != "Wall art" and st.session_state.selected_subtype != "None" and st.session_state.selected_subtype in requires_placement_subtypes
    show_surface = (st.session_state.scene_type == "Indoor" or st.session_state.scene_type == "Outdoor") and st.session_state.selected_category != "Wall art" and st.session_state.selected_subtype != "None"
    if show_placement or show_surface:
        st.subheader("📍 Placement & Surface")
        if show_placement: st.selectbox("Placement (On):", options=["None"] + list(placement_options_indoor.keys())[1:], key="placement", help="Where is it placed ON?")
        else:
             if st.session_state.placement != "None": st.session_state.placement = "None"
        if show_surface:
            current_surface_dict = get_current_surface_dict()
            if st.session_state.scene_type == "Outdoor": surface_label = "Surface (Ground/Deck):"
            elif st.session_state.selected_category in tabletop_surface_categories: surface_label = "Surface (Tabletop):"
            else: surface_label = "Surface (Floor/Under):"
            st.selectbox(surface_label, options=["None"] + list(current_surface_dict.keys())[1:], key="surface", help="What surface is it standing on?")
        else:
            if st.session_state.surface != "None": st.session_state.surface = "None"
    else:
        if st.session_state.placement != "None": st.session_state.placement = "None"
        if st.session_state.surface != "None": st.session_state.surface = "None"

    st.subheader("🌳 Environment")
    # --- Условное отображение Room Type или Outdoor Environment ---
    if st.session_state.scene_type == "Indoor":
        st.selectbox("Room Type:", options=["None"] + [r for r in room_options.keys() if r != "None"], key="room")
    elif st.session_state.scene_type == "Outdoor":
        st.selectbox("Environment:", options=["None"] + list(environment_options_outdoor.keys())[1:], key="outdoor_environment")
    # --- Конец условного отображения ---
    st.selectbox("Style Preset:", options=["None"] + list(style_prompts.keys())[1:], key="style", help="Select base style.")
    st.selectbox("Color Palette:", options=["None"] + list(color_palettes.keys())[1:], key="color_palette")

    st.subheader("📷 Visuals")
    st.selectbox("Lighting:", options=["None"] + list(lighting_control.keys())[1:], key="lighting")
    st.selectbox("Field of View (FOV):", options=["None"] + list(fov_control.keys())[1:], key="fov", help="Select the virtual camera lens field of view. Affects how much of the scene is visible and potential distortion.")
    st.selectbox("Camera View:", options=["None"] + [c for c in camera_control.keys() if c != "None"], key="camera")

    st.subheader("📷 Lens Model")
    st.selectbox("Lens Model:", options=list(lens_model_options.keys()), key="selected_lens_model", help="Select a specific lens/camera model simulation trigger.")
    selected_model_desc = lens_model_descriptions.get(st.session_state.selected_lens_model, "");
    if selected_model_desc: st.caption(selected_model_desc)

    st.subheader("🔧 Prompt Settings")
    st.checkbox("Add Quality Tokens", key="quality_enabled", help=f"Append: {quality_tokens}")

# --- Основная область ---
col1, col2 = st.columns([3, 2])
with col1:
    st.subheader("📝 Generated Prompt")
    final_prompt_text = generate_prompt(st.session_state.prompt_logic)
    st.session_state.main_prompt_area = final_prompt_text
    main_prompt_input = st.text_area("Main Prompt:", value=st.session_state.main_prompt_area, height=250, key="main_prompt_widget")

    st.markdown("---")

    # --- Раздел Style Keywords ---
    with st.expander("🎨 Style Keywords (Check to Add)", expanded=False): # Свернут по умолчанию
        for key in style_keywords.keys():
            if key not in st.session_state.style_keywords_state: st.session_state.style_keywords_state[key] = False
        kw_cols = st.columns(3); sorted_keywords = sorted(style_keywords.keys()); col_index = 0
        for key in sorted_keywords:
            with kw_cols[col_index % 3]:
                 current_value = st.session_state.style_keywords_state.get(key, False)
                 st.checkbox(key, key=f"style_kw_{key}", value=current_value, on_change=lambda k=key: st.session_state.style_keywords_state.update({k: not st.session_state.style_keywords_state[k]}), help=style_keywords.get(key, ''))
            col_index += 1

    # --- Новый раздел Presets ---
    with st.expander("🎁 Presets (Select ONE set to add)", expanded=False):
        current_scene_type = st.session_state.scene_type
        current_presets = preset_options.get(current_scene_type, {})
        preset_choices = ["None"] + list(current_presets.keys())

        # Убеждаемся, что выбранный пресет валиден для текущей сцены
        if st.session_state.selected_preset not in preset_choices:
            st.session_state.selected_preset = "None"

        st.radio(
            "Select Preset:",
            options=preset_choices,
            key="selected_preset",
            index=preset_choices.index(st.session_state.selected_preset) # Устанавливаем индекс
        )
        # Показываем описание выбранного пресета
        selected_preset_desc = current_presets.get(st.session_state.selected_preset, "")
        if selected_preset_desc:
            st.caption(f"Description: {selected_preset_desc}")

with col2:
    st.subheader("🖼️ Composition Preview")
    composition_preview_text = generate_composition_preview()
    st.text_area("Preview:", value=composition_preview_text, height=450, disabled=True, help="Textual representation of the scene.")

st.markdown("---")

# --- Детали окружения (Expander) ---
with st.expander("🌿 Surrounding Details (Check to Add)", expanded=False):
    col_sd1, col_sd2, col_sd3 = st.columns(3)
    all_detail_keys = [k for details in surrounding_details_structured.values() for k in details]
    for key in all_detail_keys:
        if key not in st.session_state.surrounding_details_state: st.session_state.surrounding_details_state[key] = False
    def create_checkbox(key, help_text): st.checkbox(key, key=f"surrounding_details_state_widget_{key}", value=st.session_state.surrounding_details_state.get(key, False), on_change=lambda k=key: st.session_state.surrounding_details_state.update({k: not st.session_state.surrounding_details_state.get(k, False)}), help=help_text)
    with col_sd1:
        st.markdown("**Left Zone / Foreground**"); zone1_keys = list(surrounding_details_structured["Left Zone"].keys()) + list(surrounding_details_structured["Foreground / Floor Area"].keys())
        for key in zone1_keys: create_checkbox(key, surrounding_details_structured.get("Left Zone", {}).get(key, surrounding_details_structured.get("Foreground / Floor Area", {}).get(key,"")))
    with col_sd2:
         st.markdown("**Right Zone / Back Wall**"); zone2_keys = list(surrounding_details_structured["Right Zone"].keys()) + list(surrounding_details_structured["Back Wall / Background"].keys())
         for key in zone2_keys: create_checkbox(key, surrounding_details_structured.get("Right Zone", {}).get(key, surrounding_details_structured.get("Back Wall / Background", {}).get(key,"")))
    with col_sd3:
        st.markdown("**Ceiling / Other Ambient**"); zone3_keys = list(surrounding_details_structured["Ceiling / Upper Area"].keys()) + list(surrounding_details_structured["Other / Ambient"].keys())
        for key in zone3_keys: create_checkbox(key, surrounding_details_structured.get("Ceiling / Upper Area", {}).get(key, surrounding_details_structured.get("Other / Ambient", {}).get(key,"")))
    if st.button("🎲 Add Random Detail"): add_random_surrounding_element()

st.markdown("---")

# --- Управление конфигурациями ---
st.subheader("💾 Configuration Management")
col_cfg1, col_cfg2 = st.columns(2)
with col_cfg1:
    config_name = st.text_input("Configuration Name:", placeholder="e.g., Cozy Living Room Setup", key="config_name_input")
    if st.button("Save Current Configuration"):
        if config_name:
            elements_to_save = {k: v for k, v in st.session_state.surrounding_details_state.items() if v}
            style_kw_to_save = {k: v for k, v in st.session_state.style_keywords_state.items() if v}
            main_prompt_to_save = st.session_state.get("main_prompt_widget", final_prompt_text);
            cat_save = st.session_state.selected_category; type_save = st.session_state.selected_type; subtype_save = st.session_state.selected_subtype
            cat_data = main_subject_options.get(cat_save, {}); has_nested_save = isinstance(next(iter(cat_data.values()), None), dict)
            config = { "scene_type": st.session_state.scene_type, "selected_category": cat_save, "selected_type": type_save if has_nested_save else "None", "selected_subtype": subtype_save, "room": st.session_state.room, "outdoor_environment": st.session_state.outdoor_environment, "selected_preset": st.session_state.selected_preset, # Добавлено
                       "style": st.session_state.style, "style_keywords_state": style_kw_to_save, "lighting": st.session_state.lighting, "fov": st.session_state.fov, "camera": st.session_state.camera, "surface": st.session_state.surface, "placement": st.session_state.placement, "color_palette": st.session_state.color_palette, "surrounding_elements": elements_to_save, "quality_enabled": st.session_state.quality_enabled, "prompt_logic": st.session_state.prompt_logic, "selected_lens_model": st.session_state.selected_lens_model, "main_prompt": main_prompt_to_save, }
            config = {k: (v if v is not None else "None") for k, v in config.items()}
            st.session_state.saved_configs[config_name] = config; st.success(f"Configuration '{config_name}' saved!")
        else: st.warning("Please enter a name.")
with col_cfg2:
    if st.session_state.saved_configs:
        saved_config_names = [""] + list(st.session_state.saved_configs.keys())
        selected_config_to_load = st.selectbox("Load Configuration:", options=saved_config_names, key="load_config_select")
        if selected_config_to_load:
            col_load, col_delete = st.columns(2)
            with col_load:
                if st.button("Load Selected"):
                    if selected_config_to_load in st.session_state.saved_configs:
                        config_to_load = st.session_state.saved_configs[selected_config_to_load]
                        st.session_state.scene_type = config_to_load.get("scene_type", "Indoor"); st.session_state.selected_category = config_to_load.get("selected_category", "Indoor Furniture")
                        cat_data_load = main_subject_options.get(st.session_state.selected_category, {}); has_nested_load = isinstance(next(iter(cat_data_load.values()), None), dict)
                        st.session_state.has_nested_types = has_nested_load
                        st.session_state.selected_type = config_to_load.get("selected_type", "None") if has_nested_load else "None"; st.session_state.selected_subtype = config_to_load.get("selected_subtype", "None")
                        if has_nested_load:
                            st.session_state.type_options = ["None"] + list(cat_data_load.keys()); type_data_load = cat_data_load.get(st.session_state.selected_type, {})
                            st.session_state.subtype_options = ["None"] + list(type_data_load.keys())
                        else:
                             st.session_state.type_options = ["None"]; st.session_state.subtype_options = ["None"] + list(cat_data_load.keys())
                        st.session_state.room = config_to_load.get("room", "None"); st.session_state.outdoor_environment = config_to_load.get("outdoor_environment", "None");
                        st.session_state.selected_preset = config_to_load.get("selected_preset", "None"); # Загружаем пресет
                        st.session_state.style = config_to_load.get("style", "None"); st.session_state.lighting = config_to_load.get("lighting", "None"); st.session_state.fov = config_to_load.get("fov", "None"); st.session_state.camera = config_to_load.get("camera", "None"); st.session_state.surface = config_to_load.get("surface", "None"); st.session_state.placement = config_to_load.get("placement", "None"); st.session_state.color_palette = config_to_load.get("color_palette", "None"); st.session_state.quality_enabled = config_to_load.get("quality_enabled", True);
                        st.session_state.prompt_logic = config_to_load.get("prompt_logic", "Nfinite"); st.session_state.selected_lens_model = config_to_load.get("selected_lens_model", "None")
                        surrounding_elements_loaded = config_to_load.get("surrounding_elements", {});
                        for key in st.session_state.surrounding_details_state: st.session_state.surrounding_details_state[key] = key in surrounding_elements_loaded
                        style_kw_loaded = config_to_load.get("style_keywords_state", {})
                        for key in st.session_state.style_keywords_state: st.session_state.style_keywords_state[key] = key in style_kw_loaded
                        st.session_state.main_prompt_area = config_to_load.get("main_prompt", "");
                        st.success(f"Configuration '{selected_config_to_load}' loaded!"); st.rerun()
                    else: st.error("Config not found.")
            with col_delete:
                 if st.button("Delete Selected"):
                    if selected_config_to_load in st.session_state.saved_configs: del st.session_state.saved_configs[selected_config_to_load]; st.success(f"Configuration '{selected_config_to_load}' deleted!"); st.rerun()
                    else: st.error("Config not found.")
    else: st.info("No saved configurations yet.")