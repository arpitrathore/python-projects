from my_file_util import create_dir, create_binary_file
import requests

url = "https://arpitrathore.com/wp-content/uploads/2020/10/pic-small.jpg"

image_dir = create_dir("images")
image_file_name = "my-image-small.jpg"

response = requests.get(url)

create_binary_file(image_dir, image_file_name, response.content)

