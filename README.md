## This project demonstrate how to store pdf into vector db and query that data based on input, There are 2 api's for this

````bash
curl --location 'http://127.0.0.1:8000/v1/upload' \
--header 'accept: application/json' \
--form 'file=@"/Users/girish/python/github.com/girishg4t/faq_rag/data/sample_faq.pdf"'```
````

```bash
curl --location 'http://127.0.0.1:8000/v1/matches' \
--header 'accept: application/json' \
--form 'sentence="What is artificial intelligence?"' \
--form 'limit="3"'
```

result:

```
{
    "matches": [
        {
            "sentence": "1. What is Artificial Intelligence (AI)?",
            "distance": 0.32040369084842185
        },
        {
            "sentence": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and adapt like humans.",
            "distance": 0.43121719304670436
        },
        {
            "sentence": "AI is used in various applications, including virtual assistants, recommendation systems, fraud detection, medical diagnosis, and autonomous vehicles.",
            "distance": 0.5171373901985227
        }
    ]
}
```
