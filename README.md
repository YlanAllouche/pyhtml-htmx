
# PyHTML-HTMX ![HTMX-Badge](https://img.shields.io/badge/%3C/%3E%20htmx-3D72D7?style=for-the-badge&logo=mysl&logoColor=white)

HTMX integration for [PyHTML](https://github.com/COMP1010UNSW/pyhtml-enhanced) - to build dynamic, hypermedia-driven web applications with only Python, Flask, optionally WebComponents and absolutely no Javascript.



## Features

-  **Type-safe** with full editor autocomplete
-  **All 35 HTMX attributes** listed from HTMX's web-type document
-  **Literal types** for (the one set of) enum values (e.g.: `swap="innerHTML"`)
-  **Comprehensive documentation** in docstrings also from the web-types.
-  **Works well with Flask and pyHtml** see snippet.

## Installation

### From GitHub

```bash
pip install pyhtml-htmx
```

### From GitHub

```bash
pip install git+https://github.com/YlanAllouche/pyhtml-htmx.git
```

### Local Development

```bash
git clone https://github.com/YlanAllouche/pyhtml-htmx.git
cd pyhtml-htmx
pip install -e . # --break-system-packages

```
## Usage



### The `htmx()` Helper Function

The `hx()` function creates HTMX attributes with a clean, intuitive API. Note that you use the attribute names **without** the `hx_` prefix inside the function since it's already the name of the function.

### Type Safety

The `htmx()` function provides full type hints with Literal types for (the one set of) enumerated values:

```python
# 'swap' parameter uses Literal type - editor will suggest valid values
**hx(
    swap="innerHTML"    # Shown as valid 
    # swap="invalid"    # LSP error in editor
)

```


## Basic Flask example


```python
import pyhtml as p
from pyhtml_htmx import hx

@app.route("/")
def index():
    return p.html(
        p.head(
            p.title("HTMX App"),
            p.script(src="https://unpkg.com/htmx.org@2.0.3")
        ),
        p.body(
            p.button(
                "Click me",
                **hx(post="/clicked", swap="outerHTML")
            )
        )
    )

@app.route("/clicked", methods=["POST"])
def clicked():
    return p.div("Button clicked")

```
## Future Potential Enhancements

- Direct attribute support: `div("content", get="/url")`
   - through monkey-patching
   - or upstream integration
- either by 
    - supporting htmx directly
    - or providing a hook for extra universal attributes
        - at which point other libraries like Alpine could also be easily added

## External documentation and dependencies

- [HTMX Official Documentation](https://htmx.org/)
- [HTMX Attributes Reference](https://htmx.org/reference/)
---
- [PyHTML Documentation](https://comp1010unsw.github.io/pyhtml-enhanced/)
- [PyHTML Enhanced](https://github.com/COMP1010UNSW/pyhtml-enhanced) by Maddy Guthridge

