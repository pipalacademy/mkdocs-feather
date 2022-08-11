# mkdocs-feather

Live code execution for MkDocs using [Feather](https://github.com/pipalacademy/feather).

## Usage

In your markdown file, you can say:

~~~markdown
```{ .python .feather }
print("Hello, World!")
```
~~~


It will render as:

```{ .python .feather }
print("Hello, World!")
```

## Features

* Code highlighting
* Multi-file support
* Specify environment variables / CLI args for execution

## Installation

Add "mkdocs-feather" to plugins in your `mkdocs.yml` config.

```yml
site_name: My Docs 
plugins:
    - mkdocs-feather
```

## Configuration

You can configure `mkdocs.yml` to use your own self-hosted Feather runtime or specify modes
that map to particular syntax-highlighting classes or runtimes.

```yaml
plugins:
    - mkdocs-feather:
        server_url: https://feather.pipal.in/
```
