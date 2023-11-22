import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Model Selection')
    parser.add_argument('--model', type=str, required=True, help='Model to use')
    args = parser.parse_args()
    return args.model

model = parse_arguments()

import requests
import threading
import subprocess
import os
import sys

import config


def setup():
    if not os.path.exists(config.model_folder):
        if input(f"Model folder {config.model_folder} does not exist. Create it? (y/n) ").lower() == 'y':
            os.mkdir(config.model_folder)
    current = os.listdir(config.model_folder)
    for model in config.models:
        if model == 'default':
            continue
        if config.models[model]['type'] == 'local':
            if config.models[model]['filename'] not in current:
                if input(f'Model {model} not found in {config.model_folder}. Would you like to download it? (y/n) ').lower() == 'y':
                    url = config.models[model]['url']
                    print(f"Downloading {model} from {url}...")
                    subprocess.run(['curl', '-L', url, '-o', os.path.join(
                        config.model_folder, config.models[model]['filename'])])
            else:
                print(f"Model {model} found in {config.model_folder}.")


class ModelPickerApp:
    def __init__(self):
        super(ModelPickerApp, self).__init__("ModelPickerApp")

        # Dynamically create menu items from the MENUBAR_OPTIONS
        self.menu_items = {}
        for option in config.models:
            if option == 'default':
                continue
            self.menu_items[option] = 

        self.menu = list(self.menu_items.values())
        self.menu_items[config.models['default']].state = True
        self.icon = "icon.png"

    def pick_model(self, sender):
        # Toggle the checked status of the clicked menu item
        sender.state = not sender.state

        # Send the choice to the local proxy app
        if sender.state:
            choice = sender.title
            try:
                response = requests.post(
                    "http://localhost:5001/set_target", json={"target": choice})
                if response.status_code == 200:
                    print(f"Successfully sent selection: {choice}.")
                else:
                    
            except requests.RequestException as e:
                

        # If other options were previously selected, deselect them
        for item in self.menu:
            if item == 'Quit':
                continue
            if item != sender.title:
                self.menu_items[item].state = False

    def run_server(self):
        subprocess.run(['python', 'proxy.py'])


if __name__ == '__main__':
    if '--setup' in sys.argv:
        setup()
    app = ModelPickerApp()
    print("Running server...")
    server_thread = threading.Thread(target=app.run_server)
    server_thread.start()
    app.run()
