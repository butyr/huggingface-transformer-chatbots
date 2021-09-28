from transformers import AutoModelForCausalLM, AutoTokenizer
import os


class DialoGPT:
    def __init__(
        self,
        model_name='microsoft/DialoGPT-large',
    ):
        if not os.path.exists('./models/dialogpt'):
            AutoModelForCausalLM.from_pretrained(model_name).save_pretrained('./models/dialogpt')
            AutoTokenizer.from_pretrained(model_name).save_pretrained('./models/dialogpt')

        self.model = AutoModelForCausalLM.from_pretrained('./models/dialogpt')
        self.tokenizer = AutoTokenizer.from_pretrained('./models/dialogpt')

    def __call__(self, user_query: str) -> str:
        inputs = self.tokenizer.encode(user_query + self.tokenizer.eos_token, return_tensors='pt')
        reply_ids = self.model.generate(inputs, max_length=1250, pad_token_id=self.tokenizer.eos_token_id)
        bot_answer = self.tokenizer.decode(reply_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)

        return bot_answer

    def run(self):
        while True:
            user_input = input("User: ")
            print("Bot:", self(user_input))
