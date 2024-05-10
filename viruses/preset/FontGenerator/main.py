import random

def glitch_text(text, intensity=0.5):
    """
    Generate glitch text from the given input text by adding characters on top of existing ones.
    
    Parameters:
        text (str): The input text to be glitched.
        intensity (float): Intensity of the glitch effect. Can be any positive number.
        
    Returns:
        str: Glitched text.
    """
    if intensity <= 0:
        raise ValueError("Intensity should be a positive number")
    
    glitched_text = ""
    for char in text:
        glitched_text += char
        if random.random() < intensity:
            for _ in range(random.randint(1, 10)):  # Increase the range for more glitchiness
                glitched_text += random.choice([
                    '\u0300',  # Combining Grave Accent
                    '\u0301',  # Combining Acute Accent
                    '\u0302',  # Combining Circumflex Accent
                    '\u0303',  # Combining Tilde
                    '\u0304',  # Combining Macron
                    '\u0305',  # Combining Overline
                    '\u0306',  # Combining Breve
                    '\u0307',  # Combining Dot Above
                    '\u0308',  # Combining Diaeresis
                    '\u0309',  # Combining Hook Above
                    '\u030A',  # Combining Ring Above
                    '\u030B',  # Combining Double Acute Accent
                    '\u030C',  # Combining Caron
                    '\u030D',  # Combining Vertical Line Above
                    '\u030E',  # Combining Double Vertical Line Above
                    '\u030F',  # Combining Double Grave Accent
                    '\u0310',  # Combining Candrabindu
                    '\u0311',  # Combining Inverted Breve
                    '\u0312',  # Combining Turned Comma Above
                    '\u0313',  # Combining Comma Above
                    '\u0314',  # Combining Reversed Comma Above
                    '\u0315',  # Combining Comma Above Right
                    '\u0316',  # Combining Grave Accent Below
                    '\u0317',  # Combining Acute Accent Below
                    '\u0318',  # Combining Left Tack Below
                    '\u0319',  # Combining Right Tack Below
                    '\u031A',  # Combining Left Angle Above
                    '\u031B',  # Combining Horn
                    '\u031C',  # Combining Left Half Ring Below
                    '\u031D',  # Combining Up Tack Below
                    '\u031E',  # Combining Down Tack Below
                    '\u031F',  # Combining Plus Sign Below
                    '\u0320',  # Combining Minus Sign Below
                    '\u0321',  # Combining Palatalized Hook Below
                    '\u0322',  # Combining Retroflex Hook Below
                    '\u0323',  # Combining Dot Below
                    '\u0324',  # Combining Diaeresis Below
                    '\u0325',  # Combining Ring Below
                    '\u0326',  # Combining Comma Below
                    '\u0327',  # Combining Cedilla
                    '\u0328',  # Combining Ogonek
                    '\u0329',  # Combining Vertical Line Below
                    '\u032A',  # Combining Bridge Below
                    '\u032B',  # Combining Inverted Double Arch Below
                    '\u032C',  # Combining Caron Below
                    '\u032D',  # Combining Circumflex Accent Below
                    '\u032E',  # Combining Breve Below
                    '\u032F',  # Combining Inverted Breve Below
                    '\u0330',  # Combining Tilde Below
                    '\u0331',  # Combining Macron Below
                    '\u0332',  # Combining Low Line
                    '\u0333',  # Combining Double Low Line
                    '\u0334',  # Combining Tilde Overlay
                    '\u0335',  # Combining Short Stroke Overlay
                    '\u0336',  # Combining Long Stroke Overlay
                    '\u0337',  # Combining Short Solidus Overlay
                    '\u0338',  # Combining Long Solidus Overlay
                    '\u0339',  # Combining Right Half Ring Below
                    '\u033A',  # Combining Inverted Bridge Below
                    '\u033B',  # Combining Square Below
                    '\u033C',  # Combining Seagull Below
                    '\u033D',  # Combining X Above
                    '\u033E',  # Combining Vertical Tilde
                    '\u033F',  # Combining Double Overline
                    '\u0340',  # Combining Gravis Below
                    '\u0341',  # Combining Acute Below
                    '\u0342',  # Combining Greek Perispomeni
                    '\u0343',  # Combining Greek Koronis
                    '\u0344',  # Combining Greek Dialytika Tonos
                    '\u0345',  # Combining Greek Ypogegrammeni
                    '\u0346',  # Combining Bridge Above
                    '\u0347',  # Combining Equals Sign Below
                    '\u0348',  # Combining Double Vertical Line Below
                    '\u0349',  # Combining Left Angle Below
                    '\u034A',  # Combining Not Tilde Above
                    '\u034B',  # Combining Homothetic Above
                    '\u034C',  # Combining Almost Equal to Above
                    '\u034D',  # Combining Left Right Arrow Below
                    '\u034E',  # Combining Upwards Arrow Below
                    '\u034F',  # Combining Grapheme Joiner
                    '\u0350',  # Combining Right Arrowhead Above
                    '\u0351',  # Combining Left Half Ring Above
                    '\u0352',  # Combining Fermata
                    '\u0353',  # Combining X Below
                    '\u0354',  # Combining Left Arrowhead Below
                    '\u0355',  # Combining Right Arrowhead Below
                    '\u0356',  # Combining Right Arrowhead and Down Arrowhead Below
                    '\u0357',  # Combining Right Half Ring Above
                    '\u0358',  # Combining Dot Above Right
                    '\u0359',  # Combining Asterisk Below
                    '\u035A',  # Combining Double Ring Below
                    '\u035B',  # Combining Zigzag Above
                    '\u035C',  # Combining Double Breve Below
                    '\u035D',  # Combining Double Breve
                    '\u035E',  # Combining Double Macron
                    '\u035F',  # Combining Double Macron Below
                    '\u0360',  # Combining Double Tilde
                    '\u0361',  # Combining Double Inverted Breve
                    '\u0362',  # Combining Double Rightwards Arrow Below
                    '\u0363',  # Combining Latin Small Letter A
                    '\u0364',  # Combining Latin Small Letter E
                    '\u0365',  # Combining Latin Small Letter I
                    '\u0366',  # Combining Latin Small Letter O
                    '\u0367',  # Combining Latin Small Letter U
                    '\u0368',  # Combining Latin Small Letter C
                    '\u0369',  # Combining Latin Small Letter D
                    '\u036A',  # Combining Latin Small Letter H
                    '\u036B',  # Combining Latin Small Letter M
                    '\u036C',  # Combining Latin Small Letter R
                    '\u036D',  # Combining Latin Small Letter T
                    '\u036E',  # Combining Latin Small Letter V
                    '\u036F'   # Combining Latin Small Letter X
                ])
    return glitched_text

