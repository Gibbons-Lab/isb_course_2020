"""Set up Qiime 2 on Google colab.

Do not use this on o local machine, especially not as an admin!
"""

import os
import sys
from subprocess import Popen, PIPE

r = Popen(["pip", "install", "rich"])
r.wait()
from rich.console import Console  # noqa
con = Console()

has_conda = "conda version" in os.popen("conda info").read()
has_qiime = "QIIME 2 release:" in os.popen("qiime info").read()


MINICONDA_PATH = (
    "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
)
QIIME_YAML_URL = (
    "https://data.qiime2.org/distro/core/qiime2-2020.8-py36-linux-conda.yml"
)
QIIME_YAML = os.path.basename(QIIME_YAML_URL)


def cleanup():
    """Remove downloaded files."""
    if os.path.exists("Miniconda3-latest-Linux-x86_64.sh"):
        os.remove("Miniconda3-latest-Linux-x86_64.sh")
    if os.path.exists(QIIME_YAML):
        os.remove(QIIME_YAML)
    con.log("Cleaned up unneeded files.")


def run_and_check(args, check, message, failure, success, console=con):
    """Run a command and check that it worked."""
    console.log(message)
    r = Popen(args, env=os.environ, stdout=PIPE, stderr=PIPE,
              universal_newlines=True)
    o, e = r.communicate()
    out = o + e
    if r.returncode == 0 and check in out:
        console.log("[blue]%s[/blue]" % success)
    else:
        console.log("[red]%s[/red]" % failure, out)
        cleanup()
        sys.exit(1)


if __name__ == "__main__":
    if not has_conda:
        run_and_check(
            ["wget", MINICONDA_PATH],
            "saved",
            ":snake: Downloading miniconda...",
            "failed downloading miniconda :sob:",
            ":snake: Done."
        )

        run_and_check(
            ["bash", "Miniconda3-latest-Linux-x86_64.sh", "-bfp", "/usr/local"],
            "installation finished.",
            ":snake: Installing miniconda...",
            "could not install miniconda :sob:",
            ":snake: Installed miniconda to `/usr/local` :snake:"
        )
    else:
        con.log(":snake: Miniconda is already installed. Skipped.")

    if not has_qiime:
        run_and_check(
            ["wget", QIIME_YAML_URL],
            "saved",
            ":mag: Downloading Qiime 2 package list...",
            "could not download package list :sob:",
            ":mag: Done."
        )

        run_and_check(
            ["conda", "env", "update", "-n", "base", "--file",
             "qiime2-2020.8-py36-linux-conda.yml"],
            "To activate this environment, use",
            ":mag: Installing Qiime 2. This may take a little bit.\n :clock1:",
            "could not install Qiime 2 :sob:",
            ":mag: Done."
        )
    else:
        con.log(":mag: Qiime 2 is already installed. Skipped.")

    sys.path.append("/usr/local/lib/python3.6/site-packages")
    con.log(":mag: Fixed import paths to include Qiime 2.")

    run_and_check(
        ["qiime", "info"],
        "QIIME 2 release:",
        ":bar_chart: Checking that Qiime 2 command line works...",
        "Qiime 2 command line does not seem to work :sob:",
        ":bar_chart: Qiime 2 command line looks good :tada:"
    )

    con.log(":bar_chart: Checking if Qiime 2 import works...")
    try:
        import qiime2  # noqa
    except Exception:
        con.log("[red]Qiime 2 can not be imported :sob:[/red]")
        sys.exit(1)
    con.log("[blue]:bar_chart: Qiime 2 can be imported :tada:[/blue]")

    cleanup()

    con.log("[green]Everything is A-OK. "
            "You can start using Qiime 2 now :thumbs_up:[/green]")
