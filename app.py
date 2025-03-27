import streamlit as st
import pyperclip
import json

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
    "Haussmannian": "with elegant architecture, high ceilings, and ornate moldings, featuring large windows, classic furniture, and luxurious decor",
    "Japandi": "combining Scandinavian simplicity with Japanese minimalism, featuring natural materials, muted colors, wooden textures, and a zen atmosphere",
    "Mid-century Modern": "with retro vibes, organic shapes, and bold colors, featuring wooden furniture, vintage decor, and clean lines",
    "Minimalist": "with clean lines, neutral colors, and functional furniture, featuring an open, simple, and clutter-free space",
    "Modern": "with clean lines, minimalistic design, and a neutral color palette, featuring sleek furniture, geometric shapes, and metallic accents",
    "Modern Traditional": "blending classic furniture with modern accents, featuring symmetry, rich colors, and elegant decor for a timeless look",
    "Rustic": "with natural materials, rough textures, and earthy tones, featuring wooden beams, stone elements, and an inviting atmosphere",
    "Traditional": "with ornate details, rich fabrics, and dark wood furniture, featuring classic patterns, antique decor, and warm colors",
    "Vintage": "with retro furniture, antique decor, and muted colors, featuring nostalgic elements and classic patterns"
}

# Контроль над камерой (Updated: Modified Front view description)
camera_control = {
    "None": "",
    "20% angle": "slightly angled view to add depth and perspective",
    "A little above view": "slightly elevated view to give a better sense of space and arrangement",
    "3/4 view": "three-quarter position allowing the viewer to see both its front and side",
    "Front view": "front view of facing directly towards the viewer",
    "Side view": "side view of"
}

# Контроль над FOV
fov_control = {
    "None": "",
    "Close up": "Close up",
    "Midshot": "Midshot",
    "Full interior": "Full interior",
    "Wide angle": "Wide angle"
}

# Контроль над освещением
lighting_control = {
    "None": "",
    "Clear daylight": "with clear daylight illuminating the room through large windows, highlighting all details",
    "Evening mood lighting": "with evening mood lighting casting distinct, warm shadows across the scene",
    "Studio lighting": "with studio lighting providing even, sharp illumination to every element",
    "Golden hour": "with golden-hour light casting sharp, warm shadows and enhancing all textures",
    "Overcast lighting": "with overcast lighting providing even, clear illumination for a detailed atmosphere"
}

# Цветовые палитры
color_palettes = {
    "None": "",
    "Pastel color tones": "Pastel color tones including light pink, baby blue, mint green, lavender, and pale yellow",
    "Neutral Palette": "Neutral Palette including tones like beige, gray, taupe, and cream, creating a timeless and elegant look",
    "Monochromatic Palette": "Monochromatic Palette focusing on varying shades and tones of a single color for a harmonious feel",
    "Complementary Palette": "Complementary Palette using colors opposite each other on the color wheel like blue and orange, red and green, for dynamic contrast",
    "Analogous Palette": "Analogous Palette combining colors next to each other on the color wheel like blue, turquoise, green, for a smooth transition",
    "Warm Palette": "Warm Palette filled with reds, oranges, and yellows to bring coziness and energy",
    "Cool Palette": "Cool Palette centered on blues, greens, and purples for calmness and relaxation",
    "Earthy Palette": "Earthy Palette inspired by natural tones like terracotta, olive green, and sandy browns",
    "Bold and Vibrant Palette": "Bold and Vibrant Palette using saturated hues like magenta, electric blue, and neon yellow for a lively atmosphere",
    "Muted Palette": "Muted Palette with subdued tones that maintain color depth without being overpowering, such as dusty pink, sage green, slate blue"
}

# Токены для качества
quality_tokens = "Photorealistic scene with sharp detail throughout, high-resolution textures, vivid colors, lifelike lighting across the entire image, clear focus on all elements."

# Токены для негативного промпта
negative_tokens = "busy patterns, dark lighting, cluttered, artificial colors, cartoon style, low resolution, blurry, noisy, grainy, distorted proportions, unrealistic textures, harsh shadows, oversaturated colors, highly decorated, chaotic composition, rough surfaces, childish design, unrefined edges, gaudy colors, overly complex, heavy appearance, dirty, worn, antique, steampunk elements, depth of field, yellow walls, warm walls, nude, NSFW."

