#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  
  url = url.strip()
  
  # scheme must start w http or https
  if not url.startswith("http://") and not url.startswith("https://"):
    return False
  
    
  #there can only be a single #
  hashcount= url.count('#')
  if hashcount > 1:
    return False

  #there can only be a single ?
  questcount= url.count ('?')
  if questcount > 1:
    return False

  #if a # is present, must appear before the ? if present
  #first, use find to determine index position of # and ? 
  hashpos= url.find('#')
  questpos= url.find('?')
  #if pos of hash is greater than pos of question mark, and its not because the question mark dne, then url invalid
  if hashpos > questpos and questpos != -1:
    return False 

  #there cannot be any spaces in the URL
  if " " in url:
    return False

  #hostname must not be empty
  before,after = url.split('://') #this line splits up the scheme as before, and the rest of the url as after
  poscolon = after.find(':') #this line finds the position of the colon if it exists
  posslash = after.find ('/') #this line finds position of the slash, dont need to specify to look after :// bc using after
  colcount= after.count(":") #no more than one colon in url
  if colcount > 1:
    return False
  slashcount= after.count("/") 
  if slashcount < 1: #must be at least one slash, need at least a slash after the hostname
    return False 
    
  if poscolon != -1:   #if the colon exists, then...
    if poscolon > posslash: #the colon must come before slash
      return False
    if after [: poscolon] == "": # the string starting at position 0 of the after string, until the position of the colon 
      return False     #must not equal "" or none or empty
  if poscolon == -1:
    if after [: posslash] == "": #else if the colon doesnt exist, then the hostname is string slice 0 to slash
      return False   # that string must not be empty
    

#port, if present, must only be digits; it must be separated from the hostname with a colon (:); no other colons may be present in the url;
  colcount= after.count(":") #no more than one colon in url after ://
  if colcount > 1:
    return False
  if colcount == 1:
    host,port = after.split (':')
    posslash = port.find ('/') 
    port= port [0:posslash]
    for char in port [0:posslash]: #each char in port must be digit
      if not port.isdigit():
        return False

      
  return True


def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")
          
            

testurl()

