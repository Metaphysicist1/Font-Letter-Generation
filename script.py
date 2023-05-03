import numpy as np
import torch 
import torchvision
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms,datasets
from torchvision.transforms import transforms
import matplotlib.pyplot as plt

Transforms = transforms.Compose([
    transforms.ToTensor()
])

dataset = datasets.ImageFolder(root='/home/metaphysicist/Coding/Research/Font_Generation/data/Images/Images_dir/a',
                                transform=Transforms)


dataset_loader = DataLoader(dataset,batch_size=64, shuffle=False)
for batch_idx, (real, i) in enumerate(dataset_loader):
    # print(batch_idx, (real, i))
    # imgTensor, labels = next(loader_iter)

    img_grid_real = torchvision.utils.make_grid(
                        real[:1], normalize=True
                    )

    img_grid_real = img_grid_real.permute(1, 2, 0)
     # Set up plot config
    plt.figure(figsize=(8, 2), dpi=300)
    plt.axis('off')

    # Plot Image Grid
    plt.imshow(img_grid_real)


    # Show the plot
    plt.show()
# b = np.load('/home/metaphysicist/Coding/Research/Font_Generation/data/character_font.npz')

# print(b['images'])


# class RealLetters(Dataset):
#     def __init__(self,root_dir,transform):
#         self.root_dir=root_dir
#         self.set = None
#         self.transform=transform
        
#     def __getitem__(self, name):
#         # image = 
#         if self.transform not None:
#             self.transform(image)

#     def __len__(self):
#         return len(self.set)
