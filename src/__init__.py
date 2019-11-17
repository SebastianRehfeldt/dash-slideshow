"""Main Module which includes constants for file paths"""
import os

SERVER_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.join(SERVER_PATH, os.pardir)
ASSETS_PATH = os.path.join(SERVER_PATH, "assets")
