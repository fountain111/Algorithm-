class BaseSGD():

    def __init__(self,loss,penalty='l2',alpha=0.001,c=1.0,
                 learning_rate  = 'optimal'):
        self.loss = loss
        self.penalty = penalty
        self.alpha = alpha
        self.c = c
        self.learning_rate = learning_rate

    @abstractmethod
    def fit(self,x,y):
        """ Fit ,don't instance"""

    def _validate_params(self):

        if self.loss not in self.loss:
            pass





class BaseSGDClassifier(six.with_metaclass(ABCMeta, BaseSGD,
                                           LinearClassifierMixin)):


    loss_functions = {
    "hinge": (Hinge, 1.0),
    "squared_hinge": (SquaredHinge, 1.0),
    "perceptron": (Hinge, 0.0),
    "log": (Log,),
    "modified_huber": (ModifiedHuber,),
    "squared_loss": (SquaredLoss,),
    "huber": (Huber, DEFAULT_EPSILON),
    "epsilon_insensitive": (EpsilonInsensitive, DEFAULT_EPSILON),
    "squared_epsilon_insensitive": (SquaredEpsilonInsensitive,
                            DEFAULT_EPSILON),
}
