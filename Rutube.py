import json
import os
import m3u8_To_MP4
import re
import requests as requests


from Parser_engine import ParserEngine


class Rutube(ParserEngine):
    def __init__(self, path, link):
        self.user_path = path
        self.user_link = link

        self.check_user_input()

    def check_user_input(self):
        while True:
            if self.user_link.find("https://rutube.ru/video/") != -1 \
                    or self.user_link.find("https://rutube.ru/channel/") != -1 \
                    or self.user_link.find("https://rutube.ru/search/") != -1:
                break
            else:
                self.user_link = input("Некорректная ссылка. Повторите ввод: ")
        self.parsing(self.user_path, self.user_link)
        self.user_link = ""

    def parsing(self, download_path, rutube_link):
        if rutube_link.find("https://rutube.ru/video/") != -1:
            self.parsing_current_video(download_path, rutube_link)

        if rutube_link.find("https://rutube.ru/channel/") != -1:
            self.parsing_channel(download_path, rutube_link)

        if rutube_link.find("https://rutube.ru/search/") != -1:
            self.parsing_search_query(download_path, rutube_link)

    def parsing_current_video(self, path, link):
        right_border_link = link.rfind("/")
        id_video = link[link[:right_border_link].rfind("/") + 1:right_border_link]
        video_json = json.loads(requests.get(f"http://rutube.ru/api/play/options/{id_video}/").content)
        html = video_json['video_balancer']['m3u8']
        content_html = requests.get(html).content.decode('utf-8')
        final_link_m3u8 = content_html[content_html.rfind("http"):content_html.rfind("?")]
        file_name = video_json['title']
        if file_name[-1:] == '.' or file_name[-1:] == ' ':
            file_name = file_name[:-1]

        mp4_file_name = re.sub(r':*<*>*\"*\\*/*\|*\?*\**\«*\»*', "", file_name) + ".mp4"

        m3u8_To_MP4.download(final_link_m3u8, mp4_file_dir=path)

        file_old_name = os.path.join(path, "m3u8_To_Mp4.mp4")
        file_new_name = os.path.join(path, mp4_file_name)
        os.rename(file_old_name, file_new_name)

    def parsing_channel(self, link, download_path):
        pass

    def parsing_search_query(self, query, download_path):
        pass
