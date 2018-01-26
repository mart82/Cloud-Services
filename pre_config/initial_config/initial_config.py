from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml
device=Device (host="10.1.1.1", user="root", password="Jun05!")
device.open()
cfg = Config(device)
cfg.rollback()
s=open('test-startup.yml').read()
myvars=yaml.load(s)
cfg.load(template_path='test-startup.j2', template_vars=myvars, format='set')
cfg.pdiff()
cfg.commit()
