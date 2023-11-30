import subprocess
import logging

def run_disk_cleanup():
    try:
        # Run the Disk Cleanup Utility silently
        subprocess.run(['cleanmgr', '/sagerun:1'], check=True)
        logging.info("Disk Cleanup completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while running Disk Cleanup: {e}")

if __name__ == "__main__":
    # Basic logging setup
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='disk_cleanup.log'
    )

    run_disk_cleanup()
