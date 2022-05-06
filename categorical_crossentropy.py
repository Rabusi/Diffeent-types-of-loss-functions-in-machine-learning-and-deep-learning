Import numpy as np
predictions = np.array([[0.25,0.25,0.25,0.25],
                        [0.01,0.01,0.01,0.96]])
targets = np.array([[0,0,0,1],
                   [0,0,0,1]])
def categorical_crossentropy(predictions, targets, epsilon=1e-10):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce_loss = -np.sum(np.sum(targets * np.log(predictions + 1e-5)))
    return ce_loss
categorical_crossentropy_loss = categorical_crossentropy(predictions, targets)
print ("Categorical_cross entropy loss is: " + str(categorical_crossentropy_loss))