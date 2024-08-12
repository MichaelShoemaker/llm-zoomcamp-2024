In this module we start by getting the cosine similarity between the answer from the original documents which is called "text" in the original documents found here

```
base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/documents-with-ids.json'
docs_url = f'{base_url}/{relative_url}?raw=1'
docs_response = requests.get(docs_url)
documents = docs_response.json()
```

And an answer generated from an LLM. 

The LLM answers are a result of loading the original documents into Elasticsearch. Retreiveing the 5 top documents and building a prompt with them.
This prompt is then sent to an LLM (OpenAI) and the Cosine similarity between the original answer "Text" and the LLM answer is then calculated.

Think these accidentally got flipped in LLM Zoomcamp 4.3 Video at timestamp 4:52

```
answer_orig = 'Yes, sessions are recorded if you miss one. Everything is recorded, allowing you to catch up on any missed content. Additionally, you can ask questions in advance for office hours and have them addressed during the live stream. You can also ask questions in Slack.'
answer_llm = 'Everything is recorded, so you won’t miss anything. You will be able to ask your questions for office hours in advance and we will cover them during the live stream. Also, you can always ask questions in Slack.'

v_llm = model.encode(answer_llm)
v_orig = model.encode(answer_orig)

v_llm.dot(v_orig)
```

We then use the ground truth dataset which was generated by an LLM (it was given the the answer and asked to generate 5 questions a student might ask). Using all
of those questions we can then pass that to Elasticsearch->Prompt Builder-> LLM to get an answer from the LLM and then using the original dataset, compare those returned answers to the originial answers "text" in the orininal documents.
 

