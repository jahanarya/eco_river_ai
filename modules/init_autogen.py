import os

# বর্তমান modules ফোল্ডার
modules_folder = os.getcwd()
init_file = os.path.join(modules_folder, "__init__.py")

# সব feature ফাইল খুঁজে বের করো
feature_files = sorted([
    f for f in os.listdir(modules_folder)
    if f.startswith("feature_") and f.endswith(".py")
])

# প্রতিটি ফাইলের জন্য import লাইন তৈরি করো
import_lines = [f"from .{f[:-3]} import *" for f in feature_files]

# নতুন __init__.py ফাইল তৈরি করো
with open(init_file, "w", encoding="utf-8") as f:
    f.write("\n".join(import_lines))

print("✅ __init__.py তৈরি হয়েছে:")
for line in import_lines:
    print("   ", line)
