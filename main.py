import tkinter as tk
import requests
from PIL import ImageTk, Image

FONT = ('Courier New', 12, 'bold')
BGC = '#D2B48C'


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Pokemon Görsel Bulma Programı')
        self.config(bg=BGC)
        self.minsize(width=650, height=650)
        self.config(pady=15)
        self.resizable(width=False, height=False)
        self.label1 = tk.Label(text='Pokemon uygulamasına hoşgeldiniz.'
                                    '\nGörmek istediğiniz pokemonun adını aşağıdaki kutuya yazıp '
                                    '\n"Göster" butonuna tıklayarak görebilirsiniz.'
                                    '\nAynı zamanda \n1 ile 1000 arasında\n sayı girerek '
                                    'pokemon çeşitlerini inceleyebilirsiniz.', font=FONT, bg=BGC, pady=5)
        self.label1.pack()

        self.entry_name = tk.Entry(width=50)
        self.entry_name.pack()

        self.show_poke_button = tk.Button(text='Göster', command=self.create_poke_label,
                                          font=('Courier New', 14, 'bold'), bg=BGC, borderwidth=0)
        self.show_poke_button.pack()

        self.result_label = tk.Label(bg=BGC)
        self.result_label.pack()

        self.frame = tk.Frame(width=400, height=360)
        self.frame.config(bg=BGC)
        self.frame.pack()

        self.name_label = tk.Label(text='', font=FONT, pady=10, bg=BGC)
        self.name_label.pack()

        self.exit_button = tk.Button(text='Uygulamayı kapatmak için tıklayın', command=self.exit_func,
                                     bg='red', borderwidth=1, font=FONT)
        self.exit_button.pack()

    def exit_func(self):
        self.destroy()

    def poke_name_func(self, my_poke_name):
        url = f'https://pokeapi.co/api/v2/pokemon/{my_poke_name}'
        self.taken_url = requests.get(url).json()['species']['name']
        self.name_label.config(text=self.taken_url)

    def create_poke(self, my_poke_name):
        with open('poke_image.png', 'wb') as self.poke:
            url = f'https://pokeapi.co/api/v2/pokemon/{my_poke_name}'
            self.taken_url = requests.get(url).json()['sprites']['other']['home']['front_default']
            self.response = requests.get(self.taken_url)
            self.base_url = self.response.content
            self.poke.write(self.base_url)

    def create_poke_label(self):
        if self.entry_name.get() == '':
            self.result_label.config(text='Boş bırakılamaz.\nLütfen bir pokemon ismi '
                                          'veya bir sayı giriniz.', fg='red', font=FONT)
            self.entry_name.delete(0, tk.END)
        elif self.entry_name.get() != '':
            try:
                self.result_label.config(text='')
                self.create_poke(self.entry_name.get())
                self.image = Image.open('poke_image.png')
                self.resized_image = self.image.resize((300, 300))
                self.img = ImageTk.PhotoImage(self.resized_image)
                self.image_label = tk.Label(self.frame, image=self.img)
                self.image_label.place(x=50, y=50)
                self.poke_name_func(self.entry_name.get())
                self.entry_name.delete(0, tk.END)
            except:
                self.result_label.config(text='Hatalı isim girdiniz.\nKontrol edip tekrar deneyin.',
                                         font=FONT, fg='red')


window = Window()
window.mainloop()
