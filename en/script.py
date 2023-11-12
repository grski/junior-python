import openai
import os
import fnmatch

openai.api_key = "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"


def check_text(text):
    return text.count("```") % 2 == 0


def make_request(text):
    prompt = f"""Take a deep breath and focus. Please translate the text below from polish into english. 
            PRESERVE MARKDOWN FORMATTING and STYLE of the author the best you can.
            ---
            {text}
            """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"]

def read_markdown(file_path):
    print("Markdown file found. Reading...")
    whole_file = ""
    with open(file_path, 'r') as file:
        print("Opened file")
        while True:
            lines = [file.readline() for _ in range(50)]
            text = ''.join(lines)
            print(lines)
            if not lines or ("" in lines and lines[-1] == ""):
                response = make_request(text)
                whole_file += response
                break
            if "" not in lines:
                is_newline_and_not_splitted = text.count("```") % 2 == 0 and (lines[-1] in {"\n", ""})
                print(f"Line is not splitted? {is_newline_and_not_splitted}")
                while not is_newline_and_not_splitted:
                    print("reading next line")
                    next_line = file.readline()
                    text += next_line
                    is_newline_and_not_splitted = check_text(text)
                    print(f"Line is not splitted? {is_newline_and_not_splitted}")
                response = make_request(text)
                whole_file += response
    return whole_file


def find_md_files(directory):
    # List to store found md files
    md_files = []

    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, '*.md'):
            # append full file path to our files list
            md_files.append(os.path.join(root, filename))

    return md_files


def main():
    directory = "./chapters/"
    md_files = find_md_files(directory)
    md_files = ["./chapters/chapter-17-kultura.md"]
    if md_files:
        print("Found .md files: ")
        # present = ["20"]
        # md_files = [file for file in md_files if any(p in file for p in present)]
        for file in md_files:
            print(file)
            print("Reading file...")
            translated_text = read_markdown(file)
            # save translated text to file
            with open(f"{file}_en", "a") as translated_file:
                translated_file.write(translated_text)
    else:
        print("No .md files found in given directory.")


if __name__ == "__main__":
    main()
