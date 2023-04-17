import numpy as np

def calculate(lista):
    
    try:
        mat = np.asarray(lista).reshape((3,3))
        print(mat)
    except:
        raise ValueError("List must contain nine numbers.")

    means = [np.mean(mat, 0).tolist(), np.mean(mat, 1).tolist(), np.mean(mat).tolist()]
    variances = [np.var(mat, 0).tolist(), np.var(mat, 1).tolist(), np.var(mat).tolist()]
    stddevs = [np.std(mat, 0).tolist(), np.std(mat, 1).tolist(), np.std(mat).tolist()]
    maxes = [np.amax(mat, 0).tolist(), np.amax(mat, 1).tolist(), np.amax(mat).tolist()]
    mins = [np.amin(mat, 0).tolist(), np.amin(mat, 1).tolist(), np.amin(mat).tolist()]
    sums = [np.sum(mat, 0).tolist(), np.sum(mat, 1).tolist(), np.sum(mat).tolist()]
    
    calculations = {'mean': means,
                    'variance': variances,
                    'standard deviation': stddevs,
                    'max': maxes,
                    'min': mins,
                    'sum': sums,
                    }
                    
    return calculations
