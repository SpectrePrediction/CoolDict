# CoolDict
将任意字典以任意方式访问，配合yaml食用更佳

## CoolDict是非侵入式的，你随时可以取回原来的dict

通过访问
```python
cd = CoolDict(temp)
cd.maintain_dict
```

## CoolDict允许混合访问

你可以通过
```python
cd.Infer.transforms[0].DecodeImage.to_rgb
```
也可以通过:
```python
cd["Infer"].transforms[0].DecodeImage.to_rgb
```
访问一个复杂的字典
```
{'Infer': {'transforms': [{'DecodeImage': {'to_rgb': True, 'channel_first': False}},
```
（由yaml转换而来）


其余都是一样的
他就像一个dict
你随时可以通过 del 删除

## 为什么叫CoolDict？

我很喜欢这个名字，这是个临时想到的简易项目，很cool😎

## MIT 享受开源
