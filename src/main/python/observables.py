import numpy as np

def magnetization(N: int, grid: [[int]]):
    grid_sum = 0
    for row in grid:
        for s in row:
            grid_sum += s

    return abs(grid_sum/(N**2))


def magnetization_mean(magnetization_list):
    return np.mean(magnetization_list), np.std(magnetization_list)

def magnetization_squared_mean(magnetization_list):
    magnetization_squared_list = list(map(lambda x: x**2, magnetization_list))
    return np.mean(magnetization_squared_list), np.std(magnetization_squared_list)

def susceptibility(N, magnetization_list):
    m_mean, m_std = magnetization_mean(magnetization_list)
    m_2_mean, m_2_std = magnetization_squared_mean(magnetization_list)

    sus = (N**2) * (m_2_mean - (m_mean ** 2))
    sus_std = (N**2) * np.sqrt(m_2_std**2 + (2 * m_mean * m_std) ** 2)
    return sus, sus_std


