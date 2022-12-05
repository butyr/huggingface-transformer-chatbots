from transformers import GPTJForCausalLM, AutoTokenizer
import os
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class DialoGPT:
    def __init__(
        self,
        model_name: str = "EleutherAI/gpt-j-6B",
        local_path="./models/gpt-j-6B",
    ):
        if not os.path.exists(local_path):
            GPTJForCausalLM.from_pretrained(model_name).save_pretrained(
                local_path,
                revision="float16",
                torch_dtype=torch.float16,
            )
            AutoTokenizer.from_pretrained(model_name).save_pretrained(local_path)

        self.model = GPTJForCausalLM.from_pretrained(
            local_path,
            revision="float16",
            torch_dtype=torch.float16,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(local_path)

    def __call__(self, inputs: str) -> str:
        input_ids = self.tokenizer(inputs, return_tensors="pt").input_ids.to(device)
        generated_ids = self.model.to(device).generate(
            input_ids, do_sample=True, temperature=0.9, max_length=200
        )
        generated_text = self.tokenizer.decode(generated_ids[0])

        return generated_text

    def run(self):
        while True:
            user_input = input("User: ")
            print("Bot:", self(user_input))


if __name__ == "__main__":
    bot = DialoGPT()
    bot.run()
