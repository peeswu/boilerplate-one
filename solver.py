import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import rotate
from scipy.signal import medfilt

input = np.load('input.npy')
target = np.load('target.npy')

# 0. Aby skrypt zadziałał, musisz zaciągnąć z serwera przewidziane dla siebie dane. Uzupełnij swój numer indeksu w skrypcie gather.py i uruchom go. Pliki ważą około 64MB, więc przy uczelnianym internecie należy wyposażyć się również w cierpliwość.
# 1. Odszum kostkę danych (input) aby uzyskać obraz. Samodzielnie odnajdź przy tym oś akwizycji
# 2. Odnajdź kąt obrotu odszumionego obrazu, o który został obrócony względem obrazu bazowego (target)
# 3. Prześlij prowadzącemu ten skrypt, wraz z krótkim opisem procedury, którą udało Ci się wykonać oraz informacją o kącie o który obrócony został obraz bazowy. Pamiętaj, że wszystkie skrypty będą poddawane analizie antyplagiatowej, a w wypadku wykrycia duplikującego się kodu, wszystkie osoby, które z niego skorzystały otrzymują ocenę niedostateczną.

fig = plt.figure(figsize=(10,10))
ax = plt.subplot(221)
ax.imshow(target, cmap='binary_r')

ax = plt.subplot(222)
ax.imshow(input[:,:,0], cmap='binary_r')

ax = plt.subplot(223)
ax.imshow(input[:,0,:], cmap='binary_r')

ax = plt.subplot(224)
ax.imshow(input[:,:,0], cmap='binary_r')

plt.savefig('foo.png')
