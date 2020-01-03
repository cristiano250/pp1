class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.channels=[]
    def on(self):
        self.is_on=True        
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on==True:
            print('TV jest włączony, kanał: {}'.format(self.channel_no))
        else:
            print('TV jest wyłączony')
    def set_channel_no(self, new_channel_no):
        self.channel_no=new_channel_no
        
    def set_channels(self,channels_list):
        self.channels+=channels_list
    
    def show_channels(self):
        j=1
        if len(self.channels)==0:
            print('Brak dostępnych kanałów')
        else:
            print('Lista dostępnych kanałów: ')
            for i in self.channels:
                print(j,end=". ")
                print(i)
                j+=1
            
telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.show_channels()
telewizor.show_status()
telewizor.set_channels(['TVP1','TVP2','TVN','POLSAT','Filmbox'])
telewizor.show_channels()
telewizor.off()
telewizor.show_status()

