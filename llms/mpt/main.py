from transformers import AutoModelForCausalLM, AutoTokenizer

from llms.model_loaders import DEFAULT_CACHE_DIR


def main():
    model_name = "mosaicml/mpt-7b-instruct"

    cache_dir = DEFAULT_CACHE_DIR
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        device_map="auto",
        cache_dir=cache_dir,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True,
        cache_dir=cache_dir,
    )

    print(model, tokenizer)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()