"""
Adapted from:
https://www.machinecurve.com/index.php/2021/03/16/easy-chatbot-with-dialogpt-machine-learning-and-huggingface-transformers/
"""


from transformers import AutoModelForCausalLM, AutoTokenizer
import os


class DialoGPT:
    def __init__(
        self,
        model_name: str ='microsoft/DialoGPT-large',
    ):
        if not os.path.exists('./models/dialogpt'):
            AutoModelForCausalLM.from_pretrained(model_name).save_pretrained('./models/dialogpt')
            AutoTokenizer.from_pretrained(model_name).save_pretrained('./models/dialogpt')

        self.model = AutoModelForCausalLM.from_pretrained('./models/dialogpt')
        self.tokenizer = AutoTokenizer.from_pretrained('./models/dialogpt')

    def __call__(self, inputs: str) -> str:
        inputs_tokenized = self.tokenizer.encode(inputs+ self.tokenizer.eos_token, return_tensors='pt')
        reply_ids = self.model.generate(inputs_tokenized, max_length=1250, pad_token_id=self.tokenizer.eos_token_id)
        reply = self.tokenizer.decode(reply_ids[:, inputs_tokenized.shape[-1]:][0], skip_special_tokens=True)

        return reply

    def run(self):
        while True:
            user_input = input("User: ")
            print("Bot:", self(user_input))
