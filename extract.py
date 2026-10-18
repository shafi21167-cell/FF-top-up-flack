import os
import zipfile

def extract_all_zips():
    current_dir = os.getcwd()
    print(f"[*] বর্তমান ফোল্ডার স্ক্যান করা হচ্ছে: {current_dir}")
    
    # ফোল্ডারের সব ফাইল চেক করা
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                extract_to = os.path.join(root, file.replace('.zip', '_extracted'))
                
                os.makedirs(extract_to, exist_ok=True)
                print(f"[+] এক্সট্রাক্ট হচ্ছে: {file} -> {extract_to}")
                
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_to)
                        print(f"[✔] সফলভাবে এক্সট্রাক্ট হয়েছে: {file}")
                        
                        # যদি এক্সট্রাক্ট হওয়া ফোল্ডারের ভেতরে আরও কোনো জিপ ফাইল থাকে (যেমন 60 Top Up জিপ)
                        for inner_root, inner_dirs, inner_files in os.walk(extract_to):
                            for inner_file in inner_files:
                                if inner_file.endswith('.zip'):
                                    inner_zip_path = os.path.join(inner_root, inner_file)
                                    inner_extract_to = os.path.join(inner_root, inner_file.replace('.zip', '_sub_extracted'))
                                    os.makedirs(inner_extract_to, exist_ok=True)
                                    with zipfile.ZipFile(inner_zip_path, 'r') as inner_zip_ref:
                                        inner_zip_ref.extractall(inner_extract_to)
                                        print(f"    [✔] সাব-জিপ এক্সট্রাক্ট হয়েছে: {inner_file}")
                except Exception as e:
                    print(f"[✖] ত্রুটি দেখা দিয়েছে {file} এক্সট্রাক্ট করার সময়: {e}")

if __name__ == "__main__":
    extract_all_zips()
