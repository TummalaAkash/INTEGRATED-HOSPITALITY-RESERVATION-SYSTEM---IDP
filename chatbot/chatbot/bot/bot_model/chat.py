import random
import json
import torch
from .model import NeuralNet
from .nltk_utils import bag_of_words, tokenize
import os
class ChatBot:
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        intents_path = os.path.join(current_directory, 'intents3.json')
        model_dir = os.path.join(current_directory, 'data.pth')
        
        with open(intents_path, 'r') as json_data:
            self.intents = json.load(json_data)

        FILE = model_dir
        data = torch.load(FILE)

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        self.all_words = data['all_words']
        self.tags = data['tags']
        model_state = data["model_state"]

        self.model = NeuralNet(input_size, hidden_size, output_size)
        self.model.load_state_dict(model_state)
        self.model.eval()

        self.bot_name = "Sam"

    def get_response(self, sentence):
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in self.intents['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])
        else:
            return "I do not understand..."

    def chat(self):
        print("Let's chat! (type 'quit' to exit)")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Goodbye!")
                break

            response = self.get_response(user_input)
            print(f"{self.bot_name}: {response}")
