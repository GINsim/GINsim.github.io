import os
import yaml

def define_env(env):
    @env.macro
    def model_table():
        model_root = os.path.join(env.project_dir, "docs", "models")
        table = "| Model name | Taxon - all terms | Process - all terms |\n|-------|-------|---------|\n"

        for model_name in sorted(os.listdir(model_root)):
            model_dir = os.path.join(model_root, model_name)
            index_path = os.path.join(model_dir, "index.md")

            if not os.path.isdir(model_dir) or not os.path.exists(index_path):
                continue

            with open(index_path, encoding="utf-8") as f:
                content = f.read()

            if content.startswith("---"):
                _, frontmatter, _ = content.split("---", 2)
                meta = yaml.safe_load(frontmatter)

                title = meta.get("title", model_name)
                taxon = ", ".join(meta.get("taxon", []))
                process = ", ".join(meta.get("process", []))

                link = f"{model_name}/"
                table += f"| [{title}]({link}) | {taxon} | {process} |\n"

        return table

def on_post_page_macros(env):
    file = env.page.file
    if not file.src_path.startswith("models/") or \
       not file.src_path.endswith("index.md") or \
       file.src_path == "models/index.md": return

    meta = env.page.meta
    meta_md = ''
    # Taxon
    taxon = meta.get("taxon", [])
    taxon_str = " | ".join(taxon) if isinstance(taxon, list) else str(taxon)
    if taxon_str: meta_md += f"<small>Taxon: {taxon_str}</small>\n\n"
    # Process
    process = meta.get("process", [])
    process_str = " | ".join(process) if isinstance(process, list) else str(process)
    if process_str: meta_md += f"<small>Process: {process_str}</small>\n\n"
    # Submitter
    submitter = meta.get("submitter", [])
    if submitter: meta_md += f"<small>Submitter: {submitter}</small>\n\n"
    # Model files
    modelfiles = meta.get("files", [])
    modeldesc = meta.get("file_descriptions", [])
    if isinstance(modelfiles, list): print('List:', modelfiles)
    if isinstance(modeldesc, list): print('List:', modeldesc)
    meta_md += "| Model file(s) | Description(s) |\n|--|--|\n"
    for i, f in enumerate(modelfiles):
        meta_md += f"| [{f}]({f}) | {modeldesc[i]} |\n"

    meta_md += "\n**Summary:**\n\n"
    env.markdown = meta_md + env.markdown
