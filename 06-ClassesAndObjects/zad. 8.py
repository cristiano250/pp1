class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname='Uniwersytet Ekonomiczny w Krakowie'
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name=new_name
        
uczelnia=University()
uczelnia.print_name()
uczelnia.set_name('AGH')
uczelnia.print_name()