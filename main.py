import torch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

app = FastAPI(title="GameFroze AI API")

# 1. Enable CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to your domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Model Configuration (Optimized for Laptop/Free Tier)
MODEL_ID = "Sonai12aa/qwen2.5-1.5b-godot"

# 4-bit quantization to save VRAM/RAM
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

print("--- Loading GameFroze AI Model ---")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto",
    low_cpu_mem_usage=True
)
print("--- Model Loaded Successfully ---")

# 3. Request Schema
class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 150

@app.get("/")
def health_check():
    return {"status": "online", "model": MODEL_ID}

@app.post("/chat")
async def chat(request: ChatRequest):
    # Prepare input
    inputs = tokenizer(request.prompt, return_tensors="pt").to(model.device)
    
    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=request.max_tokens,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    # Decode and remove the initial prompt from the output
    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response_text = full_text[len(request.prompt):].strip()
    
    return {"response": response_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)