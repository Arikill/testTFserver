import tensorflow as tf

class F1:
    def __init__(self) -> None:
        self.built = False
        pass

    def build(self, input_shape):
        self.built = True
        pass
    
    @tf.function
    def __call__(self, inputs):
        if not self.built:
            self.build(inputs.shape)
        return tf.square(inputs)