def underline_text(text):
    underlined_text = ""
    for char in text:
        underlined_text += char + "\u0332"
    return underlined_text

def bold_text(text):
    # Define offsets for lowercase and uppercase letters
    lower_offset = 0x1D41A - ord('a')
    upper_offset = 0x1D400 - ord('A')
    
    # Generate bold text by adding the respective offset to each character
    bold_text = ''.join(
        chr(ord(char) + lower_offset) if 'a' <= char <= 'z' else
        chr(ord(char) + upper_offset) if 'A' <= char <= 'Z' else
        char for char in text
    )
    
    return bold_text

def italic_text(text):
    italic_offset = 0x1D622 - ord('a')  # Offset for lowercase letters
    italic_text = ''.join(
        chr(ord(char) + italic_offset) if char.isalpha() else char for char in text)
    return italic_text

def strikethrough_text(text):
    strikethrough_text = ""
    for char in text:
        strikethrough_text += char + "\u0336"  # Unicode combining long stroke overlay (strikethrough)
    return strikethrough_text

def asktextglitch():
 try:
  intensity = int(input("How intense would you like the glitch text to be?: "))
  text = input("Enter the text to glitchify: ")
  glitched = glitch_text(text, intensity=intensity)
  print(glitched)
 except Exception as e:
  print("An error accoured: " + str(e))

def asktextbold():
 try:
  text = input("Enter the text to make bold: ")
  bold = bold_text(text)
  print(bold)
 except Exception as e:
  print("An error accoured: " + str(e))

def asktextunderline():
 try:
  text = input("Enter the text to add a underline: ")
  underline = underline_text(text)
  print(underline)
 except Exception as e:
  print("An error accoured: " + str(e))

def asktextstriketrough():
 try:
  text = input("Enter the text to add striketrough effect: ")
  striketrough = strikethrough_text(text)
  print(striketrough)
 except Exception as e:
  print("An error accoured: " + str(e))

def asktextitalic():
 try:
  text = input("Enter the text to make italic: ")
  italic = italic_text(text)
  print(italic)
 except Exception as e:
  print("An error accoured: " + str(e))

def askfont():
  font = input("what font would you like to generate? (glitch, italic, bold, striketrough, underline)")
  if(font == "glitch"):
   asktextglitch()
  elif(font == "bold"):
   asktextbold()
  elif(font == "underline"):
   asktextunderline()
  elif(font == "striketrough"):
   asktextstriketrough()
  elif(font == "italic"):
   asktextitalic()
  else:
   print("Font is invalid or isnt supported.")
  askfont()

askfont()
