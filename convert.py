import pypandoc
import os

def md_to_pdf(
    md_file: str,
    output_pdf: str,
    title: str = "Document"
):
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"{md_file} not found")

    extra_args = [
        "--pdf-engine=xelatex",
        "-V", f"title={title}",
        "-V", "geometry:margin=1in",
        "--toc",              
        "--highlight-style=pygments"
    ]

    pypandoc.convert_file(
        source_file=md_file,
        to="pdf",
        outputfile=output_pdf,
        extra_args=extra_args
    )

    print(f"✅ PDF created: {output_pdf}")

if __name__ == "__main__":
    md_to_pdf(
        md_file="OOP-Notes.md",
        output_pdf="output.pdf",
        title="Markdown to PDF Automation"
    )



