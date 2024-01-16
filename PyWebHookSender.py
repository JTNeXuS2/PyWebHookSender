import requests
#переменные: адрес вебхука, адрес аватарки автора сообщения, имя автора, текст
webhook_url = "https://discord.com/api/webhooks/1196438479559733350/SS7H2O_EHkb74DjtKOPqHf6LAsUyRgPZfGqCr6ZqU7DNABuXKJ1DGwRg7aZV3cmYdFHC"
avatar_url = "https://cdn-icons-png.flaticon.com/512/5506/5506681.png"
sender_name = "Anonymous"
message_text = "Смотреть всем @here https://www.youtube.com/watch?v=6l5Qi0uMZUY"

#формируем JSON для отправки (параметров может быть больше, смотрите документацию discord)
payload = {
    "content": message_text,
    "username": sender_name,
    "avatar_url": avatar_url
}
#отправляем JSON на вебхук дискорда
response = requests.post(webhook_url, json=payload)

if response.status_code == 204:
    print("Сообщение отправлено успешно.")
else:
    print(f"Ошибка отправки сообщения. Код ошибки: {response.status_code}")
  
