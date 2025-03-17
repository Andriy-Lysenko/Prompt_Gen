from gradio_client import Client

# Инициализация клиента
client = Client("https://a3cc06e140c640665f.gradio.live/")

# Текстовый запрос
prompt = "A living room with a leather sofa in beige, styled in a Scandinavian theme."

# Вызов API
result = client.predict(
    True,  # Generate Image Grid for Each Batch
    prompt,  # Текстовый запрос
    "",  # Negative Prompt (оставьте пустым, если не нужно)
    ["Fooocus V2"],  # Selected Styles
    "Quality",  # Performance
    "704×1408 <span style='color: grey;'> ∣ 1:2</span>",  # Aspect Ratios
    1,  # Image Number
    "png",  # Output Format
    "",  # Seed (оставьте пустым для случайного значения)
    True,  # Read wildcards in order
    0,  # Image Sharpness
    1,  # Guidance Scale
    "juggernautXL_v8Rundiffusion.safetensors",  # Base Model
    "None",  # Refiner
    0.1,  # Refiner Switch At
    True,  # Enable LoRA 1
    "None",  # LoRA 1
    -2,  # Weight for LoRA 1
    True,  # Enable LoRA 2
    "None",  # LoRA 2
    -2,  # Weight for LoRA 2
    True,  # Enable LoRA 3
    "None",  # LoRA 3
    -2,  # Weight for LoRA 3
    True,  # Enable LoRA 4
    "None",  # LoRA 4
    -2,  # Weight for LoRA 4
    True,  # Enable LoRA 5
    "None",  # LoRA 5
    -2,  # Weight for LoRA 5
    False,  # Input Image (отключено, так как мы не используем изображение)
    "",  # parameter_212 (оставьте пустым)
    "Disabled",  # Upscale or Variation
    "",  # Image (оставьте пустым)
    [],  # Outpaint Direction
    "",  # Image (оставьте пустым)
    "",  # Inpaint Additional Prompt
    "",  # Mask Upload
    True,  # Disable Preview
    True,  # Disable Intermediate Results
    True,  # Disable seed increment
    True,  # Black Out NSFW
    0.1,  # Positive ADM Guidance Scaler
    0.1,  # Negative ADM Guidance Scaler
    0,  # ADM Guidance End At Step
    1,  # CFG Mimicking from TSNR
    1,  # CLIP Skip
    "euler",  # Sampler
    "normal",  # Scheduler
    "Default (model)",  # VAE
    -1,  # Forced Overwrite of Sampling Step
    -1,  # Forced Overwrite of Refiner Switch Step
    -1,  # Forced Overwrite of Generating Width
    -1,  # Forced Overwrite of Generating Height
    -1,  # Forced Overwrite of Denoising Strength of "Vary"
    -1,  # Forced Overwrite of Denoising Strength of "Upscale"
    True,  # Mixing Image Prompt and Vary/Upscale
    True,  # Mixing Image Prompt and Inpaint
    True,  # Debug Preprocessors
    True,  # Skip Preprocessors
    1,  # Canny Low Threshold
    1,  # Canny High Threshold
    "joint",  # Refiner swap method
    0,  # Softness of ControlNet
    True,  # Enabled
    0,  # B1
    0,  # B2
    0,  # S1
    0,  # S2
    True,  # Debug Inpaint Preprocessing
    True,  # Disable initial latent in inpaint
    "None",  # Inpaint Engine
    0,  # Inpaint Denoising Strength
    0,  # Inpaint Respective Field
    True,  # Enable Advanced Masking Features
    True,  # Invert Mask When Generating
    -64,  # Mask Erode or Dilate
    True,  # Save only final enhanced image
    True,  # Save Metadata to Images
    "fooocus",  # Metadata Scheme
    "",  # Image (оставьте пустым)
    0,  # Stop At
    0,  # Weight
    "ImagePrompt",  # Type
    "",  # Image (оставьте пустым)
    0,  # Stop At
    0,  # Weight
    "ImagePrompt",  # Type
    "",  # Image (оставьте пустым)
    0,  # Stop At
    0,  # Weight
    "ImagePrompt",  # Type
    "",  # Image (оставьте пустым)
    0,  # Stop At
    0,  # Weight
    "ImagePrompt",  # Type
    True,  # Debug GroundingDINO
    -64,  # GroundingDINO Box Erode or Dilate
    True,  # Debug Enhance Masks
    "",  # Use with Enhance, skips image generation
    True,  # Enhance
    "Disabled",  # Upscale or Variation
    "Before First Enhancement",  # Order of Processing
    "Original Prompts",  # Prompt
    True,  # Enable
    "",  # Detection prompt
    "",  # Enhancement positive prompt
    "",  # Enhancement negative prompt
    "u2net",  # Mask generation model
    "full",  # Cloth category
    "vit_b",  # SAM model
    0,  # Text Threshold
    0,  # Box Threshold
    0,  # Maximum number of detections
    True,  # Disable initial latent in inpaint
    "None",  # Inpaint Engine
    0,  # Inpaint Denoising Strength
    0,  # Inpaint Respective Field
    -64,  # Mask Erode or Dilate
    True,  # Invert Mask
    True,  # Enable
    "",  # Detection prompt
    "",  # Enhancement positive prompt
    "",  # Enhancement negative prompt
    "u2net",  # Mask generation model
    "full",  # Cloth category
    "vit_b",  # SAM model
    0,  # Text Threshold
    0,  # Box Threshold
    0,  # Maximum number of detections
    True,  # Disable initial latent in inpaint
    "None",  # Inpaint Engine
    0,  # Inpaint Denoising Strength
    0,  # Inpaint Respective Field
    -64,  # Mask Erode or Dilate
    True,  # Invert Mask
    True,  # Enable
    "",  # Detection prompt
    "",  # Enhancement positive prompt
    "",  # Enhancement negative prompt
    "u2net",  # Mask generation model
    "full",  # Cloth category
    "vit_b",  # SAM model
    0,  # Text Threshold
    0,  # Box Threshold
    0,  # Maximum number of detections
    True,  # Disable initial latent in inpaint
    "None",  # Inpaint Engine
    0,  # Inpaint Denoising Strength
    0,  # Inpaint Respective Field
    -64,  # Mask Erode or Dilate
    True,  # Invert Mask
    fn_index=67  # Индекс функции
)

# Вывод результата
print(result)