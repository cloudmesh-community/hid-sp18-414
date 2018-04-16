SWAGGER=java -jar swagger-codegen-cli-2.3.1.jar
SPEC=lang.yml
all: 
	generate requirements run
	
codegen:
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
generate:
	$(SWAGGER) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/language/flaskConnexion \
		-D supportPython2=true
	cp *_controller.py server/language/flaskConnexion/swagger_server/controllers/  
run:
	cd server/language/flaskConnexion/ &&\
	python -m swagger_server
requirements:
	pip install -r requirements.txt
	cd server/language/flaskConnexion; pip install -r requirements.txt
curl:
	curl -H "Content-Type: application/json" \
		-X POST \
		-d '{"phrase":"bonjour"}' \
		http\://localhost\:8080/language

	curl -H "Content-Type: application/json" \
		-X POST \
		-d '{"phrase":"bonjour","trans_lang":"English"}' \
		http\://localhost\:8080/translate    		
docker-b:
	docker build -t cloudmesh-language.
docker-s:
	docker run -t -p 8080:8080 cloudmesh-language
clean:
	rm -rf server/
