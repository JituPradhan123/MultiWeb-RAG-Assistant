# MultiWeb RAG Assistant

## Steps to Run:

### 1. Create a venv (Virtual Environment)

```
pip install uv
uv venv multirag
multirag\Scripts\activate
```
### 2. Install all dependencies using a requirements file

```
uv pip install -r requirements.txt
```
### 3. Pest your all web urls to ***multiweb_assistant/config.py*** inside urls list variable. 

### 4. Create ***.env*** file inside the project directory and inside the ***.env*** pest your Huggingface Key

```
HUGGINGFACEHUB_API_TOKEN="***pest_your_key_here***"
```

### 5. Run the bellow code in terminal
```
streamlit run app.py  
```

# MultiWeb RAG Assistant Testing (Optional)

### To check every function work properlly or not.

### 1. Test Config Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_config.py -v
```
or 
#### It execute entire data loading process
```
python -m pytest tests/test_config.py -v -s
```

### 2. Test WebPageLoader Class

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_webpageloader.py -v
```
or 
#### It execute entire data loading process
```
python -m pytest tests/test_webpageloader.py -v -s
```

### 3. Test Document Loading Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_document_loader.py -v
```
or 
#### It execute entire data loading process
```
python -m pytest tests/test_document_loader.py -v -s
```
### 4. Test Text splitter Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_text_splitter.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_text_splitter.py -v -s
```

### 5. Test Embedding Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_embeddings.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_embeddings.py -v -s
```
### 6. Test LLM Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_llm.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_llm.py -v -s
```
### 7. Test Vector Store Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_vector_store.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_vector_store.py -v -s
```
### 8. Test Search Tool Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_search_tool.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_search_tool.py -v -s
```
### 9. Test Agent Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_agent.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_agent.py -v -s
```

### 10. Test Pipeline Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_pipeline.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_pipeline.py -v -s
```

### 11. Test Main Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_main.py -v
```
or
#### It execute entire data loading process
```
python -m pytest tests/test_main.py -v -s
```