# 以下を「model.py」に書き込み
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from functools import partial
from transformers import pipeline
from transformers.trainer_utils import set_seed

# 乱数シードを42に固定する
set_seed(42)

# モデルとトークナイザを読み込む
model_name = "udaizin/t5-base-long-livedoor-news-corpus"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = tokenizer = AutoTokenizer.from_pretrained(model_name)

# モデルを固定したpipelineを作成する
fixed_model_pipeline = partial(
    pipeline,
    "summarization",
    model=model,
    tokenizer=tokenizer,
)

def summarization_predict(content):
    summarization_pipeline = fixed_model_pipeline(
        num_beams=3,
        num_return_sequences=3,
        min_new_tokens=10,
        max_new_tokens=30,
    )
    summaries = list()
    for summary in summarization_pipeline(content):
        summaries.append(summary["summary_text"])
    return summaries
