from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Game")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height = height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks() 
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False





def main():
    win = Window(800,600)
    win.wait_for_close()

# So the file will be executed only if i execute the file directly and no if i just import it in another file
if __name__ == "__main__":
    main()

    
