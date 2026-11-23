import cv2
from pathlib import Path
import time


def main():
    dir_path = Path('images2')
    files = [f for f in dir_path.iterdir() if f.is_file()]
    files.sort()

    for file in files:
        print(str(file) + "  -----------")
        frame = cv2.imread(str(file), cv2.IMREAD_UNCHANGED)
        print(f"Dimensions: {frame.shape[1]}x{frame.shape[0]}")
        cv2.imshow("Frame", frame)
        if cv2.waitKey(15) & 0xff == ord('q'):
            break
        time.sleep(1)  # Add a small delay to avoid high CPU usage
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
