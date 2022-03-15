import yaml

from main import CoolDict

with open("test.yaml", 'r') as f:
    temp = yaml.safe_load(f)
    cd = CoolDict(temp)
    print(cd["Infer"].transforms[0].DecodeImage.to_rgb)

