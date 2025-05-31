from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


os.environ['HF_HOME'] = 'F:/huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_token=100
    )
)

model = ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of india")

print(result.content)