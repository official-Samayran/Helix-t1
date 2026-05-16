import os
import subprocess


class WindowsTool:

    @staticmethod
    def open_app(app_name):
        os.system(f"start {app_name}")

        return f"Opened {app_name}"

    @staticmethod
    def shutdown_pc():
        os.system("shutdown /s /t 0")

    @staticmethod
    def restart_pc():
        os.system("shutdown /r /t 0")

    @staticmethod
    def wifi_off():
        subprocess.run(
            'netsh interface set interface "Wi-Fi" admin=disable',
            shell=True
        )

        return "WiFi disabled"

    @staticmethod
    def wifi_on():
        subprocess.run(
            'netsh interface set interface "Wi-Fi" admin=enable',
            shell=True
        )

        return "WiFi enabled"