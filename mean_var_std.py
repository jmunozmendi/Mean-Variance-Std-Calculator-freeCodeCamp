import numpy as np

def calculate(list):

    if len(list)<9:
      raise ValueError( "List must contain nine numbers.")

    matrix = np.reshape(np.array(list),(3,3))
    calculations = {
  'mean': [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(list).tolist()],
  'variance': [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), np.var(list).tolist()],
  'standard deviation': [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(list).tolist()],
  'max': [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(list).tolist()],
  'min': [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(list).tolist()],
  'sum': [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(list)],
}


    return calculations