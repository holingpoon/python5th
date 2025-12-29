import ch26_samples
from pprint import pprint

print("name", ch26_samples.name)
print("height", ch26_samples.height)
pprint(ch26_samples.__dict__)

print("height is also", ch26_samples.__dict__["height"])

print(f"I am current {ch26_samples.height} inches tall.")

ch26_samples.__dict__['height'] = 1000
print(f"I am now {ch26_samples.height} inches tall.")

ch26_samples.height = 12
print(f"Oops, now I'm {ch26_samples.__dict__['height']} inches tall.")

from importlib import reload
reload(ch26_samples)
print("Reloaded module ch26_samples")
print(f"Oops, now I'm {ch26_samples.__dict__['height']} inches tall.")

print(pprint.__doc__)
help(pprint)
