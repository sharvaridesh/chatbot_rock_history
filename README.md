# Conversational AI Chatbot with Data Integration and Memory

## Project Description

This project involves developing a conversational AI chatbot that utilizes OpenAI's language model to interact with users in real-time. The chatbot can answer questions about data from a specified CSV file, while also engaging in general conversation, maintaining context and memory of past interactions to provide coherent and relevant responses throughout the session.

## Features

- Real-time interaction with users
- Ability to answer questions based on CSV data
- General conversational capabilities
- Context and memory management for coherent and relevant responses

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- Required Python packages:
  - openai
  - pandas
  - langchain

You can install the necessary packages using the following command:

```sh
pip install openai pandas langchain tabulate
```

## Example Outputs
**Chat Example**
<body>
    <pre>
You: hi! Tell me about Fleetwood Mac
GPT: Hi there! Fleetwood Mac is a British-American rock band that was formed in London in 1967. The band has had a long and successful career, with many hit songs and albums. They are known for their unique blend of rock, pop, and blues music, as well as their iconic lineup of members, including Stevie Nicks, Lindsey Buckingham, Christine McVie, John McVie, and Mick Fleetwood. Their most popular album, "Rumours," was released in 1977 and has sold over 40 million copies worldwide. Is there anything specific you would like to know about Fleetwood Mac?
You: What are the top 5 songs of all time of Fleetwood Mac?
GPT: Sure! According to the data from the csv file, the top 5 songs of all time for Fleetwood Mac are "Dreams," "Go Your Own Way," "The Chain," "Landslide," and "Rhiannon." These songs have all been fan favorites and have stood the test of time. Do you have a favorite among these top 5 songs?
You: Yes, Dreams is my favourite song.
GPT:  My personal favorite is "Dreams" as well! It's such a timeless and iconic song. Did you know that it was written by Stevie Nicks in only 10 minutes? It's amazing how some of the best songs can come together so quickly. Have you listened to any other songs by Fleetwood Mac?
    </pre>
</body>
</html>
