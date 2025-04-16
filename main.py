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

