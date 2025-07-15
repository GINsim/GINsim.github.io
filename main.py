import os
import yaml

# for processing supporting paper
import bibtexparser
import latexcodec
import re

def decode_latex(s):
    if not isinstance(s, str): return s
    try: 
        s_dec = s.encode('utf-8').decode('latex')
        s_clean = re.sub(r'\{([^\{\}]+?)\}', r'\1', s_dec)
        return s_clean 
    except Exception as e:
        print(f"Error decoding LaTeX string: {s}\n{e}")
        return s

# Read the bibliography file on load
with open('bibliography.bib') as bibfile:
    bib_database = bibtexparser.load(bibfile)
bib_entries = {entry["ID"]: entry for entry in bib_database.entries}

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
    if taxon_str: meta_md += f"<small><b>Taxon:</b> {taxon_str}</small>  \n"
    # Process
    process = meta.get("process", [])
    process_str = " | ".join(process) if isinstance(process, list) else str(process)
    if process_str: meta_md += f"<small><b>Process:</b> {process_str}</small>  \n"
    # Submitter
    submitter = meta.get("submitter", [])
    if submitter: meta_md += f"<small><b>Submitter:</b> {submitter}</small>\n\n"

    # Supporting paper
    supporting_id = meta.get("supporting_paper")
    if supporting_id and supporting_id in bib_entries:
      entry = bib_entries[supporting_id]
      author = decode_latex(entry.get("author", "Unknown Author"))
      title = decode_latex(entry.get("title", "Untitled"))
      journal = decode_latex(entry.get("journal", ""))
      year = entry.get("year", "")
      doi = entry.get("doi", "")
      url = entry.get("url", "")
      citation = f"{author} ({year}). *{title}*. {journal}."
      if doi: citation += f" [{doi}](https://doi.org/{doi})"
      elif url: citation += f" [Link]({url})"
      meta_md += f"<small>**Supporting paper:** {citation}</small>\n\n"
    elif supporting_id:
      meta_md += f"<small>**Supporting paper:** Entry `{supporting_id}` not found in bibliography.\n\n"
    
    # Model files
    modelfiles = meta.get("files", [])
    modeldesc = meta.get("file_descriptions", [])
    meta_md += "| Model file(s) | Description(s) |\n|--|--|\n"
    for i, f in enumerate(modelfiles):
        meta_md += f"| [{f}]({f}) | {modeldesc[i]} |\n"

    meta_md += "\n**Summary:**  \n"
    env.markdown = meta_md + env.markdown
