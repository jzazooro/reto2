from scipy import stats

class capa():
    def __init__(self, n_neuronas_capa_anterior, n_neuronas, funcion_act):
        self.funcion_act = funcion_act
        self.b = np.round(stats.truncnorm.rvs(-1, 1, loc=0, scale=1, size= n_neuronas).reshape(1, n_neuronas), 3)
        self.w = np.round(stats.truncnorm.rvs(-1, 1, loc=0, scale=1, size= n_neuronas*n_neuronas_capa_anterior).reshape(n_neuronas_capa_anterior), 3)