import torch
import typer
from transformers import AutoModelForCausalLM, AutoTokenizer

app = typer.Typer()


@app.command()
def chat(query: str, model_name: str = "Qwen/Qwen2-7B-Instruct-GPTQ-Int4"):
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}]
    text = str(tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))
    input_ids = tokenizer([text], return_tensors="pt").to("cuda:0").input_ids

    generated_ids = model.generate(
        input_ids,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.1,
    )
    generated_ids = [
        output_ids[len(input_ids) :] for input_ids, output_ids in zip(input_ids, generated_ids, strict=False)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    typer.echo(response)


if __name__ == "__main__":
    app()
