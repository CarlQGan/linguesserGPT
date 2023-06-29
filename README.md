# linguesserGPT

## Overview

`linguesserGPT` is a text-based command-line language guessing game powered by OpenAI's ChatGPT, specifically using the `gpt-3.5-turbo` model. The game leverages the language understanding capabilities of GPT to create an engaging and educational experience for users interested in linguistics. 

The application aims to guess the language input by the user, providing both entertainment and language recognition practice for users, and showcasing the natural language processing abilities of `gpt-3.5-turbo`. Currently, this game is running on ~100 different most frequently used languages from all parts of the world.

## Features

- Text-based command-line interface for easy interaction
- Powered by OpenAI's astonishing Generative Pre-trained Transformers (GPT), leveraging its advanced language recognition
- Wide range of language support, reflecting `gpt-3.5-turbo`'s extensive training data
- Engaging gameplay that tests your knowledge of different languages
- Educational and fun for users of all ages and language proficiency levels

## Installation

Before starting, please make sure you have Python 3.6 or higher installed on your system. You can verify this by running `python3 --version` in your terminal. If you don't have Python installed, you can download it [here](https://www.python.org/downloads/).

Fork this repo and clone the repository to your local machine:

```bash
git clone https://github.com/<your_user_name>/linguesserGPT.git
```

Navigate to the project directory:

```bash
cd linguesserGPT
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To start the game, run the following command in your terminal:

```bash
python3 linguesserGPT.py <your_openai_api_key>
```

Alternatively, set `OPENAI_API_KEY` to your OpenAI API Key in your system environment and simply run the following command in your terminal:

```bash
python3 linguesserGPT.py
```

The game will guide you through the process. Just input the text in the language of your choice and let the game guess!

## Contributing

Contributions are welcome! Please read the [contributing guide](https://github.com/github/docs/blob/main/CONTRIBUTING.md) to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to linguesserGPT.

## License

This project is licensed under the terms of the Creative Commons Zero 1.0 license. See the [LICENSE](LICENSE) file for the full license text.

## Disclaimer

This project is not officially affiliated with OpenAI. It's an individual project leveraging the OpenAI API.

## Contact

If you have any questions, feel free to open an issue or reach out to the maintainer directly.

---

Have fun with `linguesserGPT`, the GPT-powered language guessing game!
