Setup:
```
docker run -it --rm -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Q1:
Code - docker exec -it ollama /bin/bash
ollama -v

Q2:<p>
root@e54c5c8f7f78:~/.ollama# cd models/
root@e54c5c8f7f78:~/.ollama/models# ls
blobs  manifests
root@e54c5c8f7f78:~/.ollama/models# cd manifests/
root@e54c5c8f7f78:~/.ollama/models/manifests# ls
registry.ollama.ai
root@e54c5c8f7f78:~/.ollama/models/manifests# cd registry.ollama.ai/
root@e54c5c8f7f78:~/.ollama/models/manifests/registry.ollama.ai# ls
library
root@e54c5c8f7f78:~/.ollama/models/manifests/registry.ollama.ai# cd library
root@e54c5c8f7f78:~/.ollama/models/manifests/registry.ollama.ai/library# ls
gemma
root@e54c5c8f7f78:~/.ollama/models/manifests/registry.ollama.ai/library# cd gemma
root@e54c5c8f7f78:~/.ollama/models/manifests/registry.ollama.ai/library/gemma# ls
2b
root@e54c5c8f7f78:~/.ollama/models/manifests/registry.ollama.ai/library/gemma# cat 2b
{"schemaVersion":2,"mediaType":"application/vnd.docker.distribution.manifest.v2+json","config":{"mediaType":"application/vnd.docker.container.image.v1+json","digest":"sha256:887433b89a901c156f7e6944442f3c9e57f3c55d6ed52042cbb7303aea994290","size":483},"layers":[{"mediaType":"application/vnd.ollama.image.model","digest":"sha256:c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12","size":1678447520},{"mediaType":"application/vnd.ollama.image.license","digest":"sha256:097a36493f718248845233af1d3fefe7a303f864fae13bc31a3a9704229378ca","size":8433},{"mediaType":"application/vnd.ollama.image.template","digest":"sha256:109037bec39c0becc8221222ae23557559bc594290945a2c4221ab4f303b8871","size":136},{"mediaType":"application/vnd.ollama.image.params","digest":"sha256:22a838ceb7fb22755a3b0ae9b4eadde629d19be1f651f73efb8c6b4e2cd0eea0","size":84}]}
</p>

Q3:
root@e54c5c8f7f78:~# ollama run gemma:2b
>>> 10 * 10

Q4:
gary@Custom:~/ollama_files$ du -sh models/
1.6G	models/

Q5:
sudo chmod -R 777 ollama_files
cp -r ../ollama_files .

FROM ollama/ollama

COPY ollama_files /root/.ollama

Q6:
from openai import OpenAI
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

def llm():
    response = client.chat.completions.create(
        model='gemma:2b',
        messages=[{"role": "user", "content": "What's the formula for energy?"}]
        temperature=0.0
    )
    
    content = response.choices[0].message.content
    tokens = response.usage.total_tokens
    
    return content, tokens
    
content, tokens = llm()
tokens
