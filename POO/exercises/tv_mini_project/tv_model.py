class TV:
   
    def __init__(self, list_channel: list, list_volume: list):
        self.list_channel = list_channel#definir canal min e max
        self.list_volume = list_volume#definir volume min e max
        self.state = False
        self.channel =  self.list_channel[0]
        self.volume = self.list_volume[0]
        self.warnning = " - "

    def volume_more(self):
        if(self.volume == self.list_volume[-1]):
            self.warnning = "Volume está no máximo"
        else:
            self.volume += 1

    def volume_minum(self):
        if(self.volume == self.list_volume[0]):
            self.warnning = "Volume está no minimo"
        else:
            self.volume -= 1

    def channel_more(self):
        if(self.channel == self.list_channel[-1]):
            self.channel = self.list_channel[0]
        else:
            self.channel += 1   

    def channel_minum(self):
        if(self.channel == self.list_channel[0]):
            self.channel = self.list_channel[-1]
        else:
            self.channel -= 1

    def info(self):
        print(f"O volume está atualmente em: {self.volume}")
        print(f"O canal atual está em: {self.channel}")

    def on_tv(self):
        if(self.state == True):
            self.warnning = "A TV já está ligada."
        else:
            self.state = True

    def off_tv(self):
        if(self.state == False):
            self.warnning = "A TV já está desligada"
        else:
            self.state = False
    
    def get_state(self):
        return self.state

    def get_volume(self):
        return self.volume

    def get_channel(self):
        return self.channel

    def get_warn(self):
        return self.warnning

    def set_warn(self):
        self.warnning = "-"