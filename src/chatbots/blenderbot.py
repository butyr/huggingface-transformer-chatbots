from transformers import BlenderbotSmallTokenizer, BlenderbotSmallForConditionalGeneration
import os


class BlenderBot:
    def __init__(
        self,
        model_name='facebook/blenderbot_small-90M',
    ):
        if not os.path.exists('./models/blenderbot'):
            BlenderbotSmallForConditionalGeneration.from_pretrained(model_name).save_pretrained('./models/blenderbot')
            BlenderbotSmallTokenizer.from_pretrained(model_name).save_pretrained('./models/blenderbot')

        self.model = BlenderbotSmallForConditionalGeneration.from_pretrained('./models/blenderbot')
        self.tokenizer = BlenderbotSmallTokenizer.from_pretrained('./models/blenderbot')

    def __call__(self, user_query: str) -> str:
        inputs = self.tokenizer([user_query], return_tensors='pt')
        reply_ids = self.model.generate(**inputs)
        bot_answer = self.tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]

        return bot_answer

    def run(self):
        while True:
            user_input = input("User: ")
            print("Bot:", self(user_input))


def main():
    model = BlenderBot()
    model.run()


if __name__ == '__main__':
    main()