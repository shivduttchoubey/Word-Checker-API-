from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from better_profanity import profanity
from fastapi.encoders import jsonable_encoder

class Book(BaseModel):
    text1: str

app = FastAPI()

@app.post("/prof")
def create_book(book: Book):
    cdr=book.text1
    # wordlist.txt contains all the words which are to be looked in a text 
    profanity.load_censor_words_from_file('wordlist.txt')
    text = cdr
    censored_text = profanity.censor(text)
    print(censored_text)

    if '****' in censored_text:
        res="word is present"
        

    else:
        res="word not present"


    
    result = {
        'state': res,
        'org':text
    }
#state represent if the word is in the given text or not
#and org respresent the original text which was entered
    

    resu=jsonable_encoder(result)
    return JSONResponse(content=resu)


uvicorn.run(app, port=8002, host="127.0.0.1")



