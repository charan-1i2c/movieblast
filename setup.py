from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Movie-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "entbappy"
# SRC_REPO = "src"  # Remove or comment this line if your code isn't in 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=REPO_NAME,  # Change from SRC_REPO to your repo name
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="entbappy73@gmail.com",
    # packages=[SRC_REPO],  # Remove this line
    packages=find_packages(),  # Use find_packages() to discover all packages in the root directory
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
