# class Browser:
#     def __init__(self):
#         self.back = []
#         self.forward = []
#         self.page = None

#     def visit_page(self, url):
#         if self.page is not None:
#             self.back.append(self.page)
#         self.page = url
#         self.forward.clear()
#         print(f"visited: {url}")

#     def back_stack(self):
#         if not self.back:
#             print("ko co page")
#         else:
#             self.forward.append(self.page)
#             self.page = self.back.pop()
#             print(f"Back to: {self.page}")

#     def forward_stack(self):
#         if not self.forward:
#             print("ko co page")
#         else:
#             self.back.append(self.page)
#             self.page = self.forward.pop()
#             print(f"Forward to: {self.page}")

#     def current(self):
#         return self.page if self.page else "No page visited."


# browser_instance = Browser()
# browser_instance.visit_page("https://google.com")
# browser_instance.visit_page("https://youtube.com")
# browser_instance.visit_page("https://github.com")

# browser_instance.back_stack()
# browser_instance.back_stack()
# browser_instance.forward_stack()

# print("Current page:", browser_instance.current())                                                                                          


class MP3Player:
    def __init__(self):
        self.music_queue = []  
        self.current_song = None 

    def add_song(self, song):
        """Thêm bài hát vào hàng đợi"""
        self.music_queue.append(song)
        print(f"Added song: {song}")

    def play_next_song(self):
        """Phát bài hát tiếp theo trong hàng đợi"""
        if self.music_queue:
            self.current_song = self.music_queue.pop(0)
            print(f"Now playing: {self.current_song}")
        else:
            self.current_song = None
            print("No songs in the queue.")

    def skip_song(self):
        """Bỏ qua bài hát hiện tại và phát bài tiếp theo"""
        if self.music_queue:
            print(f"Skipped song: {self.current_song}")
            self.play_next_song()
        else:
            self.current_song = None
            print("No more songs to skip.")


player = MP3Player()

player.add_song("Song 1")
player.add_song("Song 2")
player.add_song("Song 3")


player.play_next_song()  
player.play_next_song()  

player.skip_song() 

player.add_song("Song 4")
player.play_next_song() 
