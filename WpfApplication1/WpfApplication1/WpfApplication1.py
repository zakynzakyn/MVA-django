import wpf
import System.Windows.Controls


from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication1.xaml')
    
    def button_Click(self, sender, e):
        self.label.Content = self.textBox.Text
    

if __name__ == '__main__':
    Application().Run(MyWindow())
