# DNP3 Protocol Enumeration

This tool is a DNP3 client that can scan common group/variation combinations, perform fuzzing if no data is found, and write data to a DNP3 server. It leverages the [pyDNP3](https://github.com/ChargePoint/pydnp3) library and is particularly useful for testing and validating DNP3 implementations.

## Features

- **Common Group-Variation Scan:** Scans a list of predefined common group/variation pairs (e.g., Binary Input, Analog Input) to detect available data.
- **Fuzzing Mode:** If no data is found using common groups, the tool can fuzz a range of group/variation combinations to search for responses.
- **Data Writing:** Write commands are supported for specific groups (currently Analog Input and Binary Output) to send custom values.
- **Logging & Error Reporting:** Provides console output for scan progress, errors, and data writing confirmation.

## Prerequisites

- **Python 2.7**  
  (Since Python 2.7 is no longer available by default, using [pyenv](https://github.com/pyenv/pyenv) is recommended for installation.)
- [pyDNP3](https://github.com/ChargePoint/pydnp3)

## Environment Setup with pyenv (Python 2.7)

Follow these steps to set up a Python 2.7 environment using pyenv:

### 1. Install pyenv

#### For Ubuntu/Debian:

1. **Install dependencies:**

   ```bash
   sudo apt update && sudo apt install -y \
       make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev \
       wget curl llvm libncurses5-dev xz-utils tk-dev
   ```

2. **Install pyenv:**

   ```bash
   curl https://pyenv.run | bash
   ```

3. **Configure your shell:**  
   Add the following lines to your `~/.bashrc` (or `~/.bash_profile`):

   ```bash
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv virtualenv-init -)"
   ```

4. **Reload your shell:**

   ```bash
   exec $SHELL
   ```

#### For macOS:

1. **Using Homebrew:**

   ```bash
   brew update
   brew install pyenv
   ```

2. **Configure your shell:**  
   Add the following to your shell configuration (e.g., `~/.zshrc`):

   ```bash
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   source ~/.zshrc
   ```

### 2. Install Python 2.7 via pyenv

Install Python 2.7.18 and set it as the global version:

```bash
pyenv install 2.7.18
pyenv global 2.7.18
```

Verify the installation:

```bash
python --version
```

You should see:

```
Python 2.7.18
```

### 3. Create a Virtual Environment (Optional, but Recommended)

Create and activate a virtual environment:

```bash
pyenv virtualenv 2.7.18 dnp3-env
pyenv activate dnp3-env
```

### 4. Install Dependencies

Create a `requirements.txt` file with the following line:

```
pyDNP3
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

If pip is not available, run:

```bash
python -m ensurepip
python -m pip install --upgrade pip
```

## Usage

Make sure you run the script within the `pydnp3` repository directory.

### Running the Scanner

To scan for common group/variation data on a DNP3 server, run:

```bash
python dnp3_client.py <DNP3_SERVER_IP> <PORT>
```

Example:

```bash
python dnp3_client.py 172.23.1.1 20000
```

### Writing Data

To write data to the DNP3 server, use the `--write` option followed by the parameters `<group> <variation> <index> <value>`:

```bash
python dnp3_client.py <DNP3_SERVER_IP> <PORT> --write <GROUP> <VARIATION> <INDEX> <VALUE>
```

Example:

```bash
python dnp3_client.py 172.23.1.1 20000 --write 10 2 0 123.45
```

## Additional Information

- **Fuzzing:**  
  Use the `--fuzz` flag when running the scanner to enable fuzzing if no data is found in the common groups:

  ```bash
  python dnp3_client.py <DNP3_SERVER_IP> <PORT> --fuzz
  ```

## License

This tool is provided "as is" without any warranty. Use it at your own risk.
