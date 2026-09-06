import os
import shutil

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".txt", ".pdf", ".docx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}


def organize_files():
    folder = input("\nمسیر پوشه را وارد کن: ")

    if not os.path.isdir(folder):
        print("این پوشه وجود ندارد.")
        return

    files_to_move = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if not os.path.isfile(full_path):
            continue

        extension = os.path.splitext(file)[1].lower()
        destination_folder = "Others"

        for folder_name, extensions in folders.items():
            if extension in extensions:
                destination_folder = folder_name
                break

        files_to_move.append((file, destination_folder))

    if not files_to_move:
        print("هیچ فایلی برای مرتب‌سازی پیدا نشد.")
        return

    print("\nفایل‌های پیدا شده:")
    print("-" * 35)

    for file, destination in files_to_move:
        print(f"{file} -> {destination}")

    answer = input("\nآیا مرتب‌سازی انجام شود؟ (y/n): ")

    if answer.lower() != "y":
        print("عملیات لغو شد.")
        return

    count = 0

    for file, destination_folder in files_to_move:
        source = os.path.join(folder, file)
        destination = os.path.join(folder, destination_folder)

        os.makedirs(destination, exist_ok=True)
        shutil.move(source, os.path.join(destination, file))

        print(f"{file} -> {destination_folder}")
        count += 1

    print(f"\nمرتب‌سازی با موفقیت انجام شد.")
    print(f"تعداد فایل‌های جابه‌جا شده: {count}")


def show_help():
    print("\n========== راهنما ==========")
    print("این برنامه فایل‌های یک پوشه را بر اساس نوع مرتب می‌کند.")
    print("عکس‌ها → Images")
    print("اسناد → Documents")
    print("ویدئوها → Videos")
    print("موسیقی → Music")
    print("فایل‌های ناشناخته → Others")
    print("============================")


while True:
    print("\n==============================")
    print("      File Organizer")
    print("==============================")
    print("1. مرتب‌سازی فایل‌ها")
    print("2. راهنما")
    print("3. خروج")
    print("==============================")

    choice = input("انتخاب شما: ")

    if choice == "1":
        organize_files()

    elif choice == "2":
        show_help()

    elif choice == "3":
        print("برنامه بسته شد.")
        break

    else:
        print("گزینه نامعتبر است.")
