import streamlit as st

# Промпты для каждого стиля
style_prompts = {
    "Bohemian": "A bohemian room with eclectic decor, vibrant colors, mixed patterns, and layered textiles. The space features natural materials, global influences, and cozy, artistic elements.",
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
    "A little above view": "A slightly elevated view to provide a better sense of space and arrangement"
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
negative_tokens = "busy patterns, dark lighting, cluttered, artificial colors, cartoon style, low resolution, blurry, noisy, grainy, distorted proportions, unrealistic textures, harsh shadows, oversaturated colors, highly decorated, chaotic composition, rough surfaces, childish design, unrefined edges, gaudy colors, overly complex, heavy appearance, dirty, worn, antique, steampunk elements, depth of field, yellow walls, warm walls, nude, NSFW."

# Словарь subject_subcategories
subject_subcategories = {
    "Sofa": {
        "options": [
            "2-seated sofa", "3-seated sofa", "4-seated sofa", "corner sofa",
            "L-shaped sofa", "sectional sofa", "sleeper sofa", "chaise sofa",
            "loveseat", "recliner sofa", "modular sofa", "curved sofa",
            "tufted sofa", "mid-century sofa", "chesterfield sofa"
        ],
        "tokens": "comfortable seating, plush cushions, modern design, elegant upholstery, sturdy frame"
    },
    "Table": {
        "options": ["Coffee Tables", "Dining Tables", "Side Tables", "Console Tables", "Bedside Tables",
                    "Desk Tables", "Outdoor Tables", "Accent Tables"],
        "subcategories": {
            "Coffee Tables": [
                {"name": "Round or oval wooden tables with a minimalist design",
                 "tokens": "round or oval shape, wooden finish, minimalist design, sleek legs, neutral tones"},
                {"name": "Glass-topped tables with metal or wooden bases",
                 "tokens": "glass top, metal or wooden base, modern aesthetic, reflective surface, sturdy frame"},
                {"name": "Nesting coffee tables for a modular and modern feel",
                 "tokens": "nesting design, modular layout, modern style, wooden or metal, compact storage"}
            ],
            "Dining Tables": [
                {"name": "Farmhouse-style tables with a rustic wood finish",
                 "tokens": "rustic wood, farmhouse style, sturdy legs, distressed finish, warm tones"},
                {"name": "Rectangular tables with sleek glass or marble tops",
                 "tokens": "rectangular shape, glass or marble top, sleek design, modern elegance, polished surface"},
                {"name": "Extendable dining tables for versatility and functionality",
                 "tokens": "extendable design, versatile layout, wooden or glass, functional decor, modern or classic"}
            ],
            "Side Tables": [
                {"name": "Small, modern tables with geometric frames",
                 "tokens": "small size, geometric frame, modern design, metal or wood, compact style"},
                {"name": "Ceramic pedestal tables for an artistic statement",
                 "tokens": "ceramic top, pedestal base, artistic design, unique shape, bold colors"},
                {"name": "Natural wood stump tables for a touch of organic design",
                 "tokens": "natural wood, organic shape, rustic feel, unique texture, earthy tones"}
            ],
            "Console Tables": [
                {"name": "Slim, metal-framed tables for hallways or entryways",
                 "tokens": "slim design, metal frame, hallway decor, modern style, functional top"},
                {"name": "Mirrored console tables for a glamorous vibe",
                 "tokens": "mirrored surface, glamorous style, elegant frame, reflective finish, luxurious feel"},
                {"name": "Multi-tiered designs for added storage and display",
                 "tokens": "multi-tiered, storage design, modern or classic, display space, wooden or metal"}
            ],
            "Bedside Tables": [
                {"name": "Classic nightstands with a drawer and open shelf",
                 "tokens": "classic design, drawer and shelf, wooden finish, bedside use, traditional style"},
                {"name": "Floating wall-mounted tables for a space-saving option",
                 "tokens": "floating design, wall-mounted, space-saving, modern style, minimalist look"},
                {"name": "Sculptural bedside tables with unique materials like concrete or stone",
                 "tokens": "sculptural shape, concrete or stone, unique materials, artistic design, modern vibe"}
            ],
            "Desk Tables": [
                {"name": "Minimalist writing desks with clean lines",
                 "tokens": "minimalist design, clean lines, wooden or metal, functional workspace, modern style"},
                {"name": "Standing desks with adjustable heights for modern workspaces",
                 "tokens": "standing design, adjustable height, ergonomic, modern office, sleek frame"},
                {"name": "Vintage wooden desks with intricate carvings",
                 "tokens": "vintage style, wooden finish, intricate carvings, classic design, detailed craftsmanship"}
            ],
            "Outdoor Tables": [
                {"name": "Wicker or rattan tables for patio settings",
                 "tokens": "wicker or rattan, patio decor, outdoor use, natural texture, weather-resistant"},
                {"name": "Folding metal bistro tables for compact spaces",
                 "tokens": "folding design, metal frame, bistro style, compact size, outdoor use"},
                {"name": "Teak or weatherproof wood designs for durability",
                 "tokens": "teak wood, weatherproof, durable design, outdoor setting, natural finish"}
            ],
            "Accent Tables": [
                {"name": "Round accent tables with unique finishes like metallics or ceramics",
                 "tokens": "round shape, metallic or ceramic finish, unique decor, modern style, bold accents"},
                {"name": "C-shaped or nesting accent tables for versatile use",
                 "tokens": "C-shaped or nesting, versatile design, compact size, modern or classic, functional decor"},
                {"name": "Tables with intricate inlays or mosaic designs for a pop of detail",
                 "tokens": "intricate inlays, mosaic design, detailed craftsmanship, artistic touch, luxurious feel"}
            ]
        },
        "tokens": "sturdy construction, smooth surface, modern design, wooden or glass top, functional decor"
    },
    "Dining Chair": {
        "options": [
            "Traditional: Wooden chairs with slatted or cross-back designs",
            "Modern Minimalist: Upholstered dining chairs with clean, straight lines",
            "Scandinavian: Lightwood chairs with fabric seats and gentle curves",
            "Industrial: Metal-framed chairs with wooden or leather seats",
            "Mid-Century Modern: Chairs with molded seats and tapered wooden legs"
        ],
        "tokens": "ergonomic design, comfortable seating, stylish frame, upholstered or wooden, modern or classic"
    },
    "Pouf": {
        "options": [
            "Classic Poufs",
            "Modern Poufs",
            "Bohemian Poufs",
            "Outdoor Poufs"
        ],
        "subcategories": {
            "Classic Poufs": [
                {"name": "Tufted Leather Poufs",
                 "tokens": "tufted leather, classic design, luxurious feel, plush padding, elegant style"},
                {"name": "Velvet Poufs",
                 "tokens": "velvet fabric, soft texture, classic look, plush comfort, rich colors"}
            ],
            "Modern Poufs": [
                {"name": "Minimalist Poufs",
                 "tokens": "clean lines, neutral tones, modern design, sleek shape, functional decor"},
                {"name": "Geometric Poufs",
                 "tokens": "geometric shapes, bold patterns, modern aesthetic, plush padding, contemporary style"}
            ],
            "Bohemian Poufs": [
                {"name": "Woven Poufs",
                 "tokens": "woven texture, bohemian style, natural materials, vibrant colors, eclectic design"},
                {"name": "Patterned Poufs",
                 "tokens": "patterned fabric, bohemian vibe, layered textiles, cozy feel, artistic touch"}
            ],
            "Outdoor Poufs": [
                {"name": "Weatherproof Poufs",
                 "tokens": "weatherproof material, outdoor use, durable design, vibrant colors, casual seating"}
            ]
        },
        "tokens": "cozy seating, plush padding, versatile design, modern or classic, decorative accent"
    },
    "Armchair": {
        "options": [
            "Classic Armchairs",
            "Modern Armchairs",
            "Contemporary Armchairs",
            "Casual and Relaxing Armchairs",
            "Industrial and Rustic Armchairs",
            "Eclectic and Bold Armchairs",
            "Outdoor Armchairs"
        ],
        "subcategories": {
            "Classic Armchairs": [
                {"name": "Traditional Upholstered Armchairs",
                 "tokens": "timeless designs, rolled arms, tufted backs, elegant upholstery, classic style"},
                {"name": "Wingback Chairs",
                 "tokens": "high-back chairs, elegant flared sides, formal look, plush cushions, sophisticated design"},
                {"name": "Chesterfield Armchairs",
                 "tokens": "tufted leather, luxurious appeal, deep buttoning, classic elegance, rich textures"}
            ],
            "Modern Armchairs": [
                {"name": "Minimalist Designs",
                 "tokens": "clean lines, neutral tones, metal or wooden frames, sleek design, modern aesthetic"},
                {"name": "Scandinavian Armchairs",
                 "tokens": "sleek wooden arms and legs, soft fabric cushions, light colors, minimalist style, cozy feel"},
                {"name": "Mid-Century Modern Armchairs",
                 "tokens": "angular arms, tapered wooden legs, retro vibes, bold colors, vintage charm"}
            ],
            "Contemporary Armchairs": [
                {"name": "Barrel Chairs",
                 "tokens": "rounded backrests, wrapping around the seat, cozy feel, modern design, plush upholstery"},
                {"name": "Slipper Armchairs",
                 "tokens": "low armless chairs, extended seating, contemporary touch, sleek silhouette, minimalist look"},
                {"name": "Cube Armchairs",
                 "tokens": "square designs, plush cushions, modern interiors, geometric shape, bold style"}
            ],
            "Casual and Relaxing Armchairs": [
                {"name": "Recliners",
                 "tokens": "adjustable backs, footrests, ultimate comfort, plush padding, casual style"},
                {"name": "Club Chairs",
                 "tokens": "deep seating, rounded backs, armrests, perfect for lounging, cozy design"},
                {"name": "Chaise Armchairs",
                 "tokens": "extended seat length, stretching out, relaxing, modern comfort, elegant lines"}
            ],
            "Industrial and Rustic Armchairs": [
                {"name": "Leather Armchairs",
                 "tokens": "raw aged leather, rugged industrial aesthetic, sturdy build, distressed finish, bold textures"},
                {"name": "Metal Frame Armchairs",
                 "tokens": "leather or fabric seats, sturdy metal frames, industrial design, modern edge, raw materials"},
                {"name": "Wooden Armchairs",
                 "tokens": "natural finishes, exposed wood, rustic charm, earthy tones, handcrafted feel"}
            ],
            "Eclectic and Bold Armchairs": [
                {"name": "Accent Armchairs",
                 "tokens": "vibrant colors, patterned fabrics, unique shapes, statement piece, eclectic style"},
                {"name": "Art Deco Armchairs",
                 "tokens": "geometric patterns, luxurious materials, velvet or gold accents, bold design, vintage glamour"},
                {"name": "Egg or Ball Chairs",
                 "tokens": "futuristic designs, curved shells, modern aesthetic, bold statement, cozy enclosure"}
            ],
            "Outdoor Armchairs": [
                {"name": "Wicker Armchairs",
                 "tokens": "lightweight, weather-resistant, patio or balcony, natural texture, outdoor comfort"},
                {"name": "Teak Armchairs",
                 "tokens": "durable, stylish, outdoor lounging, natural wood finish, weatherproof"},
                {"name": "Sling Armchairs",
                 "tokens": "fabric stretched over frame, lightweight metal or wood, modern outdoor design, breathable material, casual seating"}
            ]
        },
        "tokens": "plush upholstery, elegant design, high backrest, cozy seating, modern or vintage"
    },
    "Buffet": {
        "options": [
            "Classic Buffets",
            "Modern Buffets",
            "Industrial Buffets",
            "Rustic Buffets"
        ],
        "subcategories": {
            "Classic Buffets": [
                {"name": "Ornate Wooden Buffets",
                 "tokens": "ornate carvings, wooden finish, classic design, elegant storage, luxurious style"},
                {"name": "Mirrored Buffets",
                 "tokens": "mirrored panels, classic aesthetic, glamorous vibe, reflective surfaces, elegant design"}
            ],
            "Modern Buffets": [
                {"name": "Sleek Minimalist Buffets",
                 "tokens": "clean lines, minimalist design, modern aesthetic, glossy finish, functional storage"},
                {"name": "Mid-Century Buffets",
                 "tokens": "retro design, tapered legs, wooden finish, bold colors, vintage charm"}
            ],
            "Industrial Buffets": [
                {"name": "Metal and Wood Buffets",
                 "tokens": "industrial design, metal frame, wooden top, raw finish, sturdy build"},
                {"name": "Distressed Buffets",
                 "tokens": "distressed finish, industrial style, rugged look, metal accents, functional storage"}
            ],
            "Rustic Buffets": [
                {"name": "Reclaimed Wood Buffets",
                 "tokens": "reclaimed wood, rustic charm, natural finish, earthy tones, handcrafted feel"}
            ]
        },
        "tokens": "elegant storage, sturdy build, decorative accent, modern or classic, functional design"
    },
    "Sideboard": {
        "options": [
            "Classic Sideboards",
            "Modern Sideboards",
            "Industrial Sideboards",
            "Rustic Sideboards"
        ],
        "subcategories": {
            "Classic Sideboards": [
                {"name": "Traditional Wooden Sideboards",
                 "tokens": "wooden finish, classic design, ornate details, elegant storage, timeless style"},
                {"name": "Antique Sideboards",
                 "tokens": "antique design, wooden finish, vintage charm, intricate carvings, luxurious feel"}
            ],
            "Modern Sideboards": [
                {"name": "Minimalist Sideboards",
                 "tokens": "clean lines, minimalist design, modern aesthetic, glossy finish, functional storage"},
                {"name": "Mid-Century Sideboards",
                 "tokens": "retro design, tapered legs, wooden finish, bold colors, vintage charm"}
            ],
            "Industrial Sideboards": [
                {"name": "Metal and Wood Sideboards",
                 "tokens": "industrial design, metal frame, wooden top, raw finish, sturdy build"},
                {"name": "Distressed Sideboards",
                 "tokens": "distressed finish, industrial style, rugged look, metal accents, functional storage"}
            ],
            "Rustic Sideboards": [
                {"name": "Reclaimed Wood Sideboards",
                 "tokens": "reclaimed wood, rustic charm, natural finish, earthy tones, handcrafted feel"}
            ]
        },
        "tokens": "functional storage, sturdy build, decorative accent, modern or classic, elegant design"
    },
    "Rug": {
        "options": [
            "Outdoor rug",
            "Bohemian Rug",
            "Modern Rug",
            "Classic Rug"
        ],
        "subcategories": {
            "Outdoor rug": [
                {"name": "Weatherproof Outdoor Rug",
                 "tokens": "weatherproof material, outdoor use, durable design, vibrant colors, textured pattern"}
            ],
            "Bohemian Rug": [
                {"name": "Patterned Bohemian Rug",
                 "tokens": "bohemian style, vibrant patterns, layered design, cozy texture, artistic feel"}
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
        "tokens": "cozy texture, vibrant patterns, durable material, modern or classic, decorative accent"
    },
    "Dining table and chairs": {
        "options": [
            "2-seat rectangular table",
            "4-seat rectangular table",
            "6-seat rectangular table",
            "Round dining table",
            "Extendable dining table"
        ],
        "tokens": "sturdy construction, elegant design, functional dining set, modern or classic, comfortable seating"
    },
    "Bed": {
        "options": [
            "single bed",
            "double bed",
            "queen bed",
            "king bed",
            "canopy bed",
            "platform bed",
            "sleigh bed"
        ],
        "tokens": "cozy bedding, sturdy frame, elegant headboard, modern or classic design, comfortable mattress"
    },
    "Shelves": {
        "options": [
            "floating shelf",
            "wall-mounted shelf",
            "bookshelf",
            "corner shelf"
        ],
        "tokens": "functional storage, sleek design, modern or classic, sturdy build, decorative accent"
    },
    "Floor lamp": {
        "options": [
            "Minimalist Floor Lamps",
            "Industrial Floor Lamps",
            "Modern Floor Lamps",
            "Classic Floor Lamps"
        ],
        "subcategories": {
            "Minimalist Floor Lamps": [
                {"name": "Sleek Minimalist Floor Lamp",
                 "tokens": "sleek design, minimalist style, neutral tones, metal frame, modern lighting"}
            ],
            "Industrial Floor Lamps": [
                {"name": "Metal Industrial Floor Lamp",
                 "tokens": "industrial design, metal frame, raw finish, exposed bulb, modern edge"}
            ],
            "Modern Floor Lamps": [
                {"name": "Arched Modern Floor Lamp",
                 "tokens": "modern design, arched shape, sleek frame, ambient lighting, contemporary style"}
            ],
            "Classic Floor Lamps": [
                {"name": "Traditional Floor Lamp",
                 "tokens": "classic design, fabric shade, wooden base, warm lighting, elegant style"}
            ]
        },
        "tokens": "ambient lighting, sturdy base, modern or classic, elegant design, functional decor"
    },
    "Table lamp": {
        "options": [
            "Classic Table Lamps",
            "Modern Table Lamps",
            "Industrial Table Lamps",
            "Minimalist Table Lamps"
        ],
        "subcategories": {
            "Classic Table Lamps": [
                {"name": "Traditional Table Lamp",
                 "tokens": "classic design, fabric shade, wooden base, warm lighting, elegant style"}
            ],
            "Modern Table Lamps": [
                {"name": "Geometric Modern Table Lamp",
                 "tokens": "modern design, geometric shape, sleek frame, ambient lighting, contemporary style"}
            ],
            "Industrial Table Lamps": [
                {"name": "Metal Industrial Table Lamp",
                 "tokens": "industrial design, metal frame, raw finish, exposed bulb, modern edge"}
            ],
            "Minimalist Table Lamps": [
                {"name": "Sleek Minimalist Table Lamp",
                 "tokens": "sleek design, minimalist style, neutral tones, metal frame, modern lighting"}
            ]
        },
        "tokens": "ambient lighting, sleek design, modern or classic, elegant style, functional decor"
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
    .main-content {
        margin-left: 310px; /* Уменьшаем отступ от сайдбара */
    }
    .title-container {
        position: sticky;
        top: 0;
        background-color: #1a1a2e;
        padding: 10px;
        z-index: 100;
        text-align: left; /* Выравнивание названия влево */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Название в основной области с фиксированным положением
st.markdown(
    """
    <div class="title-container">
        <h1 style="color: white; margin: 0;">Furniture Product Shot Generator</h1>
        <p style="color: #d3d3d3; margin: 0;">Create detailed prompts for furniture visualization with customizable styles, camera angles, lighting, and more.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Обёртка для основной области с классом для отступа
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Боковая панель для ввода данных
with st.sidebar:
    st.header("Furniture Details")
    furniture_type = st.selectbox(
        "Select Furniture Type",
        sorted(subject_subcategories.keys()),
        help="Choose the type of furniture to visualize."
    )
    furniture_subtype = st.selectbox(
        "Select Furniture Subtype",
        sorted(subject_subcategories[furniture_type]["options"]),
        help="Select a specific subtype of the furniture."
    )
    material = st.selectbox(
        "Select Material",
        ["Leather", "Wood", "Fabric", "Metal"],
        help="Choose the material of the furniture."
    )
    color = st.selectbox(
        "Select Color",
        ["Beige", "Black", "White", "Gray", "Brown", "Blue", "Green", "Red", "Yellow", "Purple", "Pink", "Navy", "Teal"],
        help="Choose the color of the furniture."
    )

    st.header("Room Settings")
    room_type = st.selectbox(
        "Select Room Type",
        ["Living Room", "Bedroom", "Dining Room", "Office", "Kitchen", "Bathroom", "Hallway", "Patio", "Study", "Lounge"],
        help="Select the type of room for the visualization."
    )
    style = st.selectbox(
        "Select Style",
        sorted(style_prompts.keys()),
        help="Choose the interior design style."
    )

    st.header("Camera Control")
    camera = st.selectbox(
        "Select Camera Angle/View",
        sorted(camera_control.keys()),
        help="Choose the camera angle for the shot."
    )

    st.header("Lighting Control")
    lighting = st.selectbox(
        "Select Lighting",
        sorted(lighting_control.keys()),
        help="Choose the lighting conditions for the scene."
    )

    st.header("Product Position")
    position = st.selectbox(
        "Select Product Position",
        sorted(position_control.keys()),
        help="Choose the position of the furniture in the frame."
    )

    st.header("Quality and Negative Prompts")
    quality_enabled = st.session_state.get("quality_enabled", False)
    negative_enabled = st.session_state.get("negative_enabled", False)
    
    # Кнопка с динамической подсветкой для Quality Prompt
    if st.button("Enable Quality Prompt", key="quality_btn", help="Add high-quality rendering tokens to the prompt"):
        st.session_state.quality_enabled = not quality_enabled
    
    # Применение стилей через CSS (исправление селектора)
    quality_button_style = "background-color: #A9CBA4; color: white;" if quality_enabled else ""
    st.markdown(f'<style>button[data-testid="stButton"][key="quality_btn"] {{ {quality_button_style} }}</style>', unsafe_allow_html=True)

    # Кнопка с динамической подсветкой для Negative Prompt
    if st.button("Enable Negative Prompt", key="negative_btn", help="Add negative rendering tokens to exclude unwanted elements"):
        st.session_state.negative_enabled = not negative_enabled
    
    # Применение стилей через CSS
    negative_button_style = "background-color: #D4A4A4; color: white;" if negative_enabled else ""
    st.markdown(f'<style>button[data-testid="stButton"][key="negative_btn"] {{ {negative_button_style} }}</style>', unsafe_allow_html=True)

# Основная область
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Selected Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**Furniture Type:** {furniture_type}")
    st.markdown(f"**Furniture Subtype:** {furniture_subtype}")
    st.markdown("---")
with col2:
    st.markdown(f"**Material:** {material}")
    st.markdown(f"**Color:** {color}")
    st.markdown(f"**Room Type:** {room_type}")
    st.markdown("---")
with col3:
    st.markdown(f"**Style:** {style}")
    st.markdown(f"**Camera Angle/View:** {camera}")
    st.markdown(f"**Lighting:** {lighting}")
    st.markdown(f"**Product Position:** {position}")
    st.markdown("---")

st.markdown("<br>", unsafe_allow_html=True)

# Главный промпт
main_prompt = (
    f"A {room_type} with a {furniture_subtype} in {color} {material}, styled in a {style} theme. "
    f"{style_prompts[style]} {subject_subcategories[furniture_type]['tokens']} "
    f"{camera_control[camera]} {lighting_control[lighting]} {position_control[position]}"
)

# Добавляем токены качества, если кнопка была нажата
if quality_enabled:
    main_prompt += " " + quality_tokens

# Окно для негативного промпта
negative_prompt = ""
if negative_enabled:
    negative_prompt = negative_tokens

# Главный промпт с кнопкой копирования (разблокировано для редактирования)
st.subheader("Generated Prompt")
main_prompt_input = st.text_area("", value=main_prompt, height=200, key="main_prompt_area")
st.markdown(
    f'<style>.stTextArea textarea {{ background-color: #2a2a3e; color: white; word-wrap: break-word; }}</style>',
    unsafe_allow_html=True
)
if st.button("Copy Main Prompt to Clipboard", key="copy_main_btn"):
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText(`{main_prompt_input}`).then(() => alert('Main prompt copied to clipboard!'))" style="background-color: #FFA500; color: white; border: none; padding: 5px 10px; cursor: pointer;">Copy Main Prompt</button>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Негативный промпт с кнопкой копирования
st.subheader("Negative Prompt")
negative_prompt_input = st.text_area("", value=negative_prompt, height=150, key="negative_prompt_area")
st.markdown(
    f'<style>.stTextArea textarea {{ background-color: #2a2a3e; color: white; word-wrap: break-word; }}</style>',
    unsafe_allow_html=True
)
if st.button("Copy Negative Prompt to Clipboard", key="copy_negative_btn"):
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText(`{negative_prompt_input}`).then(() => alert('Negative prompt copied to clipboard!'))" style="background-color: #FFA500; color: white; border: none; padding: 5px 10px; cursor: pointer;">Copy Negative Prompt</button>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Кнопка для сброса настроек
if st.button("Reset Settings", help="Reset all settings to default"):
    st.session_state.clear()
    st.experimental_rerun()

# Кнопка для сохранения настроек
st.divider()
if st.button("Save Configuration", help="Save the current configuration"):
    config = {
        "furniture_type": furniture_type,
        "furniture_subtype": furniture_subtype,
        "material": material,
        "color": color,
        "room_type": room_type,
        "style": style,
        "camera": camera,
        "lighting": lighting,
        "position": position,
        "quality_enabled": quality_enabled,
        "negative_enabled": negative_enabled,
        "main_prompt": main_prompt_input,
        "negative_prompt": negative_prompt_input
    }
    st.session_state.config = config
    st.success("Configuration saved!")

# Кнопка для загрузки сохранённых настроек
if "config" in st.session_state:
    if st.button("Load Saved Configuration", help="Load the previously saved configuration"):
        config = st.session_state.config
        furniture_type = config["furniture_type"]
        furniture_subtype = config["furniture_subtype"]
        material = config["material"]
        color = config["color"]
        room_type = config["room_type"]
        style = config["style"]
        camera = config["camera"]
        lighting = config["lighting"]
        position = config["position"]
        st.session_state.quality_enabled = config["quality_enabled"]
        st.session_state.negative_enabled = config["negative_enabled"]
        st.success("Configuration loaded!")
        st.experimental_rerun()

# Показ сохранённых настроек
if "config" in st.session_state:
    st.subheader("Saved Configuration")
    st.write(st.session_state.config)

# Закрытие обёртки основной области
st.markdown('</div>', unsafe_allow_html=True)