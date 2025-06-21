Como rodar

No terminal, vá até a pasta do projeto:
bash
cd todo_web_app

Construa a imagem:
bash
docker build -t todo-web-app .

Execute o container:
bash
docker run -it --rm -p 5000:5000 todo-web-app

Abra no navegador:
arduino
http://localhost:5000