import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = 'Simsun (founder extended)'
x = np.linspace(-10, 10, 100)
y = np.sin(x)
z = np.cos(x)
fig = plt.figure(figsize=(4, 3))
ax = fig.gca()
ax.plot(x, y, label='正弦曲线')
ax.plot(x, z, label='余弦曲线')
ax.set_xlim((-10, 10))
ax.set_xlabel('相位角（rad）')
ax.set_ylabel('三角函数值')
ax.legend()
fig.tight_layout()
plt.show()
# fig.savefig('fig3.png', dpi=150)