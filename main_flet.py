#!/usr/bin/env python3
"""
DE-GUI - Flet Version
Modern cross-platform GUI for the Drane Engineering assistive robotic arm

This is an alternative Flet-based GUI that provides the same functionality
as the PyQt6 version with a more modern, cross-platform interface.

Features:
- YOLOv11 real-time object detection
- MediaPipe face landmark tracking
- RealSense depth sensing (optional)
- Manual robotic arm controls
- Cross-platform (desktop, web, mobile)
"""

import sys
import warnings

import flet as ft

# Suppress user warnings
warnings.simplefilter("ignore", UserWarning)

from flet_gui.main_window import FletMainWindow


def main(page: ft.Page):
    """
    Flet application entry point

    Args:
        page: Flet page object
    """
    # Create main window
    window = FletMainWindow(page)

    # Handle cleanup on close
    def on_window_close(e):
        window.cleanup()

    page.on_close = on_window_close


if __name__ == "__main__":
    # Run Flet app
    print("Starting DE-GUI (Flet version)...")
    print("Press 'T' to toggle between face tracking and object detection")
    print("Close the window to exit")

    ft.app(target=main)
