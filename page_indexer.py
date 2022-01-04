import os


def index_tree(root, output):
    for f in os.scandir(root):
        if f.is_dir():
            link_text = ' '.join(f.name.split("_"))
            # create directory page
            create_dir_page(f, link_text)
            # write link to directory page, and index internal files
            link_url = f"{{% link {'/'.join(['indexes', f.name])}_index.md %}}"
            output.write(f"- [{link_text}]({link_url})\n")
        elif f.is_file():
            if f.name[0] == '.':
                continue
            link_text = ' '.join(os.path.splitext(f.name)[0].split("_"))
            link_url = f"{{% link {'/'.join(os.path.split(f.path))} %}}"
            output.write(f"- [{link_text}]({link_url})\n")


def create_dir_page(dir_obj, title):
    page = open(f"indexes/{dir_obj.name}_index.md", 'w')
    page.write(f"# {title}\n")
    index_tree(dir_obj.path, page)
    page.close()


with open("_includes/base_index.md", 'w') as base:
    index_tree("out/", base)
