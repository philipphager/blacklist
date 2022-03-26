import typer
import validators

from blacklist_cli.blacklist import Blacklist

app = typer.Typer()
blacklist = Blacklist("/etc/hosts")


@app.command()
def block(domain: str):
    domains = blacklist.get_domains()

    if validators.domain(domain):

        if domain in domains:
            typer.echo(f"{domain} is already blacklisted.")
        else:
            domains.append(domain)
            blacklist.set_domains(domains)
            typer.echo(f"{domain} added to blacklist.")
    else:
        typer.echo(f"'{domain}' is not a valid domain.")


@app.command()
def unblock(domain: str):
    domains = blacklist.get_domains()

    if domain in domains:
        domains.remove(domain)
        blacklist.set_domains(domains)
        typer.echo(f"{domain} removed from blacklist.")
    else:
        typer.echo(f"{domain} is not blacklisted.")


@app.command()
def show():
    domains = blacklist.get_domains()

    if len(domains) == 0:
        typer.echo("No domains are blacklisted.")
    else:
        typer.echo(f"List of blacklisted domains:")

        for domain in domains:
            typer.echo(f" - {domain}")
