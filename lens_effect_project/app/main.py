from torchvision import transforms

from model.data.dataLoaders import DataLoaderFactory, DataLoaderLabels
from model.utils import const, tools
from model import trainers

def train_and_test_cifar10():
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
    ])
    train_dataloader, test_dataloader = DataLoaderFactory.get_cifar10(
        const.PATH_TO_SAVE_MODEL,
        True,
        const.BATCH_SIZE_32,
        transform
    )
    classes = DataLoaderLabels.cifar10

    device = tools.select_device()

    trainer = trainers.CNNTrainer(
        classes, 
        train_dataloader,
        device
    )
    trainer.train()
    trainer.test(test_dataloader)

    trainer.save(
        const.PATH_TO_SAVE_MODEL + 'cifar10_model.pth'
    )


def train_and_test_simple_gan():
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
    ])
    train_dataloader = DataLoaderFactory.get_galaxy(
        const.PATH_OF_PREDOs_PC,
        transform,
        const.BATCH_SIZE_128
    )

    device = tools.select_device()

    trainer = trainers.SimpleGANTrainer(train_dataloader, device)

    # p_disc = '/home/ariel/Documents/tesis-ia/lens_effect_project/app/data/save_model/save_modelsimple_gan_model_dis'
    # p_gen = '/home/ariel/Documents/tesis-ia/lens_effect_project/app/data/save_model/save_modelsimple_gan_model_gen'
    # trainer.train(p_disc, p_gen, 1)
    trainer.train()

    trainer.save(
        'simple_gan_model.pth'
    )


def train_and_test_wgan():
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
    ])
    train_dataloader = DataLoaderFactory.get_galaxy(
        const.PATH_OF_PREDOs_PC,
        transform,
        const.BATCH_SIZE_128
    )

    device = tools.select_device()

    trainer = trainers.WGANTrainer(train_dataloader, device)

    # p_disc = '/home/ariel/Documents/tesis-ia/lens_effect_project/app/data/save_model/save_modelsimple_gan_model_dis'
    # p_gen = '/home/ariel/Documents/tesis-ia/lens_effect_project/app/data/save_model/save_modelsimple_gan_model_gen'
    # trainer.train(p_disc, p_gen, 1)
    trainer.train()

    trainer.save(
        'wgan_model.pth'
    )

def main():
    train_and_test_wgan()
    

if __name__ == '__main__':
    try:
        import torch
        torch.cuda.empty_cache()
    except Exception as e:
        print(f"Error: {e}")
    main()