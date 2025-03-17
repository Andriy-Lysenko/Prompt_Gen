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

# Контроль над камерой
camera_control = {
    "None": "",
    "Close-up": "focusing on the details of the furniture",
    "Mid-range": "capturing the furniture and its immediate surroundings",
    "Wide-angle": "showing the entire room with the furniture as the focal point",
    "20% angle": "featuring a slightly angled view to add depth and perspective",
    "Full interior": "showcasing the entire room layout",
    "A little above view": "providing a slightly elevated view to give a better sense of space and arrangement",
    "3/4 view": "positioned at an angle, allowing the viewer to see both its front and side"
}

# Контроль над освещением
lighting_control = {
    "None": "",
    "Soft natural daylight": "with soft natural daylight streaming through large windows, creating a warm and inviting atmosphere",
    "Evening mood lighting": "with evening mood lighting featuring soft, warm tones to create an inviting ambiance",
    "Studio lighting": "with studio lighting providing balanced brightness to highlight the furniture details",
    "Golden hour": "with golden hour lighting featuring warm, golden tones to enhance the textures and colors",
    "Overcast lighting": "with overcast lighting providing diffused natural light for a calm and serene atmosphere"
}

# Контроль над позицией продукта
position_control = {
    "None": "",
    "Center": "positioned in the center of the frame, drawing immediate attention",
    "Left side": "placed on the left side of the frame, creating a balanced composition",
    "Right side": "placed on the right side of the frame, adding visual interest",
    "Foreground": "in the foreground, with the rest of the room in the background",
    "Background": "in the background, with other elements in the foreground to create depth"
}

# Токены для качества
quality_tokens = "Hyperrealistic 3D rendering, ultra-detailed, 8K resolution, photorealistic, cinematic quality, sharp focus, lifelike lighting, realistic shadows, intricate details, crystal-clear image quality, bright lighting, vivid colors."

# Токены для негативного промпта
negative_tokens = "busy patterns, dark lighting, cluttered, artificial colors, cartoon style, low resolution, blurry, noisy, grainy, distorted proportions, unrealistic textures, harsh shadows, oversaturated colors, highly decorated, chaotic composition, rough surfaces, childish design, unrefined edges, gaudy colors, overly complex, heavy appearance, dirty, worn, antique, steampunk elements, depth of field, yellow walls, warm walls, nude, NSFW."

# Полный словарь subject_subcategories
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
        ],
        "tokens": "featuring comfortable seating, plush cushions, modern design, elegant upholstery, and a sturdy frame"
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
        },
        "tokens": "featuring sturdy construction, smooth surface, modern design, wooden or glass top, and functional decor"
    },
    "Dining Chair": {
        "options": [
            "None",
            "Traditional: Wooden chair with slatted or cross-back design",
            "Modern Minimalist: Upholstered dining chair with clean, straight lines",
            "Scandinavian: Lightwood chair with fabric seat and gentle curves",
            "Industrial: Metal-framed chair with wooden or leather seat",
            "Mid-Century Modern: Chair with molded seat and tapered wooden legs"
        ],
        "tokens": "featuring ergonomic design, comfortable seating, stylish frame, upholstered or wooden construction, and a modern or classic look"
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
        },
        "tokens": "featuring plush padding, versatile design, modern or classic style, and a decorative accent"
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
        },
        "tokens": "featuring plush upholstery, elegant design, high backrest, comfortable seating, and a modern or vintage look"
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
        },
        "tokens": "featuring elegant storage, sturdy build, decorative accent, modern or classic design, and functional decor"
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
        },
        "tokens": "featuring functional storage, sturdy build, decorative accent, modern or classic design, and elegant decor"
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
        },
        "tokens": "featuring vibrant patterns, durable material, modern or classic style, and a decorative accent"
    },
    "Dining table and chairs": {
        "options": [
            "None",
            "two-seat rectangular table",
            "four-seat rectangular table",
            "six-seat rectangular table",
            "Round dining table",
            "Extendable dining table"
        ],
        "tokens": "featuring sturdy construction, elegant design, functional dining set, modern or classic style, and comfortable seating"
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
        ],
        "tokens": "featuring comfortable bedding, sturdy frame, elegant headboard, modern or classic design, and a supportive mattress"
    },
    "Shelves": {
        "options": [
            "None",
            "floating shelf",
            "wall-mounted shelf",
            "bookshelf",
            "corner shelf"
        ],
        "tokens": "featuring functional storage, sleek design, modern or classic style, sturdy build, and a decorative accent"
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
        },
        "tokens": "featuring ambient lighting, sturdy base, modern or classic design, elegant style, and functional decor"
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
        },
        "tokens": "featuring ambient lighting, sleek design, modern or classic style, elegant look, and functional decor"
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
            <img src="https://via.placeholder.com/30" alt="Nfinite Logo" width="30" height="30">
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
if "position" not in st.session_state:
    st.session_state.position = "Center"
