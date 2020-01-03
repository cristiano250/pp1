class TV():
    def __init__(self):
        self.is_on=False
    def on(self):
        self.is_on=True        
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on==True:
            print('TV jest włączony')
        else:
            print('TV jest wyłączony')
            
telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.off()
telewizor.show_status()
