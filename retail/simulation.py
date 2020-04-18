import numpy as np
import matplotlib.pyplot as plt


class Product:
    def __init__(self,
                 id_sku,
                 time_interval='week',
                 demand_mean_general=200,
                 demand_var=5,
                 adjust_mean=5,
                 adjust_var=1):

        self.id_sku = id_sku
        self.demand_mean_general = demand_mean_general
        self.demand_var = demand_var

        self.adjust_mean = adjust_mean
        self.adjust_var = adjust_var

        self.time_interval = time_interval

        if time_interval == 'day':
            self.demand_mean = np.ones(365)
        elif time_interval == 'week':
            self.demand_mean = np.ones(52)
        elif time_interval == 'month':
            self.demand_mean = np.ones(12)
        else:
            self.demand_mean = np.ones(time_interval)

        self.demand_mean *= self.demand_mean_general

        self._add_demand_adjustment()
        self._generate_demand_lambda()
        self._generate_demand()

    def _add_demand_adjustment(self):
        # XXX: Change this adjustment
        self.demand_mean += np.random.normal(self.adjust_mean, self.adjust_var)

    def _generate_demand_lambda(self):
        self.demand_lambda = np.zeros(1)

        while not (self.demand_lambda > 0).min():
            self.demand_lambda = np.random.normal(
                                 self.demand_mean, self.demand_var)

    def _generate_demand(self):
        self.demand = np.random.poisson(self.demand_lambda)

    def plot_demand(self, show=True):
        plt.plot(np.arange(len(self.demand_mean)), self.demand)
        plt.grid('--')
        plt.ylim(0, 1500)
        if show:
            plt.show()


if __name__ == '__main__':
    products = 5
    for p in range(products):
        product = Product(id_sku=str(p), demand_mean_general=400,
                          # demand_mean_general=(p+1)*200,
                          adjust_mean=100, adjust_var=300)
        # print(product.demand)
        product.plot_demand(show=False)
    plt.show()
