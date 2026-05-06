import os
from WordFrequencies import WordFrequencies
from sample import WeightedSample

class WordGrid:

  def get_template_path(self):
    file_path = os.path.realpath(__file__)
    template_path = file_path
    template_path = os.path.abspath(os.path.join(template_path, os.pardir))
    #template_path = os.path.join(template_path, 'rsrc')
    template_path = os.path.join(template_path, 'grid-template.html')
    return template_path

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






def main():
    wg = WordGrid()
    wf = WordFrequencies()

    adjectives = wf.get_source('adjectives')
    wsAdjectives = WeightedSample(adjectives, 27)
    adjectiveSample = wsAdjectives.extract()

    nouns = wf.get_source('nouns')
    wsNouns = WeightedSample(nouns, 27)
    nounSample = wsNouns.extract()

    path = wg.get_template_path()
    p_list = [
      "10111", "10112", "10113", 
      "10121", "10122", "10123",
      "10131", "10132", "10133",
      "10211", "10212", "10213", 
      "10221", "10222", "10223",
      "10231", "10232", "10233",
      "10311", "10312", "10313", 
      "10321", "10322", "10323",
      "10331", "10332", "10333",

      "20111", "20112", "20113", 
      "20121", "20122", "20123",
      "20131", "20132", "20133",
      "20211", "20212", "20213", 
      "20221", "20222", "20223",
      "20231", "20232", "20233",
      "20311", "20312", "20313", 
      "20321", "20322", "20323",
      "20331", "20332", "20333",
      ]
    r_list = [item[1] for item in adjectiveSample] + [item[1] for item in nounSample]
    with open(path, newline='') as file:
      lines = [wg.templated_replacement_by_line(line, p_list, r_list) for line in file]
    text = "".join(lines)

    with open("page0.html", "w", newline='') as output:
      output.write(text)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