# Полный словарь subject_subcategories (Category-level tokens removed)
subject_subcategories = {
    "None": {
        "options": ["None"],
        "tokens": ""
    },
    "Sofa": {
        "options": [
            "None",
            "two-seated sofa", "three-seated sofa", "four-seated sofa", "corner sofa",
            "L-shaped sofa", "sectional sofa", "sleeper sofa", "chaise sofa",
            "loveseat", "recliner sofa", "modular sofa", "curved sofa",
            "tufted sofa", "mid-century sofa", "chesterfield sofa"
        ]
    },
    "Table": {
        "options": [
            "None",
            "Coffee Table", "Dining Table", "Side Table", "Console Table", "Bedside Table",
            "Desk Table", "Outdoor Table", "Accent Table"
        ],
        "subcategories": {
            "Coffee Table": [
                {"name": "Round or oval wooden table with a minimalist design",
                 "tokens": "round or oval shape, wooden finish, minimalist design, sleek legs, neutral tones"},
                {"name": "Glass-topped table with metal or wooden base",
                 "tokens": "glass top, metal or wooden base, modern aesthetic, reflective surface, sturdy frame"},
                {"name": "Nesting coffee table for a modular and modern feel",
                 "tokens": "nesting design, modular layout, modern style, wooden or metal, compact storage"}
            ],
            "Dining Table": [
                {"name": "Farmhouse-style table with a rustic wood finish",
                 "tokens": "rustic wood, farmhouse style, sturdy legs, distressed finish, warm tones"},
                {"name": "Rectangular table with sleek glass or marble top",
                 "tokens": "rectangular shape, glass or marble top, sleek design, modern elegance, polished surface"},
                {"name": "Extendable dining table for versatility and functionality",
                 "tokens": "extendable design, versatile layout, wooden or glass, functional decor, modern or classic"}
            ],
            "Side Table": [
                {"name": "Small, modern table with geometric frame",
                 "tokens": "small size, geometric frame, modern design, metal or wood, compact style"},
                {"name": "Ceramic pedestal table for an artistic statement",
                 "tokens": "ceramic top, pedestal base, artistic design, unique shape, bold colors"},
                {"name": "Natural wood stump table for a touch of organic design",
                 "tokens": "natural wood, organic shape, rustic feel, unique texture, earthy tones"}
            ],
            "Console Table": [
                {"name": "Slim, metal-framed table for hallways or entryways",
                 "tokens": "slim design, metal frame, hallway decor, modern style, functional top"},
                {"name": "Mirrored console table for a glamorous vibe",
                 "tokens": "mirrored surface, glamorous style, elegant frame, reflective finish, luxurious feel"},
                {"name": "Multi-tiered design for added storage and display",
                 "tokens": "multi-tiered, storage design, modern or classic, display space, wooden or metal"}
            ],
            "Bedside Table": [
                {"name": "Classic nightstand with a drawer and open shelf",
                 "tokens": "classic design, drawer and shelf, wooden finish, bedside use, traditional style"},
                {"name": "Floating wall-mounted table for a space-saving option",
                 "tokens": "floating design, wall-mounted, space-saving, modern style, minimalist look"},
                {"name": "Sculptural bedside table with unique materials like concrete or stone",
                 "tokens": "sculptural shape, concrete or stone, unique materials, artistic design, modern vibe"}
            ],
            "Desk Table": [
                {"name": "Minimalist writing desk with clean lines",
                 "tokens": "minimalist design, clean lines, wooden or metal, functional workspace, modern style"},
                {"name": "Standing desk with adjustable height for modern workspaces",
                 "tokens": "standing design, adjustable height, ergonomic, modern office, sleek frame"},
                {"name": "Vintage wooden desk with intricate carvings",
                 "tokens": "vintage style, wooden finish, intricate carvings, classic design, detailed craftsmanship"}
            ],
            "Outdoor Table": [
                {"name": "Wicker or rattan table for patio settings",
                 "tokens": "wicker or rattan, patio decor, outdoor use, natural texture, weather-resistant"},
                {"name": "Folding metal bistro table for compact spaces",
                 "tokens": "folding design, metal frame, bistro style, compact size, outdoor use"},
                {"name": "Teak or weatherproof wood design for durability",
                 "tokens": "teak wood, weatherproof, durable design, outdoor setting, natural finish"}
            ],
            "Accent Table": [
                {"name": "Round accent table with unique finishes like metallics or ceramics",
                 "tokens": "round shape, metallic or ceramic finish, unique decor, modern style, bold accents"},
                {"name": "C-shaped or nesting accent table for versatile use",
                 "tokens": "C-shaped or nesting, versatile design, compact size, modern or classic, functional decor"},
                {"name": "Table with intricate inlays or mosaic design for a pop of detail",
                 "tokens": "intricate inlays, mosaic design, detailed craftsmanship, artistic touch, luxurious feel"}
            ]
        }
    },
    "Dining Chair": {
        "options": [
            "None",
            "Traditional: Wooden chair with slatted or cross-back design",
            "Modern Minimalist: Upholstered dining chair with clean, straight lines",
            "Scandinavian: Lightwood chair with fabric seat and gentle curves",
            "Industrial: Metal-framed chair with wooden or leather seat",
            "Mid-Century Modern: Chair with molded seat and tapered wooden legs"
        ]
    },
    "Pouf": {
        "options": [
            "None",
            "Classic Pouf",
            "Modern Pouf",
            "Bohemian Pouf",
            "Outdoor Pouf"
        ],
        "subcategories": {
            "Classic Pouf": [
                {"name": "Tufted Leather Pouf",
                 "tokens": "tufted leather, classic design, luxurious feel, plush padding, elegant style"},
                {"name": "Velvet Pouf",
                 "tokens": "velvet fabric, soft texture, classic look, plush comfort, rich colors"}
            ],
            "Modern Pouf": [
                {"name": "Minimalist Pouf",
                 "tokens": "clean lines, neutral tones, modern design, sleek shape, functional decor"},
                {"name": "Geometric Pouf",
                 "tokens": "geometric shapes, bold patterns, modern aesthetic, plush padding, contemporary style"}
            ],
            "Bohemian Pouf": [
                {"name": "Woven Pouf",
                 "tokens": "woven texture, bohemian style, natural materials, vibrant colors, eclectic design"},
                {"name": "Patterned Pouf",
                 "tokens": "patterned fabric, bohemian vibe, layered textiles, artistic feel"}
            ],
            "Outdoor Pouf": [
                {"name": "Weatherproof Pouf",
                 "tokens": "weatherproof material, outdoor use, durable design, vibrant colors, casual seating"}
            ]
        }
    },
    "Armchair": {
        "options": [
            "None",
            "Classic Armchair",
            "Modern Armchair",
            "Contemporary Armchair",
            "Casual and Relaxing Armchair",
            "Industrial and Rustic Armchair",
            "Eclectic and Bold Armchair",
            "Outdoor Armchair"
        ],
        "subcategories": {
            "Classic Armchair": [
                {"name": "Traditional Upholstered Armchair",
                 "tokens": "timeless designs, rolled arms, tufted backs, elegant upholstery, classic style"},
                {"name": "Wingback Chair",
                 "tokens": "high-back chair, elegant flared sides, formal look, plush cushions, sophisticated design"},
                {"name": "Chesterfield Armchair",
                 "tokens": "tufted leather, luxurious appeal, deep buttoning, classic elegance, rich textures"}
            ],
            "Modern Armchair": [
                {"name": "Minimalist Design",
                 "tokens": "clean lines, neutral tones, metal or wooden frames, sleek design, modern aesthetic"},
                {"name": "Scandinavian Armchair",
                 "tokens": "sleek wooden arms and legs, soft fabric cushions, light colors, minimalist style"},
                {"name": "Mid-Century Modern Armchair",
                 "tokens": "angular arms, tapered wooden legs, retro vibes, bold colors, vintage charm"}
            ],
            "Contemporary Armchair": [
                {"name": "Barrel Chair",
                 "tokens": "rounded backrests, wrapping around the seat, modern design, plush upholstery"},
                {"name": "Slipper Armchair",
                 "tokens": "low armless chair, extended seating, contemporary touch, sleek silhouette, minimalist look"},
                {"name": "Cube Armchair",
                 "tokens": "square design, plush cushions, modern interiors, geometric shape, bold style"}
            ],
            "Casual and Relaxing Armchair": [
                {"name": "Recliner",
                 "tokens": "adjustable back, footrest, ultimate comfort, plush padding, casual style"},
                {"name": "Club Chair",
                 "tokens": "deep seating, rounded back, armrests, perfect for lounging"},
                {"name": "Chaise Armchair",
                 "tokens": "extended seat length, relaxing, modern comfort, elegant lines"}
            ],
            "Industrial and Rustic Armchair": [
                {"name": "Leather Armchair",
                 "tokens": "raw aged leather, rugged industrial aesthetic, sturdy build, distressed finish, bold textures"},
                {"name": "Metal Frame Armchair",
                 "tokens": "leather or fabric seat, sturdy metal frame, industrial design, modern edge, raw materials"},
                {"name": "Wooden Armchair",
                 "tokens": "natural finishes, exposed wood, rustic charm, earthy tones, handcrafted feel"}
            ],
            "Eclectic and Bold Armchair": [
                {"name": "Accent Armchair",
                 "tokens": "vibrant colors, patterned fabrics, unique shapes, statement piece, eclectic style"},
                {"name": "Art Deco Armchair",
                 "tokens": "geometric patterns, luxurious materials, velvet or gold accents, bold design, vintage glamour"},
                {"name": "Egg or Ball Chair",
                 "tokens": "futuristic design, curved shell, modern aesthetic, bold statement"}
            ],
            "Outdoor Armchair": [
                {"name": "Wicker Armchair",
                 "tokens": "lightweight, weather-resistant, patio or balcony, natural texture, outdoor comfort"},
                {"name": "Teak Armchair",
                 "tokens": "durable, stylish, outdoor lounging, natural wood finish, weatherproof"},
                {"name": "Sling Armchair",
                 "tokens": "fabric stretched over frame, lightweight metal or wood, modern outdoor design, breathable material, casual seating"}
            ]
        }
    },
    "Buffet": {
        "options": [
            "None",
            "Classic Buffet",
            "Modern Buffet",
            "Industrial Buffet",
            "Rustic Buffet"
        ],
        "subcategories": {
            "Classic Buffet": [
                {"name": "Ornate Wooden Buffet",
                 "tokens": "ornate carvings, wooden finish, classic design, elegant storage, luxurious style"},
                {"name": "Mirrored Buffet",
                 "tokens": "mirrored panels, classic aesthetic, glamorous vibe, reflective surfaces, elegant design"}
            ],
            "Modern Buffet": [
                {"name": "Sleek Minimalist Buffet",
                 "tokens": "clean lines, minimalist design, modern aesthetic, glossy finish, functional storage"},
                {"name": "Mid-Century Buffet",
                 "tokens": "retro design, tapered legs, wooden finish, bold colors, vintage charm"}
            ],
            "Industrial Buffet": [
                {"name": "Metal and Wood Buffet",
                 "tokens": "industrial design, metal frame, wooden top, raw finish, sturdy build"},
                {"name": "Distressed Buffet",
                 "tokens": "distressed finish, industrial style, rugged look, metal accents, functional storage"}
            ],
            "Rustic Buffet": [
                {"name": "Reclaimed Wood Buffet",
                 "tokens": "reclaimed wood, rustic charm, natural finish, earthy tones, handcrafted feel"}
            ]
        }
    },
    "Sideboard": {
        "options": [
            "None",
            "Classic Sideboard",
            "Modern Sideboard",
            "Industrial Sideboard",
            "Rustic Sideboard"
        ],
        "subcategories": {
            "Classic Sideboard": [
                {"name": "Traditional Wooden Sideboard",
                 "tokens": "wooden finish, classic design, ornate details, elegant storage, timeless style"},
                {"name": "Antique Sideboard",
                 "tokens": "antique design, wooden finish, vintage charm, intricate carvings, luxurious feel"}
            ],
            "Modern Sideboard": [
                {"name": "Minimalist Sideboard",
                 "tokens": "clean lines, minimalist design, modern aesthetic, glossy finish, functional storage"},
                {"name": "Mid-Century Sideboard",
                 "tokens": "retro design, tapered legs, wooden finish, bold colors, vintage charm"}
            ],
            "Industrial Sideboard": [
                {"name": "Metal and Wood Sideboard",
                 "tokens": "industrial design, metal frame, wooden top, raw finish, sturdy build"},
                {"name": "Distressed Sideboard",
                 "tokens": "distressed finish, industrial style, rugged look, metal accents, functional storage"}
            ],
            "Rustic Sideboard": [
                {"name": "Reclaimed Wood Sideboard",
                 "tokens": "reclaimed wood, rustic charm, natural finish, earthy tones, handcrafted feel"}
            ]
        }
    },
    "Rug": {
        "options": [
            "None",
            "Outdoor Rug",
            "Bohemian Rug",
            "Modern Rug",
            "Classic Rug"
        ],
        "subcategories": {
            "Outdoor Rug": [
                {"name": "Weatherproof Outdoor Rug",
                 "tokens": "weatherproof material, outdoor use, durable design, vibrant colors, textured pattern"}
            ],
            "Bohemian Rug": [
                {"name": "Patterned Bohemian Rug",
                 "tokens": "bohemian style, vibrant patterns, layered design, artistic feel"}
            ],
            "Modern Rug": [
                {"name": "Geometric Modern Rug",
                 "tokens": "geometric patterns, modern design, neutral tones, sleek texture, contemporary style"}
            ],
            "Classic Rug": [
                {"name": "Persian Classic Rug",
                 "tokens": "classic design, intricate patterns, rich colors, plush texture, luxurious feel"}
            ]
        }
    },
    "Dining table and chairs": {
        "options": [
            "None",
            "two-seat rectangular table",
            "four-seat rectangular table",
            "six-seat rectangular table",
            "Round dining table",
            "Extendable dining table"
        ]
    },
    "Bed": {
        "options": [
            "None",
            "single bed",
            "double bed",
            "queen bed",
            "king bed",
            "canopy bed",
            "platform bed",
            "sleigh bed"
        ]
    },
    "Shelves": {
        "options": [
            "None",
            "floating shelf",
            "wall-mounted shelf",
            "bookshelf",
            "corner shelf"
        ]
    },
    "Floor Lamp": {
        "options": [
            "None",
            "Minimalist Floor Lamp",
            "Industrial Floor Lamp",
            "Modern Floor Lamp",
            "Classic Floor Lamp"
        ],
        "subcategories": {
            "Minimalist Floor Lamp": [
                {"name": "Sleek Minimalist Floor Lamp",
                 "tokens": "sleek design, minimalist style, neutral tones, metal frame, modern lighting"}
            ],
            "Industrial Floor Lamp": [
                {"name": "Metal Industrial Floor Lamp",
                 "tokens": "industrial design, metal frame, raw finish, exposed bulb, modern edge"}
            ],
            "Modern Floor Lamp": [
                {"name": "Arched Modern Floor Lamp",
                 "tokens": "modern design, arched shape, sleek frame, ambient lighting, contemporary style"}
            ],
            "Classic Floor Lamp": [
                {"name": "Traditional Floor Lamp",
                 "tokens": "classic design, fabric shade, wooden base, warm lighting, elegant style"}
            ]
        }
    },
    "Table Lamp": {
        "options": [
            "None",
            "Classic Table Lamp",
            "Modern Table Lamp",
            "Industrial Table Lamp",
            "Minimalist Table Lamp"
        ],
        "subcategories": {
            "Classic Table Lamp": [
                {"name": "Traditional Table Lamp",
                 "tokens": "classic design, fabric shade, wooden base, warm lighting, elegant style"}
            ],
            "Modern Table Lamp": [
                {"name": "Geometric Modern Table Lamp",
                 "tokens": "modern design, geometric shape, sleek frame, ambient lighting, contemporary style"}
            ],
            "Industrial Table Lamp": [
                {"name": "Metal Industrial Table Lamp",
                 "tokens": "industrial design, metal frame, raw finish, exposed bulb, modern edge"}
            ],
            "Minimalist Table Lamp": [
                {"name": "Sleek Minimalist Table Lamp",
                 "tokens": "sleek design, minimalist style, neutral tones, metal frame, modern lighting"}
            ]
        }
    }
}

