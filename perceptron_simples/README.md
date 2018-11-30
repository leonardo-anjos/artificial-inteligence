
## perceptron simple

algorithm inspired by the information processing of a single reural cell called a neuron 

this algorithm solve the problem of classification dermatology

@see<br>
https://towardsdatascience.com/6-steps-to-write-any-machine-learning-algorithm-from-scratch-perceptron-case-study-335f638a70f3<br>
https://sebastianraschka.com/Articles/2015_singlelayer_neurons.html<br>

![artificial network](https://upload.wikimedia.org/wikipedia/commons/6/60/ArtificialNeuronModel_english.png)

**algorithm goal** <br>
determine the type of erythematous-squamous disease

**obs:** remove old column in dataset

**relevant informations:**
- the basis has ***34*** attributes, of which ***33*** are valued linear and ***1*** of them and nominal
- the family history has value ***1*** if any of these diseases have been observed and ***0*** otherwise
- all clinical and histopathological characteristics were given a range degree from ***0*** to ***3***

***
0: indicates that the resource was not present <br>
3: indicates the largest quantity possible <br>
1, 2: relative intermediate values
***

***to run code:*** <br>
python v3.x <br>
python slp_dermatology.py