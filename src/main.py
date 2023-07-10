try:
  from PIL import Image
  import bfi
  import sys
except:
  print('Intsall Dependencies')
class Compiler:
  def __init__(self):
    self.code = ''
    self.image = ''
    self.pixel_values = []
    
    self.pixel_size = 1
    self.lang = {
      (255, 0, 0): '>',
      (0, 255, 0): '<',
      (0, 0, 255): '+',
      (0, 255, 255): '-',
      (255, 0, 255): '.',
      (255, 255, 0): ',',
      (255, 165, 0): '[',
      (128, 0, 128): ']'
    }
  def img_export(self,file_path:str,export_path:str):
    with open(file_path, "r") as self.export_code:
      self.export_code_content = self.export_code.read()
    self.width = len(self.export_code_content)
    self.height = 1
    
    self.export_image = Image.new("RGB", (self.width * self.pixel_size, self.height * self.pixel_size), color=(255, 255, 255))
    self.export_pixels = self.export_image.load()
    self.export_lang ={
      '>' : (255, 0, 0),
      '<' : (0, 255, 0),
      '+' : (0, 0, 255),
      '-' : (0, 255, 255),
      '.' : (255, 0, 255),
      ',' : (255, 255, 0),
      '[' : (255, 165, 0),
      ']' : (128, 0, 128)
    }
    index = 0
    for char in self.export_code_content:
        if char in self.export_lang:
            rgb_value = self.export_lang[char]
            x = index * self.pixel_size
            y = 0
            for i in range(self.pixel_size):
                for j in range(self.pixel_size):
                    self.export_pixels[x + i, y + j] = rgb_value
            index += 1
    self.export_image.save(export_path)
  def load_src_img(self,file_path:str):
    self.image = Image.open(file_path)
    self.image = self.image.convert("RGB")
    self.pixel_values = list(self.image.getdata())
  def compile_and_run(self):
      for i in range(len(self.pixel_values)):
        if i % 1 == 0:
            token = self.pixel_values[i]
            if token in self.lang:
                sign = self.lang[token]
                self.code += sign
      bfi.interpret(self.code)
if __name__ == "__main__":
  arguments = sys.argv
  session = Compiler()
  
  if arguments[1] == 'compile':
    session.load_src_img(arguments[2])
    session.compile_and_run()
  elif arguments[1] == 'export':
    session.img_export(arguments[2],arguments[3])
  else:
    print('Invalid Feature')