if "furniture_type" not in st.session_state:
    st.session_state.furniture_type = "None"
if "furniture_subtype" not in st.session_state:
    st.session_state.furniture_subtype = "None"
if "material" not in st.session_state:
    st.session_state.material = "None"
if "color" not in st.session_state:
    st.session_state.color = "None"
if "room_type" not in st.session_state:
    st.session_state.room_type = "None"
if "model_type" not in st.session_state:
    st.session_state.model_type = "Fooocus"  # По умолчанию Fooocus
if "main_prompt" not in st.session_state:
    st.session_state.main_prompt = ""  # Храним промпт в session_state
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
    color = st.selectbox(
        "Select Color",
        ["None", "Beige", "Black", "White", "Gray", "Brown", "Blue", "Green", "Red", "Yellow", "Purple", "Pink", "Navy", "Teal"],
        index=0,
        key="color",
        help="Choose the color of the furniture. For example, 'Beige' for a neutral look or 'Blue' for a pop of color."
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

    st.header("Product Position")
    position = st.selectbox(
        "Select Product Position",
        sorted(position_control.keys()),
        index=1,  # Устанавливаем "Center" по умолчанию
        key="position",
        help="Choose the position of the furniture in the frame."
    )

    st.header("Prompt Settings")
    max_length = st.slider("Max Prompt Length", min_value=100, max_value=1000, value=400, step=50, help="Set the maximum character limit for the optimized prompt.")

    st.header("Quality and Negative Prompts")
    # Кнопка для Quality Prompt с динамическим классом
    quality_button_class = "quality-enabled" if st.session_state.quality_enabled else ""
    if st.button("Enable Quality Prompt", key="quality_btn", help="Add high-quality rendering tokens to the prompt"):
        st.session_state.quality_enabled = not st.session_state.quality_enabled
        st.rerun()

    # Применяем класс подсветки после рендеринга кнопки
    st.markdown(f'<script>document.querySelector("button[data-testid=\'stButton\'][key=\'quality_btn\']").classList.add("{quality_button_class}");</script>', unsafe_allow_html=True)

    # Кнопка для Negative Prompt с динамическим классом
    negative_button_class = "negative-enabled" if st.session_state.negative_enabled else ""
    if st.button("Enable Negative Prompt", key="negative_btn", help="Add negative rendering tokens to exclude unwanted elements"):
        st.session_state.negative_enabled = not st.session_state.negative_enabled
        st.rerun()
    st.markdown(f'<script>document.querySelector("button[data-testid=\'stButton\'][key=\'negative_btn\']").classList.add("{negative_button_class}");</script>', unsafe_allow_html=True)

# Основная область
st.markdown("<br>", unsafe_allow_html=True)

# Функция для генерации промпта
def get_furniture_description():
    if st.session_state.furniture_type == "Table" and (st.session_state.furniture_subtype == "Bedside Table" or st.session_state.furniture_subtype == "Side Table"):
        return f"A stylish {st.session_state.furniture_subtype} as the main focus, made of {st.session_state.material} in {st.session_state.color}, featuring sturdy construction, smooth surface, modern design, and functional decor."
    else:
        return f"A {st.session_state.furniture_subtype} made of {st.session_state.material} in {st.session_state.color}, featuring {subject_subcategories[st.session_state.furniture_type]['tokens']}."

def get_room_description():
    if st.session_state.room_type != "None" and st.session_state.style != "None":
        return f" in a {st.session_state.style} {st.session_state.room_type}"
    return ""

def generate_prompt(model_type="Fooocus"):
    furniture_desc = get_furniture_description()
    room_desc = get_room_description()
    lighting_desc = f" with {lighting_control[st.session_state.lighting]}" if st.session_state.lighting != "None" else ""
    camera_desc = f" Captured in a {camera_control[st.session_state.camera]} view." if st.session_state.camera != "None" else ""
    position_desc = f" The {st.session_state.furniture_subtype} is {position_control[st.session_state.position]}." if st.session_state.position != "None" else ""
    
    prompt = f"{furniture_desc}{room_desc}{lighting_desc}{camera_desc}{position_desc}"
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

# Кнопки Optimize, Flux и Обновить
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("Optimize", key="optimize_btn", help=f"Optimize the prompt to fit within {max_length} characters"):
        main_prompt = optimize_prompt(st.session_state.main_prompt, max_length)
        st.session_state.main_prompt = main_prompt
        st.rerun()
with col2:
    if st.button("Flux", key="flux_btn", help="Switch to Flux model prompt"):
        st.session_state.model_type = "Flux"
        st.session_state.main_prompt = generate_prompt("Flux")
        st.rerun()
with col3:
    if st.button("Обновить", key="refresh_btn", help="Regenerate the current prompt"):
        st.session_state.main_prompt = generate_prompt(st.session_state.model_type)
        st.rerun()

# Главный промпт с кнопкой копирования
st.subheader("Generated Prompt")
main_prompt_input = st.text_area("", value=st.session_state.main_prompt, height=200, key="main_prompt_area")
st.markdown(
    f'<style>.stTextArea textarea {{ background-color: #2a2a3e; color: white; word-wrap: break-word; }}</style>',
    unsafe_allow_html=True
)
if st.button("Copy Main Prompt to Clipboard", key="copy_main_btn"):
    pyperclip.copy(main_prompt_input)
    st.success("Main prompt copied to clipboard!")

st.markdown("<br>", unsafe_allow_html=True)

# Негативный промпт с кнопкой копирования
st.subheader("Negative Prompt")
negative_prompt_input = st.text_area("", value=negative_prompt, height=150, key="negative_prompt_area")
st.markdown(
    f'<style>.stTextArea textarea {{ background-color: #2a2a3e; color: white; word-wrap: break-word; }}</style>',
    unsafe_allow_html=True
)
if st.button("Copy Negative Prompt to Clipboard", key="copy_negative_btn"):
    pyperclip.copy(negative_prompt_input)
    st.success("Negative prompt copied to clipboard!")

st.markdown("<br>", unsafe_allow_html=True)

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
        "color": st.session_state.color,
        "room_type": st.session_state.room_type,
        "style": st.session_state.style,
        "camera": st.session_state.camera,
        "lighting": st.session_state.lighting,
        "position": st.session_state.position,
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
        st.session_state.color = config["color"]
        st.session_state.room_type = config["room_type"]
        st.session_state.style = config["style"]
        st.session_state.camera = config["camera"]
        st.session_state.lighting = config["lighting"]
        st.session_state.position = config["position"]
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

# Функция оптимизации промпта
def optimize_prompt(prompt, max_length=400):
    if len(prompt) <= max_length:
        return prompt
    words = prompt.split()
    optimized = []
    word_count = 0
    for word in words:
        if word_count + len(word) + 1 <= max_length:
            optimized.append(word)
            word_count += len(word) + 1
        else:
            break
    optimized_prompt = " ".join(optimized) + "... (optimized)"
    if len(optimized_prompt) > max_length:
        st.warning(f"Prompt still exceeds {max_length} characters after optimization. Consider reducing the input.")
    return optimized_prompt
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