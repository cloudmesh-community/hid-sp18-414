## Swagger Assignment
This API can identify the language of the submitted string and translate the string.
 
 ### Swagger Spec:
  Lang.yaml
 
 ### Setup:
  
  - Step 1: Make codegen
  - Step 1a: Make requirements(only needed on first run thru)
  - Step 2: Make generate
  - Step 3: Make run
    Console should output the following message:
     * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
  - Step 4: Make curl
    Console should output the following message:
      * curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"phrase":"je suis un poisson"}' \
        http\://localhost\:8080/language
      "\"French\""
      * curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"phrase":"bonjour","trans_lang":"English"}' \
        http\://localhost\:8080/translate
      "\"Hello\""

  To run with Docker:
   - Step 1: make docker-b
   - Step 2: make docker-s
