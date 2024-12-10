# NL2DB

The model ft:gpt-4o-mini-2024-07-18:personal:db-and-explanation:AbxJwl0k was trained on data/training/training.jsonl and validated with data/training/validated.jsonl

Running llm_chat_interface.py will test all of data/training/test.jsonl set on the finetuned model

Use the create_response function from llm_chat_interface.py to test a single input.

To Run the fastApi server - You have install few dependencies,

pip install fastapi uvicorn

Once dependencies installed fire up the fastapi server by running - 

uvicorn main:app --reload

