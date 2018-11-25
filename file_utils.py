def read_game_names(filename):
  with open(filename) as f:
    content = f.readlines()
    if content:
      content = map(lambda x: x.rstrip('\r\n').split(',')[0].decode('utf-8','ignore').encode('utf-8'), content)
      return content
