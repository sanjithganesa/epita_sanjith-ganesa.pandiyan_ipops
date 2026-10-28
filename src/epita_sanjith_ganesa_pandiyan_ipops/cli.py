from rich.console import Console
from rich.table import Table

from .client import get_ipinfo


console = Console()


def main():
    data = get_ipinfo()

    table = Table(title="IPInfo Geolocation")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("IP Address", data.get("ip", "N/A"))
    table.add_row("City", data.get("city", "N/A"))
    table.add_row("Region", data.get("region", "N/A"))
    table.add_row("Country", data.get("country", "N/A"))
    table.add_row("Organization", data.get("org", "N/A"))
    table.add_row("Timezone", data.get("timezone", "N/A"))

    console.print(table)


if __name__ == "__main__":
    main()
