replacements = {}

with open("what_to_do_in_car_accident_eng.cfg", "r", encoding="utf8") as fh:
    for line in fh:
        replacement, description = line.strip().split(' ', 1)
        replacements[replacement] = description.strip()

template_fh = open ("what_to_do_in_car_accident.template", "r", encoding="utf8")
template = template_fh.read()

for index in replacements:
    template = template.replace('{{{}}}'.format(index), replacements[index].rstrip())

dot_file = open ("what_to_do_in_car_accident_eng.dot", "w", encoding="utf8")
dot_file.write(template)
dot_file.close()

replacements.clear()

with open("what_to_do_in_car_accident_rus.cfg", "r", encoding="utf8") as fh:
    for line in fh:
        replacement, description = line.strip().split(' ', 1)
        replacements[replacement] = description.strip()

template_fh = open ("what_to_do_in_car_accident.template", "r", encoding="utf8")
template = template_fh.read()

for index in replacements:
    template = template.replace('{{{}}}'.format(index), replacements[index].rstrip())

template_fh.close()

dot_file = open ("what_to_do_in_car_accident_rus.dot", "w", encoding="utf8")
dot_file.write(template)
dot_file.close()
