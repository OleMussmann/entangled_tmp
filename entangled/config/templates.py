from dataclasses import dataclass


@dataclass
class Template:
    """Officially supported templates. Templates are pulled from external GitHub
    repositories: `entangled new <template name>`. These templates are the ones
    we officially support. Other templates can be used with valid copier URL
    notation, like: `entangled new gh:<url>`. See
    https://copier.readthedocs.io/en/stable/reference/vcs/#copier.vcs.get_repo
    for valid URL examples.
    """

    handle: str
    name: str
    url: str
    description: str


templates = [
    Template("mkdocs", "MkDocs", "gh:entangled/template-mkdocs", "Fancy description here"),
    Template("other", "Other", "gh:example/example", "Also fancy description here"),
]
