# Math Question API

### How to install

```
git clone https://github.com/Saikomantisu/math-question-api.git

pip install fastapi

pip install uvicorn
```

#### Run

 ```uvicorn main:app --reload```
 
 ---
 
### Endpoints
`/api` - Get all the questions

| Key | Description | Data Type
| ----------- | ----------- | ----------- |
| `level` | Get question based on the level - ["easy", "medium", "hard"] | `String`
| `limit` | Limit the question array | `Intiger`

`/api/random` - Get a random question

| Key | Description | Data Type
| ----------- | ----------- | ----------- |
| `level` | Get question based on the level - ["easy", "medium", "hard"] | `String`
