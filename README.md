# PixelArtAvatarGenerator

This readme will outline the methodology taken throughout the project.

Tools:
-----------------------
1. canny.py: script for generating canny edges
2. dirRez.py: script for resizing directories of images
3. promptGenerator.ipynb: script for generating prompts for pixel art.

Start:
-----------------------
1. The dataset was obtained from an online sprite sheet obtained by dumping the game.
2. The data set was resized to 256x256 and 1024x1024 using the resize script.
3. The canny edges for each size were obtained using the canny script provided.
4. A portion of the FFHQ dataset was obtained (1000 images).

CycleGAN Baselines:
-----------------------
1. Cloned the cycleGAN Repo.
2. Installed the associated conda environment.
3. Structured the dataset in a way that is acceptable to cycleGAN (domainA and domainB)
4. Direct cycleGAN translation of Real Images into pixel ART [~ 10 hours on a v100 w/ 32 GB mem]:
   
	cd courses/genAI/project/CycleGAN_Real/pytorch-CycleGAN-and-pix2pix/
	conda activate pytorch-CycleGAN-and-pix2pix
	srun --time=12:30:00 --gres=gpu:v100:1 --mem=32G --resv-ports=1 --pty /bin/bash -l
	ssh -NfR $SLURM_STEP_RESV_PORTS:localhost:$SLURM_STEP_RESV_PORTS $(whoami)@glogin.ibex.kaust.edu.sa
	python3 train.py --display_id -1 --no_html --dataroot ../sp1024 --model cycle_gan

6. Repeat the same process to translate real images into sketches and then fine tune it using the pixel ART

BLIPv2 prompt Generation:
----------------------- 
1. run cells in ipynb file

ControlNET Baselines:
----------------------- 
(The three files associated with ControlNet are prompt.json, 
and the tutorial files which are modified versions of the ones from the OG repo)
1. Cloned the cycleGAN Repo.
2. Installed the associated conda environment.
3. Structured the dataset in a way that is acceptable to ControlNet (using the prompt JSON notation)
4. Followed instruction largely from: https://github.com/lllyasviel/ControlNet/blob/main/docs/train.md

   
