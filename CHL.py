import time
from pywinusb import hid

VENDOR_ID, PRODUCT_ID = 0x2508, 0x0032

def float_to_fix16_16(v: float) -> bytes:
    i = int(v * 65536)
    return bytes([(i >> s) & 0xFF for s in (24, 16, 8, 0)])

def construct_packet(vals) -> bytes:
    hdr = bytes([0, 0x60, 0, 0x30, 0])
    flts = b"".join(float_to_fix16_16(vals[i] if i < len(vals) else 0.0) for i in range(12))
    sfx = bytes([0, 0, 128, 231, 11, 55, 35, 1, 0, 0, 128])
    return hdr + flts + sfx + b"\x00"

def send_report(dev, pkt: bytes):
    for func, msg in ((dev.find_output_reports, "No output reports found!"),
                      (dev.find_feature_reports, "No feature reports found!")):
        reports = func()
        if reports:
            reports[0].set_raw_data(list(pkt))
            reports[0].send()
            return True
        print(msg)
    return False

def main():
    devices = hid.HidDeviceFilter(vendor_id=VENDOR_ID, product_id=PRODUCT_ID).get_devices()
    if not devices:
        print("Titan Two device not found. Ensure it's connected.")
        return
    cv_flag = 1
    example_signal = 100
    dev = devices[0]
    print(f"Found Titan Two device: {dev} - opening...")
    dev.open()
    vals = [cv_flag, example_signal]
    print("Press Ctrl+C to stop.")

    try:
        while True:
            send_report(dev, construct_packet(vals))
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("Stopping...")
        send_report(dev, construct_packet([1, 0]))
        time.sleep(0.5)
    finally:
        dev.close()
        print("Closed Titan Two device.")

if __name__ == "__main__":
    main()
