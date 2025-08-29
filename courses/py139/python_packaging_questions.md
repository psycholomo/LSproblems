# Python Packaging and PyPI Practice Questions

## Basic Questions

1. **Basic**: What is PyPI and what is its primary purpose in the Python ecosystem?

2. **Basic**: What is `pip` and what is its main function?

3. **Basic**: Explain the difference between a Python module and a Python package.

4. **Basic**: Write the command to install the `requests` package using `pip`.

5. **Basic**: What command would you use to see a list of all packages installed in your current virtual environment?

6. **Basic**: Describe the purpose of the `README.md` and `LICENSE` files when creating a Python package.

7. **Basic**: Which command-line tool is used to upload a package to a repository like PyPI or TestPyPI?

## Intermediate Questions

8. **Intermediate**: Why is it considered a best practice to use virtual environments when managing Python packages for different projects?

9. **Intermediate**: Write the command to install a specific version of a package. For example, how would you install version `2.25.1` of the `requests` package?

10. **Intermediate**: You have installed the `numpy` package. Show two different ways you can import the `pi` constant from this package into your Python script.

11. **Intermediate**: What is a subpackage? If a package named `qux` has a subpackage named `foo`, does the statement `import qux` also import the `foo` subpackage? Explain why or why not.

12. **Intermediate**: What is the role of the `pyproject.toml` file in a modern Python packaging workflow?

13. **Intermediate**: What is the purpose of the `python -m build` command in the package creation process?

14. **Intermediate**: After running `python -m build`, what two types of distribution files are typically created in the `dist` directory? Describe the difference between them.

15. **Intermediate**: What is TestPyPI, and why is it useful for developers who are creating new packages?

16. **Intermediate**: When using `twine` to upload a package with an API token, what username should you provide at the prompt?

17. **Intermediate**: Write the command to upgrade an already installed package, such as `numpy`, to its latest version.

18. **Intermediate**: Write the full command to upload all distribution archives from your `dist` directory to the TestPyPI repository using `twine`.

## Advanced Questions

19. **Advanced**: You've just published a package named `my-package` to TestPyPI. Write the full `pip` command needed to install this package from TestPyPI into a clean virtual environment for verification.

20. **Advanced**: Describe the general directory structure of a simple Python package. What are the key files and folders (e.g., `src`, `pyproject.toml`) and what is their purpose?

---

# Answer Key

## Basic Questions

1. **PyPI (Python Package Index)** is the official repository for Python packages. Its primary purpose is to serve as a centralized location where developers can publish their Python packages and where users can discover and install packages using tools like `pip`.

2. **pip** is the standard package installer for Python. Its main function is to install and manage Python packages from repositories like PyPI, allowing users to easily add third-party libraries to their Python environment.

3. A **Python module** is a single Python file (`.py`) containing Python code, while a **Python package** is a directory containing multiple modules and an `__init__.py` file that makes Python treat the directory as a package.

4. ```bash
   pip install requests
   ```

5. ```bash
   pip list
   ```

6. - **README.md**: Provides documentation about the package, including what it does, how to install it, usage examples, and other important information for users
   - **LICENSE**: Specifies the legal terms under which the package can be used, distributed, and modified

7. **twine** is the command-line tool used to upload packages to repositories like PyPI or TestPyPI.

## Intermediate Questions

8. Virtual environments are considered best practice because they:
   - Isolate dependencies for each project
   - Prevent version conflicts between different projects
   - Allow different projects to use different versions of the same package
   - Keep the global Python environment clean
   - Make projects more reproducible and portable

9. ```bash
   pip install requests==2.25.1
   ```

10. Two ways to import the `pi` constant from numpy:
    ```python
    # Method 1: Import numpy and use dot notation
    import numpy
    pi_value = numpy.pi
    
    # Method 2: Import pi directly
    from numpy import pi
    ```

11. A **subpackage** is a package contained within another package (a nested package structure). The statement `import qux` does **NOT** automatically import the `foo` subpackage. You need to explicitly import subpackages with `import qux.foo` or use relative imports within the package structure.

12. **pyproject.toml** is the modern configuration file that specifies:
    - Build system requirements and configuration
    - Package metadata (name, version, description, etc.)
    - Dependencies and optional dependencies
    - Build tool settings
    - It replaces the older `setup.py` approach

13. `python -m build` creates distribution packages from your source code. It reads the `pyproject.toml` file and generates the distribution files that can be uploaded to PyPI.

14. Two types of distribution files created:
    - **Source distribution (.tar.gz)**: Contains the source code and can be built on any platform
    - **Wheel (.whl)**: A pre-built distribution that can be installed directly without building, making installation faster

15. **TestPyPI** is a test instance of PyPI that allows developers to:
    - Test the package upload process
    - Verify package installation before publishing to the real PyPI
    - Practice the publishing workflow without affecting the main repository

16. When using an API token with twine, you should use `__token__` as the username.

17. ```bash
    pip install --upgrade numpy
    ```
    or
    ```bash
    pip install -U numpy
    ```

18. ```bash
    twine upload --repository testpypi dist/*
    ```

## Advanced Questions

19. ```bash
    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ my-package
    ```

20. **General Python package directory structure**:
    ```
    my-package/
    ├── src/
    │   └── my_package/
    │       ├── __init__.py
    │       └── module.py
    ├── tests/
    │   └── test_module.py
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE
    └── .gitignore
    ```
    
    **Key components**:
    - **src/**: Contains the actual package source code (src layout)
    - **pyproject.toml**: Build configuration and metadata
    - **README.md**: Package documentation
    - **LICENSE**: Legal terms for package usage
    - **tests/**: Test files for the package
    - **__init__.py**: Makes directories into Python packages