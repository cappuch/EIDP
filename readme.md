# EIDP (Enhanced Inverse Dynamics Prediction)
EIDP is the codebase accompanying the micro-paper titled 'Enhanced Inverse Dynamics Prediction for Robot Control Using Deep Residual Networks' (also referred to as a beefed up IDM).

Paper: [EIDP](https://wandb.ai/mikusdevr/IDM/reports/Enhanced-Inverse-Dynamics-Prediction-for-Robot-Control-Using-Deep-Residual-Networks--Vmlldzo3NDczNDc1)

## Models
### ResNet-18-V1
  [ResNet18-V1 epochs 0-64](https://huggingface.co/opensdetenn/resnet18_linear_v1)
  
  [ResNet18-V1 with the lowest validation loss](https://huggingface.co/opensdetenn/resnet18_linear_v1-optimal/resolve/main/pytorch_model.pth)

## Colab
A Colab notebook will be available soon. For now, please use the current code provided. Download the weights you need and run inference.

## Usage
Running this code is rather self-explanatory. Simply download the weights you require and run inference. If someone on this project wishes to commit to a proper README, feel free to contribute.

## Architecture
The architecture is based on the ResNet-18 architecture, fine-tuned on the driving dataset. Each of the vectors is attached to a linear neuron. It's a simple yet efficient setup.
