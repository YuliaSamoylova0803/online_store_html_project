from http.server import BaseHTTPRequestHandler, HTTPServer

# Настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        try:
            # Открываем файл contacts.html для чтения
            with open("src/contacts.html", "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            # Если файл не найден, отправляем сообщение об ошибке
            content = "<html><body><h1>Ошибка: Файл contacts.html не найден</h1></body></html>"

        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(content, "utf-8"))  # Тело ответа

    def do_POST(self):
        """ Метод для обработки входящих POST-запросов """
        # Получаем длину тела запроса
        content_length = int(self.headers["Content-Length"])
        # Читаем тело запроса
        post_data = self.rfile.read(content_length)

        # Выводим данные в консоль
        print("Получены POST-данные:", post_data.decode("utf-8"))

        # Отправляем ответ клиенту
        self.send_response(200)  # Успешный ответ
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("POST-запрос успешно обработан", "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Запуск веб-сервера
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Остановка сервера по Ctrl+C
        pass

    # Корректная остановка веб-сервера
    webServer.server_close()
    print("Server stopped.")