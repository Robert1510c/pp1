class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.channels_list=[]

    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False
    
    def show_status(self):
        if self.is_on==True:
            print(f'Tv is on {self.channel_no},{self.channels_list[self.channel_no-1]}')
        elif self.is_on==False:
            print('Tv is off')
    
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no

    def set_channels(self,channels_list):
        self.channels_list.append(channels_list)

    def show_channels(self):
        print("available  channels:")
        for i in range(len(self.channels_list)):
            print(f'{i+1}. {self.channels_list[i]}')



tv1=TV()
tv1.turn_on()
tv1.turn_off()
tv1.turn_on()
tv1.set_channels('TVP1')
tv1.set_channels('TVP2')
tv1.set_channels('Polsat')
tv1.set_channels('TVN')
tv1.set_channels('Filmbox')
tv1.set_channels('Discovery')
tv1.show_channels()
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.set_channel(3)
tv1.show_status()
tv1.set_channel(6)
tv1.show_status()
