import yaml
with open("data.yaml", "r") as f:
    yaml_data = yaml.safe_load(f)
print(yaml_data)

a = [[{'a': 1}, 'admin2'], 'admin3',11]

with open("data3", "w") as f:
    yaml.safe_dump(a,f)