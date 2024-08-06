from __future__ import annotations

import logging
from enum import Enum
from typing import Any, Dict, List, cast

import typer
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

logging.getLogger("vllm").setLevel(logging.WARN)
app = typer.Typer()


class LangType(str, Enum):
    EN = "en"
    ZH = "zh"


SUMMARY_PROMPT_TEMPLATE_EN = """
{context}
----------------
Please summarize the above text.
"""

SUMMARY_PROMPT_TEMPLATE_ZH = """
{context}
----------------
请总结以上内容。
"""


def format_messages(model_name: str, messages: List[Dict[str, Any]]) -> str:
    return cast(
        str,
        AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True,
        ).apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        ),
    )


@app.command()
def chat(
    query: str,
    fp8_cache: bool = False,
    model_name: str = "Qwen/Qwen2-7B-Instruct-GPTQ-Int4",
):
    llm = LLM(model_name, kv_cache_dtype="fp8" if fp8_cache else "auto", trust_remote_code=True)
    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}]
    text = format_messages(model_name, messages)
    response = llm.generate(text, use_tqdm=False, sampling_params=SamplingParams(temperature=0.1, max_tokens=512))
    typer.echo(response[0].outputs[0].text)


@app.command()
def summary(
    lang: LangType = LangType.EN,
    fp8_cache: bool = False,
    model_name: str = "Qwen/Qwen2-7B-Instruct-GPTQ-Int4",
):
    PROMPT_TEMP = SUMMARY_PROMPT_TEMPLATE_EN if lang == LangType.EN else SUMMARY_PROMPT_TEMPLATE_ZH
    llm = LLM(model_name, kv_cache_dtype="fp8" if fp8_cache else "auto", trust_remote_code=True)
    with open("sample.txt", "r") as f:
        context = f.read()
    query = PROMPT_TEMP.format(context=context)
    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}]
    text = format_messages(model_name, messages)
    response = llm.generate(text, use_tqdm=False, sampling_params=SamplingParams(temperature=0.1, max_tokens=512))
    typer.echo(response[0].outputs[0].text)


if __name__ == "__main__":
    app()