# Настройка ширины боковой панели и отступов через CSS
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        width: 300px !important;
    }
    [data-testid="stSidebar"] > div:first-child {
        width: 300px !important;
    }
    /* Уменьшаем отступ от сайдбара */
    .main-content {
        margin-left: 310px !important;
        padding-left: 10px !important;
    }
    /* Уточняем селектор для основной области Streamlit */
    [data-testid="stAppViewContainer"] > div:first-child {
        margin-left: 310px !important;
    }
    .title-container {
        position: sticky;
        top: 0;
        padding: 10px;
        z-index: 100;
        text-align: left !important; /* Выравнивание названия влево */
        background-color: transparent; /* Убираем фон */
    }
    .title-container h1 {
        text-align: left !important; /* Дополнительное выравнивание */
        display: inline-flex;
        align-items: center;
    }
    .title-container img {
        margin-right: 10px; /* Отступ между логотипом и текстом */
        vertical-align: middle;
    }
    /* Стили для кнопок */
    .stButton button {
        background-color: #353c58;
        color: white;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #2a2f45;
    }
    /* Стили для кнопки Quality Prompt */
    .quality-enabled {
        background-color: #285319 !important;
        color: white !important;
    }
    /* Стили для кнопки Negative Prompt */
    .negative-enabled {
        background-color: #531919 !important;
        color: white !important;
    }
    .stTextArea textarea {
        background-color: #2a2a3e;
        color: white;
        word-wrap: break-word;
    }
    .stMarkdown {
        color: white;
    }
    @media (max-width: 600px) {
        .main-content {
            margin-left: 10px !important;
            padding-left: 10px !important;
        }
        [data-testid="stSidebar"] {
            width: 100% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Название в основной области с логотипом
st.markdown(
    """
    <div class="title-container">
        <h1 style="color: white; margin: 0;">
            <img src="https://raw.githubusercontent.com/Andriy-Lysenko/Prompt_Gen/refs/heads/main/Logo_white.png?token=GHSAT0AAAAAADAFMWJDSRA4ECXKHOUFRO5QZ7D6QOQ" width="60" height="60">
            Nfinite Prompt Generator
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Инициализация состояния для полей, чтобы гарантировать "None" по умолчанию
if "style" not in st.session_state:
    st.session_state.style = "None"
if "camera" not in st.session_state:
    st.session_state.camera = "None"
if "lighting" not in st.session_state:
    st.session_state.lighting = "None"
if "fov" not in st.session_state:
    st.session_state.fov = "None"
if "furniture_type" not in st.session_state:
    st.session_state.furniture_type = "None"
if "furniture_subtype" not in st.session_state:
    st.session_state.furniture_subtype = "None"
if "material" not in st.session_state:
    st.session_state.material = "None"
if "color_palette" not in st.session_state:
    st.session_state.color_palette = "None"
if "room_type" not in st.session_state:
    st.session_state.room_type = "None"
if "model_type" not in st.session_state:
    st.session_state.model_type = "Fooocus"
if "main_prompt" not in st.session_state:
    st.session_state.main_prompt = ""
if "quality_enabled" not in st.session_state:
    st.session_state.quality_enabled = False
if "negative_enabled" not in st.session_state:
    st.session_state.negative_enabled = False
if "saved_configs" not in st.session_state:
    st.session_state.saved_configs = []

# Обёртка для основной области с классом для отступа
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Боковая панель для ввода данных
with st.sidebar:
    st.header("Furniture Details")
    furniture_type = st.selectbox(
        "Select Furniture Type",
        ["None"] + sorted([key for key in subject_subcategories.keys() if key != "None"]),
        index=0,
        key="furniture_type",
        help="Choose the type of furniture to visualize. Options include sofas, tables, chairs, and more."
    )
    furniture_subtype = st.selectbox(
        "Select Furniture Subtype",
        sorted(subject_subcategories[furniture_type]["options"]),
        index=0,
        key="furniture_subtype",
        help="Select a specific subtype of the furniture. For example, a 'Coffee Table' or 'Dining Chair'."
    )
    material = st.selectbox(
        "Select Material",
        ["None", "Leather", "Wood", "Fabric", "Metal"],
        index=0,
        key="material",
        help="Choose the material of the furniture. For example, 'Leather' for a sofa or 'Wood' for a table."
    )
    color_palette = st.selectbox(
        "Select Color Palette",
        sorted(color_palettes.keys()),
        index=0,
        key="color_palette",
        help="Choose the color palette for the furniture."
    )

    st.header("Room Settings")
    room_type = st.selectbox(
        "Select Room Type",
        ["None", "Living Room", "Bedroom", "Dining Room", "Office", "Kitchen", "Bathroom", "Hallway", "Patio", "Study", "Lounge"],
        index=0,
        key="room_type",
        help="Select the type of room for the visualization or select None to skip."
    )
    style = st.selectbox(
        "Select Style",
        sorted(style_prompts.keys()),
        index=0,
        key="style",
        help="Choose the interior design style or select None to skip."
    )

    st.header("Camera Control")
    camera = st.selectbox(
        "Select Camera Angle/View",
        sorted(camera_control.keys()),
        index=0,
        key="camera",
        help="Choose the camera angle for the shot."
    )

    st.header("Lighting Control")
    lighting = st.selectbox(
        "Select Lighting",
        sorted(lighting_control.keys()),
        index=0,
        key="lighting",
        help="Choose the lighting conditions for the scene."
    )

    st.header("FOV")
    fov = st.selectbox(
        "Select Field of View",
        sorted(fov_control.keys()),
        index=0,
        key="fov",
        help="Choose the field of view for the shot."
    )

    st.header("Prompt Settings")
    max_length = st.slider("Max Prompt Length", min_value=100, max_value=1000, value=400, step=50, help="Set the maximum character limit for the optimized prompt.")

    st.header("Quality and Negative Prompts")
    quality_button_class = "quality-enabled" if st.session_state.quality_enabled else ""
    if st.button("Enable Quality Prompt", key="quality_btn", help="Add high-quality rendering tokens to the prompt"):
        st.session_state.quality_enabled = not st.session_state.quality_enabled
        st.rerun()

    st.markdown(f'<script>document.querySelector("button[data-testid=\'stButton\'][key=\'quality_btn\']").classList.add("{quality_button_class}");</script>', unsafe_allow_html=True)

    negative_button_class = "negative-enabled" if st.session_state.negative_enabled else ""
    if st.button("Enable Negative Prompt", key="negative_btn", help="Add negative rendering tokens to exclude unwanted elements"):
        st.session_state.negative_enabled = not st.session_state.negative_enabled
        st.rerun()
    st.markdown(f'<script>document.querySelector("button[data-testid=\'stButton\'][key=\'negative_btn\']").classList.add("{negative_button_class}");</script>', unsafe_allow_html=True)

# Основная область
st.markdown("<br>", unsafe_allow_html=True)

# Функция для генерации описания мебели
def get_furniture_description():
    furniture_type = st.session_state.furniture_type
    subtype = st.session_state.furniture_subtype
    material = st.session_state.material
    color_palette = st.session_state.color_palette

    # If furniture type or subtype is "None", return an empty string
    if furniture_type == "None" or subtype == "None":
        return ""

    # Base description starts with the subtype
    desc = f"A {subtype}"

    # Add material if not "None"
    if material != "None":
        desc += f" made of {material}"
    
    # Add color palette if not "None"
    if color_palette != "None":
        desc += f" in a {color_palette} palette"

    # Add subcategory tokens if available
    if 'subcategories' in subject_subcategories[furniture_type] and subtype in subject_subcategories[furniture_type]['subcategories']:
        for sub in subject_subcategories[furniture_type]['subcategories'][subtype]:
            if sub['name'] == subtype:
                desc += f", {sub['tokens']}"
                break

    # Special case for Bedside/Side Table
    if furniture_type == "Table" and (subtype == "Bedside Table" or subtype == "Side Table"):
        desc = f"A stylish {subtype}"
        if material != "None":
            desc += f" made of {material}"
        if color_palette != "None":
            desc += f" in a {color_palette} palette"
        desc += ", featuring sturdy construction, smooth surface, modern design, and functional decor"

    return desc

# Функция для генерации промпта
def generate_prompt(model_type="Fooocus"):
    # Furniture description (might be empty if all are "None")
    furniture_desc = get_furniture_description()

    # Room and background description with style tokens
    if st.session_state.room_type != "None" and st.session_state.style != "None":
        room_desc = f" in a {st.session_state.style} {st.session_state.room_type} with a detailed interior featuring visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity {style_prompts[st.session_state.style]}"
    elif st.session_state.room_type != "None":
        room_desc = f" in a {st.session_state.room_type} with a detailed interior featuring visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity"
    else:
        room_desc = " in a detailed indoor setting with visible furniture, plain walls, and distinct decor elements, all rendered with crisp clarity"

    # Lighting description (skip if "None")
    lighting_desc = f" with {lighting_control[st.session_state.lighting]}" if st.session_state.lighting != "None" else " with clear daylight illuminating the scene, highlighting all details"

    # FOV and Camera Control logic
    fov = st.session_state.fov
    camera = st.session_state.camera
    view_desc = ""

    if fov != "None" and camera != "None":
        if camera == "3/4 view":
            # For 3/4 view: "FOV + Camera Control"
            view_desc = f"{fov_control[fov].lower()} view from a {camera_control[camera]}"
        else:
            # For other camera angles: "Camera Control + FOV"
            view_desc = f"{fov_control[fov]} {camera_control[camera]}"
    elif fov != "None":
        view_desc = f"{fov_control[fov]}"
    elif camera != "None":
        view_desc = f"from a {camera_control[camera]}"

    # Combine view description with furniture description
    if view_desc and furniture_desc:
        prompt_start = f"{view_desc} of {furniture_desc.lower()}"
    elif furniture_desc:
        prompt_start = furniture_desc
    else:
        prompt_start = ""

    # Default centering phrase (always included if furniture is specified)
    centering_desc = f" The {st.session_state.furniture_subtype} is positioned in the center of a composition." if furniture_desc else ""

    # Combine the prompt
    if prompt_start:
        prompt = f"{prompt_start}{room_desc}{lighting_desc}{centering_desc}"
    else:
        prompt = f"{room_desc[1:]}{lighting_desc}"  # Remove leading " in" for grammatical correctness

    # Add quality tokens if enabled
    if st.session_state.quality_enabled:
        prompt += " " + quality_tokens
    return prompt

# Генерируем начальный промпт и сохраняем в session_state
if not st.session_state.main_prompt:
    st.session_state.main_prompt = generate_prompt()

# Обновляем промпт при каждом рендере
st.session_state.main_prompt = generate_prompt(st.session_state.model_type)

# Окно для негативного промпта
negative_prompt = ""
if st.session_state.negative_enabled:
    negative_prompt = negative_tokens

# Главный промпт с кнопкой копирования (закомментировано)
st.subheader("Generated Prompt")
main_prompt_input = st.text_area("Generated Prompt", value=st.session_state.main_prompt, height=200, key="main_prompt_area")
st.markdown(
    f'<style>.stTextArea textarea {{ background-color: #2a2a3e; color: white; word-wrap: break-word; }}</style>',
    unsafe_allow_html=True
)

# Закомментируем кнопку копирования
# if st.button("Copy Main Prompt to Clipboard", key="copy_main_btn"):
#     try:
#         pyperclip.copy(main_prompt_input)
#         st.success("Main prompt copied to clipboard!")
#     except pyperclip.PyperclipException:
#         st.error("Unable to copy to clipboard. Please manually copy the prompt above. Ensure 'xclip' or 'xsel' is installed on your system if you're on Linux.")

st.markdown("<br>", unsafe_allow_html=True)

# Негативный промпт с кнопкой копирования (закомментировано)
st.subheader("Negative Prompt")
negative_prompt_input = st.text_area("Negative Prompt", value=negative_prompt, height=150, key="negative_prompt_area")
st.markdown(
    f'<style>.stTextArea textarea {{ background-color: #2a2a3e; color: white; word-wrap: break-word; }}</style>',
    unsafe_allow_html=True
)

# Закомментируем кнопку копирования
# if st.button("Copy Negative Prompt to Clipboard", key="copy_negative_btn"):
#     try:
#         pyperclip.copy(negative_prompt_input)
#         st.success("Negative prompt copied to clipboard!")
#     except pyperclip.PyperclipException:
#         st.error("Unable to copy to clipboard. Please manually copy the prompt above. Ensure 'xclip' or 'xsel' is installed on your system if you're on Linux.")

# Кнопка для сброса настроек
if st.button("Reset Settings", help="Reset all settings to default"):
    st.session_state.clear()
    st.rerun()

# Кнопка для сохранения настроек
st.divider()
if st.button("Save Configuration", help="Save the current configuration"):
    config = {
        "furniture_type": st.session_state.furniture_type,
        "furniture_subtype": st.session_state.furniture_subtype,
        "material": st.session_state.material,
        "color_palette": st.session_state.color_palette,
        "room_type": st.session_state.room_type,
        "style": st.session_state.style,
        "camera": st.session_state.camera,
        "lighting": st.session_state.lighting,
        "fov": st.session_state.fov,
        "quality_enabled": st.session_state.quality_enabled,
        "negative_enabled": st.session_state.negative_enabled,
        "model_type": st.session_state.model_type,
        "main_prompt": main_prompt_input,
        "negative_prompt": negative_prompt_input
    }
    st.session_state.saved_configs.append(config)
    st.success("Configuration saved!")

# Кнопка для загрузки сохранённых настроек
if st.session_state.saved_configs:
    st.subheader("Load Saved Configuration")
    config_names = [f"Configuration {i+1}" for i in range(len(st.session_state.saved_configs))]
    selected_config = st.selectbox("Select a saved configuration", config_names)
    if st.button("Load Selected Configuration", help="Load the selected configuration"):
        config_index = config_names.index(selected_config)
        config = st.session_state.saved_configs[config_index]
        st.session_state.furniture_type = config["furniture_type"]
        st.session_state.furniture_subtype = config["furniture_subtype"]
        st.session_state.material = config["material"]
        st.session_state.color_palette = config["color_palette"]
        st.session_state.room_type = config["room_type"]
        st.session_state.style = config["style"]
        st.session_state.camera = config["camera"]
        st.session_state.lighting = config["lighting"]
        st.session_state.fov = config["fov"]
        st.session_state.quality_enabled = config["quality_enabled"]
        st.session_state.negative_enabled = config["negative_enabled"]
        st.session_state.model_type = config["model_type"]
        st.session_state.main_prompt = config["main_prompt"]
        st.success("Configuration loaded!")
        st.rerun()

# Показ сохранённых настроек
if st.session_state.saved_configs:
    st.subheader("Saved Configurations")
    st.write(st.session_state.saved_configs)

# Закрытие обёртки основной области
st.markdown('</div>', unsafe_allow_html=True)

# Экспорт промптов в JSON или TXT
if st.button("Export Prompts to JSON", key="export_json_btn"):
    config = {
        "main_prompt": st.session_state.main_prompt,
        "negative_prompt": negative_prompt_input
    }
    json_str = json.dumps(config, indent=4)
    st.download_button(
        label="Download JSON",
        data=json_str,
        file_name="prompts.json",
        mime="application/json"
    )

if st.button("Export Prompts to TXT", key="export_txt_btn"):
    txt_content = f"Main Prompt:\n{st.session_state.main_prompt}\n\nNegative Prompt:\n{negative_prompt_input}"
    st.download_button(
        label="Download TXT",
        data=txt_content,
        file_name="prompts.txt",
        mime="text/plain"
    )
