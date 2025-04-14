def define_env(env):
    # Inject metadata at the top of model pages
    def on_page_markdown(markdown, page, config, files):
        if page.file.src_path.startswith("models/") and page.file.name == "index.md" and page.file.src_path != "models/index.md":
            meta = page.meta
            keys = ["title", "type", "author", "accuracy"]
            lines = [f"**{k.capitalize()}:** {meta.get(k, '')}  " for k in keys if k in meta]
            inject = "\n".join(lines) + "\n\n"
            return inject + markdown
        return markdown
    env.on_page_markdown = on_page_markdown

    # Macro to generate the summary table of models
    @env.macro
    def model_table():
        pages = env.variables.get("model_registry", [])
        headers = ["Title", "Type", "Author", "Accuracy"]
        table = "| " + " | ".join(headers) + " |\n"
        table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
        for page in pages:
            meta = page.meta
            row = [
                f"[{meta.get('title', page.title)}]({page.url})",
                meta.get("type", ""),
                meta.get("author", ""),
                str(meta.get("accuracy", ""))
            ]
            table += "| " + " | ".join(row) + " |\n"
        return table

def on_files(env, files, config):
    # Discover all model pages except the main index
    model_pages = [
        f.page for f in files
        if f.src_path.startswith("models/") and
           f.name == "index.md" and
           f.src_path != "models/index.md"
    ]
    env.variables["model_registry"] = model_pages
    return files

