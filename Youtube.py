import pafy

from Parser_engine import ParserEngine


class Youtube(ParserEngine):
    def __init__(self, path, link):
        self.user_path = path
        self.user_link = link

        self.check_user_input()

    def check_user_input(self):
        while True:
            if self.user_link.find("https://www.youtube.com/watch") != -1:
                self.parsing(self.user_path, self.user_link)
                break
            else:
                self.user_link = input("Некорректная ссылка. Повторите ввод: ")
        self.user_link = ""

    def parsing(self, download_path, youtube_link):
        if youtube_link.find("/watch") != -1:
            self.parsing_current_video(download_path, youtube_link)

        if youtube_link.find("https://www.youtube.com/c/") != -1:
            self.parsing_channel(download_path, youtube_link)

    def parsing_current_video(self, path, url):
        yt = pafy.new(url)
        video = yt.getbest(preftype='mp4', ftypestrict=True)
        print("Идет установка...")
        video.download(filepath=path, quiet=False)
        print("Успешно")

    def parsing_channel(self, link, download_path):
        pass
