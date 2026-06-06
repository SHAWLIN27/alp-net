import typer
from rich.console import Console
from rich.table import Table

from alpnet.config.settings import get_settings
from alpnet.db.graph_store import GraphStore
from alpnet.ingest.pipeline import IngestPipeline

app = typer.Typer(help="ALP_Net command line tools")
console = Console()


@app.command()
def ingest(
    full: bool = typer.Option(False, "--full", help="Run full ingestion"),
):
    """Run the data ingestion pipeline: vault → graph + embeddings + ChromaDB."""
    settings = get_settings()
    pipeline = IngestPipeline(settings)

    try:
        stats = pipeline.run(full=full)
        console.print(f"\n[green]✅ Ingestion complete![/green]")
        console.print(f"   Nodes: {stats.get('nodes', 0)}, Edges: {stats.get('edges', 0)}")
        console.print(f"   Chunks indexed: {stats.get('chunks_indexed', 0)}")
        console.print(f"   Time: {stats.get('elapsed_seconds', 0)}s")
    except Exception as e:
        console.print(f"\n[red]❌ Ingestion failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        raise typer.Exit(code=1)


@app.command()
def stats():
    """Show graph and vector store statistics."""
    settings = get_settings()

    # Graph stats
    gs = GraphStore(settings.graph_path)
    gs.load()
    graph_stats = gs.stats()

    table = Table(title="ALP_Net Storage Stats")
    table.add_column("Store", style="cyan")
    table.add_column("Metric", style="green")
    table.add_column("Value", style="white")

    table.add_row("Graph", "Nodes", str(graph_stats["nodes"]))
    table.add_row("Graph", "Edges", str(graph_stats["edges"]))
    table.add_row("Graph", "File", str(settings.graph_path))

    console.print(table)


@app.command()
def info():
    """Show system info."""
    console.print("[bold cyan]ALP_Net[/bold cyan] — A-Level Physics Knowledge Graph RAG")
    console.print(f"  Vault: {get_settings().vault_path}")
    console.print(f"  Data:  {get_settings().data_dir}")


if __name__ == "__main__":
    app()
