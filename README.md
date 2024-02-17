**Sponsor Challenge**: MIT Quantum Computing: Quandela Challenge - 3rd Place Winner

**Project Name**: QForce

**Topic**: Quantum Generative Adversarial Learning in Photonics
 
**Contributors**: Connor Totilas, Edward Zhang, Pranavkrishna Suresh, Sameer Arora, Shokhruz Kakharov

**Introduction**:
Quantum Generative Adversarial Networks have potential advantages in comparison to their classical counterparts. However, current research shows that noise and defects have a significant impact on QGAN models and potentially decrease their fidelity. In our work, we aimed to find a suitable classical optimizer to better variationally train our quantum circuits and reduce as much noise and error as possible.

**Big Ideas and Implementation**:
- **Circuit Overview**: Wang et. al. in his paper proposed a variational quantum circuit arhcitecture for a QGAN implementation in photonics. The following is the composite implementation shown in the paper:
<img width="800" alt="Screenshot 2024-02-04 at 9 52 46 AM" src="https://github.com/pranavkrishnasuresh/Photonic-Quantum-GAN/assets/85195581/31865952-054b-4e45-b87e-5b01c60211e8">

  The following is our circuit implementation accounting for phase changes and beam shifts combining the generator and discriminator architecture.
  
  ![Screenshot 2024-02-04 at 9 10 13 AM](https://github.com/pranavkrishnasuresh/Photonic-Quantum-GAN/assets/85195581/0d740ef9-4c13-435a-b465-4f74c8dec7a5)

- **Generator**: The generator is one of the two main components of the QGAN which actively competes with the discriminator during the training process. 
The generator circuit creates a candidate quantum Fock state that attempts to replicate the true state in order to fool the discriminator.
- **Discriminator**:
The discriminator takes measurements on the input state to decide whether or not the generated state is the true state or not.
Acts as a feedback loop to assess the effectiveness of the generator based on the direction and magnitude of the loss function over its evolution.
- **Adversarial Loss**:
To assess the effectiveness of the QGAN, we implement a loss function accounting for parameters representing the generator and discriminator.
The discriminator and generator alternate in executing where the discriminator first optimizes its parameters to maximize d(θ<sub>G</sub>, θ<sub>D</sub>) then the generator optimizes to minimize d(θ<sub>G</sub>, θ<sub>D</sub>).
Through repetitive execution, the QGan evolves to solve the minimax problem as d(θ<sub>G</sub>, θ<sub>D</sub>).
<img width="589" alt="Screenshot 2024-02-04 at 9 21 21 AM" src="https://github.com/pranavkrishnasuresh/Photonic-Quantum-GAN/assets/85195581/1e2ee748-6d71-48a5-a1f7-18fd85039a05">

- **Optimizer**: 
THe optimizer that we decided to use was the Broyden-Fletcher-Goldfarb-Shanno (BFGS) and the limited memory variant (L-BFGS). We believe that other optimizers may yield better results - specific optimizers that compare relative qualities better in order to converge, even if at reduced speed. We choose L-BFGS because it was a very quick optimizer because it requires limited memory.

**How we built it:**
Using Perceval-Quandela’s framework for photonic quantum computers, we created two main Variational Quantum Circuits (VQC) - the generator and discriminator models found in classical GANs. Classical optimizers were built using Scipy optimizer classes. Results including probabilities of circuits and the losses are graphed.

**Challenges we faced:**
Since the Quandela Challenge focused on implementing an architecture from several papers, we had to piece together all the different components, which seemed initially diverse, into one cohesive codebase and workflow. We had a bit of trouble understanding the inputs and outputs of each circuit and network at every new stage and understanding how the classical optimization scheme would integrate in our VQCs without the use of classical machine learning model optimizers like backpropagation. 

More specifically, 
1. We were initially unsure if we should convert Fock states to Quqarts but we realized after that we didn’t need to do any conversions during training.
2. We figured out that we needed to create two distinct circuits because different parameters from the discriminator and the generator needed to be updated at different times.
3. The generator was not updating while the discriminator was updating: we tried to change the order with optimization/minimization but the generated output values still remained static. One thing that we also noticed was that the discriminator optimization ran for far fewer passes than the generator. 
<img width="449" alt="Screenshot 2024-02-04 at 9 30 42 AM" src="https://github.com/pranavkrishnasuresh/Photonic-Quantum-GAN/assets/85195581/98432d61-92fa-45f7-927f-e26d648ab847">

**What we learned**:
Through the course of the hackathon, we have become more experienced with Quandela’s Perceval framework which has also enabled us to attain a greater level of understanding of photon-based quantum computing. We have also learned how to implement QGan's and about the optimization process of running the Generator and Discriminator.

