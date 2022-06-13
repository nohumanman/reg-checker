from RegRenderer import RegRenderer
from os import listdir
from os.path import isfile, join


def test_plates():
    plate_names = [
        f[0:-4] for f in listdir("image_tests/")
        if isfile(join("image_tests/", f))
    ]
    print(plate_names)
    success = 0
    for plate_name in plate_names:
        read_plate = RegRenderer().get_text_from_image(
            "image_tests/" + plate_name + ".png"
        )
        try:
            assert read_plate == plate_name, ()
            print(f"Plate {read_plate} has passed!")
            success += 1
        except AssertionError:
            print(
                f"Plate '{plate_name}' failed! "
                f"Should be '{plate_name}' NOT '{read_plate}'"
            )
    print(
        f"{success}/{len(plate_names)}"
        f" ({success/len(plate_names)*100}%) plates passed!"
    )


if __name__ == "__main__":
    test_plates()
