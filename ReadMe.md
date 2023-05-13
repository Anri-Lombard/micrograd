# Micrograd

Micrograd is a compact, self-contained, and easy-to-understand deep learning library. If you're looking to learn how deep learning works under the hood, this is an excellent starting point. As an Autograd library, Micrograd automatically computes gradients for you. Additionally, it serves as a neural network library, which means it can compute gradients and update your neural network's weights.

## Andrej-approved Notes

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Very nice notes! 👍👍</p>&mdash; Andrej Karpathy (@karpathy) <a href="https://twitter.com/karpathy/status/1594537380144623616?ref_src=twsrc%5Etfw">November 21, 2022</a></blockquote>


## Review of video and project

Andrej Karpathy is an inspiring figure as an engineer, leader, and teacher. He is passionate about teaching as a way to create more "Happy Humans," and that's a fantastic goal to strive for. I've been following his work for some time, and I'm thrilled to watch this video and build the project alongside him. As budding engineers, we're fortunate to have access to such valuable resources for free.


This video demonstrates the fundamental aspects of training a neural network. It strips away padding for efficiency and complex training methods, leaving only the core principles. This approach provides an excellent opportunity to grasp what's happening under the hood. Although the course may seem slightly daunting for beginners who haven't heard terms like "gradient descent" before, Andrej thoroughly explains each concept and avoids using jargon.


If you have high expectations for this video, you won't be let down. Andrej's pace is relatively fast compared to other videos and courses, but keeping up with his speed is both enjoyable and rewarding. A massive thank you to Andrej!

## Tips I found useful in learning to build this project

I have 14 years of formal schooling under my belt (primary/high school and university), and I've spent countless hours learning. Over time, I've realized the importance of online learning and figured out effective learning strategies through iteration.

1. Watch a section of the video without coding. If it helps you focus, take notes (as long as you concentrate - notes aren't always necessary, but they help me internalize the information).
2. Go through the code step by step without the video, attempting to explain and label each step in your own words. If you get stuck, refer back to what Andrej said.
3. (Optional - Completing steps 1 and 2 provides 80% of the learning, while this step adds a few extra percent) Try implementing the project on your own without referring to Andrej's code.

## Building Micrograd

### Overview

* Micrograd performs the mathematical operations required to train a neural network, such as:
    1. Forward pass
        * Computes the neural network's output given an input and a set of weights
    2. Backpropagation
        * Calculates the gradient of the loss function with respect to the neural network's weights by computing the gradient of the loss function concerning the neural network's output and then computing the gradient of the output with respect to the neural network's weights. This process is performed recursively until the gradient of the loss function concerning the neural network's input is computed.
* Andrej asserts that Micrograd is all you need to train neural networks, and the rest is added for efficiency and convenience. This is why understanding Micrograd is so crucial.
    1. For example, tensors (which Micrograd does not use) are employed to perform multiple scalar operations in parallel.
    2. Despite being a fundamental component of machine learning, Micrograd is surprisingly simple, consisting of only two Python files.

### Derivative of a simple function

* The derivative of a function represents the slope of the tangent line at a specific point or the rate of change of the function at that point.
    1. Although Andrej assumes that we have taken a calculus class, he still provides a detailed explanation of what the derivative of a function is.

    ![differentiability of a function](images/Differentiablility.png)

    He uses the differentiability definition of a function to demonstrate how single and multi-variable inputs might affect a function's derivative.

### Building the Core Value Object of Micrograd and its Visualization

* Micrograd's core object is the Value object. It's a straightforward object with a value and a gradient. The gradient is the derivative of the value concerning the input of the function. The gradient is initialized to 0 and updated by the backward() function.
    1. Andrej walks through implementing the Value object and demonstrates how it performs computations with different operations we specify.
    2. He uses the Graphviz library to visualize the computation graph of the Value object, providing an excellent way to see the computation graph and understand how the gradient is computed.

    ![Value object](images/Value.jpeg)

### Backpropagation

* A considerable amount of calculus is used to calculate partial derivatives (thank goodness I study math! Look, mom, I'm using it!)
    1. To perform backpropagation, we use the chain rule to determine the effect of each operation on the gradient of the output.
* Neurons are categorized into input neurons, hidden neurons, and output neurons. Input neurons provide input to the neural network, hidden neurons are found in the hidden layers, and output neurons produce the neural network's output.
    1. Neurons have complex mathematical representations, but we use a simplified representation of a neuron as a Value object with a weight and a bias.
    2. We pass all inputs through an activation function (in this case, a tanh function) to obtain the neuron's output.
    3. The result is the dot product of the inputs and the neuron's weights, plus the neuron's bias.
* We manually implemented backpropagation before automating it for one neuron.
    1. We implemented the backward() function for each operation to perform automatic backpropagation.
    2. To automate the process, we constructed a directed acyclic graph (DAG) of the computation graph, which displays the order of operations and the dependencies between them.

### Putting it together

* We implemented all necessary operations to perform forward and backpropagation with any operation (+, -, /, *, tanh).
    1. Andrej emphasizes mastering the basics, so we explored derivative rules and dissected the tanh function into an equation using the hyperbolic tangent function.
      - He demonstrated that regardless of how complicated the function we use is, as long as we correctly execute the forward pass and backpropagation, we can use any suitable function.
* Andrej showed how PyTorch handles these operations using tensors, which allow for parallel computation of numerous scalar operations. Tensors are arrays of scalar values.

### Building a neural net library (multi-layer perceptron)

* First, we implemented a neuron class and added forward pass and backpropagation functionality.
* Next, we implemented a Layer class containing a list of neurons, followed by the MLP class, which houses a list of layers.

### Training the neural net

* We added parameters to the Neuron, Layer, and MLP classes and performed gradient descent on a small, makeshift dataset.
    1. Andrej showed how easy it is to overstep the gradient descent and overshoot the minimum, which is what makes it a subtle art to get the right learning rate.
    2. Andrej made the exact mistake he tweeted in 2018 to avoid, which was pretty funny and insightful. We need to .zero_grad() before .backward() to avoid accumulating gradients.

### Summary

A neural network takes in inputs, does a forward pass to make predictions, then does a backpropagation to update the weights of the neural network so that it makes even more accurate predictions (known as gradient descent). This is done iteratively until the neural network is good enough to make accurate predictions.

This is done in many different ways, but all of them make use of these fundamentals detailed in Micrograd. The only difference is how they are implemented, and how they are used to train neural networks. Micrograd is a great way to understand the fundamentals of neural networks and how they are trained.


## References

* [Andrej Karpathy's Micrograd Project](https://github.com/karpathy/micrograd)
* [Andrej Karpathy's Micrograd Video](https://youtu.be/VMj-3S1tku0)
