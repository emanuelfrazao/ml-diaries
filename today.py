from datetime import datetime
from pathlib import Path
from textwrap import dedent

DATE_FORMAL_FORMAT = "%y-%m-%d"
DATE_INFORMAL_FORMAT = "%B %d, %Y"

README_TEMPLATE = dedent("""
    **{date}**
        
    # plan of the day
    * [item]

    # [item]
""")

ROOT = Path(__file__).parent

def main():
    # Get today's date
    today = datetime.today()
    
    # Make folder named after today's date
    folder = ROOT / today.strftime(DATE_FORMAL_FORMAT)
    try:
        folder.mkdir()
    except FileExistsError:
        print("Day already created")
        
    # Create README.md
    readme = folder / "README.md"
    readme.touch()
    readme.write_text(
        README_TEMPLATE.format(date=today.strftime(DATE_INFORMAL_FORMAT))
    )
    
if __name__ == "__main__":
    main()
