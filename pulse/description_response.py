import json
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import CountVectorizer
import random
from torch.nn.functional import softmax
from .models import client_request
from pulse.GPT_response import chatgpt_response
import pandas as pd
import numpy as np

# Load intents
with open('pulse/models/description.json', 'r') as file:
    intents = json.load(file)

# Create vectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([pattern for intent in intents['intents'] for pattern in intent['patterns']])


# Define the model architecture
class ChatModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(ChatModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Initialize the model
model = ChatModel(X.shape[1], len(intents['intents']))

# Load the saved model
model.load_state_dict(torch.load('pulse/models/chatpulse_response.pth'))
model.eval()

def get_disease_name(username):
    try:
        disease=client_request.objects.get(username=username).disease
    except:
        disease=""
    return disease


# Test the model
def get_description(message,username):
    with torch.no_grad():
        prediction = model(torch.tensor(vectorizer.transform([message]).toarray()[0]).float())
        prediction = softmax(prediction, dim=0)  # Apply softmax to the outputs
        confidence, predicted_idx = torch.max(prediction, 0)
        print('Confidence:', confidence.item())  # print the confidence score
        if confidence < 0.7:  # confidence threshold
            disease_name=get_disease_name(username)
            response=chatgpt_response(message,disease_name)
        else:
            tag = intents['intents'][predicted_idx.item()]['tag']
            response = random.choice([intent['responses'] for intent in intents['intents'] if intent['tag'] == tag][0])
            print(response)
            df=pd.read_excel('pulse/models/Skin_cancer_solution.xlsx')
            df=df[["Name",response]]
            disease_name=get_disease_name(username)
            df = df[df['Name'] == disease_name]
            print(df[response].values[0])
            response=", ".join(map(str, df[response].values))
        return response
