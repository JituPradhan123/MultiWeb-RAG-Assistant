# MultiWeb RAG Assistant

## Steps to Run:

### 1. Create a venv (Virtual Environment)

```
pip install uv
uv venv multirag
multirag\Scripts\activate
```
# MultiWeb RAG Assistant Testing


### 1. Test Document Loading Function

#### It only say the test is done or not without execute the print statement
```
python -m pytest tests/test_document_loader.py -v
```
#### It execute entire data loading process
```
python -m pytest tests/test_document_loader.py -v -s
```