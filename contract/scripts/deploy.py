from brownie import CommunityAudits, network, config
from scripts.helpers import get_account
import shutil
import os
import yaml
import json
from web3 import Web3


def deploy_community_audits(update_client_flag=False):
    account = get_account()
    community_audits = CommunityAudits.deploy({"from": account})

    print("Deployed CommunityAudits contract to:", community_audits.address)
    if update_client_flag:
        update_client()


def update_client():
    print("Updating front end...")
    # The Build
    copy_folders_to_client("./build/contracts", "../client/src/chain-info")

    # The Contracts
    copy_folders_to_client("./contracts", "../client/src/contracts")    
    # The Map
    copy_files_to_client(
        "./build/deployments/map.json",
        "../client/src/chain-info/map.json",
    )

    # The Config, converted from YAML to JSON
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("../client/src/brownie-config-json.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Front end updated!")


def copy_folders_to_client(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def copy_files_to_client(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copyfile(src, dest)


def main():
    deploy_community_audits(update_client_flag=True)
