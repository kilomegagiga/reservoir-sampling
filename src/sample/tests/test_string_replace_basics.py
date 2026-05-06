import os

class Test_string_replacement:
  def test_must_replace_strings(self):
    s = "text 10111 text"
    replaced = s.replace("10111", "red", 1)
    assert "text red text" == replaced

class Test_template:
  def get_template_path(self):
    file_path = os.path.realpath(__file__)
    template_path = file_path
    template_path = os.path.abspath(os.path.join(template_path, os.pardir))
    template_path = os.path.join(template_path, 'test_rsrc')
    template_path = os.path.join(template_path, 'template.html')
    return template_path

  def test_must_exist(self):
    path = self.get_template_path()
    assert os.path.exists(path)
    with open(path, newline='') as file:
      lines = file.readlines()
    assert 20 == len(lines)

  def replace_multiple(self, line):
    reply = line
    reply = reply.replace("10111", "red")
    reply = reply.replace("10112", "green")
    reply = reply.replace("10113", "blue")
    reply = reply.replace("10121", "cyan")
    reply = reply.replace("10122", "magenta")
    reply = reply.replace("10123", "yellow")
    return reply
    
  def test_must_replace_placeholders(self):
    path = self.get_template_path()
    with open(path, newline='') as file:
      lines = [self.replace_multiple(line) for line in file]
    text = "\n".join(lines)
    assert -1 == text.find("10111")
    assert -1 == text.find("10123")
    assert -1 != text.find("red")
    assert -1 != text.find("yellow")

  def make_replacement_tuples(self, placeholders, replacements):
    size = len(placeholders)
    if size > len(replacements):
      size = len(replacements)
    reply = []
    for index in range(size):
      reply.append( (placeholders[index], replacements[index]) )
    return reply
      
  def templated_replacement_by_line(self, line, placeholders, replacements):
    reply = line
    tuples = self.make_replacement_tuples(placeholders, replacements)
    for rule in tuples:
      reply = reply.replace(rule[0], rule[1])
    return reply

  def test_must_fill_template(self):
    path = self.get_template_path()
    p_list = ["10111", "10112", "10113", "10121", "10122", "10123"]
    r_list = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    with open(path, newline='') as file:
      lines = [self.templated_replacement_by_line(line, p_list, r_list) for line in file]
    text = "\n".join(lines)
    assert -1 == text.find("10111")
    assert -1 == text.find("10123")
    assert -1 != text.find("red")
    assert -1 != text.find("yellow")
