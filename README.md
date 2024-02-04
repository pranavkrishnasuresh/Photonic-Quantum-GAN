**Sponsor Challenge**: Quandela

**Topic**: Quantum Generative Adversarial Learning in Photonics

**Contributors**: Connor Totilas, Edward Zhang, Pranavkrishna Suresh, Sameer Arora, Shokhruz Kakharov

**Introduction**:
Quantum Generative Adversarial Networks have potential advantages in comparison to their classical counterparts. However, current research shows that noise and defects have a significant impact on QGAN models and potentially decrease their fidelity. In our work, we aimed to find a suitable classical optimizer to better variationally train our quantum circuits and reduce as much noise and error as possible.

**Implementation Details**

- **Generator**: The generator is one of the two main components of the QGAN which actively competes with the discriminator during the training process. 
The generator circuit creates a candidate quantum Fock state that attempts to replicate the true state in order to fool the discriminator.
- **Discriminator**:
The discriminator takes measurements on the input state to decide whether or not the generated state is the true state or not.
Acts as a feedback loop to assess the effectiveness of the generator based on the direction and magnitude of the loss function over its evolution.
- **Adversarial Loss**:
To assess the effectiveness of the QGAN, we implement a loss function accounting for parameters representing the generator and discriminator.
The discriminator and generator alternate in executing where the discriminator first optimizes its parameters to maximize d(θ<sub>G</sub>, θ<sub>D</sub>) then the generator optimizes to minimize d(θ<sub>G</sub>, θ<sub>D</sub>).
Through repetitive execution, the QGan evolves to solve the minimax problem as d(thetaG, thetaD).
<img width="589" alt="Screenshot 2024-02-04 at 9 21 21 AM" src="https://github.com/pranavkrishnasuresh/Photonic-Quantum-GAN/assets/85195581/1e2ee748-6d71-48a5-a1f7-18fd85039a05">

